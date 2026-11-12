---
archive_id: techtunes-489306
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 489306
title: Windows 10 কে কিভাবে Hotspot বানাবেন এবং Internet Share করবেন Mobile or অন্য
  PC তে
slug: windows-489306
language: bn
status: publish
published_at: '2018-05-12T09:08:00+00:00'
modified_at: '2018-05-12T09:08:00+00:00'
original_url: https://www.techtunes.io/windows/tune-id/489306
author: Era IT
author_url: https://www.techtunes.io/tuner/alaminera77
categories:
- উইন্ডোস
tags:
- WiFi HotSpot
- windows hotspot
content_hash: 449d5f0cd0340ffb2af3910f69fa621b1539ad3456d59ce41b90d57baa533854
archived_at: '2026-11-12T12:54:49.033534+00:00'
---

আশাকরি সবাই ভাল আছেন। আর ভাল থাকুন এটাই কামনা করছি। আজ একটা খুবই গুরুত্বপূর্ন বিষয় নিয়ে আলোচনা করব। তার আগে সবাইকে ধন্যবাদ জানাচ্ছি আমার IT Related YouTube Channel Era IT তে সাবস্ক্রাইব ও ভিডিও গুলো দেখার জন্য। যারা এখনও Subscribe করেননি তারা এখনই সাবস্ক্রইব করুন কারন আমি প্রতিদিনই নতুন নতুন ভিডিও  আপলোড করছি।  কোন না কোন ভিডিও আপনার কাজে লাগবেই। মূল কথায় আসি।

আমরা আমাদের পিসির ইন্টারনেট অন্য কোন মোবাইল বা পিসিতে শেয়ার করার জন্য অনেক ধরনের সফটওয়্যার ব্যবহার করে থাকি। কিন্তু এই সফটওয়্যারগুলো র কিছু সমস্যা আছে। যেমন: ইন্টারনেট স্লোা  এবং সিকিউরিটি কম। তাই আজ আমি দেখাব কিভাবে আপনি কোন ধরনের সফটওয়্যার ছাড়া আপনি Laptop কে Hotspot বানাবেন।

![](https://dnc.techtunes.io/tDrive/tuner/alaminera77/489306/hotspot-featured.jpg)

## স্টেপ ০১ :

প্রথমে আপনার ল্যাপটপ হটস্পট এর উপযোগী কিনা তা চেক করে দেখতে হবে। তার জন্য আপনার পিসির Search এ গিয়ে CMD লিখুন এবং Command Prompt পেইজ ওপেন করুন। এবং  NETSH WLAN show drivers  এই কোডটা লিখে Enter Press করুন।

## স্টেপ ০২ :

এখন আপনার ল্যাপটপের ইটস্টপ  এর ID and Password সেট করতে হবে। তার জন্য NETSH WLAN set hostednetwork mode=allow ssid=**Your\_SSID** key=**Your\_Passphrase**  এই কোডটা টাইপ করতে হবে। এখানে কোডটার আনডারলাইন করা লেখাগুলো আপনি ইচ্ছে করলে Edit করতে পারেন। SSID  এটা হল আপনার ID  and Key হল পাসওয়ার্ড। এখন  NETSH WLAN start hostednetwork এই কোডটা আবার কপি পেষ্ট করে এন্টার দিন তাহলে আপনার পিসির হটস্পট অন হবে। এখন আপনার আপনার মোবাইলের Wifi অন করে দেখুন এবং পাসওয়ার্ড দেন এবং ব্যবহার করুন।

## ভিডিওতে আরো বিস্তারিতভাবে দেওয়া আছে :

[Embedded External Content: https://www.youtube.com/embed/1qBuBZ74LHU?feature=oembed]

> **সৌজন্য:**
>
> **[Era IT](https://www.youtube.com/channel/UCPvlrAhTI206bSH5scCyxUg?sub_confirmation=1)**
