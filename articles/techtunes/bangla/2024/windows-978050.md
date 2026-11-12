---
archive_id: techtunes-978050
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 978050
title: Windows 10, 11 এ যেভাবে SmartScreen এনেবল ডিজেবল করবেন
slug: windows-978050
language: bn
status: publish
published_at: '2024-10-15T14:06:00+00:00'
modified_at: '2024-10-03T14:08:00+00:00'
original_url: https://www.techtunes.io/windows/tune-id/978050
author: সোহানুর রহমান
author_url: https://www.techtunes.io/tuner/sohanur-raihan
categories:
- উইন্ডোস
tags:
- Tips টিপস
- অনলাইন ভাইরাস
- এন্টিভাইরাস
content_hash: 3dd6ce108202f2027cec2db0d0b873e6271f06a8c7290379e5b9977964075dc9
archived_at: '2026-11-12T12:03:08.557622+00:00'
---

আসসালামু আলাইকুম, কেমন আছেন টেকটিউনস কমিউনিটি? আশা করছি সবাই ভাল আছেন। আমিও ভালো আছি। আজকে আবার হাজির হলাম আপনাদের জন্য নতুন টিউন নিয়ে। তাহলে চলুন শুরু করা যাক।

উইন্ডোজ সিকিউরিটি সলিউশনের একটি অংশ হচ্ছে Microsoft Defender SmartScreen। একটি কমন থ্রেড এর বিপক্ষে আপনাকে ওয়ার্নিং দেবে। ইন্টারনেট থেকে বা অন্য কারো পিসি থেকে কোন ম্যালিসিয়াস ফাইল যেন ডাউনলোড বা ইন্সটল না হয় সেজন্য আপনাকে ওয়ার্নিং দেখাবে।

SmartScreen ডিফল্ট ভাবেই পিসিতে এনেবল থাকে এবং এতে সমস্যা হচ্ছে কখনো কখনো জেনুইন ফাইলকেও এটি ম্যালিসিয়াস বলতে পারে। কোন সমস্যা নেই আপনি চাইলে খুব সহজেই এই SmartScreen কিন্তু ডিজেবল করতে পারেন। আজকের টিউনে SmartScreen ডিজেবল নিয়ে আলোচনা হবে।

## Windows SmartScreen Filter কীভাবে কাজ করে?

SmartScreen মূলত অপ্রত্যাশিত ওয়েবসাইট এবং অ্যাপ থেকে পিসিকে বাঁচতে Reputation Based Protection এর উপর নির্ভর করে। যখন ফিচারটি এনেবল থাকবে তখন আপনি যখন কোন কিছু ডাউনলোড করবেন তখন SmartScreen চেক করে দেখবে এটা কোন ম্যালিসিয়াস ওয়েবসাইট বা ডেভেলপারের ফাইল কিনা। যদি ম্যালিসিয়াস ডেভেলপারের ফাইল হয় তবে আপনাকে ওয়ার্নিং দেখাবে। এটি ডাউনলোড ব্লক এবং সাইটের এক্সেস ও রেস্ট্রিক্ট করার ক্ষমতা রাখে। SmartScreen পিসিকে ওয়েবসাইট এমনকি অ্যাপ স্টোরের কম সুনামধন্য অ্যাপ গুলো ব্লক করতেও সাহায্য করবে।

SmartScreen, Microsoft Edge সিকিউরিটি সেটিং এরও পার্ট। Microsoft Edge  এ এটি এনেবল করে দিলে কম্পিউটারকে আপনি ম্যালিসিয়াস ওয়েবসাইট এবং ফিশিং ওয়েবসাইট থেকে বাঁচতে পারবেন৷

চলুন দেখে নেয়া যাক কীভাবে SmartScreen ডিজেবল করা যায়,

## ১. উইন্ডোজ সিকিউরিটি সেটিংস থেকে SmartScreen ডিজেবল করা

উইন্ডোজ সেটিং থেকে আপনি সহজেই SmartScreen ইইচ্ছেমতো কনফিগারেশন করতে পারবেন।

Win+I প্রেস করে Settings এ যান

