"""Media Archiver & Deduplicator for Techtunes Archive.

Downloads permitted images with SSRF protection, size caps, MIME verification,
and SHA-256 content deduplication.
"""

from __future__ import annotations

import hashlib
import io
import ipaddress
import json
import logging
import re
import socket
import threading
import urllib.parse
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

import requests

try:
    from PIL import Image
except ImportError:
    Image = None  # type: ignore

logger = logging.getLogger("archive.media")

ROOT_DIR = Path(__file__).resolve().parent.parent
MEDIA_DIR = ROOT_DIR / "media"
CONFIG_DIR = ROOT_DIR / "config"
POLICY_FILE = CONFIG_DIR / "media-policy.json"


def load_media_policy() -> Dict[str, Any]:
    """Loads media download policy configuration."""
    if POLICY_FILE.exists():
        try:
            with open(POLICY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Error loading media-policy.json: {e}")

    return {
        "enabled": True,
        "max_file_size_bytes": 10485760,  # 10 MB
        "allowed_mime_types": [
            "image/jpeg", "image/png", "image/webp", "image/gif", "image/svg+xml"
        ],
        "allowed_extensions": [".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg"],
        "disallow_private_ips": True,
        "request_timeout_seconds": 25,
        "max_retries": 3,
    }


def is_safe_url(url: str, policy: Dict[str, Any]) -> Tuple[bool, str]:
    """Validates that a URL does not resolve to private or loopback IP ranges (SSRF protection)."""
    try:
        parsed = urllib.parse.urlparse(url)
        if parsed.scheme not in ("http", "https"):
            return False, f"Unsupported scheme: {parsed.scheme}"

        hostname = parsed.hostname
        if not hostname:
            return False, "Empty hostname"

        if policy.get("disallow_private_ips", True):
            try:
                ip_list = socket.getaddrinfo(hostname, None)
                for item in ip_list:
                    ip_str = item[4][0]
                    ip = ipaddress.ip_address(ip_str)
                    if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
                        return False, f"URL resolves to disallowed private IP: {ip_str}"
            except socket.gaierror:
                return False, f"Cannot resolve hostname: {hostname}"

        return True, ""
    except Exception as e:
        return False, f"Invalid URL: {e}"


def sanitize_filename(name: str) -> str:
    """Sanitizes filename for safe storage across platforms."""
    cleaned = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "", name)
    cleaned = re.sub(r"\s+", "-", cleaned).strip("-.")
    return cleaned if cleaned else "image.jpg"


