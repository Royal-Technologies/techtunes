---
archive_id: techtunes-379304
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 379304
title: কি করে বন্ধ করবেন উইণ্ডোস অটো আপডেট পর্ব দুই এবং অন্তিম।
slug: windows-379304
language: bn
status: publish
published_at: '2015-08-21T07:35:00+00:00'
modified_at: '2020-09-19T03:41:00+00:00'
original_url: https://www.techtunes.io/windows/tune-id/379304
author: অভিষেক হাজরা
author_url: https://www.techtunes.io/tuner/jibonre
categories:
- উইন্ডোস
tags:
- উইন্ডোজ
- টেকটিউনস
- ডাউনলোড
content_hash: 2142a7f411206e22125d1a17b13368b4496d05ea6fd47abe6bcb50b74f1f486e
archived_at: '2026-11-12T12:56:22.020964+00:00'
---

সুপ্রিয় টেকটিউনস পরিবারের  
 সবাইকে আমার আন্তরিক ভালোবাসা এবং শুভেচ্ছা জানিয়ে শুরু করছি কি করে বন্ধ করবেন উইণ্ডোস ১০ অটো আপডেট টিউনের দ্বিতীয় পর্ব এবং অন্তিমপর্ব।

এর আগের পর্বে আমরা [কি করে বন্ধ করবেন উইণ্ডোস ১০](https://www.techtunes.io/windows/tune-id/376163) অটো আপডেট মাত্র ছয় ধাপে বিষয়ে প্রয়োজনীয় আলোচনা করেছিলাম।

এবং সেটা নির্ভুল ভাবে কার্য করতে সক্ষম, তাহলে প্রশ্ন আসতেই পারে, দ্বিতীয় পর্ব এর প্রয়োজন হলো কেন?  
 হ্যা প্রয়োজন আছে তাই এই টিউন টি করা।

![](https://dnc.techtunes.io/tDrive/tuner/jibonre/379304/critical-Error.png)  
 উইন্ডোস অটো আপডেট একবার বন্ধ করা হলে, দ্বিতীয় বার শুরু হওয়া উচিত নয়, কিন্তু windows১০ এ নেট কানেকশন অন থাকলে windows১০ ট্রাবলশ্যুটিং অপসন নিজে থেকে এই প্রবলেম ফিক্স করার চেষ্টা করে, আর তাই ফিক্স অপসন একবার সিলেক্ট হয়ে গেলে। আবার উইণ্ডোস আপডেট চালু হয়ে যাবে, তাই চলুন windows১০ ট্রাবলশ্যুটিং অপসন যাতে আপনার আপডেট ফিক্স করতে না পারে সেই রকম ভাবে বন্ধ করব অটো আপডেট। মাইক্রোসফট তার উইণ্ডোসে একটি ডিফল্ট মাস্টার একাউন্ট বানায়, যার হাতে থাকে সব পারমিসন, যে হলো লোকাল অ্যাডমিন।  
 আর তাই লোকাল অ্যাডমিন যদি উইন্ডোস আপডেট বন্ধ করে, তখন মাইক্রোসফট ডেটা সেন্টারের কাছে ইনফরমেশন থাকে, যে আপনার আপডেট ইনস্টল করার পারমিসন নেই, আর তাই ট্রাবলশ্যুটিং আপডেট ফিক্স করার চেষ্টাও করবেনা। চলুন তবে করা যাক উইন্ডোস আপডেট ডিসএবল বাই লোকাল অ্যাডমিন।

#### প্রথম পদ্ধতি

টাইপ করুন সার্চ বারে EDIT GROUP POLICY  
 ওপেন করুন EDIT GROUP POLICY,  
 LOCAL GROUP POLICY EDITOR খুলবে  
 সেখানে পাবেন Computer Configuration  তারথেকে  Administrative Template তারথেকে Windows Components  
 তারথেকে Windows Update  একদম শেষে  
 সিলেক্ট করুন Windows Update ডানদিকে পেজটি তে পাবেন Configure Automatic Updates  
 Configure Automatic Updates এ Right ক্লিক করুন Edit অপসন পাবেন  
 Edit অপসন সিলেক্ট করুন,   Configure Automatic Updates Enable করুন  
 নিচে Options এ Configure Automatic Updating এ ৫ম অপসন Allow Local Admin To Chose Settings সিলেক্ট করুন আর Apply, ব্যাস আপনার কাজ complete.

ও হ্যা, নিচে ছবিতে দেখালাম কি করে করবেন।

![](https://dnc.techtunes.io/tDrive/tuner/jibonre/379304/Disable-Update-1.png)

![](https://dnc.techtunes.io/tDrive/tuner/jibonre/379304/Disable-Update-2.png)

![](https://dnc.techtunes.io/tDrive/tuner/jibonre/379304/Disable-Update-31.png)

![](https://dnc.techtunes.io/tDrive/tuner/jibonre/379304/Disable-Update-41.png)

![](https://dnc.techtunes.io/tDrive/tuner/jibonre/379304/Disable-Update-5.png)

টাইপ করুন সার্চ বারে Advanced Windows Update Options

আপনি এই পেজটা দেখতে পাবেন।

![](https://dnc.techtunes.io/tDrive/tuner/jibonre/379304/Disable-Update-Complete.png)

#### দ্বিতীয় পদ্ধতি

ডিসএবল করার জন্য আমাদের কিছু লাগবে না আমি সব তৈরী করে রেখেছি আগে থেকেই খালি ডাউনলোড করুন আর Merge করুন ব্যাস আপনার কাজ complete.

৪ টে REG ফাইল, সবার কাজ অনুযায় RENAME করেছি

1. [অটো ডাউনলোড করে ইনস্টল করার আগে জানাবে আপনাকে](http://www.mediafire.com/download/mpct8ziddsjb9g0/%E0%A6%85%E0%A6%9F%E0%A7%8B_%E0%A6%A1%E0%A6%BE%E0%A6%89%E0%A6%A8%E0%A6%B2%E0%A7%8B%E0%A6%A1_%E0%A6%95%E0%A6%B0%E0%A7%87_%E0%A6%87%E0%A6%A8%E0%A6%B8%E0%A7%8D%E0%A6%9F%E0%A6%B2_%E0%A6%95%E0%A6%B0%E0%A6%BE%E0%A6%B0_%E0%A6%86%E0%A6%97%E0%A7%87_%E0%A6%9C%E0%A6%BE%E0%A6%A8%E0%A6%BE%E0%A6%AC%E0%A7%87_%E0%A6%86%E0%A6%AA%E0%A6%A8%E0%A6%BE%E0%A6%95%E0%A7%87.reg)

2.[অটো ডাউনলোড করুন এবং সময়সূচী অনুসারে ইনস্টল হবে পরে](http://www.mediafire.com/download/fagbb1esyvgd220/%E0%A6%85%E0%A6%9F%E0%A7%8B_%E0%A6%A1%E0%A6%BE%E0%A6%89%E0%A6%A8%E0%A6%B2%E0%A7%8B%E0%A6%A1_%E0%A6%95%E0%A6%B0%E0%A7%81%E0%A6%A8_%E0%A6%8F%E0%A6%AC%E0%A6%82_%E0%A6%B8%E0%A6%AE%E0%A6%AF%E0%A6%BC%E0%A6%B8%E0%A7%82%E0%A6%9A%E0%A7%80_%E0%A6%85%E0%A6%A8%E0%A7%81%E0%A6%B8%E0%A6%BE%E0%A6%B0%E0%A7%87_%E0%A6%87%E0%A6%A8%E0%A6%B8%E0%A7%8D%E0%A6%9F%E0%A6%B2_%E0%A6%B9%E0%A6%AC%E0%A7%87_%E0%A6%AA%E0%A6%B0%E0%A7%87.reg)

3.[ডাউনলোডের জন্য সূচিত করবে এবং ইনস্টল জন্য অবহিত করবে আপনাকে](http://www.mediafire.com/download/nr7oevrheh4nxp6/%E0%A6%A1%E0%A6%BE%E0%A6%89%E0%A6%A8%E0%A6%B2%E0%A7%8B%E0%A6%A1%E0%A7%87%E0%A6%B0_%E0%A6%9C%E0%A6%A8%E0%A7%8D%E0%A6%AF_%E0%A6%B8%E0%A7%82%E0%A6%9A%E0%A6%BF%E0%A6%A4_%E0%A6%95%E0%A6%B0%E0%A6%AC%E0%A7%87_%E0%A6%8F%E0%A6%AC%E0%A6%82_%E0%A6%87%E0%A6%A8%E0%A6%B8%E0%A7%8D%E0%A6%9F%E0%A6%B2_%E0%A6%9C%E0%A6%A8%E0%A7%8D%E0%A6%AF_%E0%A6%85%E0%A6%AC%E0%A6%B9%E0%A6%BF%E0%A6%A4_%E0%A6%95%E0%A6%B0%E0%A6%AC%E0%A7%87_%E0%A6%86%E0%A6%AA%E0%A6%A8%E0%A6%BE%E0%A6%95%E0%A7%87.reg)

4.[উইন্ডোস ১০ ডিফল্ট সেটিংস পূর্বাবস্থায় ফিরিয়ে আনুন](http://www.mediafire.com/download/fagbb1esyvgd220/%E0%A6%85%E0%A6%9F%E0%A7%8B_%E0%A6%A1%E0%A6%BE%E0%A6%89%E0%A6%A8%E0%A6%B2%E0%A7%8B%E0%A6%A1_%E0%A6%95%E0%A6%B0%E0%A7%81%E0%A6%A8_%E0%A6%8F%E0%A6%AC%E0%A6%82_%E0%A6%B8%E0%A6%AE%E0%A6%AF%E0%A6%BC%E0%A6%B8%E0%A7%82%E0%A6%9A%E0%A7%80_%E0%A6%85%E0%A6%A8%E0%A7%81%E0%A6%B8%E0%A6%BE%E0%A6%B0%E0%A7%87_%E0%A6%87%E0%A6%A8%E0%A6%B8%E0%A7%8D%E0%A6%9F%E0%A6%B2_%E0%A6%B9%E0%A6%AC%E0%A7%87_%E0%A6%AA%E0%A6%B0%E0%A7%87.reg)

#### তৃতীয় পদ্ধতি

খুব সহজ যদি আপনি WiFi ইউস করেন তাহলে প্রযজ্য। কিছুই নয় খালি আপনার WiFi Connected করুন,

আর আপনার WiFi কে  Meter Connection হিসাবে set করুন ব্যাস

Windows Update File দেখাবে কিন্তু  Download করবে না।

নিচে ছবিতে দেখালাম কি করে করবেন। ![](https://dnc.techtunes.io/tDrive/tuner/jibonre/379304/Disable-Update-By-WIFI-1.png)

![](https://dnc.techtunes.io/tDrive/tuner/jibonre/379304/Disable-Update-By-WIFI-2.png)

![](https://dnc.techtunes.io/tDrive/tuner/jibonre/379304/Disable-Update-By-WIFI-3.png)

```
এই পরিবারের সবার কাছে আমার একটি অনুরোধ অনুসরন করুন কিন্তু অনুকরণ করবেন না।
এই প্রথমবার আমি আমার চিত্রগুলাতে কপিরাইট সিম্বল দিলাম কারণ কিছু 
শিক্ষিত বা অশিক্ষিত এই টেকটিউনসের ছবি গুলা কে নিজের চিত্র বলে, নিজের Blog /Site টে ব্যবহার করছে। 
তাই সকল টিউনার ভাই এর কাছে আমার একটাই অনুরোধ, নিজের টিউনে ব্যবহৃত চিত্র গুলিতে © টেকটিউনস এই সিম্বল ব্যবহার করুন।
এতে ওই শিক্ষিত বা অশিক্ষিত ব্যাটারা সায়েস্তা হবে। 
আর যারা টিউনমেন্টে তাদের অসুবিধার কথা বলেন তারা যেন পরে আর একবার টিউনমেন্ট করেন, সাহায্য পেলে বা উপকৃত হলে। 
কারণ তাহলে জানা সম্ভব হয় যে সাহায্য করতে পারলাম কিনা। 
আমার এই টিউন যদি কারোর খারাপ লেগে থাকে তবে আমি একান্তই দুঃখিত।  
আমার কাউকে দুখিত করার কোনো প্রকার উদ্দেশা নেই। 
ভালো থাকবেন, ভালো রাখবেন, আর প্রবেলম হলে আমিতো টেকটিউনসে আছি। 

"Updates are additions to software that can help prevent or fix problems, improve how your computer works,
or enhance your computing experience. " - Microsoft says 
মাইক্রোসফট এ কাজ করি তো তাই একটু ওদের কথাও লিখে দিলাম।
```

```
উফ লেখা শেষ, এবার শান্তি।
```