![](https://dnc.techtunes.io/tDrive/tuner/2023/12/techtunes_e6ce936d0a3ad04fc512404566b49e58.png)

বামপাশের ট্যাব থেকে Privacy and Security > Windows Security এ ক্লিক করুন

![](https://dnc.techtunes.io/tDrive/tuner/2023/12/techtunes_ebec73615bf1220eaea48e6c5d611d9e.png)

এবার  App & browser control  এ ক্লিক করুন।

![](https://dnc.techtunes.io/tDrive/tuner/2023/12/techtunes_c1146fded6eb0b98e43da8fad5dc29c0.png)

Reputation-based protection এর নিচ থেকে Reputation Based Protection এ ক্লিক করুন।

![](https://dnc.techtunes.io/tDrive/tuner/2023/12/techtunes_19d53dceb9756185f3c02d826eb2e4b3.png)

এবার এখানে আপনি SmartScreen কে বিভিন্ন ভাবে কনফিগারেশন করতে পারবেন। আপনি ফাইল এবং অ্যাপ ফিল্টার অফ করতে, **Check apps and files  এবং Potentially unwanted app blocking** দুটি অপশন অফ করে দিন। বাকি দুইটি Microsoft Edge এবং Microsoft Store apps নিয়ে।

![](https://dnc.techtunes.io/tDrive/tuner/2023/12/techtunes_68748f6c67c81602e7cfc58350123925.png)

যদি SmartScreen পুরোপুরি অফ করে দিতে চান তাহলে চারটি ফিল্টারই ডিজেবল করে দিন।

## ২. Microsoft Edge থেকে কীভাবে SmartScreen ডিজেবল করবেন

Microsoft Edge এ এই ফিচারটি ডিফল্ট ভাবেই এনেবল করা থাকে। আপনি যদি এটি অফ করতে চান তাহলে নিচের ধাপ গুলো ফলো করুন,

Microsoft Edge ওপেন করে থ্রিডটে ক্লিক করুন

![](https://dnc.techtunes.io/tDrive/tuner/2023/12/techtunes_5992007152697df6ad3a11b85489e6cd.png)

Settings > Privacy,  search, and services  যান নিচে স্ক্রুল করে Security সেকশনে যান।

![](https://dnc.techtunes.io/tDrive/tuner/2023/12/techtunes_cc07dcaf5d06f6f4ce012a30141ece61.png)

Microsoft Defender SmartScreen অপশনটি অফ করে দিন। Block potentially unwanted apps  অপশনটিও অফ হয়ে যাবে। Microsoft Defender SmartScreen এনেভল করলে ম্যানুয়ালি আবার Block potentially unwanted apps এনেবল করতে হবে।

এছাড়াও Windows Security অ্যাপ এবং Registry এডিট করেও Microsoft Edge এর SmartScreen ডিজেবল করতে পারেন৷

### Windows Security অ্যাপ থেকে ডিজেবল করা

Win+R প্রেস করে লিখুন **windowsdefender://**, **Windows Security**  ওপেন হবে।

![](https://dnc.techtunes.io/tDrive/tuner/2023/12/techtunes_d3a3e20157ee8ded2c3a8d805a55a3ff.png)

বামপাশ থেকে App & browse control এ ক্লিক করুন

![](https://dnc.techtunes.io/tDrive/tuner/2023/12/techtunes_e0d4f04e35b377475796f1e0cf29b834.png)

**Reputation-based protection settings এ ক্লিক করুন**

![](https://dnc.techtunes.io/tDrive/tuner/2023/12/techtunes_ac372cacd2584dfa79b71bc851823dfb.png)

**SmartScreen for Microsoft Edge** অফ করে দিন।

![](https://dnc.techtunes.io/tDrive/tuner/2023/12/techtunes_3fcab118222d0a93273cb17e5b798bf1.png)

### Registry এডিটর দিয়ে অফ করা

Win+ R প্রেস করুন regedit লিখে Ok ক্লিক করুন

1. ```
   HKEY_CURRENT_USER\Software\Microsoft\Edge\SmartScreenEnabled
   ```

এই লোকেশনে যান। Default এ Modify এ ক্লিক করুন। ভ্যালু হিসেবে 1 দিয়ে Ok প্রেস করুন

![](https://dnc.techtunes.io/tDrive/tuner/2023/12/techtunes_da35c07233e580c7fdff1f23e56d1c06.png)

পিসি রিস্টার্ট দিন, কাজ শেষ।

## Internet Properties থেকে ডিজেবল করা

আপনি চাইলে Internet Properties থেকে SmartScreen ডিজেবল করতে পারবেন।

Win+Run প্রেস করুন। Control লিখে ok প্রেস করুন। Control panel এ প্রবেশ করবে। Large icons সিলেক্ট করুন। Internet Options এ ক্লিক করুন।  Advanced ট্যাব থেকে **Enable Windows Defender SmartScreen আনচেক করে দিন।**

![](https://dnc.techtunes.io/tDrive/tuner/2023/12/techtunes_9d314fd207c1640f0e0f20b43935194d.png)

Apply এ ক্লিক করে ok তে ক্লিক করুন

উইন্ডোজ এর নতুন ভার্সন গুলোতে এনেবল ডিজেবল অপশন নাও পেতে পারেন। আমার Windows 11 এ অপশনটি নেই। সেক্ষেত্রে পরের মেথড ফলো করুন,

### Registry এডিটের মাধ্যমে SmartScreen ডিজেবল করা

Internet Properties থেকে SmartScreen ডিজেবল না করতে পারলে Registry থেকে এটি ডিজেবল করতে পারবেন।

Win+R প্রেস করে লিখুন Regedit এবং লিখুন

লোকেশনে ন্যাভিগেট করুন

1. ```
   HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System
   ```

ডান পাশে দেখুন **EnableSmartScreen** আছে কিনা।

![](https://dnc.techtunes.io/tDrive/tuner/2023/12/techtunes_4ab1e84911a43626898c68eb28b1fa7a.png)

না থাকলে নতুন ভ্যালু ক্রিয়েট করতে হবে। ক্রিয়েট করতে System এ ক্লিক করে রাইট ক্লিক করুন এবং New এ ক্লিক করে **DWORD (32-bit) Value** সিলেক্ট করুন।  **EnableSmartScreen** এর নাম দিন। এবং Modify এ ক্লিক করে এর ভ্যালু দিন 0 এবং সেভ করে দিন। পরবর্তীতে এটি এনেবল করতে ভ্যালু 1 দিন।

আপনি চাইলে String Value ক্রিয়েট করে আরও দুটি অপশন এনেবল করতে পারেন যেমন Warn অথবা Block। Warn এর মাধ্যমে আপনি ওয়ার্ন পাবেন আর ব্লকের মাধ্যমে সরাসরি অ্যাপ ব্লক হয়ে যাবে। System থেকে New এ ক্লিক করে String Value তে ক্লিক করুন এবং নাম দিন  **ShellSmartScreenLevel।** এবার এটি Modify এ ক্লিক করুন। Warn অথবা Block লিখে সেভ করুন।

## Groupe policy এর মাধ্যমে ডিজেবল করা

Win + R ক্লিক করে লিখুন gpedit.msc ওকে করে গ্রুপ পলিসি ওপেন করুন।

1. ```
   Computer Configuration > Administrative Templates > Windows Components > File Explorer.
   ```

লোকেশনে যান। ![](https://dnc.techtunes.io/tDrive/tuner/2023/12/techtunes_358ebd2f332d6988163262e89d46a109.png)

রাইট ক্লিক করে এডিট এ ক্লিক করুন। এখানে আপনি ডিজেবল  এনেবল অপশন পেয়ে যাবেন।

![](https://dnc.techtunes.io/tDrive/tuner/2023/12/techtunes_8acd5a30c2794401f2f5d368a86f95c1.png)

Ok তে ক্লিক করে রিস্টার্ট দিন।

## শেষ কথা

উইন্ডোজের SmartScreen ফিচারটি ভালই তবে কখনো আপনার প্রয়োজনীয় অ্যাপ ইন্সটল করতে সমস্যা তৈরি করতে পারে, সেক্ষেত্রে এটি ডিজেবল করাই বুদ্ধিমানের কাজ হবে। আশা করছি এই টিউনটির মাধ্যমে আপনি সহজের SmartScreen ফিল্টার ডিজেবল করতে পারবেন।

তো আজকে এই পর্যন্তই, কেমন হল আজকের টিউন তা অবশ্যই টিউমেন্টের মাধ্যমে জানাবেন। পরবর্তী টিউন পর্যন্ত ভাল থাকুন, আল্লাহ হাফেজ।