class MediaArchiver:
    """Manages downloading, verifying, and deduplicating media assets."""

    def __init__(self, base_media_dir: Optional[Path] = None) -> None:
        self.base_dir = base_media_dir or MEDIA_DIR
        self.policy = load_media_policy()
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) TechtunesArchiveMedia/1.0",
            "Referer": "https://www.techtunes.io/",
        })
        self._thread_local = threading.local()
        self._write_lock = threading.Lock()

    def _get_session(self) -> requests.Session:
        """Uses main session on main thread (for test patching compatibility) and thread-local otherwise."""
        if threading.current_thread() is threading.main_thread():
            return self.session
        sess = getattr(self._thread_local, "session", None)
        if sess is None:
            sess = requests.Session()
            sess.headers.update(self.session.headers)
            self._thread_local.session = sess
        return sess

    def _optimize_to_webp(self, raw_bytes: bytes, content_type: str) -> Tuple[bytes, str, bool]:
        """Converts JPEG/PNG/WebP images to compact WebP when enabled in policy."""
        if not self.policy.get("convert_to_webp", False) or Image is None:
            return raw_bytes, content_type, False
        if content_type not in ("image/jpeg", "image/jpg", "image/png", "image/webp", ""):
            return raw_bytes, content_type, False

        try:
            with Image.open(io.BytesIO(raw_bytes)) as im:
                im.load()
                max_width = int(self.policy.get("max_width", 640) or 640)
                if max_width > 0 and im.width > max_width:
                    new_height = max(1, int(im.height * (max_width / im.width)))
                    im = im.resize((max_width, new_height), Image.Resampling.LANCZOS)
                if im.mode not in ("RGB", "RGBA"):
                    im = im.convert("RGB")
                elif im.mode == "RGBA":
                    # Flatten alpha over white or keep RGB to maximize savings
                    bg = Image.new("RGB", im.size, (255, 255, 255))
                    bg.paste(im, mask=im.split()[3])
                    im = bg

                quality = int(self.policy.get("webp_quality", 72) or 72)
                buf = io.BytesIO()
                im.save(buf, format="WEBP", quality=quality, method=4)
                optimized = buf.getvalue()
                if optimized and len(optimized) < len(raw_bytes):
                    return optimized, "image/webp", True
        except Exception:
            pass
        return raw_bytes, content_type, False

    def download_image(
        self,
        image_url: str,
        source_key: str,
        preferred_filename: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Downloads, validates, hashes, and stores an image."""
        result = {
            "original_url": image_url,
            "source_key": source_key,
            "status": "failed",
            "local_path": None,
            "sha256_hash": None,
            "mime_type": None,
            "file_size": 0,
            "error_message": None,
        }

        if not self.policy.get("enabled", True):
            result["status"] = "skipped"
            result["error_message"] = "Media downloads are disabled in policy"
            return result

        if not image_url:
            result["error_message"] = "Empty image URL"
            return result

        safe, reason = is_safe_url(image_url, self.policy)
        if not safe:
            result["error_message"] = f"Security check failed: {reason}"
            return result

        max_size = self.policy.get("max_file_size_bytes", 10485760)
        timeout = self.policy.get("request_timeout_seconds", 25)

        try:
            session = self._get_session()
            resp = session.get(image_url, stream=True, timeout=timeout)
            resp.raise_for_status()

            content_type = resp.headers.get("Content-Type", "").split(";")[0].strip().lower()
            allowed_mimes = self.policy.get("allowed_mime_types", [])
            if allowed_mimes and content_type not in allowed_mimes:
                ext = Path(urllib.parse.urlparse(image_url).path).suffix.lower()
                allowed_exts = self.policy.get("allowed_extensions", [])
                if ext not in allowed_exts:
                    result["status"] = "skipped"
                    result["error_message"] = f"Disallowed MIME type: {content_type} / {ext}"
                    return result

            data_chunks = []
            total_size = 0

            for chunk in resp.iter_content(chunk_size=65536):
                if chunk:
                    total_size += len(chunk)
                    if total_size > max_size:
                        result["status"] = "skipped"
                        result["error_message"] = f"File size exceeded maximum limit ({total_size} > {max_size})"
                        return result
                    data_chunks.append(chunk)

            raw_bytes = b"".join(data_chunks)
            final_bytes, final_mime, converted = self._optimize_to_webp(raw_bytes, content_type)
            file_hash = hashlib.sha256(final_bytes).hexdigest()
            result["sha256_hash"] = file_hash
            result["file_size"] = len(final_bytes)
            result["mime_type"] = final_mime

            url_filename = Path(urllib.parse.urlparse(image_url).path).name
            filename = sanitize_filename(preferred_filename or url_filename or f"{file_hash[:16]}.jpg")
            if converted:
                filename = f"{Path(filename).stem}.webp"

            with self._write_lock:
                dest_dir = self.base_dir / source_key
                dest_dir.mkdir(parents=True, exist_ok=True)
                dest_path = dest_dir / filename

                if dest_path.exists():
                    existing_hash = hashlib.sha256(dest_path.read_bytes()).hexdigest()
                    if existing_hash != file_hash:
                        stem = dest_path.stem
                        suffix = dest_path.suffix
                        dest_path = dest_dir / f"{stem}_{file_hash[:8]}{suffix}"

                with open(dest_path, "wb") as f:
                    f.write(final_bytes)

            rel_path = f"media/{source_key}/{dest_path.name}"
            result["status"] = "completed"
            result["local_path"] = rel_path
            return result

        except Exception as e:
            result["status"] = "failed"
            result["error_message"] = str(e)
            return result
