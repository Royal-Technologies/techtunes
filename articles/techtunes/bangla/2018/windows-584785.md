---
archive_id: techtunes-584785
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 584785
title: কিভাবে PC তে Virtual Hard Drive তৈরী করবেন
slug: windows-584785
language: bn
status: publish
published_at: '2018-06-05T20:42:00+00:00'
modified_at: '2018-06-12T17:07:00+00:00'
original_url: https://www.techtunes.io/windows/tune-id/584785
author: Era IT
author_url: https://www.techtunes.io/tuner/alaminera77
categories:
- উইন্ডোস
tags:
- Change Virtual Memory
- virtual harddrive space increase
content_hash: 0fa708ba2df0a41840e6e754fcc4d018da31df59fd08a0168bcf0fd146a4f4ac
archived_at: '2026-11-12T12:31:10.878739+00:00'
---

আশাকরি প্রতিদিনের মত আজও সবাই ভাল আছেন। আর ভাল থাকুন এটাই কামনা করি সারাক্ষন। আজ একটা খুবই গুরুত্বপূর্ন বিষয় নিয়ে আলোচনা করব। যারা কম্পিউটার ব্যবহার করেন তারা সবাই জানেন আপনার পিসির কত জিবি হার্ডডিস্ক আছে, কতগুলো ড্রাইভ আছে। কিন্তু কখনও কি চিন্তা করেছেন কিভাবে আপনার পিসিতে Virtual Hard Drive তৈরী করবেন? আজ তা নিয়েই আলোচনা করব।

প্রথমে আপনার ডেস্কটপের My PC or My Computer এ রাইট ক্লিক করুন। রাইট ক্লিক করলে যে উইন্ডো ওপেন হবে সেখান থেকে Manage এ ক্লিক করুন। দেখবেন নতুন একটা পেইজ ওপেন হবে। নিচের মত একটা পেইজ ওপেন হবে।

[![](https://dnc.techtunes.io/tDrive/tuner/2018/06/techtunes_a1356eb058a19e41d4096e4cafa37cc1.jpg)](https://dnc.techtunes.io/tDrive/tuner/2018/06/techtunes_a1356eb058a19e41d4096e4cafa37cc1.jpg)

এই পেইজ থেকে Disk Management এর উপর রাইট ক্লিক করুন। এবং এখান থেকে Create VHD তে ক্লিক করুন। তারপর দেখবেন নতুন আরেকটা উইন্ডো ওপেন হবে। এখান থেকে আপনি যে ড্রাইভের আন্ডারে আপনি ভার্চুয়াল ড্রাইভ তৈরী করবেন সেই ড্রাইভ ব্রাউজ করে আপনি আপনার Drive Name দিবেন।

[![](https://dnc.techtunes.io/tDrive/tuner/2018/06/techtunes_8005ad7fe2acfc7e4c6d56a03640f6fd.jpg)](https://dnc.techtunes.io/tDrive/tuner/2018/06/techtunes_8005ad7fe2acfc7e4c6d56a03640f6fd.jpg)

তারপর আপনার Drive Size দিবেন, তারপর Virtual Hard Disk Format - VHD সিলেক্ট করুন, Virtual Hard Disk Type - Fixed Size সিলেক্ট করুন এবং ok তে ক্লিক করুন।

এবার আপনার Virtual Hard Drive Setup করার পালা -

এখন আপনার পিসির Disk Management এর বাম দিকে দেখুন Disk 1 নামে নতুন একটা ড্রাইভ তৈরী হয়ে গিয়েছে। [![](https://dnc.techtunes.io/tDrive/tuner/2018/06/techtunes_a520c7da5444d9f81f562656b77e09f3.jpg)](https://dnc.techtunes.io/tDrive/tuner/2018/06/techtunes_a520c7da5444d9f81f562656b77e09f3.jpg)

Disk 1 এর উপর রাইট ক্লিক করুন এবং Initialize Disk এ ক্লিক করুন। নিচের মত আরেকটা পেইজ ওপেন হবে।

[![](https://dnc.techtunes.io/tDrive/tuner/2018/06/techtunes_6d1ff21faa053e1a2323bd03779dc1e5.jpg)](https://dnc.techtunes.io/tDrive/tuner/2018/06/techtunes_6d1ff21faa053e1a2323bd03779dc1e5.jpg)

নতুন এই উইন্ডোতে Disk 1 Select করুন। নিচের দিকে MBR (Master Boot Record)  সিলেক্ট করুন এবং ok তে ক্লিক করুন। নিচের মত আরেকটা পেইজ ওপেন হবে।

[![](https://dnc.techtunes.io/tDrive/tuner/2018/06/techtunes_821c819ee0024f9cf2e45da99ede764a.jpg)](https://dnc.techtunes.io/tDrive/tuner/2018/06/techtunes_821c819ee0024f9cf2e45da99ede764a.jpg)

এখানে আপনার Virtual Drive তৈরী হয়েছে। যা unallocated অবস্থায় থাকবে। এই unallocated ড্রাইভে রাইট করুন। তারপর New Simple Volume এ ক্লিক করুন তারপর আপনার ড্রাইভ এর Size দেখাবে। সাইট সিলেক্ট করে Next করুন। পরের পেইজে Drive Letter সিলেক্ট করে Next এ ক্লিক করুন। এর পরে যে পেইজটা আসবে তা নিচের মত দেখাবে।

[![](https://dnc.techtunes.io/tDrive/tuner/2018/06/techtunes_243ca6fd96f600cc0b322159d69010ee.jpg)](https://dnc.techtunes.io/tDrive/tuner/2018/06/techtunes_243ca6fd96f600cc0b322159d69010ee.jpg)

এই পেইজে File System - NTFS, Allocation unit Size - Default, Volume Label-WCData সিলেক্ট করুন। Perform a Quick Format এর টিক চিহ্ন দিতে হবে এবং Next এ ক্লিক করুন তাপর Finish এ ক্লিক করুন।

আপনার পিসিতে Virtual Hard Drive তৈরী হয়েছে। উপরের টিউনটি যদি বুঝতে সমস্যা হয় তাহলে **[এই ভিডিওটা](https://youtu.be/o4h0NHK0aLQ)** দেখে নিতে পারেন। তাহলে আপনি আরো ভাল ভাবে বুঝতে পারবেন।

**টিউন টি ভাল লাগলে নিচে দেওয়া আমার চ্যানেলে Subscribe করে রাখুন প্লিজ -**

**[আমার ইউটিউব চ্যানেল](https://goo.gl/2e63NS)।** [**আমার ফেসবুক পেইজ**](https://www.facebook.com/eraitbd)
