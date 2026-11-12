---
archive_id: techtunes-996757
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 996757
title: Nvidia আনছে DGX Station! ডেস্কটপ কম্পিউটিংয়ের ভবিষ্যৎ কি এটাই?
slug: techtunes-techboom-996757
language: bn
status: publish
published_at: '2025-03-25T03:33:00+00:00'
modified_at: '2025-03-25T03:33:00+00:00'
original_url: https://www.techtunes.io/techtunes-techboom/tune-id/996757
author: টেকটিউনস টেকবুম
author_url: https://www.techtunes.io/tuner/techboom
categories:
- টেকটিউনস টেকবুম
tags: []
content_hash: b0ff2c6c0182044139757cbacaff425f83fd340cc474f984c9b86cb026b27278
archived_at: '2026-11-12T11:53:40.784459+00:00'
---

Nvidia DGX Station এমন একটা ডিভাইস নিয়ে, যা ডেস্কটপ কম্পিউটিংয়ের ধারণাকেই বদলে দিতে পারে। Nvidia DGX Station শুধু একটা নতুন কম্পিউটার নয়, বরং আপনার টেবিলে বসানো একটা আস্ত সুপারকম্পিউটার। চলুন, এর অন্দরমহলের খুঁটিনাটি জেনে আসি।

## DGX Station আসলে কী? পুরনো দিনের PC, নাকি অন্য কিছু?

