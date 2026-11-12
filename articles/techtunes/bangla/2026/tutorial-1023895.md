---
archive_id: techtunes-1023895
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 1023895
title: Filee – কম্পিউটারে File Conversion-এর অভিজ্ঞতায় এক বৈপ্লবিক বিপ্লব! Mouse-এর
  এক Drag-এ রূপান্তর করুন যেকোনো File Completely Offline-এ!
slug: tutorial-1023895
language: bn
status: publish
published_at: '2026-11-06T09:23:00+00:00'
modified_at: '2026-11-06T09:23:00+00:00'
original_url: https://www.techtunes.io/tutorial/tune-id/1023895
author: মো আতিকুর ইসলাম
author_url: https://www.techtunes.io/tuner/atikurofficial
categories:
- টিউটোরিয়াল
tags:
- Docx ফাইল
- ফটো কনভার্টর
- ফ্রী ফটো কনভার্টর
content_hash: 2278a669c597f6aea50bd91a4a5c665de10fb76251d6adc83959897de43a670e
archived_at: '2026-11-12T11:34:21.944481+00:00'
---

আমরা যারা প্রতিদিন কাজের সূত্রে Computer ব্যবহার করি—চাই আমরা Office-এর কাজ করি, পড়ালেখা করি, Software Development করি, Graphics Design করি কিংবা Digital Content Creation করি—আমাদের সবাইকে প্রতিনিয়ত একটি সাধারণ কিন্তু চরম বিরক্তিকর সমস্যার মুখোমুখি হতে হয়। আর তা হলো File Format Conversion বা File-এর Format পরিবর্তন করা।

একবার ভাবুন তো, আপনার কাছে হয়তো একটি Image রয়েছে যা HEIC বা RAW Format-এ আছে, কিন্তু আপনার Client বা সহকর্মী তা চাচ্ছেন সাধারণ JPG বা PNG Format-এ। কিংবা আপনার কাছে একটি Korean HWP বা HWPX File এসেছে, অথবা একটি PDF File রয়েছে যা থেকে আপনাকে Word Document বা DOCX File তৈরি করতে হবে। এমন পরিস্থিতিতে সাধারণ User-রা মূলত দুটো পথ বেছে নেন:

1. **Online File Converter Websites:** বাধ্য হয়ে আমরা Internet-এ Search করে অজানা কোনো Website-এ আমাদের গুরুত্বপূর্ণ Files-গুলো Upload করি। কিন্তু এর ফলে আমাদের ব্যক্তিগত গোপনীয়তা বা Privacy মারাত্মক হুমকির মুখে পড়ে। Sites-গুলোতে File Size-এর Limit থাকে, স্লো Internet-এর কারণে Upload ও Download হতে দীর্ঘ সময় লাগে, আর সেই সাথে থাকে হাজারো বিরক্তিকর Advertisement ও Spam-এর ঝামেলা।
2. **ভারী Software Suites:** দ্বিতীয় উপায়টি হলো PC-তে Gigabyte-এর পর Gigabyte জায়গা দখল করে থাকা ভারী সব Software Install করা—যেমন Microsoft Office, Hancom Office কিংবা LibreOffice। এসব ভারী Software Background-এ PC-র প্রচুর RAM ও Processor Capacity নষ্ট করে এবং পুরো Computer-কে স্লো বা ধীরগতির করে ফেলে।

কিন্তু যদি এমন একটি Magic-এর মতো Solution থাকত, যা আপনার Computer-এর Background-এ একদম Silently বসে থাকবে, যার জন্য কোনো ভারী App Window Open করতে হবে না, আর কেবল একটি Keyboard Key চেপে Mouse দিয়ে File Drag করতেই আপনার Mouse Cursor-এর চারপাশে একটি নান্দনিক Donut Menu ভেসে উঠবে? আর সেই Menu থেকে এক নিমেষেই যেকোনো File Convert হয়ে Save হয়ে যাবে ঠিক মূল File-এর পাশেই?

ঠিক এই বৈপ্লবিক চিন্তাধারার Solution নিয়ে তৈরি করা হয়েছে Filee! South Korean ডেভেলপার Myeonggu Kim (KnifeLemon)-এর একক প্রচেষ্টা ও উন্মুক্ত অবদানে তৈরি এই Project-টি একটি সম্পূর্ণ Free এবং Open-Source Desktop Application। এটি আধুনিক.NET 10 SDK এবং Avalonia Cross-Platform Framework ব্যবহার করে C# ভাষায় তৈরি করা হয়েছে। File Conversion-এর চিরাচরিত নিয়মকে বদলে দেওয়া এই অসাধারণ Tool-টির প্রতিটি বিস্তারিত দিক, এর ভেতরে থাকা Engine-এর গঠন, Format Support, Security Policy এবং Installation Guide নিয়ে নিচে অত্যন্ত গভীরভাবে আলোচনা করা হলো।

