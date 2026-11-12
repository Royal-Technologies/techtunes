---
archive_id: techtunes-653827
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 653827
title: Windows 10 এর অজানা ইনফরমেশন বের করুন WMIC দিয়ে! WMIC কি? এবং WMIC এর কমন কিছু
  কমান্ড
slug: windows-653827
language: bn
status: publish
published_at: '2025-02-21T07:11:00+00:00'
modified_at: '2025-02-21T07:11:00+00:00'
original_url: https://www.techtunes.io/windows/tune-id/653827
author: সোহানুর রহমান
author_url: https://www.techtunes.io/tuner/sohanur-raihan
categories:
- উইন্ডোস
tags:
- উন্ডোজ কমান্ড
- কমান্ড প্রোমোট
- কমান্ড লাইন
content_hash: 78c261b5b2647c4f85bc9652ed3cf0af410a5b2d1b6652343a7864d689ce4b23
archived_at: '2026-11-12T12:24:44.936383+00:00'
---

আসসালামু আলাইকুম, কেমন আছেন টেকটিউনস কমিউনিটি? আশা করছি সবাই ভাল আছেন। আজকে আবার হাজির হলাম নতুন টিউন নিয়ে। আমি আজকে আলোচনা করব WMIC নিয়ে। চলুন শুরু করা যাক।

## WMIC কি?

WMIC এর পূর্ণ রূপ হচ্ছে Windows Managment Interface Command। এটি উইন্ডোজ Command Prompt এর একটি টুল, যা উইন্ডোজ যে সিস্টেমের উপর চলছে তার তথ্য দেয়। WMIC কে কিছু বাড়তি Batch Script এবং Command line interface দিয়ে WMI থেকে উন্নত করা হয়েছে। WMIC এর আগে আমরা WMI এনে-বল কম্পিউটার গুলোতে শুধু WMI এর উপর তৈরি করা এপ্লিকেশন, Scripting API, CIM ূtudio এর মত টুল গুলো ব্যবহার করতাম।

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_af951db74378d99d9cd284d1f340aafd.png)

## WMIC

অফিসিয়াল লিংক @ [WMIC](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmic)

## কিছু WMIC কমান্ড

[WMIC](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmic) এর মাধ্যমে আপনি জেনে নিতে পারবেন কম্পিউটারের নানা তথ্য। যেমন আপনার WMI দ্বারা চালিত কম্পিউটারের মডেল জনতে, আপনার পিসির Command Prompt এ যান এবং নিচের কমান্ড ব্যবহার করুন।

```
 WMIC ComputerSystem GET Model
```

দেখতেই পাচ্ছেন আমার কম্পিউটারের মডেল দেখাচ্ছে।

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_f1b6d49837fff4a24af996c44a8f3cb1.png)

চলুন আরও কিছু কমন [WMIC](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmic) কমান্ড দেখে নেয়া যাক,

**কম্পিউটারের নাম বের করতে**

```
wmic computersystem get name, systemtype
```

**কম্পিউটারের সিরিয়াল নাম্বার বের করতে**

```
wmic bios get serialnumber
```

তাছাড়া এই কমান্ডটিও ব্যবহার করতে পারেন

```
wmic csproduct get identifyingnumber
```

**আপনার কম্পিউটারের ম্যাক এড্রেস বের করতে**

```
wmic nic get macaddress, description
```

**মাদারবোর্ড মডেল নাম্বার বের করতে**

```
wmic baseboard get product, Manufacturer, version, serialnumber
```

**কম্পিউটারের ফিজিক্যাল মেমরি চেক করতে**

```
wmic COMPUTERSYSTEM get TotalPhysicalMemory
```

**রানিং প্রোগ্রাম গুলোর মেমরি ইউজ দেখতে**

```
wmic process get workingsetsize, commandline
```

**পার্টিশন টাইপ এবং সাইজ দেখতে**

```
wmic partition get name, size, type
```