![Nvidia আনছে DGX Station! ডেস্কটপ কম্পিউটিংয়ের ভবিষ্যৎ কি এটাই?](https://dnc.techtunes.io/tDrive/tuner/2025/03/techtunes_ca97ceb1912aec6db61e302eeda16375.png)

Nvidia-র GTC 2025 ইভেন্টে [DGX Station](https://www.nvidia.com/en-us/products/workstations/dgx-station/)-এর ঘোষণাটা ছিল অনেকের কাছেই বিশাল একটা সারপ্রাইজ। প্রথম দর্শনে এটিকে সাধারণ Tower Computer-এর মতো মনে হলেও, এর ভেতরের ইঞ্জিনিয়ারিং রীতিমতো তাক লাগিয়ে দেওয়ার মতো। এতে ব্যবহার করা হয়েছে ARM-Based CPU, যা সাধারণ ডেস্কটপ PC থেকে এটিকে আলাদা করে তুলেছে।

আগে Nvidia, AMD-র সঙ্গে পার্টনারশিপ করে DGX Station A100 নামে একটি ওয়ার্কস্টেশন বাজারে এনেছিল। কিন্তু সেই মডেলে Nvidia-র নিজস্ব Arm CPU ছিল না, এবং আলাদা PCIe AI Accelerators (A100) এর প্রয়োজন পড়ত। শুধু তাই নয়, সেটির দামও ছিল প্রায় আকাশছোঁয়া - $100, 000 এরও বেশি!

কিন্তু Nvidia DGX Station-এর নতুন মডেলে সেই অসুবিধাগুলো দূর করা হয়েছে।

## কারা DGX Station বানাচ্ছে?

![Nvidia আনছে DGX Station! ডেস্কটপ কম্পিউটিংয়ের ভবিষ্যৎ কি এটাই?](https://dnc.techtunes.io/tDrive/tuner/2025/03/techtunes_40cd4ac29706cf6ae6579863c6c17061.jpg)

এখানেও একটা ইন্টারেস্টিং ব্যাপার আছে। Nvidia একা DGX Station তৈরি করছে না। বরং, Asus, Boxx, Dell, HP, Lambda এবং Supermicro-র মতো প্রথম সারির PC ম্যানুফ্যাকচারাররা এর নিজস্ব ভার্সন তৈরি করবে। তবে Lenovo-কে এই তালিকায় দেখা যাচ্ছে না। কেন নেই, সেই প্রশ্নটা হয়তো অনেকের মনে উঁকি দিচ্ছে।

এবার আসা যাক পাওয়ারের কথায়। DGX Station-এর মূল শক্তি হল GB300 Grace Blackwell Ultra Desktop Superchip। Nvidia-র দাবি অনুযায়ী, এটি "20 PFlops AI পারফরম্যান্স" দিতে সক্ষম। যদিও এই পারফরম্যান্স FP4 With Sparsity ব্যবহার করে মাপা হবে বলেই ধারণা করা হচ্ছে। এখন প্রশ্ন হল, এই Superchip টি আসলে কতটা শক্তিশালী?

বিশেষজ্ঞরা মনে করছেন, GB200 Grace Blackwell Superchip-এর থেকে এর পারফরম্যান্স কিছুটা কম হতে পারে। Nvidia এই বিষয়ে কোনও স্পষ্ট তথ্য না দেওয়ায় ধোঁয়াশা থেকেই যাচ্ছে। কেউ কেউ বলছেন, GB300-এর একাধিক ভার্সন থাকতে পারে। শুধু তাই নয়, Nvidia GB300-তে ঠিক কতগুলো বা কী ধরনের (Arm) CPU কোর ব্যবহার করেছে, সেই বিষয়েও কোনো তথ্য প্রকাশ করেনি। GPU Subsystem নিয়েও তারা মুখে কুলুপ এঁটেছে।

## DGX Station-এর স্পেসিফিকেশন, যা জানা গেছে

![Nvidia আনছে DGX Station! ডেস্কটপ কম্পিউটিংয়ের ভবিষ্যৎ কি এটাই?](https://dnc.techtunes.io/tDrive/tuner/2025/03/techtunes_476c095cfc625d3054a9feaa77ab032c.jpg)

যতদূর জানা গেছে, এর পূর্বসূরি GH200-তে 72টি Arm Neoverse 2 CPU কোর ছিল, যেগুলোর ক্লক স্পিড ছিল 3.1GHz, 144GB HBMe Memory এবং 480GB LPDDR5x Memory ছিল।

নতুন DGX Station-এ 784GB Unified System Memory থাকার কথা। মনে করা হচ্ছে, এর মধ্যে HBM (288GB HBM3e) এর পাশাপাশি Nvidia যাকে ফাস্ট মেমোরি বলছে (সম্ভবত 496GB LPDDR5x) সেটিও থাকবে। এই বিশাল পরিমাণ মেমোরি নিশ্চিত করবে যে DGX Station অনায়াসে জটিল এবং রিসোর্স-ইনটেনসিভ কাজগুলো করতে পারবে।

## নেটওয়ার্কিং স্পিড, ডেটা যেন চোখের পলকে ট্রান্সফার হয়!

![Nvidia আনছে DGX Station! ডেস্কটপ কম্পিউটিংয়ের ভবিষ্যৎ কি এটাই?](https://dnc.techtunes.io/tDrive/tuner/2025/03/techtunes_0c7967524b33a0b7203820406d728939.jpg)

Nvidia আরও জানিয়েছে, DGX Station তাদের নিজস্ব ConnectX-8 SuperNIC ব্যবহার করবে। এই Network Technology ডেটা সেন্টার ক্লাসের 800Gb/s Connectivity দিতে সক্ষম। এই স্পিড এতটাই বেশি যে, বিশাল আকারের ডেটা ট্রান্সফার চোখের পলকেই হয়ে যাবে।

এবার একটু DGX Station-এর চেসিসটা খুলে দেখা যাক। তাহলে চোখে পড়বে তিনটি ফরোয়ার্ড ফেসিং 120mm ফ্যান, তিনটি PCIe স্লটযুক্ত মাদারবোর্ড, একটি Nvidia-ব্র্যান্ডেড সোল্ডার্ড চিপ (সম্ভবত SuperNic) এবং দুটি বড় আনকভারড ডাইস। যার মধ্যে একটি Grace GPU এবং অন্যটিতে আটটি আলাদা টাইলস, Blackwell GPU। এই কম্পোনেন্টগুলো একসঙ্গে কাজ করে DGX Station-কে পাওয়ারফুল এবং একইসঙ্গে কুল রাখতে সাহায্য করবে।

তবে DGX Station-এর Expansion বা স্টোরেজ ক্যাপাবিলিটিস, PSU Capacity, Cooling Solution অথবা দাম সম্পর্কে এখনও পর্যন্ত কিছুই জানা যায়নি। এছাড়াও, DGX Station-এর পারফরম্যান্স আরও বাড়ানোর জন্য H200 NVL (বা B300 NVL)-এর মতো Accelerator Card ব্যবহার করা যাবে কিনা, সেই বিষয়েও Nvidia কোনও তথ্য জানায়নি।

বিশেষজ্ঞরা মনে করছেন, DGX Station, Camino Grando-এর মতো EPYC-পাওয়ার্ড টাওয়ার ওয়ার্কস্টেশনের সঙ্গে জোর টক্কর দেবে। উল্লেখ্য, Camino Grando-তে দুটি AMD CPU এবং আটটি পর্যন্ত GPU রয়েছে।

## Nvidia-র ভবিষ্যৎ পরিকল্পনা, আর কী কী আসছে?

![Nvidia আনছে DGX Station! ডেস্কটপ কম্পিউটিংয়ের ভবিষ্যৎ কি এটাই?](https://dnc.techtunes.io/tDrive/tuner/2025/03/techtunes_1779c215cf17acbd38c496e270917daf.jpg)

Nvidia-র GTC Keynote-এ DGX Spark (যা আগে Project Digits নামে পরিচিত ছিল), 12টি নতুন প্রফেশনাল GPU এবং Nvidia-র সবচেয়ে শক্তিশালী GPU Blackwell Ultra (বা GB300)-ও লঞ্চ করা হয়েছে। এই নতুন প্রোডাক্টগুলো Nvidia-র AI এবং ডেটা সায়েন্সের ভবিষ্যৎ পরিকল্পনাকে আরও স্পষ্ট করে তোলে।

Nvidia-র এই নতুন DGX Station নিয়ে আপনাদের কী মতামত? এটি কি সত্যিই ডেক্সটপ কম্পিউটিংয়ের ভবিষ্যৎ? টিউমেন্ট করে আমাদের জানাতে ভুলবেন না। আর হ্যাঁ, টেকনোলজির দুনিয়ার আরও নতুন টিউন পেতে টেকটিউনসের সাথেই থাকুন। খুব শীঘ্রই DGX Station-এর দাম এবং Availability নিয়ে নতুন তথ্য প্রকাশ করা হবে, তাই চোখ রাখুন টেকটিউনসে!

-

টেকটিউনস টেকবুম