## ১. User Interface-এর জাদুকরী অভিজ্ঞতা: Cursor-এর পাশে Donut Menu

![Filee](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_5ecb5356c1997082964792f6f1003e1e.png)

Filee ব্যবহারের পুরো অভিজ্ঞতাটিকে একটি শব্দে ব্যাখ্যা করলে তা হবে—'জাদুকরী'। অন্যান্য প্রতিটি Traditional Application যেখানে আপনাকে প্রথাগত বড় কোনো App Window Open করতে বাধ্য করে, Filee সেখানে পুরো বিষয়টিকেই নিয়ে এসেছে আপনার Mouse Cursor-এর ডগায়।

```
[Your Mouse Cursor] ──(Hold Ctrl / Option &amp; Drag File)──&gt; [Interactive Donut Menu Appears] │ ├──&gt; Drop on 'PNG'  ──&gt; Saved photo.png! ├──&gt; Drop on 'PDF'  ──&gt; Saved photo.pdf! └──&gt; Drop on 'WEBP' ──&gt; Saved photo.webp!
```

### কীভাবে কাজ করে এই Donut Menu?

- **Hold Trigger Key:** আপনি আপনার কাজের Flow নষ্ট না করে কেবল Keyboard-এর একটি নির্দিষ্ট Key চেপে ধরে রাখবেন। Windows এবং Linux Users-দের জন্য এটি হলো **Ctrl** Key, আর macOS Users-দের জন্য এটি **Option** Key।
- **Mouse Drag Gesture:** যে File বা Files-গুলোকে Convert করতে চান, সেটিকে Mouse দিয়ে Select করে Drag করা শুরু করুন।
- **Donut Menu Appearance:** সাথে সাথেই আপনার Mouse Cursor-এর ঠিক চারপাশ ঘিরে একটি নান্দনিক বৃত্তাকার **Donut Menu** ফুটে উঠবে।
- **Context-Awareness Filtering:** এই Donut Menu-টি অত্যন্ত বুদ্ধিমান ও Smart। এটি Drag করা File-টির ধরন চিনে নেয় এবং কেবল সেই সব Formats-ই আপনার সামনে প্রদর্শন করে যা সেই File-টির জন্য বাস্তবে উপযুক্ত। যেমন—আপনি যদি কোনো Image Drag করেন, তবে এটি Audio বা Video Format দেখাবে না, কেবল Image সম্পর্কিত Formats-গুলোই On-Screen ভেসে উঠবে।
- **Instant Drop & Save:** আপনার পছন্দের Format-এর ওপর File-টি নিয়ে ছেড়ে (Drop) দিন। নিমেষের মধ্যেই Background-এ Processing শেষ হয়ে মূল File-এর Directory-তেই নতুন File-টি Save হয়ে যাবে!

### File Type ভিত্তিক Customized Toolbar এবং Presets

কেবল এক Click-এ Convert করাই নয়, Advanced Users-দের সুবিধার জন্য Filee-তে রয়েছে প্রতি File Type-এর জন্য পৃথক Custom Toolbar তৈরি ও সাজানোর ক্ষমতা। Drag And Drop-এর মাধ্যমে সাজানো এই Toolbars-গুলোতে আপনি কাজের জন্য প্রয়োজনীয় Presets আগে থেকেই Set করে রাখতে পারবেন:

- **Quality & Compression Presets:** Image-এর Output Quality (যেমন ৮০% বা ১০০%) এবং Compression Level আগে থেকে ঠিক করে রাখা।
- **Size & Resolution Presets:** File-এর Pixel Dimension বা Height-Width নির্দিষ্ট করা।
- **DPI Settings:** Printing কাজের জন্য DPI Configure করা।
- **PDF Pages & Selection:** PDF File-এর কত নম্বর Page Convert হবে সেই Page Ranges আগে থেকেই Define করা।
- **Video & Audio Presets:** Video-র Resolution (যেমন 720p, 1080p), Frame Rate, Audio Bitrate ও Channel Customize করা।
- **Output Folder & Naming Rules:** Convert হওয়া Files-গুলো মূল File-এর পাশে Save হবে, নাকি নির্দিষ্ট কোনো Output Folder-এ যাবে এবং Files-গুলোর File Names কেমন হবে তার স্বয়ংক্রিয় Rules Set করা।

