---
archive_id: techtunes-952657
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 952657
title: জেনে নিন Windows 11 এর দারুণ ৪ টি ট্রিকস
slug: windows-952657
language: bn
status: publish
published_at: '2024-05-02T17:19:00+00:00'
modified_at: '2024-04-30T15:22:00+00:00'
original_url: https://www.techtunes.io/windows/tune-id/952657
author: সোহানুর রহমান
author_url: https://www.techtunes.io/tuner/sohanur-raihan
categories:
- উইন্ডোস
tags:
- pc ট্রিকস
- Tips টিপস
- উইন্ডোজে ট্যাবড ব্রাউজিং
content_hash: 766b0e8f3b2bece8fb2cfb9419666e593409e57b5dfa444962bee37f0b6582f7
archived_at: '2026-11-12T12:07:07.192116+00:00'
---

আসসালামু আলাইকুম টেকটিউনস কমিউনিটি, কেমন আছেন সবাই? আশা করছি ভাল আছেন। বরাবরেই মত আজকেও চলে এসেছি নতুন টিউন নিয়ে।

আজকে আমি Windows 11 এর দারুণ তিনটি ট্রিকস নিয়ে আলোচনা করব যেগুলো সম্পর্কে আপনি হয়তো অবগত নন।

## ১. উইন্ডোজ স্ক্রিন-রেকর্ড

![](https://dnc.techtunes.io/tDrive/tuner/2022/12/techtunes_7d6c230a246419f5b8e743bd4e90dda1.png)

প্রায় সময়ই আমাদের উইন্ডোজের স্ক্রিন রেকর্ডের প্রয়োজন পড়ে। এজন্য আমরা ব্যবহার করে অভ্যস্ত থার্ডপার্টি বিভিন্ন অ্যাপ। আপনি চাইলে এই কাজটি কোন ধরনের অ্যাপ ছাড়াই এখন করতে পারেন। আপনি যদি Windows 11 ইউজার হয়ে থাকেন তাহলে এই কাজটি ছোট একটি শর্টকাটের মাধ্যমে করতে পারেন।

প্রেস করুন Win+G, আপনি গেমবার দেখতে পাবেন এখান থেকে আপনার স্ক্রিন রেকর্ডিং শুরু করুন।

## ২. ভয়েস টাইপিং

![](https://dnc.techtunes.io/tDrive/tuner/2022/12/techtunes_6869b3b899c8e1ba55c16521ab2a5c7a.png)

Windows 11 ইউজাররা পাচ্ছে বিল্ড-ইন একটা ভয়েস টাইপিং ফিচার। যেকোনো ডকুমেন্টে Win+H প্রেস করলে আপনার সামনে চলে আসবে ভয়েস টাইপিং ফিচার। যা বলবেন স্বয়ংক্রিয়ভাবে সেটা টাইপ হতে থাকবে

## ৩. মাল্টিপল ট্যাব ওপেন

আপনি অবাক হলেও সত্যি গুগলে ক্রোমের মত আপনি উইন্ডোজ এক্সপ্লোরারেও মাল্টিপল ট্যাব ওপেন করতে পারবেন।

এটা করার জন্য আপনার সিস্টেমে Windows 11 22H2 Stable Build (22621 অথবা পরের ভার্সন) লাগবে। প্রথমেই পিসিতে [ViveTool](https://github.com/thebookisclosed/ViVe/releases), টুলটি সেটআপ করতে হবে।

[ViveTool](https://github.com/thebookisclosed/ViVe/releases)  ডাউনলোড করে Extract করুন।

![](https://dnc.techtunes.io/tDrive/tuner/2022/12/techtunes_2b6205abd0b622201990df01a0741d43.png)

এক্সট্রাক্ট করা ফোল্ডারটিতে রাইট ক্লিক করুন এবং “Copy as path” অপশনটি সিলেক্ট করুন।

![](https://dnc.techtunes.io/tDrive/tuner/2022/12/techtunes_c70e8cbd8d42e7c709ad99f846f38d71.png)

এবার এডমিন রাইট দিয়ে, Command Prompt ওপেন করুন।

![](https://dnc.techtunes.io/tDrive/tuner/2022/12/techtunes_74a185573af2535c12215dbcf9744c3e.png)

Command Prompt এ, cd টাইপ করুন এবং আগে কপি করা কমান্ডটি পেস্ট করুন। আপনার পিসির জন্য এই কমান্ড ভিন্ন হতে পারে। যেমন,  
 "C:\Users\azureuser\Downloads\ViVeTool-v0.3.2"

![](https://dnc.techtunes.io/tDrive/tuner/2022/12/techtunes_84d8e4b64cef9f69cbbe42f4001d5887.png)

নিচের কমান্ডটি এক্সিকিউট করুন, এটি উইন্ডোজ এক্সপ্লোরারে নতুন ট্যাব ওপেন করুন ফিচার এড করবে।

vivetool /enable /id:36354489

![](https://dnc.techtunes.io/tDrive/tuner/2022/12/techtunes_4c11d37355e6d3d972ffc32a736deba5.png)

এবার নিচের কমান্ড দিন এটি উইন্ডোজ এক্সপ্লোরারে SV2Navpane নামে নতুন ন্যাভিগেশন এড করবে

vivetool /enable /id:37634385

![](https://dnc.techtunes.io/tDrive/tuner/2022/12/techtunes_0c8532abc39c1684d2dc8202e15e0482.png)

সর্বশেষ আপনি নিচের কমান্ডটি দিন এবং পিসি রিস্টার্ট করুন  
 vivetool /enable /id:39145991

![](https://dnc.techtunes.io/tDrive/tuner/2022/12/techtunes_16925ba7f457046c303dde8001f55c31.png)

ফাইনালি এনেভল হয়ে গেলে চমৎকার ফিচারটি যা ডার্ক মুডেও দারুণ ভাবে সাপোর্ট করবে। আপনি চাইলে ট্যাব গুলো রিএরেঞ্জ ও করতে পারেন।

![](https://dnc.techtunes.io/tDrive/tuner/2022/12/techtunes_9a2c2051b46a3076eb57e7a4188ecdb0.png)

তবে আপনি যদি কখনো এই ফিচারটি অফ করতে চান তাহলে নিচের কমান্ড গুলো দিন

vivetool /disable /id:36354489  
 vivetool /disable /id:37634385  
 vivetool /disable /id:39145991

## ৪. সিস্টেম ভলিউম কন্ট্রোল

আপনি Windows 11 এ চমৎকার ভাবে সিস্টেম ভলিউম কন্ট্রোল করতে পারবেন। টাস্কবারে ভলিউম আইকনে মাউস পয়েন্টার রাখুন এবং মাউসের স্ক্রুলটি ঘুরান। কি চমৎকার না?

![](https://dnc.techtunes.io/tDrive/tuner/2022/12/techtunes_7873e0552bab15fc79629aa1a8694803.png)

## শেষ কথা

আজকের এই টিউনে যে ট্রিকস গুলো দেখালাম আমি নিশ্চিত আপনি এর যেকোনো একটি সম্পর্কে জানতেন না। আশা করছি সব গুলো ট্রিকসই আপনার ভাল লেগেছে।

বলা যায় এই টিউনে আপনি নতুন কিছু জানতে পেরেছেন, তো আজকে এই পর্যন্তই পরবর্তী টিউন পর্যন্ত ভাল থাকুন আল্লাহ হাফেজ।
