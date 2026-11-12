---
archive_id: techtunes-653731
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 653731
title: MuxEmail – ফ্রিতে ২৫ হাজার Email Newsletter পাঠান Amazon SES ব্যবহার করে! সেই
  সাথে Drag and Drop Email Builder ব্যবহার করে করুন Email Campaign আর Campaign এর
  যাবতীয় রিপোর্ট দেখুন
slug: webware-653731
language: bn
status: publish
published_at: '2024-01-08T02:18:00+00:00'
modified_at: '2025-01-08T02:19:00+00:00'
original_url: https://www.techtunes.io/webware/tune-id/653731
author: সোহানুর রহমান
author_url: https://www.techtunes.io/tuner/sohanur-raihan
categories:
- ওয়েবওয়্যার
tags:
- অসাধারন একট ওয়েবসাইট
- আজানের সফট
- ইমেইল মার্কেটিং
content_hash: db7ec65c6b754a0035fb329d513f9a068f3737f3d9a665063e3191095312651f
archived_at: '2026-11-12T12:24:45.043664+00:00'
---

আসসালামু আলাইকুম, কেমন আছেন টেকটিউনস কমিউনিটি? আশা করছি সবাই ভাল আছেন। আজকে আবার হাজির হলাম নতুন টিউন নিয়ে। চলুন শুরু করা যাক।