### Filee

অফিসিয়াল ওয়েবসাইট @ [Filee](https://filee.sh/)

## কীভাবে Filee ব্যবহার করবেন?

![কীভাবে Filee ব্যবহার করবেন?](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_9dc10aa048d97b6b87fb6c1778e3a704.jpg)

১. উইন্ডোজ বা লিনাক্সে কিবোর্ডের Ctrl (ম্যাকে Option) চেপে ধরে ফাইল এক্সপ্লোরার থেকে নির্দিষ্ট ফাইল ড্র্যাগ করা শুরু করুন।  
 ![ফাইল ড্র্যাগ](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_cef2fcc955481d19209bc4fe3cbc9891.png)  
 ২. মাউস কার্সারের চারপাশে ভেসে ওঠা বৃত্তাকার ডোনাট মেনু (Donut Menu) থেকে উপযুক্ত ফরম্যাট চিহ্নের ওপর ফাইলটি ড্রপ করুন।  
 ![Donut Menu](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_160d5cb904a13318d18c718ed48d978c.png)  
 ৩. প্রসেসিং শেষ হওয়া মাত্রই রূপান্তর হওয়া নতুন ফাইলটি স্বয়ংক্রিয়ভাবে মূল ফাইলের ডিরেক্টরিতেই সংরক্ষিত হবে।  
 ![প্রসেসিং](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_fe6b175a734b727b780c341c943ff41b.png)  
 ৪. বিকল্প উপায়ে কনভার্ট করতে ফাইলের ওপর রাইট-ক্লিক মেনু, কিবোর্ড শর্টকাট অথবা অ্যাপের মূল উইন্ডোর ড্রপ জোন ব্যবহার করুন।  
 ![মূল উইন্ডোর ড্রপ জোন](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_1330de3ec3147bc26d4faba329bcaf7a.png)

## ২. মূল Highlights: কেন Filee অন্যান্য Converter থেকে আলাদা?

![কেন Filee অন্যান্য Converter থেকে আলাদা?](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_0b028ef1762bcd119498124e20280509.jpg)

- **Right at Your Cursor:** কোনো বড় App Window Open করার প্রয়োজনই পড়ে না। আপনি আপনার Computer-এর যে Screen-এ বা যে Folder-এ কাজ করছেন, Drag করার সাথে সাথেই Format Options-গুলো আপনার Mouse Cursor-এর ডগায় উপস্থিত হয়।
- **244 Formats, No Other Software:** Images, PDF, Word, Excel, PowerPoint, HWP, E-Books, Archives, Fonts, CAD এবং 3D Models—সবকিছুই কোনো Microsoft Office, Hancom Office কিংবা LibreOffice ছাড়াই ইনস্ট্যান্টলি কাজ করে।
- **Stays on Your Computer:** আপনার PC থেকে কোনো Data, File বা Metadata Internet-এ Upload হয় না। Filee ১০০% Offline-এ কাজ করে এবং আপনার PC-র নিজস্ব Processor ব্যবহার করে মূল File-এর পাশেই Result Save করে।
- **Interactive Media & Demos:** Official Domain `filee.sh`-এ Filee-র একটি ২৭ সেকেন্ডের আকর্ষণীয় Demo Video এবং Live Interactive Demo ডেমোন্ডস্ট্রেট করা রয়েছে। এছাড়া এর Home Screen-এ রয়েছে Custom Donut Toolbar Editor, একটি Dedicated Drop Zone এবং সাম্প্রতিক Conversions দেখার সুব্যবস্থা।

## ৩. Filee-র Powerful Features-সমূহ

![Filee-র Powerful Features-সমূহ](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_92476b0377712a35e9356f3d49de937d.jpg)

সাধারণ File Conversion ছাড়াও Professional-দের কথা মাথায় রেখে Filee-তে যুক্ত করা হয়েছে চমৎকার কিছু Powerful Features:

- **A Donut at The Cursor:** Mouse Cursor-এর কাছে সাথে সাথে Donut Menu ফুটে ওঠে এবং File অনুযায়ী কেবল উপযোগী Formats-গুলো Filter করে প্রদর্শন করে।
- **One Toolbar per File Type:** প্রতিটি File Type-এর জন্য আলাদা Customized Toolbar এবং পূর্ব-নির্ধারিত Preset Set করার সুবিধা।
- **Parallel Multi-File Processing:** আপনি যদি একসাথে ১০টি, ২০টি বা ১০০টি File Select করে Drag করেন, Filee আপনার Processor-এর সবকটি Core ব্যবহার করে সমান্তরালভাবে (in Parallel) Process করে দ্রুততম সময়ে Result তৈরি করে।
- **Automated Multi-Step Route Calculation:** অনেক সময় কোনো File-কে সরাসরি কাঙ্ক্ষিত Format-এ রূপান্তর করার সরাসরি কোনো Library থাকে না। Filee স্বয়ংক্রিয়ভাবে Algorithm ব্যবহার করে Multi-Step Route খুঁজে বের করে (যেমন: `HWP → HWPX → DOCX`) এবং File-টিকে নিখুঁতভাবে Convert করে।
- **Watch Folders:** আপনার কাজের গতিকে বহুগুণ বাড়িয়ে দিতে এতে রয়েছে "Watch Folder" Feature। আপনি PC-র যেকোনো Folder-কে Watch Folder হিসেবে Set করে দিলে, সেই Folder-এ নতুন কোনো File Drop হওয়া মাত্রই Filee Background-এ তা স্বয়ংক্রিয়ভাবে নির্দিষ্ট Format-এ Convert করে ফেলে।
- **Multiple Entry Points:** File Drop ও Process করার জন্য Filee-তে ৫টি পৃথক পথ বা Entry Points রয়েছে:
  1. **Donut Menu** (Mouse দিয়ে Drag করে)
  2. **Right-Click Menu** (System File Manager-এর Mouse-এর ডান Click-এ)
  3. **Keyboard Shortcut** (Global Keyboard Shortcut চেপে)
  4. **Drop Zone** (Application-এর Home Screen-এর Drop Zone-এ এনে)
  5. **CLI** (`filee` Command Line Interface দিয়ে)
- **Themes & Localization:** চোখে স্বাচ্ছন্দ্য দিতে App-টিতে রয়েছে চমৎকার **Light Theme** এবং **Dark Theme**। পুরো Interface-টি English, Korean (한국어) এবং Simplified Chinese (简体中文) এই তিনটি ভাষায় চমৎকারভাবে ব্যবহার করা যায়।

## ৪. সমর্থিত ২৪৪টি Formats-এর সম্পূর্ণ বিস্তারিত তালিকা এবং Engine Architecture

![সমর্থিত ২৪৪টি Formats](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_bbcdae76fb1af091ade1d7f5bdcdbbeb.jpg)

Filee কোনো তথ্য বাদ না দিয়ে ২৪৪টি Format Support করে। নিচে ১৭টি Category-তে প্রতিটি Input এবং Output সক্ষমতার বিস্তারিত তালিকা দেওয়া হলো:

### ১. Images

- **from (Input):** JPG, PNG, WEBP, AVIF, TIFF, BMP, GIF, APNG, ICO, ICNS, JPEG XL, JPEG 2000, PSD/PSB, TGA, PPM, HEIC, QOI, DDS, PCX, MNG, CUR; GIMP XCF, Camera RAW (CR2, CR3, NEF, ARW, DNG), DICOM, OpenEXR, HDR Read।
- **to (Output):** উপরের যেকোনো Image Format (HEIC-এর জন্য FFmpeg Engine প্রয়োজন⁵), PDF, SVG (Traced Vector), Resized Image, এবং Grayscale।

### ২. Vector Graphics

- **from (Input):** SVG, SVGZ, EMF, WMF, AI, EPS¹, PS¹, CDR², VSD², CGM², ODG², FODG²।
- **to (Output):** Vector PDF, PNG এবং অন্যান্য Raster Images, SVG ↔ SVGZ, SVG → DXF/DWG, PDF → EPS/PS¹, SVG → EMF, WMF, ODG²।

### ৩. PDF Documents

- **from (Input):** PDF।
- **to (Output):** DOCX, HWPX, TXT, PNG, JPG, TIFF, CBZ, SVG²; সাথে রয়েছে Merge, Split এবং Page Ranges নির্ধারণের চমৎকার সুবিধা।

### ৪. Text Documents

- **from (Input):** DOCX, DOCM, DOTX, EML, Outlook MSG, DOC², ODT², FODT², OTT², RTF², WPS², WPD², Pages², ClarisWorks², MacWrite², T602²।
- **to (Output):** PDF, DOCX, HWPX, EPUB, TXT, HTML; এবং MSG → EML, ODT², FODT², OTT²।

### ৫. Spreadsheets

- **from (Input):** XLSX, XLSM, XLS², XLT², ODS², CSV, TSV, OTS², FODS², Numbers², ET²।
- **to (Output):** PDF, XLSX, ODS, CSV, TSV, JSON, HWPX, HTML, XLT², OTS²।

### ৬. Presentations

- **from (Input):** PPTX, PPTM, POTX, PPSX, PPT², ODP², OTP², FODP², Keynote²।
- **to (Output):** PDF, PNG, JPG, DOCX, HWPX, OTP²।

### ৭. HWP / HWPX

- **from (Input):** HWP, HWPX।
- **to (Output):** PDF, PNG, DOCX, HWPX ↔ HWP, TXT, Markdown, HTML।

### ৮. Text & Markup

- **from (Input):** TXT, Markdown, HTML, reStructuredText³, LaTeX³, Org³, AsciiDoc³, Typst³, MediaWiki³, DocBook³, Jupyter³, Textile³, man³, OPML³।
- **to (Output):** PDF, DOCX, HWPX, EPUB, Formats-গুলোর নিজেদের মধ্যে Interface/Interchange, এবং PPTX Slides³।

### ৯. E-Books

- **from (Input):** EPUB, KEPUB, MOBI⁴, AZW3⁴, AZW⁴, AZW4⁴, FB2, CBZ, CBR, CB7, HTMLZ, TXTZ, LIT⁴, LRF⁴, CHM⁴, PDB⁴।
- **to (Output):** PDF, EPUB, KEPUB (Kobo), DOCX, TXT, HTML, HWPX, MOBI⁴, AZW3⁴।

### ১০. Video

- **from (Input)⁵:** MP4, MOV, MKV, WEBM, AVI, WMV, FLV, MPEG, TS, M2TS, 3GP, OGV, VOB।
- **to (Output):** MP4 (H.264, HEVC, AV1 Codecs), WEBM, MOV, MKV, AVI, GIF, APNG, MP3, M4A, 720p Resolution, Subtitles (SRT, ASS, WebVTT)।

### ১১. Audio

- **from (Input)⁵:** MP3, M4A, AAC, WAV, FLAC, OGG, OPUS, WMA, AIFF, AMR, APE, WavPack, TTA, DSD (DSF, DFF), DTS, AC3, E-AC3।
- **to (Output):** MP3, M4A (AAC, ALAC), WAV, FLAC, OGG, OPUS, AAC, WavPack, TTA, W64, AC3, E-AC3।

### ১২. Subtitles

- **from (Input):** SRT, ASS/SSA, WebVTT, SAMI (SMI), LRC, TTML, MicroDVD, SCC।
- **to (Output):** UTF-8 Encoding সহ একে অপরের মধ্যে রূপান্তর (Korean CP949 Font File সঠিকভাবে Read করতে পারে)।

### ১৩. Archives

- **from (Input):** ZIP, 7Z, RAR, TAR, TAR.GZ, TAR.BZ2, TAR.XZ, GZ, ISO, CAB, DMG, ALZ, EGG।
- **to (Output):** Extract, ZIP, 7Z, TAR, TAR.GZ; যেকোনো Multiple Files → একটি ZIP File।

### ১৪. CAD

- **from (Input):** DWG, DXF।
- **to (Output):** PDF, SVG, PNG, DWG ↔ DXF।

### ১৫. Fonts

- **from (Input):** TTF, OTF, WOFF, WOFF2, EOT।
- **to (Output):** প্রতিটি Font Format-এর মধ্যে Inter-Change।

### ১৬. Data

- **from (Input):** JSON, JSON Lines, YAML, TOML, XML, vCard।
- **to (Output):** Data Formats-গুলোর নিজেদের মধ্যে রূপান্তর, CSV এবং XLSX (Table Data-তে), vCard ↔ CSV।

### ১৭. 3D Models

- **from (Input):** GLB, glTF, STL, OBJ (+ MTL), 3MF, PLY।
- **to (Output):** 3D Model Formats-গুলোর নিজেদের মধ্যে রূপান্তর এবং PNG Preview Generate করা।

### Conversion Engines-এর Footnotes ও কারিগরি ব্যাখ্যা

উপরের তালিকায় যেসব Formats-এর পাশে কোনো বিশেষ নম্বর চিহ্নিত নেই, সেগুলো Filee-র নিজস্ব Light-Weight Native Code দিয়ে কোনো External Software ছাড়া সরাসরি কাজ করে। তবে বিশেষ চিহ্নযুক্ত Formats-গুলোর জন্য Filee Optional Engines ব্যবহার করে, যা User যখন সেই কাজ Select করবেন কেবল তখনই on-Demand Download-এর অনুমতি চায়:

- **¹ Ghostscript:** PS এবং EPS PostScript File Process করার জন্য।
- **² LibreOffice:** জটিল Proprietary ও Legacy Office File রূপান্তরের জন্য।
- **³ Pandoc:** Advanced Text, Markdown ও Document Structuring-এর জন্য।
- **⁴ calibre:** E-Book-এর জটিল Format Encoding-এর জন্য।
- **⁵ FFmpeg:** সমস্ত Audio, Video Media File ও Subtitle Encoding-এর জন্য।

Engines-গুলোর সমস্ত বিস্তারিত তথ্য ও Configuration পাওয়া যাবে Project-এর `ENGINES.md` Documentation-এ।

## ৫. বিভিন্ন Operating System-এ Installation Guidelines

![বিভিন্ন Operating System-এ Installation Guidelines](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_4aa6eaba7c21e5e4fa7613bc80e4c558.jpg)

Filee Download-এর জন্য ব্যবহার করতে হবে এর Official GitHub-এর Releases Section। Operating System ভেদে Installation নির্দেশাবলী নিচে বিশদভাবে আলোচনা করা হলো:

```
 ┌─────────────────────────────────────────┐ │ Filee Installation │ └────────────────────┬────────────────────┘ │ ┌─────────────────────────────┼─────────────────────────────┐ ▼ ▼ ▼ [Windows 10/11] [macOS 14+] [Linux x64/ARM64] • Setup.exe / Portable • osx-arm64 / osx-x64 •./install.sh (Python 3) • Adds Explorer Menu •./install.sh • X11 for Drag Gestures • Adds CLI &amp; Autostart • Privacy: "Open Anyway" • Wayland: Drop Zone/Menu
```

### Windows 10/11 Users-দের জন্য:

- **Installer Version:** `Filee-<version>-win-Setup.exe` File-টি Run করুন। Filee Install হওয়ার সময় File Explorer-এর Right-Click Explorer Menu যুক্ত করা, System-এ Sign-in করার সময় Autostart হওয়া, System-এ `filee` Command Set করা এবং প্রয়োজনীয় Optional Engines যুক্ত করার সুব্যবস্থা প্রদান করে।
- **Portable Version:** কোনো প্রকার Installation ছাড়া সরাসরি ব্যবহার করতে চাইলে `win-Portable.zip` Unzip করে সরাসরি `Filee.exe` চালালেই হবে।

### macOS 14+ (Preview) Users-দের জন্য:

- আপনার Mac-এর Processor Type অনুযায়ী `osx-arm64` (Apple Silicon M1/M2/M3) অথবা `osx-x64` (Intel) Package Download করে Unpack করুন এবং Terminal-এ `./install.sh` Run করুন।
- *Security Note:* Project-টির Release Build এখনো Apple দ্বারা Notarized করা হয়নি। তাই প্রথমবার App চালু করার সময় আপনার Mac-এর **System Settings → Privacy & Security → Open Anyway** Option বেছে নিয়ে চালুর অনুমতি দিতে হবে।

### Linux x64/ARM64 (Preview) Users-দের জন্য:

- Package Unpack করে Terminal-এ `./install.sh` Run করুন (এর জন্য কোনো Root Permission-এর প্রয়োজন নেই, তবে System-এ Python 3 Install থাকতে হবে)।
- *Display Note:* Cursor-এর Gesture ব্যবহার করে Drag And Drop করার জন্য System-এ **X11** Display Server প্রয়োজন। আপনি যদি **Wayland** Display Server ব্যবহার করেন, তবে Cursor Gesture-এর বদলে Filee-র Dedicated Drop Zone অথবা File Manager-এর Right-Click Menu ব্যবহার করতে হবে।

### Auto-Update সুবিধা

Filee তার Menu Bar-এ নতুন Release-এর Update Notification প্রদর্শন করে এবং User-এর ব্যক্তিগত Settings ও Install করা Engine-এর File অক্ষুণ্ণ রেখে নিজেকে স্বয়ংক্রিয়ভাবে Update করতে পারে।

## ৬. Command Line Interface (CLI) Masterclass

![Command Line Interface (CLI) Masterclass](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_45f4712a10a52153786ae95bcf366d5b.jpg)

Developer এবং Power Users-দের কাজের সুবিধার্থে Filee প্রদান করে একটি পূর্ণাঙ্গ Command Line Interface। System-এ Filee Install করার সময় Setup বা `./install.sh` Command-টি Path-এ Add করে দেয়, যা Filee-র সমস্ত Native Engine ও Preset ব্যবহার করে Terminal থেকেই File Process করতে সক্ষম।

```
 $ filee convert photo.heic -to jpg $ filee convert *.png -to webp -quality 80 -o converted $ filee watch D:\Inbox -to pdf -move-originals
```

### গুরুত্বপূর্ণ CLI Commands-এর উদাহরণ ও ব্যবহার:

1. **একটি HEIC ছবিকে সরাসরি JPG-তে Convert করা:**

   ```
   filee convert photo.heic -to jpg
   ```
2. **একসাথে সমস্ত PNG ছবিকে ৮০% Quality-তে WebP বানিয়ে নির্দিষ্ট একটি Folder-এ পাঠানো:**

   ```
   filee convert *.png -to webp -quality 80 -o converted
   ```
3. **একটি নির্দিষ্ট Folder Background-এ Watch করা, File এলে স্বয়ংক্রিয়ভাবে PDF করা এবং মূল File সরাতে:**

   ```
   filee watch D:\Inbox -to pdf -move-originals
   ```

Command Line-এর সমস্ত Commands ও Options দেখতে Visit করুন `filee.sh/cli` Site-এ অথবা Terminal-এ Run করুন `filee help`।

## ৭. Developer Ecosystem & Source Building Guide

![Developer Ecosystem & Source Building Guide](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_778ecc853ac44ea4fda71d26448a1947.jpg)

আপনি যদি একজন.NET Developer হন এবং Filee Project-টির Code দেখতে বা এতে অবদান রাখতে চান, তবে.NET 10 SDK ব্যবহার করে খুব সহজেই এটি Build করতে পারবেন:

### Source Code Build করার ধাপসমূহ:

```
</p>

<h1>Project Clone করুন</h1>

<p>git clone https://github.com/KnifeLemon/Filee.git</p>

<h1>Project Directory-তে প্রবেশ করুন</h1>

<p>cd Filee</p>

<h1>প্রয়োজনীয় Optional Engine Fetch করতে (যেমন: rhwp, pandoc)</h1>

<p>pwsh build/fetch-engines.ps1 -Only rhwp, pandoc</p>

<h1>App Run করতে</h1>

<p>dotnet run -project src/Filee.App</p>

<h1>Test Suite Run করতে</h1>

<p>dotnet test
```

Development সম্পর্কিত গভীর Guidelines-এর জন্য Repository-র Documentation-গুলো পড়ুন:

- `ARCHITECTURE.md` (Architecture বোঝা)
- `ENGINES.md` (Conversion Engine-এর কাজ)
- `ADDING-A-CONVERTER.md` (নতুন Converter যুক্ত করা)
- `ADDING-A-LANGUAGE.md` (নতুন Language যোগ করা)
- `CONTRIBUTING.md` (অবদান রাখার নিয়মাবলী)

Project-টিতে Pull Requests সাদরে গ্রহণ করা হয়। Filee যদি আপনার অমূল্য সময় বাঁচিয়ে দেয়, তবে Project-এর GitHub Repository-তে একটি ⭐ (Star) দেওয়ার অনুরোধ জানানো হয়েছে।

## ৮. Code Signing Policy এবং Security স্বচ্ছতা

![Code Signing Policy এবং Security স্বচ্ছতা](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_a20e3e64ca682e85ea0de4a01cf330a5.jpg)

User-এর নিরাপত্তা ও Software Trust নিশ্চিত করতে Developer অত্যন্ত স্বচ্ছতার সাথে Code Signing Policy প্রকাশ করেছেন:

- **Developer ও প্রকাশক:** Filee Project-টির মূল স্বত্বাধিকারী ও Publisher হলেন **Myeonggu Kim** (**KnifeLemon**)।
- **Windows Code Signing:** Windows-এর জন্য Release Packages-গুলো Myeonggu Kim-এর নামে Issue করা একটি **Certum Open Source Code Signing Certificate** দিয়ে Digitally Sign করা হবে। বর্তমানে Digital Certificate-টি Issue হওয়ার প্রক্রিয়ায় থাকায় Windows SmartScreen Installation-এর সময় সতর্কতা দেখাতে পারে (এ ক্ষেত্রে "More info" → "Run anyway" Option বেছে নিতে হবে)।
- **macOS Code Signing:** Mac-এর Release Packages-গুলো Ad-Hoc Signed করা এবং এগুলো এখনো Notarized নয়।
- **Security Guarantee:** কেবল Installer এবং এই Repository-র **GitHub Actions Release Workflow** দিয়ে Build হওয়া Files-গুলোই Manually Review-এর মাধ্যমে Sign করা হয়। Bundled থাকা Third-Party Software-গুলো (যেমন: rhwp, 7-Zip) তাদের মূল Publisher-এর Digital File ও Signature বজায় রাখে।

## ৯. স্বকীয় ও স্বচ্ছ Privacy Policy

![স্বকীয় ও স্বচ্ছ Privacy Policy](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_bd46313245b46bdb9691e76b5f8298b2.jpg)

Filee সম্পূর্ণভাবে User Privacy বজায় রেখে কাজ করে। এটি আপনার নিজস্ব PC-র Hardware ব্যবহার করে File Process করে এবং কোনো File কখনো কোনো Server-এ Upload করে না। এটি কোনো Usage Data সংগ্রহ করে না এবং কোনো ধরনের Telemetry বা Tracking পাঠায় না।

এটি কেবল নিচের ৩টি নির্দিষ্ট কাজ ছাড়া কখনোই Internet-এর সাথে সংযোগ স্থাপন করে না:

1. App চালু হওয়ার পরপর এবং প্রতি কয়েক ঘণ্টা পর পর নতুন কোনো Version এসেছে কিনা তা জানার জন্য GitHub API (`api.github.com`)-এ Request পাঠাতে। (এটি বন্ধ করতে চাইলে: Settings → About Section-এ গিয়ে "Check for updates automatically" Option-টির টিকচিহ্ন তুলে দিন)।
2. User যখন নিজে কোনো Optional Conversion Engine Install করার সিদ্ধান্ত নেন, তা `engines.json` File-এ Pin করে রাখা Official Link থেকে Download করতে।
3. আপনি যখন App-এর ভেতর কোনো Link-এ Click করেন, যা আপনার PC-র Web Browser Open করে।

## ১০. Sponsorship ও Support Channels-সমূহ

![Sponsorship ও Support Channels-সমূহ](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_4890e216ccb1bc740dad31af3b3fcc6d.jpg)

Filee একটি সম্পূর্ণ Free Project এবং এটি চিরকাল Free থাকবে। আপনি যদি Development-এর এই ধারাবাহিকতা বজায় রাখতে অবদান রাখতে চান, তবে বিভিন্ন মাধ্যমে Support পাঠাতে পারেন:

- **Sponsorship Channels:** GitHub Sponsors, Patreon, Ko-fi, PayPal, এবং Fairy (যা Korean Cards ও Easy-pay Support করে)।
- **Sponsor Perks:** Monthly Backers-দের নাম এবং Sponsors-দের Logo Filee-র README File এবং App-এর About Page-এ প্রদর্শন করা হয়। এককালীন Support প্রদানকারীরাও চাইলে Sponsor তালিকায় নাম যুক্ত করার জন্য On-Request জানাতে পারেন।

## ১১. Licensing এবং সার্বিক তথ্য

![Licensing এবং সার্বিক তথ্য](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_99700c31ba68e1b81d9e6dc9f3fdb785.jpg)

Filee Project-টি উন্মুক্ত MIT License-এর অধীনে প্রকাশিত (© 2026 Myeonggu Kim / KnifeLemon এবং Filee Contributors)। Project-এ Bundled থাকা Third-Party উপাদানের নিজস্ব License রয়েছে, যা `THIRD-PARTY-NOTICES.md` File-এ বিশদভাবে উল্লেখ আছে। Project-টির Statistics ও Popularity Graph দেখতে `star-history.com` Reference সংযুক্ত রয়েছে।

## শেষ কথা

![শেষ কথা](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_742abdf657f4b9471730de389757a976.jpg)

File Conversion-এর চিরাচরিত ঝামেলা, Privacy চিন্তা এবং ভারী Software-এর নির্ভরশীলতা এক নিমেষেই মুছে দিতে Filee হতে পারে আপনার নিত্যদিনের কাজের সেরা সঙ্গী। কোনো Third-Party Site-এ File Upload না করে সম্পূর্ণ Offline-এ, নিরাপদে এবং দ্রুত File Convert করতে আজই Try করে দেখুন অসাধারণ এই Open-Source App-টি! আর Project-টি ভালো লাগলে এর GitHub Repository-তে একটি ⭐ (Star) দিয়ে Developer-কে অনুপ্রাণিত করতে ভুলবেন না!
