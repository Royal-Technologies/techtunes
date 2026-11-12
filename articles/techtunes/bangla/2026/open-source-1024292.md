---
archive_id: techtunes-1024292
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 1024292
title: "ArtCraft Launcher – \uFEFFAdobe-এর একচেটিয়া সাম্রাজ্য গুঁড়িয়ে দিতে চলে এলো\
  \ ArtCraft Launcher এবং Craft Apps! Rust দিয়ে তৈরি 12 Free Open-Source Apps, Claude\
  \ Opus 55 AI সাপোর্ট, WASM, CLI এবং 1-Click Install ফিচার্স নিয়ে এটি যেন টেক দুনিয়ায়\
  \ এক মহাপ্রলয়!"
slug: open-source-1024292
language: bn
status: publish
published_at: '2026-11-06T13:20:00+00:00'
modified_at: '2026-11-06T13:20:00+00:00'
original_url: https://www.techtunes.io/open-source/tune-id/1024292
author: মো আতিকুর ইসলাম
author_url: https://www.techtunes.io/tuner/atikurofficial
categories:
- ওপেন সোর্স
tags:
- এডোবি ফটোসপ
- ওপেন সোর্স টুল
- ওপেন সোর্স সফটওয়ার
content_hash: 5b2b748e71b58bf432e61806508775d042ec2c23f9c781912f7742bafea40dcd
archived_at: '2026-11-12T10:15:49.000505+00:00'
---

Craft Apps হলো ArtCraft Team-এর Rust Programming Language দিয়ে একদম শুরু থেকে (Ground Up) তৈরি করা ১২টি Free ও Open-Source Desktop Software-এর একটি স্যুট, যা Photoshop, Premiere Pro-এর মতো ব্যয়বহুল Adobe Software-এর বিকল্প হিসেবে বিকাশ করা হয়েছে। আর ArtCraft Launcher হলো একটি ছোট Management Program, যা Windows, macOS, এবং Linux-এ এই সফটওয়্যারগুলো এক জায়গায় সেন্ট্রালি Install এবং Update করতে সাহায্য করে।

## ১. ব্যাকগ্রাউন্ড ও পটভূমি: Adobe-এর সাবস্ক্রিপশন যন্ত্রণা এবং Rust-এর বৈপ্লবিক উত্থান

![ArtCraft Launcher](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_82c341484bef905666154efac5275a34.png)

আজকের ডিজিটাল ক্রিয়েটিভ ওয়ার্ল্ডে কনটেন্ট ক্রিয়েটর, ডিজাইনার, বা ভিডিও এডিটরদের সবচেয়ে বড় ভালোবাসার পাশাপাশি বিরক্তির জায়গা কোনটি? এক বাক্যে উত্তর—Adobe-এর কড়া Subscription System। প্রতি মাসে ভারী অঙ্কের ফি দিয়ে সফটওয়্যার ব্যবহার করা তো একপ্রকার বাধ্যতামূলক হয়ে দাঁড়িয়েছেই, কিন্তু আসল বিপত্তি দেখা দেয় যদি আপনি কখনো চুক্তির মাঝপথে Subscription Cancel করতে যান। তখন Adobe এমন চড়া অঙ্কের Cancellation Fee দাবি করে যে ক্রিয়েটরদের পকেট খালি হওয়ার জোগাড় হয়!

এই দীর্ঘদিনের সমস্যা ও ক্ষোভের এক অভিনব প্রযুক্তিগত জবাব নিয়ে হাজির হয়েছেন ডেভেলপার Brandon Thomas এবং তাঁর নেতৃত্বাধীন ArtCraft Team। 2026 সালের October মাসে তাঁরা একযোগে প্রকাশ করেছেন ফ্রি ও ওপেন সোর্স সফটওয়্যারের এক বিশাল সিরিজ।

