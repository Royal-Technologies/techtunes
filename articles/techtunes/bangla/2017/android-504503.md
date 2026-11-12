---
archive_id: techtunes-504503
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 504503
title: (সমাধান) Xiaomi Redmi Note 4/4x ফোন Root করার পর USB Connect হচ্ছে না? (Solution)Not
  connecting USB in Xiaomi Redmi Note 4/4x
slug: android-504503
language: bn
status: publish
published_at: '2017-07-25T04:46:00+00:00'
modified_at: '2017-07-25T04:46:00+00:00'
original_url: https://www.techtunes.io/android/tune-id/504503
author: সাব্বির হোসেন
author_url: https://www.techtunes.io/tuner/sabbccc
categories:
- অ্যান্ড্রয়েড
tags:
- not connecting
- SolutionNot connecting
content_hash: 4135797f84cf553551ab6a354635e48a27c9c99c6f70eac8ff1f09bac7e89dd1
archived_at: '2026-11-12T12:45:20.137967+00:00'
---

এটি Techtunes-এ আমার প্রথম টিউন। বানান বা লেখার ভুলের জন্য প্রথমেই ক্ষমা চেয়ে নিচ্ছি।

Xiaomi Redmi Note 4/4x ফোনগুলো বেশ জনপ্রিয়তা পেয়েছে অল্প সময়েই। যারা সাধারন এন্ড্রয়েড ব্যবহারকারীদের চেয়ে একটু বেশী ঘাটাঘাটি করতে পছন্দ করেন এবং Superuser হিসেবে ফোন ব্যবহার করতে চান তাদের জন্য দারুন একটি ফোন এটি। Superuser Permission পেতে হলে আপনাকে অবশ্যই ফোন Root করতে হবে।যারা ফোন Root করে ফেলেছেন,তারা অবশ্যই জানেন,Root করার সুবিধা সম্পর্কে।

Xiaomi Redmi Note 4/4x ফোনগুলো Root করার পর কিছু সমস্যা হতে পারে।তার মধ্যে অন্যতম USB কানেক্ট না হওয়া।আপনারও যদি একই সমস্যা হয়ে থাকে তাহলে এই টিউনটি আপনার জন্য।  কথা না বাড়িয়ে আসল কথায় আসি।(অবশ্যই Rooted ফোনের জন্য)

## যা লাগবেঃ

ES Explorer (Pro ভার্শন হলে ভালো)

- ১ম ধাপঃ ES Explorer ওপেন করে বাম পাশের মেন্যু অপশান থেকে Root Explorer অপশানটি চালু করে নিন।
- ২য় ধাপঃ Device মেমোরী(Root মেমোরী) যান।
- ৩য় ধাপঃ system ফোল্ডারটি ওপেন করুন।
- ৪র্থ ধাপঃ একেবারে নীচে থাকা build.prop ফাইলটিতে ক্লিক করুন।ES Note Editor সিলেক্ট করুন।
- ৫ম ধাপঃ পেন্সিল আইকনটিতে ক্লিক করুন(ফাইলটি Edit করার জন্য)।

৬ষ্ঠ ধাপঃ স্ক্রল করে একেবারে নীচে এই ৩টি লাইন লিখুন-

persist.service.adb.enable=1

persist.service.debuggable=1

persist.sys.usb.config=mtp,adb

[এডিট করার আগে build.prop ফাইলটি অবশ্যই কপি করে রাখবেন। তাহলে ভুলবশত ফাইলটি Corrupted হয়ে গেলে Copy করা ফাইলটি Restore করতে পারবেন]

- ৭ম ধাপঃ উপরের তীর(<--) চীহ্নটিতে ক্লিক করে Save দিয়ে বেরিয়ে আসুন।
- ৮ম ধাপঃ Settings থেকে About phone এ ক্লিক করুন। সেখানে MIUI version লেখাটিতে কয়েকবার ক্লিক করলে Developer Options Enable হয়ে যাবে। এরপর Back করে Additional settings-এ যান।Accessibility-র নীচে developer options-এ ক্লিক করুন। স্ক্রল করে নীচে গিয়ে USB debugging চালু করে দিন।
- ৯ম ধাপঃ ফোন রিস্টার্ট দিন। এবার  USB কানেক্ট করে দেখুন কানেক্ট হয়ে গেছে।

হয়ে গেল USB connection-এর সমস্যার সমাধান।

ধন্যবাদ। 😀
