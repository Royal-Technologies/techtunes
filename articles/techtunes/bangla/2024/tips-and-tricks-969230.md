---
archive_id: techtunes-969230
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 969230
title: WuMgr – Windows 10 ও 11 এর জন্য ফ্রি ও ওপেনসোর্স আপডেট ম্যানেজমেন্ট টুল
slug: tips-and-tricks-969230
language: bn
status: publish
published_at: '2024-05-23T18:19:00+00:00'
modified_at: '2024-04-30T15:23:00+00:00'
original_url: https://www.techtunes.io/tips-and-tricks/tune-id/969230
author: সোহানুর রহমান
author_url: https://www.techtunes.io/tuner/sohanur-raihan
categories:
- টিপস এন্ড ট্রিকস
tags:
- Tips টিপস
- অটোআপডেট
- অটো আপডেট ডিজেবল / বন্ধ করুন
content_hash: dc7ecf2c62dcf2e7da8cfb3765650efd910a8e2c9dbf3982c372b1e132001d8a
archived_at: '2026-11-12T12:04:53.588388+00:00'
---

আসসালামু আলাইকুম কেমন আছেন সবাই, আশা করছি ভাল আছেন। বরাবরের মত হাজির হলার নতুন একটি টিউন নিয়ে।

## WuMgr কী?

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_01e453956e8be365a6e215fd5aa1b3e1.png)

WuMgr একটি Windows 10 এর ফ্রি আপডেট ম্যানেজমেন্ট টুল। এর মাধ্যমে মাইক্রোসফট সব প্রোডাক্টের আপডেট সহজে ম্যানেজ করা যায়। এটি একটি ওপেন সোর্স সফটওয়্যার যা Microsoft.NET এ ডেভেলপ করা হয়েছে।

WuMgr বিভিন্ন আপডেট, খুঁজে বের করবে, ডাউনলোড করবে এবং ইন্সটল করবে তাছাড়া ইউজাররা আপডেটের উপর পূর্ণ কন্ট্রোল পাবে। এটাকে আগের Windows 7 এবং 8.1. ভার্সন থেকে আরও উন্নত করা হয়েছে। WuMgr তৈরি করা হয়েছে Windows Update Agent API এর মাধ্যমে যার ফলে প্রোগ্রামার এবং সিস্টেম এডমিনিস্ট্রেটরা WSUS (Windows Server Update Services) এ এক্সেস পেতে পারে।

আমরা সবাই জানি Windows 10 এর আপডেট প্রক্রিয়া কতটা ঝামেলার এবং যখন তখন আপডেট থাকে। কিন্তু WuMgr এর মাধ্যমে আপনি এই আপডেট ইচ্ছে মতো নিয়ন্ত্রণ করতে পারবেন। দারুণ এই অ্যাপ ব্যবহার করে আপনি অটো আপডেট বন্ধ করতে পারবেন, আপডেট শিডিউল কর‍তে পারবেন চাইলে গ্রুপ অথবা ক্যাটাগরি অনুযায়ী আপডেট ইন্সটল করতে পারবেন।

wsusscn2.cab ফাইল ব্যবহার করে WuMgr অফলাইনেও আপডেট সার্চ কর‍তে পারে। এটি একটি ডিজিটাল সাইনড Cabinet ফাইল যাতে সিকিউরিটি রিলেটেড আপডেট গুলোর ইনফরমেশন থাকে যা মাইক্রোসফট প্রতিমাসে একবার প্রকাশ করে।

### WuMgr

গিটহাব লিংক @ [WuMgr](https://github.com/DavidXanatos/wumgr/releases)

## কীভাবে ব্যবহার করবেন WuMgr?

প্রথমে [WuMgr](https://github.com/DavidXanatos/wumgr/releases) প্রোগ্রামটি ডাউনলোড করে নিন এবং আনজিপ করে ওপেন করুন

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_f236aa8574751f6a714a1935e00bc96e.png)

কোন আপডেট আছে কিনা জানতে ‘Search’ আইকনে ক্লিক করুন।

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_dcfc877133d9561937e58fc06933f1bc.png)

সার্চ কমপ্লিট হলে উপরে বাম পাশের আইকনে ক্লিক করুন। এখানে Windows Updates, Installed Updates, Hidden Updates and Update History অপশন গুলো পাবেন

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_3ebbe1d017386b310841a7844a923263.png)

যেকোনো বাটনে ক্লিক করলে আপনাকে ডানপাশে আপডেটের Category, Release date, Size, State (Pending / Installed / Succeeded) অনুযায়ী বিস্তারিত তথ্য দেখাবে। ক্যাটাগরি অনুযায়ী আপডেট করতে স্ক্রিনের Group Updates বাটনে ক্লিক করুন।

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_3ebbe1d017386b310841a7844a923263.png)

যেকোনো আপডেট ডাউনলোড বা ইন্সটল করতে চেক বক্সে ক্লিক করে সেটা সিলেক্ট করুন। ডাউনলোড বা ইন্সটল কর‍তে ‘Download’ অথবা ‘Install’ বাটনে ক্লিক করুন। ইন্সটল হয়ে গেলে সেগুলো আপনি ‘Installed Updates’ লিস্ট এ পাবেন। চাইলে আপনি বামপাশের প্যানেল থেকে আপডেট ডিলিট বা হাইডও করতে পারেন।

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_42e5e02bf12156c70a4d6444ac192235.png)

অফলাইন মুড, ম্যানুয়াল ডাউনলোড, ব্যাকগ্রাউন্ড রানের মত অপশন গুলো পেতে নিচের বামপাশের Option ট্যাবে ক্লিক করুন। কিছু অপশন এনেভল করতে পিসি রিস্টার্ট দেয়া লাগতে পারে।

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_823a97978bc923326f105b5e47ec61ac.png)

অটো আপডেট বন্ধ করতে Auto Update বাটনে ক্লিক করুন। এখানে অটো আপডেট, ড্রাইভার আপডেটও শিডিউল আপডেট অপশন গুলো পাবেন।

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_fb838d60c61f102dfd97c9d1219f0166.png)

## শেষ কথা

WuMgr একটি চমৎকার টুল যার মাধ্যমে Windows 10 আপডেটের ক্ষেত্রে আপনি পূর্ণ কন্ট্রোল পেয়ে যাবেন। এটি Windows Update Mini Tool (WUMT) টুলেরও সেরা বিকল্প হতে পারে যা C / C+ ডেভেলপ করা হয়েছে। Windows 10 এর বিভিন্ন আপডেট সংক্রান্ত ইস্যুতে আপনাকে দারুণ ভাবে সাহায্য করতে পারে WuMgr।

আজকে এ পর্যন্তই শীঘ্রই দেখা হবে নতুন কোন টিউনের সাথে ততদিন ভাল থাকুন, আল্লাহ হাফেজ।