প্রযুক্তি জগতের জন্য সবচেয়ে চমকপ্রদ তথ্য হলো, এই সফটওয়্যারগুলোর পুরো কোডবেস কোনো তৈরি ফ্রেমওয়ার্ক বা পুরনো কোড ছাড়াই, একদম জিরো থেকে Rust Programming Language দিয়ে লেখা হয়েছে। মিডিয়া রিপোর্টে প্রকাশ পেয়েছে, এই বিশাল সফটওয়্যার কোডবেস তৈরির Development Process-এ সহায়তা করার জন্য ব্যবহার করা হয়েছে অত্যাধুনিক AI Model—Claude Opus 5.5!

এই সম্পূর্ণ নতুন সিরিজটির নাম দেওয়া হয়েছে Craft Apps। এটি মূলত Photoshop, Illustrator, Premiere Pro-এর মতো জনপ্রিয় Adobe Software-এর সরাসরি বিকল্প বা Alternative হিসেবে ডেভেলপ করা হয়েছে। বর্তমানে এদের Official Website-এ সফটওয়্যার সংখ্যা বাড়িয়ে ১২টিতে উন্নীত করা হয়েছে, যার মধ্যে শুধু গ্রাফিক্স বা ভিডিও নয়—যুক্ত করা হয়েছে Word Processing, Spreadsheet, Presentation, CAD এবং Audio Editing Software-ও!

এখন প্রশ্ন হলো, এতগুলো আলাদা আলাদা Applications ব্যবহার করতে চাইলে কি আপনাকে GitHub-এ গিয়ে একটা একটা করে Installation File খুঁজে নামাতে হবে? মোটেও না! ডেভেলপার টিম এর সমাধান হিসেবে ArtCraft Launcher নামে একটি ছোট Management Program নিয়ে এসেছে, যার কাজ হলো সমস্ত সফটওয়্যার এক জায়গায় জমা রাখা এবং সহজেই সেগুলোকে ইনস্টল ও আপডেট করা।

আজকের এই ব্লগে আমরা শুরুতেই নামগুলোর বিভ্রান্তি পরিষ্কার করব, এরপর ১২টি Craft Apps-এর বিস্তারিত তালিকা জানব এবং ধাপে ধাপে ArtCraft Launcher ব্যবহারের কৌশল শিখব।

### ArtCraft Launcher