**কম্পিউটারের ম্যানুফেকচার দেখতে**

```
WMIC COMPUTERSYSTEM GET MANUFACTURER
```

**ভার্সন দেখতে নিচের কমান্ড ব্যবহার করুন**

```
wmic csproduct get version
```

## সিস্টেম ইনফরমেশন

আপনার কম্পিউটারের সিস্টেম ইনফরমেশন যেমন, Service, Process, startup ইত্যাদি তথ্য জানতে নিচের তিনটি কমান্ড ব্যবহার করুন।

```
wmic service list brief
wmic process list brief
wmic startup list brief
```

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_c083886ae58b1843dfa5a58dc8fba03c.png)

## প্রসেস ম্যানেজমেন্ট

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_13e7568177598f69c0c8d95bae9ae1bb.jpg)

আপনি [WMIC](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmic) ব্যবহার করে আপনার কম্পিউটারে বিভিন্ন ভাবে নির্দেশনা দিতে পারবেন। যেমন, যেকোনো একটি প্রোগ্রাম ছাড়া বাকি সব প্রোগ্রাম ক্লোজ হয়ে যাওয়া। আপনি যদি ফায়ার-ফক্সের সকল উইন্ডো বন্ধ করে দিতে চান তাহলে নিচের কমান্ড ব্যবহার কর‍তে পারেন।

```
wmic process where name=“firefox.exe” call terminate
```

## আউট-পুট ফাইলে সেভ করা

![](https://dnc.techtunes.io/tDrive/tuner/2020/07/techtunes_45288e22b6f2d8c7185296ba7473a23d.png)

এতক্ষণে হয়তো আমরা অনেক ইনফরমেশন দেখে ফেলেছি। এবার কেমন হবে যদি ইনফরমেশন গুলো টেক্সট ফাইলে সেভ করে নেয়া যায়?

এবার আমি দেখাব কিভাবে আউট পুট গুলো ফাইলে সেভ করে ফেলতে পারবেন।

কমান্ড গুলোর নিচের কোডটি  বসিয়ে দিন।

```
 wmic /output:&amp;quot;G:\output.txt&amp;quot;
```

**G:\output.txt** এর মানে হচ্ছে আপনি কি নামে কোন ফোল্ডারে ফাইলটি রাখতে চান। আরেকটি বিষয় মাথায় রাখতে হবে, **wmic**এটি একবারই বসবে এবং প্রথমে।

উদাহরণ হিসাবে ধরুন আপনি,

```
 wmic computersystem get name, systemtype
```

এই কমান্ড টির আউট-পুট ফাইলে সেভ করতে চান তাহলে আপনাকে লিখতে হবে,

```
 wmic /output:&amp;quot;G:\output.txt&amp;quot; computersystem get name, systemtype
```

![](https://dnc.techtunes.io/tDrive/tuner/2020/07/techtunes_cd4b45ee6b40e3b5381b5aa2edb20aea.png)

দেখুন আমার আউট-পুট একটি টেক্সট ফাইলে সেভ হয়ে গিয়েছে।

![](https://dnc.techtunes.io/tDrive/tuner/2020/07/techtunes_28ecb35809798491d1c80bad621aa649.png)

## শেষ কথাঃ

যাদের [WMIC](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmic) সম্পর্কে ধারণা আছে আশা করছি টিউনে উল্লেখিত কমান্ড গুলো কাজে আসবে।

পরবর্তী টিউন পর্যন্ত ভাল থাকুন। আমাদের সমসাময়িক যে সংকট চলছে এর থেকে রক্ষা পেতে সবাই সচেতন থাকবেন কারণ আপনার সচেতনতাই পারে আমাদের সবাইকে খারাপ অবস্থা থেকে বাঁচাতে। সবাই বাসায় থাকুন আর আল্লাহর উপর ভরসা রাখুন, আল্লাহ হা-ফেজ।