[Amazon SES (Simple Email Service)](https://aws.amazon.com/ses/) হচ্ছে [Amazon](https://www.amazon.com/) এর ক্লাউড Based ইমেইল সেন্ডিং সার্ভিস। অন্য যেকোনো ইমেইল সার্ভিস থেকে [Amazon SES (Simple Email Service)](https://aws.amazon.com/ses/) এর চার্জ প্রায় অর্ধেক, তাই সকল ডিজিটাল মার্কেটর এবং ডেভেলপারদের প্রথম পছন্দ এই Amazon SES। একটি সমস্যা হচ্ছে Amazon SES এর ইন্টারফেস Console টাইপ হওয়াতে এটি ইউজার-ফ্রেন্ডলি না এবং সেখানে Email Campaigns এর কোন অপশন নেই।

Amazon SES ব্যবহার করে ইউজার ইন্টারফেস ভিত্তিক অনেক সার্ভিস রয়েছে যা Amazon SES এর ইউজারদের ইউজার-ফ্রেন্ডলি ইন্টারফেস প্রোভাইড করে। এরকম অনেক সার্ভিস আছে যেগুলো ইউজার ফ্রেন্ডলি ইন্টারফেস দিয়ে Email Campaign এর সুবিধা করে দেয়। তবে এসব সার্ভিসের দারুণ একটি সমস্যা হচ্ছে এগুলোর বেশিরভাগই পেইড প্ল্যাটফর্ম যা দিয়ে ইমেইল ক্যাম্পেইন করতে হলে প্ল্যাটফর্ম ব্যবহারের জন্য আপনাকে ডলার গুনতে হয়। এই সমস্যা সমাধানের জন্য আজকে আমি পরিচয় করিয়ে দেব MuXEmail এর সাথে।

## MuxEmail কি?

MuxEmail  একটি ফ্রি এপ্লিকেশন যার মাধ্যমে ব্যবহার করে Email Eewsletter পাঠাতে পারবেন। এখানে অনেক বেশি ফিচার না থাকলেও এর মাধ্যমে আপনি কোথাও হোস্টিং করা ছাড়াই ফ্রিতে ২৫০০০/২৫ হাজার মেইল পাঠাতে পারবেন।

Amazon SES এর সাথে কানেক্ট হয়ে MuxEmail এর মাধ্যমে আপনি সহজেই Drag and Drop Email Builder ব্যবহার করে Email Campaign তৈরি করতে পারবেন। এখানে শিডিউল ইমেইল ক্যাম্পেইনের পাশাপাশি দেখতে পারবেন ইমেইল রিপোর্টও।

## MuxEmail

অফিশিয়াল ওয়েবসাইট @ [MuxEmail](https://muxemail.com/)

## কিভাবে ব্যবহার করবেন, MuxEmail?

চলুন দেখে নেয়া যাক কিভাবে এই [MuxEmail](https://muxemail.com/) ব্যবহার করে ফ্রি ইমেইল নিউজলেটার পাঠাবেন।

### ধাপ ১

প্রথমে [MuxEmail](https://muxemail.com/) এর ওয়েবসাইটে চলে যান এবং ইমেইল ভেরিফিকেশন করে লগইন করুন। ওয়েবসাইটে আপনি Audience, Campaigns, Templates, AWS Configuration এর মত আলাদা আলাদা সেকশন পাবেন। কাজ শুরু করার আগে আপনার [Amazon SES (Simple Email Service)](https://aws.amazon.com/ses/) একাউন্টটি কানেক্ট করতে হবে।

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_7e7b632814dcebf37b2c8f4464f087a3.png)

এজন্য আপনি একটি [Amazon SES (Simple Email Service)](https://aws.amazon.com/ses/)একাউন্ট খুলে নিন অথবা আগে থাকলে সেটিও ব্যবহার করতে পারেন। প্রয়োজনীয় তথ্য দিয়ে Amazon SES একাউন্টটি কানেক্ট করে ফেলুন।

### ধাপ ২

এবার আপনার audience তৈরি করার পালা। আপনি চাইলে CSV ফাইল Import করে কন্টাক্ট এড করতে পারেন অথবা গ্রুপ তৈরি করতে পারেন। audience মেনটেন করার জন্য গ্রুপ তৈরি করে নেওয়াই ভাল।

### ধাপ ৩

যেকোনো ক্যাম্পেইন তৈরি করার আগে, একটি ইমেইল ক্যাম্পেইন প্রথমে টেম্পলেট আকারে সেভ করে নিতে পারেন। আপনি [MuxEmail](https://muxemail.com/) এর Drag and drop editor ফিচার ব্যবহার করে Email Template ডিজাইন করতে পারেন অথবা আগে থেকে HTML ফরমেটে  Email Template থাকলে সেটিও HTML editor এ পেস্ট করে দিতে পারেন। তবে Drag and Drop Editor ব্যবহার করে নিজের মত টেম্পলেট তৈরি করে নেওয়াই ভাল। এখানে বিভিন্ন ধরনের কন্টেন্ট, ব্লক এবং ফর্মেটিং এর মাধ্যমে সহজেই নিজের মত টেম্পলেট বানিয়ে নেয়া যায়।

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_f5afd7a48c4f0740e7d86d54da32beda.png)

### ধাপ ৪

আপনার Audience এবং Template রেডি হয়ে গেলে এবার চলে যান Campaign সেকশনে এবং নতুন একটি ইমেইল ক্যাম্পেইন তৈরি করুন। প্রথমে ধাপে আপনি, নাম, সাবজেক্ট, সেন্ডার ইনফো ইত্যাদি দিন এর পর নতুন অথবা সেভ টেম্পলেট সিলেক্ট করুন। পরের ধাপে Audience নির্দিষ্ট করে দিন এবং চাহিদা মত তারিখে ক্যাম্পেইনটি শিডিউল করে দিন।

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_8492139749f516e14fb13997772f40ce.png)

ক্যাম্পেইন পাঠিয়ে দেবার পর আপনি Campaign সেকশন থেকে যাবতীয় রিপোর্ট দেখতে পাবেন যেমন, Subscribers, Opens, Clicks, Bounces, এবং Unsubscribes ইত্যাদি।

## MuxEmail এর সুবিধা

চলুন দেখে নেয়া যাক কেন ব্যবহার করবেন [MuxEmail](https://muxemail.com/) এবং এর কিছু সুবিধা।

- Amazon SES ব্যবহার করে Email Newsletters পাঠাতে পারবেন।
- ফ্রিতে ২৫০০০ ইমেইল পাঠাতে পারবেন।
- Drag and Drop Builder এর মাধ্যমে নিজেই সহজে ইমেইল টেম্পলেট বানিয়ে ফেলতে পারবেন।

### শেষ কথা:

আপনি দেখতেই পেলেন [MuxEmail](https://muxemail.com/) এর ইমেইল মার্কেটিং সার্ভিস, যা ব্যবহার করে আপনি ফ্রিতে প্রায় ২৫০০০  Email Newsletter পাঠাতে পারবেন। [MuxEmail](https://muxemail.com/) এর মাধ্যমে ফ্রিতে যেমন ইমেইল পাঠানো যায় তেমনি ইমেইল টেম্পলেট ও তৈরি করা যায় খুব সহজে। আমি মনে করছি যারা ইমেইল মার্কেটিং করছেন তাদের কাছে সার্ভিসটি চমৎকার লাগবে।

কেমন হল আজকের টিউন তা অবশ্যই টিউমেন্টের মাধ্যমে জানাবেন। আমাদের জানান আপনার কাছে কেমন লেগেছে এই ওয়েব-ওয়্যারটি।

পরবর্তী টিউন পর্যন্ত ভাল থাকুন। আল্লাহর উপর ভরসা রাখুন, আল্লাহ হা-ফেজ।
