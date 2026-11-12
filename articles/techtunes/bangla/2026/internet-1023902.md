---
archive_id: techtunes-1023902
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 1023902
title: Pingora Proxy Manager – Cloudflare Pingora এবং Rust-ভিত্তিক High-Performance
  Zero-Downtime Reverse Proxy
slug: internet-1023902
language: bn
status: publish
published_at: '2026-11-06T09:55:00+00:00'
modified_at: '2026-11-06T09:55:00+00:00'
original_url: https://www.techtunes.io/internet/tune-id/1023902
author: মো আতিকুর ইসলাম
author_url: https://www.techtunes.io/tuner/atikurofficial
categories:
- ইন্টারনেট
tags:
- ওপেন সোর্স
- ওয়েবসার্ভার
content_hash: 0f7f4f72cfa2c7ec1df4c225a81f3efa34a9f01044f123aca1d16a7733648e7e
archived_at: '2026-11-12T11:34:21.671163+00:00'
---

আজকের আধুনিক Digital World-এ আপনি যদি একজন Web Developer, System Administrator বা DevOps Engineer হয়ে থাকেন, তবে আপনার কাজের সবচেয়ে গুরুত্বপূর্ণ অংশগুলোর একটি হলো Server-এর Traffic প্রবাহকে সঠিকভাবে নিয়ন্ত্রণ করা। যখন কোনো ওয়েবসাইট বা Web Application-এ হাজার হাজার User একসাথে প্রবেশ করেন, তখন Traffic-কে সঠিক Backend Services বা Upstream Servers-এ পাঠিয়ে দেওয়া এবং একই সাথে Security নিশ্চিত করার দায়িত্ব পালন করে একটি Reverse Proxy।

কিন্তু প্রথাগত Reverse Proxy ব্যবহার করতে গিয়ে আমরা প্রায় সবাই একটি অত্যন্ত বিরক্তিকর সমস্যার মুখোমুখি হয়ে থাকি। যখনই সিস্টেমের কোনো Configuration পরিবর্তন করা হয়, যেমন—নতুন কোনো Host যোগ করা, Routing Rule পরিবর্তন করা কিংবা SSL Certificates আপডেট করা—তখন পরিবর্তনগুলো প্রয়োগ করার জন্য Process Reload বা Restart দিতে হয়। আর ঠিক এই Reload-এর সময়টুকুর মধ্যেই অনাকাঙ্ক্ষিতভাবে কিছু Active Connections কেটে যায়, কিংবা কিছু সময়ের জন্য Server Service দিতে ব্যর্থ হয়, যাকে আমরা Downtime বলি।

এই চিরচেনা সমস্যার এক চমৎকার ও ভবিষ্যৎমুখী Solution নিয়ে এসেছে Pingora Proxy Manager (PPM)। Cloudflare-এর নিজস্ব প্রযুক্তিতে তৈরি বিশ্বখ্যাত Pingora Framework এবং অতি নিরাপদ Rust Programming Language-এর ওপর ভিত্তি করে এটি তৈরি করা হয়েছে। আজকের এই সুবিশাল Masterclass Blog-এ আমরা Pingora Proxy Manager-এর ভেতরে থাকা প্রতিটি Technical Feature, এর Installation প্রক্রিয়া, Advanced Networking Control এবং Development Guide-সহ সমস্ত তথ্য একদম বিস্তারিত ও গভীরভাবে বিশ্লেষণ করবো।

## Overview – পিঙ্গোরা প্রক্সি ম্যানেজার কী এবং কেন এটি বিশেষ

![](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_7882a902cdd37f1483bd979ebfd25c93.png)

Pingora Proxy Manager হলো একটি Next-Generation Reverse Proxy Solution, যা মূলত চরম Speed, অটুট Reliability এবং Zero-Downtime-এর নিশ্চয়তা দেওয়ার জন্য Design করা হয়েছে।

বিশ্বের অন্যতম বৃহত্তম Content Delivery Network (CDN) Provider Cloudflare এতদিন ধরে তাদের মূল Infrastructure-এ Nginx ব্যবহার করে আসছিল। কিন্তু পরবর্তীতে তারা চরম Memory দক্ষতা এবং Multi-Threading Performance পাওয়ার জন্য নিজেদের তৈরি Pingora Engine ব্যবহার শুরু করে, যা Rust ভাষায় লেখা। Pingora Proxy Manager মূলত এই শক্তিশালী Engine-এর ওপর ভিত্তি করেই গড়ে উঠেছে।