অফিসিয়াল ওয়েবসাইট @ [ArtCraft Launcher](https://getartcraft.com/apps)

## কীভাবে ArtCraft Launcher এবং Craft Apps ব্যবহার করবেন?

![কীভাবে ArtCraft Launcher এবং Craft Apps ব্যবহার করবেন?](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_8f215abcd6492c149b79e60112c2e16f.jpg)

১. অফিশিয়াল ওয়েবসাইটে প্রবেশ করে "Download Launcher" বাটনে ক্লিক করে আপনার অপারেটিং সিস্টেমের (Windows, macOS বা Linux) জন্য নির্ধারিত ইনস্টলার ফাইলটি নামিয়ে নিন।

![Download Launcher](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_049cc8aac60df7b70314489848a219d0.png)

২. ডাউনলোড করা ফাইলটি ওপেন করে সাধারণ নিয়মে আপনার কম্পিউটারে ArtCraft Launcher ইনস্টল ও রান করুন।

![ArtCraft Launcher ইনস্টল ও রান](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_1a82062a8908e479c18be3a5b70afe75.png)

৩. লঞ্চার চালু হলে প্রদর্শিত ক্রাফট অ্যাপসের তালিকা থেকে আপনার প্রয়োজনীয় সফটওয়্যারটির (যেমন: PhotoCraft বা PdfCraft) নিচে থাকা "Install" বাটনে ক্লিক করুন।

![Install](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_6850085d54ffeaaaadc57ad7a2782701.png)

৪. লঞ্চার ব্যবহার করতে না চাইলে ওয়েবসাইটে নির্দিষ্ট সফটওয়্যারের বর্ণনার নিচে থাকা "View in GitHub" লিংকে গিয়ে Releases পেজ থেকে সরাসরি সিঙ্গেল ইনস্টলার ফাইল ডাউনলোড করে নিন।

![View in GitHub](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_8955b78eaf1b92dce77a3ffddd16384d.png)

ইনস্টলেশন সম্পন্ন হওয়ার পর আপনার অপারেটিং সিস্টেমের অ্যাপ্লিকেশন মেনু বা ফোল্ডার থেকে সরাসরি সফটওয়্যারটি ওপেন করে কাজ শুরু করুন।

## ২. প্রারম্ভিক অস্পষ্টতা নিরসন: ArtCraft, ArtCraft Launcher এবং Craft Apps-এর পার্থক্য

![ArtCraft, ArtCraft Launcher এবং Craft Apps-এর পার্থক্য](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_23a15e7b5b7fecc2b884d88b3c64db19.jpg)

প্রথমবার ArtCraft ইকোসিস্টেমে পা রাখলে নামগুলোর কাছাকাছি বানানের কারণে মাথা গুলিয়ে যাওয়া অস্বাভাবিক কিছু নয়। বিভ্রান্তি এড়াতে নিচের ছকটি ভালো করে দেখে নিন:

| Name | What it is | Remarks |
| --- | --- | --- |
| ArtCraft | মূল Development Team এবং সামগ্রিক Brand নাম | Official Website: `getartcraft.com` |
| ArtCraft App | টিমটির আসল প্রাথমিক Product, যা একটি AI Image ও Video Generation Studio | ব্যবহার করতে Account লাগে, AI Generation-এর জন্য Paid Points প্রয়োজন। এটি আমাদের আজকের আর্টিকেলের আলোচ্য বিষয় নয়。 |
| ArtCraft Launcher | এটি একটি Installation & Update Tool, যা Craft Apps সেন্ট্রালি ইনস্টল করতে সাহায্য করে | এর নিজস্ব কোনো Image Editing বা Generation Feature নেই। |
| Craft Apps (Crafting Apps) | ১২টি আলাদা Desktop Software-এর একটি স্যুট (যেমন: PhotoCraft, PdfCraft) | সম্পূর্ণ Free ও Open-Source। Launcher দিয়ে ইনস্টল করা যায় অথবা আলাদা Download করা যায়。 |

সহজ ভাষায় ব্যাখ্যা করলে: ArtCraft Launcher হলো আপনার কম্পিউটারের জন্য একটি "সফটওয়্যার স্টোর প্লাস আপডেটার", Craft Apps হলো এর ভিতরের আসল সফটওয়্যারগুলো (অর্থাৎ PhotoCraft, PdfCraft, WordCraft ইত্যাদি), আর ArtCraft App হলো টিমটির সম্পূর্ণ আলাদা একটি AI Generation Product Line।

```
+-+
| ArtCraft |
| (Overall Brand &amp; Team) |
+-+-+ | +-+-+ | | [ArtCraft App] [Craft Apps] (Paid AI Generator) (12 Free Open-Source Apps)</p>

<ul>
<li>Needs Account &amp; Points |</li>
<li>2D/3D Editing &amp; Posing Installed &amp; Managed by:
[ArtCraft Launcher]
```

⚠️ বিশেষ সতর্কবার্তা:  
 আপনি যদি প্রথমবার ভুল করেন, তবে হয়তো ভুল করে ArtCraft Launcher-এর জায়গায় ArtCraft App ডাউনলোড করে ফেলবেন! স্ক্রিনে একটি AI Image & Video Generation Studio দেখতে পাবেন, যেখানে 2D/3D Editing, Character Posing ইত্যাদি ফিচার রয়েছে এবং বিভিন্ন AI Model কানেক্ট করা যায়। এটি ওপেন করার পর ইন্টারফেস দেখতে আমাদের আজকের আলোচ্য ArtCraft Launcher-এর থেকে সম্পূর্ণ আলাদা হবে। তাই ভুল সফটওয়্যার ডাউনলোড করা থেকে বিশেষভাবে সতর্ক থাকুন!

## ৩. Craft Apps কী? ১২টি সফটওয়্যারের ইন-ডেপথ গাইড

![Craft Apps কী? ১২টি সফটওয়্যারের ইন-ডেপথ গাইড](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_61766bca548c03365fdde25aa20ee4e7.jpg)

অফিসিয়াল ডকুমেন্টেশন অনুযায়ী, প্রতিটি Craft Apps একদম জিরো থেকে Rust দিয়ে লেখা হয়েছে। এগুলো আপনার সিস্টেমে Native Execution হিসেবে চলে এবং কোনো মেমোরি-হাংরি Electron Framework ব্যবহার করে না!

বর্তমানে অফিশিয়াল ওয়েবসাইটে যে ১২টি সফটওয়্যার তালিকাবদ্ধ করা হয়েছে, তাদের বিবরণ নিচে দেওয়া হলো:

| Software | Purpose | Target Alternative |
| --- | --- | --- |
| PhotoCraft | Image Editing এবং PSD Support | Photoshop |
| VectorCraft | Vector Drawing ও ডিজাইন | Illustrator |
| FilmCraft | Video Editing, Color Grading এবং Audio Effects | Premiere Pro |
| LightCraft | Photo Management এবং RAW Processing | Lightroom |
| PdfCraft | PDF Reading, Organizing, Merging, Splitting ও Annotations | Acrobat *(প্রাথমিক রিপোর্টে একে PrintCraft বলা হয়েছিল)* |
| EffectCraft | Motion Graphics এবং Visual Effects | After Effects |
| DesignCraft | Layout ও Publishing | InDesign |
| WordCraft | Word Processing | Official Website-এ লেখা নেই *(মিডিয়া এটিকে Word-এর মতো বলেছে)* |
| GridCraft | Spreadsheet এবং Data Analysis | Official Website-এ লেখা নেই *(মিডিয়া এটিকে Excel-এর মতো বলেছে)* |
| DeckCraft | Presentation ডিজাইন | Official Website-এ লেখা নেই *(মিডিয়া এটিকে PowerPoint-এর মতো বলেছে)* |
| CADCraft | Computer-Aided Design (CAD) এবং ড্রয়িং | Official Website-এ লেখা নেই *(প্রচলিত CAD Software-এর বিকল্প)* |
| SoundCraft | Audio Recording, Editing এবং Mixing | Official Website-এ লেখা নেই *(প্রচলিত DAW / Audio Software-এর বিকল্প)* |

অনুলিখিত শেষের পাঁচটি সফটওয়্যার কোন Commercial Software-এর বিকল্প, তা Official Website-এ সরাসরি লেখা না থাকলেও টেক মিডিয়া এগুলোকে যথাক্রমে Word, Excel, PowerPoint, CAD এবং Audio Software-এর বিকল্প বলেই অভিহিত করেছে।

### 🛠️ Craft Apps-এর সাধারণ কারিগরি সুবিধাসমূহ:

1. **Cross-Platform Support:** এগুলো **Windows**, **macOS**, এবং **Linux** অপারেটিং সিস্টেমে নির্বিঘ্নে চলে। তাছাড়া **FilmCraft** বাদে বাকি ১১টি সফটওয়্যারের **WebAssembly (WASM)** ব্রাউজার সংস্করণও রয়েছে!
2. **Open-Source License:** কোডবেসটি **MIT** অথবা **Apache 2.0 Dual License**-এর অধীনে প্রকাশ করা হয়েছে এবং সমস্ত **Source Code** **GitHub**-এ পাবলিক করা আছে।
3. **Zero Learning Curve:** সফটওয়্যারগুলোর **Interface**, **Menu** এবং **Shortcuts** হুবহু অরিজিনাল **Adobe Software**-এর মতো করে তৈরি করা হয়েছে, যাতে ইউজারদের নতুন করে কাজ শিখতে কষ্ট করতে না হয়।
4. **Automation & AI Ready:** প্রতিটি সফটওয়্যার **Command Line (CLI)**, **JSON Control Channel**, এবং **MCP Server** সাপোর্ট করে। ফলে ডেভেলপাররা খুব সহজেই **AI Agent** বা **Automation Script** দিয়ে এগুলো স্বয়ংক্রিয়ভাবে পরিচালনা করতে পারবেন।

## ৪. ArtCraft Launcher কী এবং এর সিস্টেম রিকোয়ারমেন্ট

![ArtCraft Launcher কী এবং এর সিস্টেম রিকোয়ারমেন্ট](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_44482de204f2b8b8899563a10aeb2b25.jpg)

ArtCraft Launcher হলো একই টিমের তৈরি একটি ছোট কিন্তু অত্যন্ত শক্তিশালী Manager Program। macOS সিস্টেমে এটি আপনার Menu Bar-এ সবসময় তৈরি হয়ে বসে থাকে।

### এর প্রধান ৩টি ফিচার:

- **One-Click Installation:** লঞ্চারের ভেতরে সফটওয়্যারের নিচে থাকা "Install" বাটনে ক্লিক করলেই ফাইল নামিয়ে ইনস্টল হয়ে যায়।
- **Centralized Update:** আপনার কম্পিউটারের সব **Craft Apps**-কে এক ক্লিকে সর্বদা **Latest Version**-এ আপডেট রাখে।
- **Menu Bar Resident:** আপনার স্ক্রিনের ওপরের **Menu Bar Icon** থেকে "Show ArtCraft Launcher"-এর পাশাপাশি মূল ওয়েবসাইট, **GitHub**, এবং **Discord Community**-র ডিরেক্ট লিংক পাওয়া যায়।

### 💻 System Requirements (2026-এর October-এর অফিশিয়াল তথ্য অনুযায়ী):

| System | Requirement |
| --- | --- |
| Windows | Windows 10 এবং Windows 11 |
| macOS | macOS 11 Big Sur বা তার পরবর্তী ভার্সন |
| Linux | x86\_64 এবং aarch64 আর্কিটেকচার, glibc 2.35 বা তার ওপরে (যেমন: Ubuntu 22.04+, Debian 12+, Fedora 36+) |

## ৫. ArtCraft Launcher ব্যবহারের টিউটোরিয়াল (macOS Example)

![ArtCraft Launcher ব্যবহারের টিউটোরিয়াল](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_36edad43c57cc008efb17d417a57f8e6.jpg)

নিচে macOS সিস্টেমের উদাহরণ দিয়ে টিউটোরিয়ালটি সাজানো হলো (এর জন্য macOS 11 Big Sur বা তার ওপরের ভার্সন লাগবে):

### Step 1: Download Launcher

প্রথমে Craft Apps-এর অফিশিয়াল ওয়েবসাইটে (`getartcraft.com/apps`) যান। সেখানে থাকা কালো রঙের "Download Launcher" বাটনে ক্লিক করুন। ব্রাউজার স্বয়ংক্রিয়ভাবে আপনার অপারেটিং সিস্টেম চিনে নিয়ে GitHub থেকে সঠিক DMG File ডাউনলোড করে দেবে।

### Step 2: Drag & Open Launcher

ডাউনলোড করা DMG File-টি ওপেন করে ArtCraft Launcher আইকনটিকে ধরে "Applications" Folder-এ ড্র্যাগ করে ছেড়ে দিন। macOS-এর `spctl` কম্যান্ড দিয়ে ফাইলটি সিকিউরিটি চেক করা হয়েছে এবং এটি সম্পূর্ণ ভেরিফাইড পাওয়া গেছে। প্রথমবার চালু করার সময় সিকিউরিটি অ্যালার্ট দেখালে "Open" বাটনে ক্লিক করুন।

### Step 3: Click Install

ArtCraft Launcher ওপেন করলে এটি একটি Management Center হিসেবে দেখা দেবে। আপনার যে সফটওয়্যারটি পছন্দ, সেটির নিচে থাকা "Install" বাটনে ক্লিক করুন। লঞ্চার স্বয়ংক্রিয়ভাবে সঠিক ফাইল ডাউনলোড করে আপনার Applications Folder-এ অ্যাপটি ইনস্টল করে দেবে। আপনার সব অ্যাপ একবারে ইন্সটল করার কোনো দরকার নেই—আপনার যা প্রয়োজন (যেমন: PhotoCraft বা PdfCraft), শুধু সেটিই নামিয়ে নিন।

### Step 4: Direct Download Option (Bypass Launcher)

আপনি যদি লঞ্চার ইনস্টল করতে না চান, তবে কোনো সমস্যা নেই! Crafting Apps পেজ থেকে নির্দিষ্ট সফটওয়্যারের ডেসক্রিপশনের নিচে থাকা "View in GitHub" বাটনে ক্লিক করুন। এটি আপনাকে সেই সফটওয়্যারের GitHub Repository-তে নিয়ে যাবে, সেখান থেকে "Releases" সেকশনে গিয়ে সরাসরি সিঙ্গেল Installer File ডাউনলোড করে নিতে পারবেন।

## ৬. ইনস্টল করার পর কোন অ্যাপ দুটি আগে টেস্ট করে দেখবেন?

![ইনস্টল করার পর কোন অ্যাপ দুটি আগে টেস্ট করে দেখবেন?](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_85c31b0dd44b5d41d74062b03b64a884.jpg)

বর্তমানে ১২টি সফটওয়্যারের মধ্যে কেবল ২টি সফটওয়্যারে "Early Alpha" লেবেল দেওয়া হয়েছে, অর্থাৎ এগুলো বাকিগুলোর চেয়ে কিছুটা বেশি তৈরি ও স্থিতিশীল। এগুলো হলো PhotoCraft এবং PdfCraft।

### 🎨 PhotoCraft পরীক্ষা করার অভিজ্ঞতা:

PhotoCraft টেস্ট করার পর দেখা গেছে যে, এটি দেখতে সত্যিই চমৎকার এবং এতে Traditional Chinese Interface-ও রয়েছে! এটি চালু হওয়ার স্পিড অত্যন্ত দ্রুত এবং বেশ লাইটওয়েট।

- **Features:** এটি **Layered PSD File** ওপেন, এডিট এবং সেভ করতে পারে। এতে **Layer Adjustment**, **Layer Style**, **Text Layer** এবং লোকাল পিসিতে এগজিকিউট হওয়া **Smart Selection** ফিচার রয়েছে।
- **⚠️ Warning:** তবে অ্যাপটির অফিশিয়াল **README** ফাইলে ডেভেলপাররা স্পষ্ট লিখে দিয়েছেন যে, *এটি কিন্তু এখনও Photoshop-এর পূর্ণাঙ্গ বিকল্প নয় এবং দৈনন্দিন পেশাদার কাজের জন্য এটি ব্যবহারের উপযোগী নয়*।
- **অনলাইন বিকল্প:** আপনার যদি এখনই ব্রাউজারে ব্যবহারযোগ্য একটি **PSD Supported Editor** লাগে, তবে আপনি **Photopea Free Image Editor** ব্যবহার করতে পারেন।

### 📄 PdfCraft পরীক্ষা করার অভিজ্ঞতা:

Acrobat-এর বিকল্প হিসেবে তৈরি PdfCraft দিয়ে আপনি PDF Reading, Page Organizing, Merging, Splitting, Real-Time Search, এবং Annotations প্রয়োগ করতে পারবেন। এটি পাসওয়ার্ড সুরক্ষার Password Protected File-ও ওপেন করতে পারে।

- **ফ্রি বিকল্প:** আপনার যদি এখনই কাজের জন্য একটি ভালো **Free PDF Editing Tool** প্রয়োজন হয়, তবে **JOPDF Free PDF Editor** (Traditional Chinese Interface সহ) অথবা **Stirling PDF Free PDF Editor** দেখতে পারেন।

## ৭. ব্যবহার করার আগে অত্যন্ত জরুরি কিছু সতর্কতা

![ব্যবহার করার আগে অত্যন্ত জরুরি কিছু সতর্কতা](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_dbc7dc819ec31f2be875c19c8a8482c9.jpg)

এই চমৎকার ওপেন সোর্স প্রজেক্টটি ব্যবহার করার আগে কিছু গুরুত্বপূর্ণ বিষয় মাথায় রাখা অত্যন্ত জরুরি:

1. **Early Alpha Stage:** অধিকাংশ অ্যাপই এখনো প্রাথমিক **Alpha Stage**-এ রয়েছে। অ্যাপে প্রচুর অপূর্ণতা এবং বাগ থাকতে পারে। তাই **সাময়িকভাবে এটিকে আপনার কাজের Main Workhorse বা প্রধান সফটওয়্যার বানাবেন না**। তবে প্রজেক্টটির আপডেট স্পিড বেশ ফাস্ট।
2. **Legal & Clean Room Risks:** ডেভেলপাররা বলেছেন এগুলো **Rust** দিয়ে জিরো থেকে লেখা, কিন্তু তারা কোনো **Clean Room Development**-এর স্পষ্ট ব্যাখ্যা বা প্রমাণ দেননি। যেহেতু ইন্টারফেসগুলো **Adobe Software**-এর হুবহু নকল, তাই এর আইনি স্থায়িত্ব নিয়ে টেক পাড়ায় বিতর্ক রয়েছে। কোডগুলো **MIT** বা **Apache 2.0 License**-এ থাকলেও, **বাণিজ্যিক প্রজেক্টে বা কোনো Company Environment-এ ব্যবহারের আগে নিজে আইনি ঝুঁকি বা Legal Risk Assessment করে নিন** (২০২৬ সালের অক্টোবর মাসের তথ্যানুযায়ী)।
3. **Free Scope Clear-up:** **ArtCraft Launcher** এবং **Craft Apps** শতভাগ ফ্রি। তবে বিভ্রান্ত হয়ে **ArtCraft App**-এর **AI Generation Service** ব্যবহার করতে যাবেন না, কারণ সেখানে পয়েন্ট ও টাকা লাগে।

## ৮. Frequently Asked Questions (FAQ)

![FAQ](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_6bd59ad56d07a9fde3a285e0b9487bdc.jpg)

প্রশ্ন ১: Craft Apps ইন্সটল করার জন্য কি অবশ্যই ArtCraft Launcher ব্যবহার করতে হবে?  
 উত্তর: একদমই না! প্রতিটি সফটওয়্যারের GitHub Releases Page-এ আলাদা আলাদা Installation File দেওয়া আছে। লঞ্চার কেবল সহজে এক জায়গায় ম্যানেজ করার জন্য তৈরি।

প্রশ্ন ২: ArtCraft Launcher কি সম্পূর্ণ বিনামূল্যে পাওয়া যায়?  
 উত্তর: হ্যাঁ, অফিশিয়াল তথ্য অনুযায়ী Craft Apps এবং ArtCraft Launcher ডাউনলোডের জন্য কোনো টাকা দিতে হয় না। এগুলো MIT বা Apache 2.0 License-এর অধীনে সম্পূর্ণ ফ্রি।

প্রশ্ন ৩: Launcher কোন কোন অপারেটিং সিস্টেম সাপোর্ট করে?  
 উত্তর: Windows 10/11, macOS 11 Big Sur বা তার নতুন ভার্সন, এবং Linux (x86\_64 ও aarch64, glibc 2.35+)।

প্রশ্ন ৪: ১২টি সফটওয়্যারই কি এখন সঠিকভাবে ব্যবহার করা সম্ভব?  
 উত্তর: না, আপাতত কেবল PhotoCraft এবং PdfCraft কিছুটা ব্যবহারের উপযোগী (Early Alpha)। বাকি ১০টি এখনো ডেভেলপিং স্টেজে আছে।

প্রশ্ন ৫: ArtCraft Launcher এবং ArtCraft App-এর মধ্যে পার্থক্য কী?  
 উত্তর: Launcher কেবল ফ্রি Craft Apps ইনস্টল ও আপডেট করে। আর ArtCraft App হলো একটি পয়েন্ট-ভিত্তিক পেইড AI Image & Video Generation Tool। দুটি সম্পূর্ণ ভিন্ন প্রোডাক্ট।
