---
archive_id: techtunes-223693
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 223693
title: সফটওয়্যার ব্যাতিত পিসির ড্রাইভ লুকান অথবা তালা মেরে রাখুন!
slug: tips-and-tricks-223693
language: bn
status: publish
published_at: '2019-03-09T11:54:00+00:00'
modified_at: '2019-03-09T11:57:00+00:00'
original_url: https://www.techtunes.io/tips-and-tricks/tune-id/223693
author: ফাহাদ হোসেন
author_url: https://www.techtunes.io/tuner/little-jimmy
categories:
- টিপস এন্ড ট্রিকস
tags:
- GameWala
- গেমওয়ালা
- দরিদ্র
content_hash: 39bd1f1ba6cfe8c71f8bc545a3c2023ddaec84cbc090d821d8c4d46ee7f677f4
archived_at: '2026-11-12T12:58:29.759964+00:00'
---

অনেক সময় অনেক প্রয়োজনে আমাদের পিসির যেকোনো একটি ড্রাইভ যেটিতে আমরা পারসোনাল ডাটা সংরক্ষণ করে থাকি তা লুকিয়ে / লক করে রাখতে হয়। তখন দেখা যায় যে পিসিতে ড্রাইভ লুকানোর কোনো সফটওয়্যার নেই! মেজাজ খারপ? ব্যাপার না! 😉

**বি:দ্র: টিপসটি পিসি এক্সপার্টদের জন্য। নতুন ব্যবহারকারীরা ট্রাই না করাই উত্তম!**

**স্টেপস:**

> র্স্টাট মেনু থেকে রান কমান্ডে ক্লিক করে লিখুন regedit, রেজিস্টি এডিটর পর্দা আসবে।

[![](https://dnc.techtunes.io/tDrive/tuner/little-jimmy/223693/scss.jpg)](https://www.techtunes.io/tips-and-tricks/tune-id/223693/scss)

> এখন এই ফোল্ডারগুলোতে একে একে যান। ধৈর্য্য রেখে আস্তে আস্তে খুঁজুন:

HKEY\_CURRENT\_USER > Software > Microsoft > Windows > Current Version > Policies > Explorer

[![](https://dnc.techtunes.io/tDrive/tuner/little-jimmy/223693/২.jpg)](https://www.techtunes.io/tips-and-tricks/tune-id/223693/%e0%a7%a8-6)

> Explorer ফোল্ডারের ভিতর একটি নতুন ভ্যালু খুলুন। এরপর ভ্যালুর ধরন দিবেন DWORD Value

[![](https://dnc.techtunes.io/tDrive/tuner/little-jimmy/223693/৩.jpg)](https://www.techtunes.io/tips-and-tricks/tune-id/223693/%e0%a7%a9-9)

> নতুন ভ্যালুর নামকরণ করুন:

ড্রাইভ লুকাতে চাইলে নাম দিন : NoDrives

ড্রাইভ আবারো আনতে নাম দিন: NoViewOnDrive

[![](https://dnc.techtunes.io/tDrive/tuner/little-jimmy/223693/4.jpg)](https://www.techtunes.io/tips-and-tricks/tune-id/223693/4-906)

> NoDrives ভ্যালুটির উপর এন্টার দিন অথবা ডাবল ক্লিক করুন। নিচের মতো পর্দা আসবে:

[![](https://dnc.techtunes.io/tDrive/tuner/little-jimmy/223693/5.jpg)](https://www.techtunes.io/tips-and-tricks/tune-id/223693/5-696)

> এবার হলো আসল কাজ:

Value Data অংশে নিচের যেকোনো একটি ড্রাইভের ভ্যালু কপি পেস্ট করে দিন যেই ড্রাইভটি লুকাতে চান:

```
A = 1
B = 2
C = 4
D = 8
E = 10
F = 20
G = 40
H = 80
I = 100
J = 200
K = 400
L = 800
M = 1000
N = 2000
O = 4000
P = 8000
Q = 10000
R = 20000
S = 40000
T = 80000
U = 100000
V = 200000
W = 400000
X = 800000
Y = 1000000
Z = 2000000
```

মানে হচ্ছে যদি আপনি E ড্রাইভটি লুকাতে চান তাহলে ভ্যালু লিখুন 10

> এবার ok তে ক্লিক করে পিসি রির্স্টাট দিন। ব্যাস হয়ে গেল! 😮

আবার যদি লুকানো ড্রাইভটি ফিরিয়ে আনতে চান তাহলে ভ্যালুর সংখ্যা 0 (শুণ্য) লিখে পিসি রির্স্টাট দিতে হবে। 🙂

**টেকটিউনসে অথবা অন্যান্য যেকোনো ব্লগে ইমোশন ব্যবহার করতে পারেন। নিচের চার্টটি সংগ্রহে রেখে দিন কাজে লাগবে! 🙄**

[![](https://dnc.techtunes.io/tDrive/tuner/little-jimmy/223693/Tunerpage-EMu.jpg)](https://www.techtunes.io/tips-and-tricks/tune-id/223693/tunerpage-emu)
