---
archive_id: techtunes-374554
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 374554
title: দ্বিতীয় বার এক্টিভেটর ব্যবহার করতে হবেনা উইন্ডোস ইনস্টল করার সময়
slug: windows-374554
language: bn
status: publish
published_at: '2018-08-24T11:09:00+00:00'
modified_at: '2018-08-24T11:09:00+00:00'
original_url: https://www.techtunes.io/windows/tune-id/374554
author: অভিষেক হাজরা
author_url: https://www.techtunes.io/tuner/jibonre
categories:
- উইন্ডোস
tags:
- Activation of windows
- how to save activation
- Windows 10
content_hash: 2662f1473ba3c02728a27cf24da0e265a53df8eb1cde52849e090063439eddd2
archived_at: '2026-11-12T12:56:22.251935+00:00'
---

আজ আপনাদের এমন একটা পদ্ধতির সম্বন্ধে কথা বলব যা দেখলে আপনাদের আর দ্বিতীয় বার এক্টিভেটর ব্যবহার করতে হবেনা উইন্ডোস ইনস্টল করার সময়  
 হ্যা ঠিক তাই আমি অ্যাক্টিভেটেড উইন্ডোস থেকে আবার রিইনস্টল করার কথা বলছি  
 এই যেমন ধরুন ২৯ জুলাই মাইক্রোসফট ফ্রি তে উইন্ডোস১০ আপগ্রেড করে দিল আপনাকে এবং সেটা ফ্রি তে অনলাইন এক্টিভেট হয়ে গেল,  
 কিন্তু আপনি হয়ত জানেন না যে ফ্রি তে আপগ্রেড করার জন্য আপনার হার্ড ড্রাইভ এর ৩৭ জিবি জায়গা নষ্ট হবে,  
 ৩৭ জিবি জায়গা কিকরে নষ্ট হবে?  আপগ্রেড ফাইল সাইজও ৪ জিবি windows.old ১৭ জিবি  
 নতুন windows ১১ জিবি ও আনুসঙ্গিক নিয়া মোটামুটি ৩৫-৩৭ জিবি হবেই  
 এর পর আপনি যখন ক্লিন ইনস্টল এর কথা ভাববেন তখন আবার এক্টিভেট করতে গেলে সমস্যা।  
 তাই আগে থেকে জেনেনিন কি করে সেভ করে রাখবেন আপনার এক্টিভেশন বৈধ ভাবে

প্রথমে  
 Run গিয়া টাইপ করুন C:\Windows\System32\spp  
 এবং  ENTER  
 Copy the folder named "Store" এবং অন্যত্র সেভ করুন মানে ড্রাইভএ  
 ![](https://dnc.techtunes.io/tDrive/tuner/jibonre/374554/vdf.png)

এটাই হলো আপনার এক্টিভেশন কি বা ফাইল

কেমন করে কাজ করে জানতে হলে প্রথমে  
 open command prompt as Admin and type "slmgr/upk"  
 একটা ম্যাসেজ আসবে "Product key successfully uninstalled"

![](https://dnc.techtunes.io/tDrive/tuner/jibonre/374554/Untitled.jpg)

এবার সেফ মোডএ পিসি রিস্টার্ট করুন, [সেফ মোড পিসি রিস্টার্ট করার জন্য প্রথমে রান-এ টাইপ করুন "msconfig" and press ENTER  
 System Configuration পেজটি খুলবে, তার থেকে Boot ট্যাব Boot option Safe Boot click করুন  এবং  ENTER  
 একটা ম্যাসেজ আসবে restart or exit without restart সিলেক্ট  restart এবং  ENTER]

![](https://dnc.techtunes.io/tDrive/tuner/jibonre/374554/123.png)

SAFE MODE এ পিসি রিস্টার্ট হলে  
 open command prompt as Admin and type "net stop sppsvc"  
 একটা ম্যাসেজ আসবে Software Protection Platform service stopped successfully press ENTER

![](https://dnc.techtunes.io/tDrive/tuner/jibonre/374554/1234.png)  
 এবার Run গিয়া টাইপ করুন C:\Windows\System32\spp এবং  ENTER  
 and replace the "store" Folder with the previously Save "Store" Folder

![](https://dnc.techtunes.io/tDrive/tuner/jibonre/374554/12345.png)  
 এবার নরমাল মোড পিসি রিস্টার্ট করুন [সেফ মোড পিসি রিস্টার্ট করার জন্য প্রথমে রান-এ টাইপ করুন "msconfig" and press ENTER  
 System Configuration পেজটি খুলবে, তার থেকে Boot ট্যাব Boot option Safe Boot click করুন এবার Disable করার জন্য  এবং  ENTER  
 একটা ম্যাসেজ আসবে restart or exit without restart সিলেক্ট  restart এবং  ENTER]  
 NORMAL MODE এ পিসি রিস্টার্ট হলে open command prompt as Admin and type "slmgr.vbs/ato"

![](https://dnc.techtunes.io/tDrive/tuner/jibonre/374554/123456.png)

ব্যাস আপনার উইন্ডোস আবার এক্টিভেট কোনো এক্টিভেটর  ছাড়া।

![](https://dnc.techtunes.io/tDrive/tuner/jibonre/374554/1234567.png)

নিজে করে দেখুন ভালো লাগবে। আমি নিজে WINDOWS ১০ তে করে দেখালাম  আর একটা কথা Store এই ফাইল টি কিন্তু একই WINDOWS ভার্সন কাজ করে মানে ধরুন WINDOWS ৮ PRO WINDOWS ৮ PRO তে কাজ করবে, আপনার store অন্য কারো পিসিতে কাজ করবেনা।  
 আর দয়া করে সবাই টিউমেন্ট করবেন ভালো না লাগলেও।
