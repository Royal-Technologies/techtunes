---
archive_id: techtunes-651574
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 651574
title: Windows 10 এর এক্সক্লুসিভ ফিচার Modern Standby মুড কি? চেক করুন আপনার পিসিতে
  সাপোর্ট করে কিনা এই Modern Standby
slug: tips-and-tricks-651574
language: bn
status: publish
published_at: '2025-04-02T03:45:00+00:00'
modified_at: '2025-02-23T03:48:00+00:00'
original_url: https://www.techtunes.io/tips-and-tricks/tune-id/651574
author: সোহানুর রহমান
author_url: https://www.techtunes.io/tuner/sohanur-raihan
categories:
- টিপস এন্ড ট্রিকস
tags:
- Tips টিপস
- অসাম ফিচারস
- আপনার পিসি
content_hash: 638d4b1c147e1e75d3151f39838c4b0fb7adc923808d1e6bbdf2dd830bcb8c41
archived_at: '2026-11-12T12:25:10.766057+00:00'
---

টেকটিউনস কমিউনিটি, কেমন আছেন সবাই? আশা করছি সবাই ভাল আছেন। বরাবরের মত চলে এসেছি নতুন কোন টিউন নিয়ে। চলুন শুরু যাক!

আজকে আমি আলোচনা করব Windows 10 এর Modern Standby ফিচার নিয়ে। এই ফিচারটি মূলত Windows 8 এর connected Standby মুড এর উন্নত সংস্করণ। এই ফিচারে অতিরিক্ত কিছু সুবিধা এড করা হয়েছে।

## Modern Standby কি

![](https://dnc.techtunes.io/tDrive/tuner/2020/04/techtunes_5e70fd183a775a0a2489e2e5f46ea604.jpg)

Modern Standby কি জানতে হলে আপনাকে আগে জানতে হবে Windows 8 এর Connected Standby মূলত কি ছিল। ধরুন আপনি আপনার পিসিকে Sleep মুডে দিয়ে দিলেন এখন যদি আপনার পিসি ইন্টারনেটে কানেক্ট থাকে এবং আপনি ইমেইল, ইনস্ট্যান্ট মেসেজের নোটিফিকেশন পান তাহলে এটি হচ্ছে Connected Standby Mode। আবার যদি Sleep করার পরে আপনার ইন্টারনেট কানেকশন অফ হয়ে যায় সেটি হচ্ছে Disconnected Standby Mode।

কিন্তু windows 8 এ শুধু মাত্র Connected Mode কাজ করতো। তাই মাইক্রোসফট এই ফিচারটিকে বর্ধিত করে  তৈরি করেছে Modern Standby। যেখানে একই সাথে Conected/Disconected উভয় মুডই সাপোর্ট করে।

## কিভাবে কাজ করে

![](https://dnc.techtunes.io/tDrive/tuner/2020/04/techtunes_112cadc929f7921b5cf77dd083f62f1a.png)

এই নতুন মুডটি শুধু মাত্র মডার্ন হার্ডওয়্যার গুলোতেই সাপোর্ট করবে। এই মুডটি মূলত Legacy Standby কে ব্যবহার করে ব্যাকগ্রাউন্ডে কিছু কিছু সার্ভিস চালু রাখে যেমন, ইন্টারনেট, ডিস্ক ইত্যাদি।

আপনি যখন আপনার ডিভাইসকে Modern Standby মুডে রাখবেন আপনার পিসি তখন সকল হার্ডওয়্যারকে Low পাওয়ারে নিয়ে যাবে। এবং কিছু কিছু টাস্ক যেমন নেটওয়ার্কিং এবং মেসেজ রিসিভ করা চালু রাখবে।

## কিভাবে বুঝবেন আপনার পিসি সাপোর্ট করবে কিনা

আপনার পিসিতে Modern Standby সাপোর্ট করবে কিনা জানতে চলে যান Command Prompt এ এবং run as Administrator এ ওপেন করুন।  
 নিচে কমান্ডটি দিন

powercfg /availablesleepstates

![](https://dnc.techtunes.io/tDrive/tuner/2020/04/techtunes_fd29272f660dbf5488d7ee883f6ee1ee.png)

এখানে স্ক্রিনশটটি খেয়াল করুন, আমার পিসি Standby (S3) সাপোর্টেড কিন্তু Standby (S0) সাপোর্টেড না। আর এখানে Standby (S0)  মানেই হচ্ছে Modern Standby। সুতরাং আমার পিসিতে এই ফিচারটি কাজ করে না।

## শেষ কথা

নিঃসন্দেহে Modern Standby একটি চমৎকার ফিচার, যা আপনাকে স্লিপ মুডেও বিভিন্ন নোটিফিকেশন দিয়ে কাজের সাথে কানেক্ট রাখবে। এটি একই সাথে আপনার ব্যাটারি লাইফ বাড়ানোর সাথে সাথে জরুরী কাজ গুলোরও নোটিফিকেশন দিতে থাকবে।

তো আর দেরি কেন এখনি চেক করে নিন আপনার পিসিতে সাপোর্ট করে কিনা Modern Standby!

পরবর্তী টিউন পর্যন্ত ভাল থাকুন। আমাদের সমসাময়িক যে সংকট চলছে এর থেকে রক্ষা পেতে সবাই সচেতন থাকবেন কারণ আপনার সচেতনতাই পারে আমাদের সবাইকে খারাপ অবস্থা থেকে বাচাতে। সবাই বাসায় থাকুন আর আল্লাহর উপর ভরসা রাখুন, আল্লাহ হা-ফেজ।