এটি Rust-এর Raw Performance এবং Cloudflare Pingora Engine-এর দ্রুতগতিকে একটি অত্যন্ত আকর্ষণীয় ও ব্যবহারবান্ধব Dashboard-এর সাথে যুক্ত করেছে। এর Admin Dashboard-টি তৈরি করা হয়েছে React 19 এবং Tailwind CSS দিয়ে। ফলে এটি কেবল Backend-এই শক্তিশালী নয়, বরং Frontend-এও Interface-এর দিক থেকে অত্যন্ত সুবিধাজনক।

### Zero-Downtime Reloading কীভাবে কাজ করে?

প্রথাগত Reverse Proxy-তে Configuration পরিবর্তন করতে গেলে Worker Processes Restart নিতে হয়। কিন্তু Pingora Proxy Manager-এর Architecture এমনভাবে তৈরি করা হয়েছে যে, এতে রয়েছে Zero-Downtime Configuration Reloading সুবিধা। এর অর্থ হলো, যখনই আপনি নতুন কোনো Virtual Host যুক্ত করবেন, Path Routing বদলাবেন কিংবা SSL Certificates আপডেট করবেন, সিস্টেম Memory-তে সরাসরি Routing Tables আপডেট করে নেবে। এর ফলে Process Restart দেওয়ার প্রয়োজন পড়ে না এবং আপনার Server-এ থাকা কোনো Client Connection বা Active Session বিন্দুমাত্র Drop হয় না।

### Pingora Proxy Manager

