---
archive_id: techtunes-509009
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 509009
title: NQ Vault – আপনার ফাইল কতটুকু নিরাপদ? [পর্ব-২]
slug: altering-509009
language: bn
status: publish
published_at: '2017-08-16T12:27:00+00:00'
modified_at: '2021-08-31T03:27:00+00:00'
original_url: https://www.techtunes.io/altering/tune-id/509009
author: ইব্রাহীম রাফি
author_url: https://www.techtunes.io/tuner/rafiibrahim8
categories:
- অল্টারিং
tags:
- NQ Vault
- Vault
content_hash: 8ce16eb259d368ba7376cacbc4fff609104527ef41ae4b04c8ce78d29fd0f873
archived_at: '2026-11-12T12:42:38.880378+00:00'
---

আস্‌-সালামু-আলাইকুম।

দ্বিতীয় পর্বে আপনাকে স্বাগতম। আপনি যদি প্রথম পর্ব মিস করে থাকেন তাহলে [এখান](https://www.techtunes.io/hacking/tune-id/508962) থেকে ঘুরে আসতে পারেন। যথারীতি টিউন শুরু করার আগে কিছু সিরিয়াস কথাবার্তা বলে নিই,

***Disclaimer: এই টিউনটি শুধু শিক্ষা এবং বিনোদনের উদ্দেশ্যে লিখা। কারও গোপনীয়তা ভঙ্গ করা এই টিউনের উদ্দেশ্য নয়। এই টিউনের বিষয়বস্তু ব্যবহার করে কোন ব্যক্তি অন্যের ব্যক্তিগত তথ্য হাতিয়ে নিলে বা নেওয়ার চেষ্টা করলে লেখক দায়ী থাকবে না।***

গত পর্বে আমরা ফাইল এক্সটেনশন নিয়ে কথা বলছিলাম। যেহেতু NQ Vault-এর সেভ করা সব ফাইল.bin এ সেভ হয় তাই সরাসরি আসল এক্সটেনশন খুঁজে পাওয়া যায় না। এ সমস্যা থেকে সহজেই পরিত্রাণ পাওয়া যায় File Signature ব্যবহার করে।

## File Signature কী?

File Signature (File Magic Number বলেও পরিচিত) হল ফাইলের শুরুতে কয়েকগুচ্ছ ধারাবাহিক বাইট, যা ফাইলের ধরন নির্দেশ করে। উদাহরন সরুপ chocolates.jpg-এর হেক্সঃ

![](https://dnc.techtunes.io/tDrive/tuner/rafiibrahim8/509009/sc1.1.png)

এখন প্রথম কয়েক বাইট লক্ষ করি FF D8 FF। সব.jpg ফাইলই শুরু হয় এই তিনটি বাইট দিয়ে (.jpg-র ক্ষেত্রে ৪র্থ বাইটও মোটামুটি নির্দিষ্ট; E0, E8, E1 এর যেকোন একটি হয়)। আমরা যদি কখনো ফাইলের শুরুতে FF D8 FF দেখি তাহলে আমরা তাকে.jpg ফাইল হিসেবে ধরে নিতে পারি। এমনি ভাবে প্রায় সব ফাইলেরই File Signature আছে। যা ব্যবহার করে আমরা সহজেই ফাইলের এক্সটেনশন খুঁজে পেতে পারি।

তো File Signature-এর ধারণা নিয়েই তৈরি হয়েছে আমাদের Vault Cracking প্রোগ্রাম Vault Blaster.exe। Vault Blaster সরাসরি XOR Key, ফাইল এক্সটেনশন ডিটেক্ট এবং ফাইল ডিক্রিপ্ট (Reverse XOR) করতে পারে। ইচ্ছে করলে Manually ও কাজ করানো যায়।

## তো Vault Blaster- দিয়ে কিভাবে ক্রাক করবেন?

প্রথমে, আগের টিউনে উল্লেখিত SystemAndroid ফোল্ডার থেকে.bin ফাইল কপি করে পিসিতে একটি ফোল্ডারে রাখুন। এরপর, Vault-Blaster.exe একই ফোল্ডারে নিয়ে আসুন।  Vault Blaster ওপেন করুন। নিচের মত স্ক্রিন দেখতে পাবেন।

![](http://i.imgur.com/PzEcQZP.png)

যেহেতু আমরা এখনও Key জানি না তাই ১ নম্বর অপশন (I don't know the key.) সিলেক্ট করব। আমাদের কাছে ফাইলের নাম চাইবে। আমদের ফাইলের নাম 1502616638681.bin লিখে এন্টার দিলাম (এত বড় নাম লিখতে না চাইলে রিনেম করে নিতে পারেন)। Vault Blaster জানতে চাইল আমরা কি মোড ব্যবহার করতে চাই।

![](http://i.imgur.com/AOWoQHw.png)

এখানে অটোমেটিক মোড দিলে, Vault Blaster স্বয়ংক্রিয়ভাবে ফাইল এক্সটেনশন ও Key ডিটেক্ট করবে। মেনুয়াল মোডে Vault Blaster আমাদের কাছে ফাইল এক্সটেনশন চাইবে এবং ২৫৬ টি ফাইল তৈরি করবে। যার মধ্য থেকে ইউজারকে আসল ফাইল এবং Key খুঁজে নিতে হবে।

আমরা আপাদত আটোমেটিক মোড দিলামঃ

![](http://i.imgur.com/9pe6x72.png)

দেখা যাচ্ছে যে, Vault Blaster ফাইল এক্সটেনশন ডিটেক্ট করেছে.jpg এবং Key 55 (দশমিক)। এরপর যেকোন নাম দিই ফাইল সেভ করার জন্য।

এক্ষেত্রে myPhoto নাম দেয়ায় একই ফোল্ডারে myPhoto.jpg নামে একটি ফাইল তৈরি হয়েছে।

![](http://i.imgur.com/gCNdFPb.png)

এবার  myPhoto.jpg ওপেন করা যাক।

![](http://i.imgur.com/mxVP7oN.jpg)

আমরা পেয়ে গেলাম আমাদের কাঙ্ক্ষিত ফাইল। এভাবে আমরা NQ Vault-এ রাখা সকল ফাইল-ই নিতে পারব ইন-শা-আল্লাহ। আবারো মনে করিয়ে দিতে চাই, কারও  গোপনীয়তা ভঙ্গ করার উদ্দেশ্যে এই টিউন ব্যবহার করবেন না।

ডাউনলোডঃ [Vault-Blaster.exe](https://drive.google.com/uc?id=0B8l-G_vWMQghMmVFZ3RBcmhuMk0&export=download) (39kb)

সোর্স কোডঃ [Vault Blaster Source](https://github.com/rafiibrahim8/Vault-Blaster)
