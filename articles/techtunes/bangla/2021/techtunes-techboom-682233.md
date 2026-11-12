---
archive_id: techtunes-682233
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 682233
title: Windows 10 version 2004 এর পাসওয়ার্ড বাগ ফিক্স করতে এসেছে অপশনাল আপডেট
slug: techtunes-techboom-682233
language: bn
status: publish
published_at: '2021-02-07T10:53:00+00:00'
modified_at: '2023-11-26T06:11:00+00:00'
original_url: https://www.techtunes.io/techtunes-techboom/tune-id/682233
author: টেকটিউনস টেকবুম
author_url: https://www.techtunes.io/tuner/techtunes-techboom
categories:
- টেকটিউনস টেকবুম
tags:
- অটোআপডেট
- টেকনিউজ
- প্রতিবেদন
content_hash: 8e714750a154a05aa9845aebdc4759274b3a39c3fc353262db6b64f8c6e495b7
archived_at: '2026-11-12T12:14:21.722813+00:00'
---

নতুন Windows 10 এর App Password Forget ইস্যু ফিক্স করবে অপশনাল Cumulative আপডেট। নতুন Cumulative আপডেটের মাধ্যমে একই সাথে ফিক্স হবে আরও অনেক গুলো বাগ।

জানা গেছে সম্প্রতি মাইক্রোসফট, Windows 10 version 2004 এর বেশ কিছু বাগ এর সমাধান নিয়ে এসেছে অপশনাল আপডেটে। Windows 10 KB4598291 cumulative আপডেট ইন্সটলে ইউজাররা পাবে সমাধান। আপডেটটি এসেছে গত ৩ ফেব্রুয়ারী। যে সমস্ত ইউজার তাদের Windows 10 মেশিনে 2004 ভার্সনটি আপডেট দিয়েছিল তারা এখন নতুন আপডেটটিও পাবে।

এখানে উল্লেখ্য, উইন্ডোজ ইউজাররা তাদের পিসিকে Windows 10 version 2004 এ আপগ্রেড করার পর একাধিক সমস্যা ফেস করতে থাকে। এর মধ্যে যে সমস্যাটি অধিকাংশ ইউজার পায় সেটি ছিল, বিভিন্ন অ্যাপ পাসওয়ার্ড ভুলে গিয়েছিল। ইউজাররা দাবী করে উইন্ডোজ আপগ্রেড করা পর বিভিন্ন অ্যাপ স্বয়ংক্রিয়ভাবে লগআউট হয়ে যায়৷ এই সমস্যাটি প্রথম বারের মত ডিটেক্ট করে গুগলের সিকিউরিটি রিসার্চার Tavis Ormandy। সে তার অভিজ্ঞতা টুইটারের একটি টুইটের মাধ্যমে প্রকাশ করে।

> I've been experiencing a really bad Windows 10 bug since the 2004 update. I got so annoyed I spent my weekend debugging it. A specific type of scheduled task can break CryptUnprotectData(). If you've seen apps losing state, eventid 8198, or NTE\_BAD\_KEY\_STATE, could be this.
>
> — Tavis Ormandy (@taviso) [September 28, 2020](https://twitter.com/taviso/status/1310619801606184960?ref_src=twsrc%5Etfw)

এই সমস্যাটি হবার কারণ হচ্ছে আপগ্রেডের পর সেভ পাসওয়ার্ড গুলো মুছে যাওয়া। পাসওয়ার্ড ক্লিয়ার হয়ে যাবার পর অ্যাপ গুলো লগআউট হবে এটাই স্বাভাবিক।

Windows 10 KB4598291 Cumulative আপডেট একটি অপশনাল আপডেট, এর মানে এটি স্বয়ংক্রিয়ভাবে আপনার পিসিতে ইন্সটল হবে না, আপনাকে ইন্সটল করে নিতে হবে। আপনিও যদি Windows 10 version 2004 ইন্সটল দেবার পর কোন সমস্যা ফেস করেন তাহলে এখনি আপডেট করে ফেলতে পারেন আপনার পিসিটি। প্রথমে Settings > Update & Security, যান এবং Check for Updates এ ক্লিক করুন। আপডেটটি অপশনাল আপডেট সেকশনে শো করবে, Download and install ক্লিক করুন। আপডেট প্রক্রিয়া সম্পাদন হয়ে গেলে পিসি রিস্টার্ট দিন।

এই আপডেটের ফলে, ডিভাইস Hibernate এর পর ব্ল্যাক স্ক্রিনের সমস্যা সমাধান করবে, Zip ফাইল Extraction এ Extract all শর্টকাট হারিয়ে যাওয়া ঠিক করবে, ফুল স্ক্রিন মুডে বা ট্যাবলেট মুডে গেমস খেলার সময় ডিভাইস Stop Responding সমস্যারও সমাধান করবে।

তাছাড়া এই আপডেটের ফলে আর কি সমস্যার সমাধান পাওয়া যাবে জানতে, [Microsoft Support](https://support.microsoft.com/en-us/topic/february-2-2021-kb4598291-os-builds-19041-789-and-19042-789-preview-6a766199-a4f1-616e-1f5c-58bdc3ca5e3b) পেজটি ভিজিট করতে পারেন। আপনার পিসিকে সব সময় নিরাপদ রাখতে এবং সমস্যা মুক্ত রাখতে আপ টু ডেট রাখার চেষ্টা করুন।

-  
 টেকটিউনস টেকবুম - ০৭ ফেব্রুয়ারি ২০২১