অফিসিয়াল ওয়েবসাইট @ [Pingora Proxy Manager](https://github.com/DDULDDUCK/pingora-proxy-manager)

## Features – এর প্রতিটি মূল ফিচারের গভীর বিশ্লেষণ

![Features – এর প্রতিটি মূল ফিচারের গভীর বিশ্লেষণ](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_34ca4ee0f998c0b46d1773b06237c285.jpg)

Pingora Proxy Manager-কে আধুনিক Development ও Production Environment-এর উপযোগী করে তোলার জন্য এতে অনেকগুলো শক্তিশালী Features যুক্ত করা হয়েছে। নিচে প্রতিটি Feature-এর In-Depth বিবরণ দেওয়া হলো:

### ১. ⚡️ High Performance

এটি Rust এবং Pingora দ্বারা চালিত। Rust-এ কোনো Garbage Collection-এর Process না থাকায় এতে Memory Leak বা হঠাৎ স্লো হয়ে যাওয়ার ভয় নেই। এর ফলে এটি আপনাকে দেয় Ultra-Low Latency এবং অবিশ্বাস্য রকমের High Throughput, যা বিশাল Traffic অনায়াসে সামলাতে পারে।

### ২. 🔄 Zero-Downtime Architecture

এর Dynamic Architecture Process Restart ছাড়াই লাইভ Service চলাকালীন সময়ে Dynamically সব Configuration Changes প্রসেস করে নেয়।

### ৩. 🔒 SSL Automation & Wildcard Support

Certificate Automation-এর জন্য এতে Let's Encrypt Integrated করা হয়েছে। এটি Domain মালিকানা প্রমাণের জন্য HTTP-01 Challenge এবং Subdomain বা একাধিক Domain-এর জন্য DNS-01 (Wildcard SSL) Challenge পুরোপুরি Support করে।

### ৪. 🌐 Proxy Hosts Management

খুব সহজেই একটি সুন্দর Dashboard থেকে Virtual Hosts, Path Routing এবং Advanced URL Rewriting মেইনটেইন ও Configure করা যায়।

### ৫. 📡 L4 Streams (TCP/UDP Forwarding)

এটি শুধু সাধারণ HTTP/HTTPS Traffic-এই সীমাবদ্ধ নয়। এটি Layer 4 বা L4 Streams Support করে। ফলে Databases, Game Servers, কিংবা যেকোনো Non-HTTP Services-এর জন্য TCP এবং UDP Forwarding খুব সহজেই Setup করা যায়।

### ৬. 🛡️ Access Control & Security

আপনার Private Services-গুলোকে সুরক্ষিত রাখতে আপনি নির্দিষ্ট IP-কে অনুমতি দিতে IP Whitelist এবং Block করতে IP Blacklist তৈরি করতে পারেন। এছাড়া বাড়তি সুরক্ষার জন্য এতে রয়েছে Basic Authentication ব্যবস্থা।

### ৭. 📊 Real-time Stats & Monitoring

লাইভ Dashboard-এ বসে আপনি Live Traffic Monitoring করতে পারবেন। কতগুলো অনুরোধ আসছে, সেগুলোর Status Codes কেমন এবং অতীতে Traffic-এর গতি কেমন ছিল, তা ঐতিহাসিক Data Visualization এবং গ্রাফের মাধ্যমে দেখতে পাবেন।

### ৮. 🐳 Docker Ready & Single Container

এটি সম্পূর্ণ Docker Ready। চমৎকার Memory Optimization-এর কারণে এর Footprint খুবই ছোট এবং পুরো সিস্টেমটি মাত্র একটি Single Container হিসেবে Deploy করা যায়।

## Quick Start – ডকার কম্পোজ দিয়ে দ্রুত ইনস্টলেশন এবং ডিপ্লয়মেন্ট গাইড

![Quick Start – ডকার কম্পোজ দিয়ে দ্রুত ইনস্টলেশন এবং ডিপ্লয়মেন্ট গাইড](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_7e9a7d2bb92dc72edd6cc042ba5e1e35.jpg)

Pingora Proxy Manager Deploy করার সবচেয়ে সহজ এবং Standard পদ্ধতি হলো Docker Compose ব্যবহার করা।

### Step 1: `docker-compose.yml` ফাইল তৈরি করা

আপনার Server-এ একটি Directory তৈরি করে তার ভেতর `docker-compose.yml` নামে একটি File তৈরি করুন এবং নিচের Code-টি হুবহু লিখুন:

```
services: pingora-proxy: image: dduldduck/pingora-proxy-manager:latest container<em>name: pingora-proxy restart: always network</em>mode: host # Recommended for performance &amp; L4 streams volumes: -./data:/app/data # Database &amp; Certs -./letsencrypt:/etc/letsencrypt # Certbot account, renewal, and live cert state -./logs:/app/logs # Access Logs environment: - JWT<em>SECRET=changeme</em>in<em>production</em>please - RUST_LOG=info
```

#### Docker Configuration-এর প্রতিটি লাইনের গভীর বিশ্লেষণ:

- **Image:** `dduldduck/pingora-proxy-manager:latest` নির্দেশ করে যে এটি Docker Hub থেকে Official Latest Image-টি Pull করবে।
- **Container Name:** Container-টির নাম দেওয়া হয়েছে `pingora-proxy`।
- **Restart Policy:** `restart: always` দেওয়ার ফলে Server কোনো কারণে Reboot হলেও Container-টি নিজে থেকেই Automatic চালু হয়ে যাবে।
- **Network Mode:** এখানে `network_mode: host` ব্যবহার করার জন্য বিশেষভাবে পরামর্শ দেওয়া হচ্ছে। Host Network Mode ব্যবহার করলে Container-টি সরাসরি Host Server-এর Network Stack ব্যবহার করে। ফলে কোনো Network Address Translation (NAT) Overhead থাকে না, যা সর্বোচ্চ Performance এবং Layer 4 TCP/UDP Streams পরিচালনার জন্য অপরিহার্য।
  - **Bridge Mode বিকল্প:** আপনি যদি Host Mode ব্যবহার করতে না চান এবং Bridge Mode ব্যবহার করতে বাধ্য হন, তবে আপনাকে Container-এর Port Mapping নিশ্চিত করতে হবে। সেক্ষেত্রে আপনাকে Container-এ Port `80:8080` (HTTP), Port `443:443` (HTTPS) এবং Port `81:81` (Admin Dashboard) Map করে দিতে হবে।
- **Volume Mounts:**
  1. `./data:/app/data`: এখানে PPM-এর Database এবং Generate হওয়া Certificates স্থায়ীভাবে জমা থাকে।
  2. `./letsencrypt:/etc/letsencrypt`: এখানে Certbot Account-এর তথ্য, Certificate Renewal State এবং Live SSL Certificate-এর File সঞ্চিত থাকে।
  3. `./logs:/app/logs`: এখানে সমস্ত Access Logs জমা থাকে।
- **Environment Variables:**
  1. `JWT_SECRET`: Admin Dashboard-এর Sign-in Session-এর Security নিশ্চিত করার জন্য JWT Token Secret। Production Environment-এ অবশ্যই `changeme_in_production_please`-এর জায়গায় একটি কঠিন Password দেবেন।
  2. `RUST_LOG`: সিস্টেম Log Level নির্ধারণ করে, যা এখানে `info` দেওয়া হয়েছে।

#### Let's Encrypt পোর্টের কার্যপ্রণালী:

Let's Encrypt সঠিকভাবে কাজ করার জন্য `./data:/app/data` এবং `./letsencrypt:/etc/letsencrypt` দুটি Volume-ই Mounted রাখা আবশ্যিক। HTTP-01 Validation সম্পন্ন করার সময় বাইরের Let's Encrypt Server Host Port `80`-তে Hit করে। PPM Container স্বয়ংক্রিয়ভাবে সেই অনুরোধকে Container-এর ভেতরের Internal Port `8080`-এ পাঠায় এবং Validation সম্পন্ন করে।

### Advanced Upstream Controls – অ্যাডভান্সড নেটওয়ার্ক এবং টাইমআউট কনফিগারেশন

যেকোনো Reverse Proxy-এর ক্ষেত্রে Upstream Server বা মূল Application Server-এর সাথে Connection Timeout সঠিকভাবে Manage করা অত্যন্ত গুরুত্বপূর্ণ। Pingora Proxy Manager-এ Dashboard-এর UI থেকেই প্রতিটি Proxy Host এবং Location-এর জন্য আলাদা আলাদা Advanced Upstream Overrides Configure করা যায়:

- `connection_timeout_ms`: Upstream Server-এর সাথে Handshake বা Connection তৈরির সর্বোচ্চ সময় (মিলিসেকেন্ডে)।
- `read_timeout_ms`: Upstream Server থেকে Data পড়ার সর্বোচ্চ অপেক্ষা (মিলিসেকেন্ডে)।
- `write_timeout_ms`: Upstream Server-এ Data পাঠানোর সর্বোচ্চ সময় (মিলিসেকেন্ডে)।
- `max_request_body_bytes`: Container-এ আসা অনুরোধের সর্বোচ্চ Size Limit (বাইটে)।

#### Default Values ও বিশেষ নিয়ম:

যদি আপনি UI-তে এই Field-গুলো খালি রেখে দেন, তবে PPM তার Built-in Default সময়গুলো মেনে চলবে:

- **Connection Timeout Default:** `500ms`
- **Read Timeout Default:** `10000ms`
- **Write Timeout Default:** `5000ms`

Hierarchy ও WebSocket নিয়ম:

1. Location-Level Values সবসময় Host-Level Values-কে Override করবে।
2. তবে এটি মনে রাখা গুরুত্বপূর্ণ যে—Upgrade বা WebSocket Requests-এর ক্ষেত্রে নিরবচ্ছিন্ন Connection বজায় রাখার জন্য Upstream Read এবং Write Timeouts স্বয়ংক্রিয়ভাবে Disabled অবস্থায় থাকে। এর ফলে দীর্ঘদিন ধরে অলস পড়ে থাকা Persistent Connections-ও হঠাৎ কেটে যায় না।

### Optional: If You Run PPM Behind Another Reverse Proxy

অনেক সময় Network Architecture-এ PPM-কে একা রাখা হয় না, বরং Traffic প্রবাহ এমন হয়:  
 `Client -> Cloudflare / Nginx / ALB -> PPM`

যদি PPM অন্য কোনো Proxy বা Load Balancer-এর পেছনে থাকে, তবে Security-র খাতিরে PPM বাই-ডিফল্ট শুধু Loopback (`127.0.0.1`) Connection-কেই Trust করে। এর ফলে আসল User বা Client IP জানার জন্য যে Forwarded Headers পাঠানো হয়, তা PPM গ্রহণ নাও করতে পারে।

এই সমস্যা সমাধানের জন্য আপনাকে `PPM_TRUSTED_PROXY_IPS` (অথবা `TRUSTED_PROXY_IPS`) Environment Variable-এ ঠিক আগের Proxy Hop-এর IP-গুলো নির্দিষ্ট করে দিতে হবে। তাহলেই কেবল PPM `X-Forwarded-For` এবং `X-Forwarded-Proto` Headers বিশ্বাস করবে।

Configuration-এর উদাহরণ:

```
PPM<em>TRUSTED</em>PROXY_IPS=127.0.0.1, 10.0.0.10
```

### Step 2: Service চালনা করা

সব Configuration ঠিক থাকলে Terminal-এ নিচের Command-টি চালিয়ে Container-টি চালু করে দিন:

```
docker compose up -d
```

Command-এর শেষে `-d` দেওয়ার কারণে Container-টি Background-এ Detached Mode-এ চলতে থাকবে।

### Step 3: Admin Dashboard-এ প্রবেশ

Service চালু হয়ে যাওয়ার পর যেকোনো Browser খুলে আপনার Dashboard-এ প্রবেশ করুন:

- **Dashboard URL:** `http://localhost:81` (অথবা আপনার Server-এর Public IP Address সহ Port 81)

Log in করার জন্য প্রাথমিক Credentials:

- **Username:** `admin`
- **Password:** `changeme`

> ⚠️ গুরুত্বপূর্ণ নিরাপত্তা নির্দেশিকা: প্রথমবার সফলভাবে Dashboard-এ প্রবেশ করার সাথে সাথেই Security-র স্বার্থে আপনার Password-টি পরিবর্তন করে নিন!

## Documentation – বিস্তারিত শিখতে গিটহাব উইকি রিসোর্স

![Documentation](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_b64ab546162a6e53e7c76be6caba0f2c.jpg)

প্রজেক্টটি কীভাবে নিখুঁতভাবে ব্যবহার করবেন, তার ওপর একটি বিশাল Documentation Guide তাদের GitHub Wiki Page-এ সংকলিত রয়েছে:

- **Getting Started:** বেসিক Installation এবং প্রথমবার ব্যবহারের নির্দেশিকা।
- **Configuration Guide:** Proxy Hosts তৈরি, SSL Certificate এবং ACLs (Access Control Lists)-এর In-Depth Tutorial।
- **Architecture:** সিস্টেমের ভেতরের Control Plane এবং Data Plane কীভাবে একে অপরের সাথে যোগাযোগ করে তার গভীর বিশ্লেষণ।
- **API Reference:** আপনি যদি কোনো Automation Code দিয়ে PPM নিয়ন্ত্রণ করতে চান, তবে তাদের REST API Integration Guide।
- **FAQ & Troubleshooting:** সচরাচর হওয়া বিভিন্ন সাধারণ জটিলতা এবং সেগুলোর সমাধান।

## Development – সোর্স কোড থেকে ডেভেলপমেন্ট করার পদ্ধতি

![Development – সোর্স কোড থেকে ডেভেলপমেন্ট করার পদ্ধতি](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_e9c1655a5c5c57c084a4797f74771d39.jpg)

আপনি যদি Open-Source Community-র অংশ হিসেবে এতে অবদান রাখতে চান, কিংবা Source Code থেকে ম্যানুয়ালি নিজের মতো Build করতে চান, তবে Native Development Setup অনুসরণ করতে পারেন। দ্রুত কাজের সুবিধার্থে এর Backend এবং Frontend একদম আলাদাভাবে Run করার ব্যবস্থা রয়েছে:

1. **Backend Setup (Rust):** Terminal-এ গিয়ে লিখুন `cd backend && cargo run` (এটি API-এর জন্য Port `81` এবং প্রক্সির জন্য Port `8080`-এ Listen করে)।
2. **Frontend Setup (React/Vite):** অন্য একটি Terminal-এ গিয়ে লিখুন `cd frontend && npm run dev` (এটি Frontend থেকে আসা API Call-গুলোকে Port `81`-এ Proxy করে পাঠিয়ে দেয়)।

আরও বিস্তারিত জানার জন্য Wiki-তে থাকা Development Setup Guide-টি অনুসরণ করতে পারেন।

## Support, Contributing & License – প্রজেক্টে সাপোর্ট এবং লাইসেন্সিং

![Support, Contributing & License – প্রজেক্টে সাপোর্ট এবং লাইসেন্সিং](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_97cfae458a60f6eade013dca4f50ca9c.jpg)

Pingora Proxy Manager প্রজেক্টটি Developer-এর প্রচুর ভালোবাসা, অঢেল Caffeine এবং অজস্র ঘুমহীন রাতের কষ্টের ফসল! এই প্রজেক্টটি যদি আপনার মূল্যবান সময় বাঁচিয়ে দেয় এবং Server Management-কে সহজ করে তোলে, তবে আপনিও প্রজেক্টের Running খরচ মেটাতে এবং নতুন Feature আনার কাজকে উৎসাহিত করতে পারেন। আপনি চাইলেই Buy Me A Coffee (`buymeacoffee.com/dduldduck`) Platform-এর মাধ্যমে Developer-কে এক কাপ Coffee Donate করতে পারেন ☕️।

### অবদানের আহ্বান (Contributing)

একটি Open-Source Community-কে সমৃদ্ধ করতে অবদানের কোনো বিকল্প নেই। আপনি প্রজেক্টটিতে যেকোনো নতুন Feature যুক্ত করতে বা Bug Fix করতে চাইলে তাদের Contributing Guide অনুসরণ করে Pull Request পাঠাতে পারেন।

### লাইসেন্স (License)

এই প্রজেক্টটি পুরোপুরি Open-Source এবং এটি MIT License-এর অধীনে প্রকাশিত। ফলে এটি বিনামূল্যে ব্যবহার বা সংশোধন করার পূর্ণ স্বাধীনতা রয়েছে। Source Code-এর ভেতরে থাকা `LICENSE` File-এ এর সমস্ত আইনি শর্তাবলী পাওয়া যাবে।
