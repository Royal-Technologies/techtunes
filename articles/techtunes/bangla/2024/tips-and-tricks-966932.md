---
archive_id: techtunes-966932
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 966932
title: ৪০ টি উইন্ডোজ কমান্ড যেগুলো আপনার জানা উচিৎ
slug: tips-and-tricks-966932
language: bn
status: publish
published_at: '2024-05-16T21:19:00+00:00'
modified_at: '2024-04-30T15:23:00+00:00'
original_url: https://www.techtunes.io/tips-and-tricks/tune-id/966932
author: সোহানুর রহমান
author_url: https://www.techtunes.io/tuner/sohanur-raihan
categories:
- টিপস এন্ড ট্রিকস
tags:
- Tips টিপস
- আইপি অ্যাড্রেস
content_hash: 9a61e54e661ed9813a7047e8b8b15df7bb6e4c6c2e76e4c48bb009c3b80cf66e
archived_at: '2026-11-12T12:05:29.106437+00:00'
---

আসসালামু আলাইকুম, কেমন আছেন টেকটিউনস কমিউনিটি? আশা করছি সবাই ভাল আছেন। আজকে আবার হাজির হলাম নতুন টিউন নিয়ে।

আজকের টিউনে আমরা ৪০ টি Command Prompt জানব যেগুলো আপনার উইন্ডোজ অভিজ্ঞতা আরও উন্নত করতে পারে।

Command Prompt ওপেন করতে প্রথমে Start ম্যানুতে যান এবং Command Prompt লিখে সার্চ দিন। Command Prompt, Run as administrator এ ওপেন করুন।

## আইপি এড্রেস

আপনি যদি আপনার পিসির আইপি এড্রেস জানতে চান তাহলে নিচের কমান্ডটি দিন। এটি আপনার আইপি এড্রেস শো করবে। IPV4 Address থেকে আপনি আইপি এড্রেস দেখতে পাবেন।

ipconfig

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_cc98bbff961a41358b0cd7d19e3b040d.png)

## ম্যাক এড্রেস, DNS এড্রেস

আপনি যদি পিসির ম্যাক এড্রেস দেখতে চান তাহলে নিচের কমান্ডটি দিন। এখান থেকে আপনি ম্যাক এড্রেস, DNS এড্রেস সহজেই দেখতে পারবেন।

ipconfig /all

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_d569f5d83ca7865b3b043fa5f4eda786.png)

স্পেসিফিক ভাবে শুধু DNS বের করতে নিচের নিচের কমান্ডটি দিন।

ipconfig /all | findstr dns

## নতুন আইপি এড্রেস

আপনি যদি পিসির জন্য একটি নতুন আইপি এড্রেস চান তাহলে প্রথমে ipconfig /release কমান্ডটি দিন এবং পরবর্তীতে দিন নিচের কমান্ডটি। ব্যাস আপনি একটি নতুন আইপি এড্রেস পেয়ে যাবেন।

ipconfig /renew

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_83947d5b414c1290f4f61c24e52b1968.png)

আপনি চাইলে প্রতিটি ইন্টারফেস রিফ্রেশ করতে পারবেন যেমন Wifi চেঞ্জ করতে চাইলে ব্যবহার করুন

ipconfig /release "Wi-Fi"

## DNS ট্রাভেলস্যুট

প্রথমে DNS দেখতে নিচের কমান্ডটি দিন।

ipconfig /displaydns

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_843aa485c0a47e11420edac5fd5aa2e3.png)

এখন আপনি যদি এই DNS গুলো কপি করতে চান তাহলে নিচের কমান্ডটি দিন

ipconfig /displaydns | clip

ব্যাস আপনার ক্লিপবোর্ডে আউটপুট কপি হয়ে গেছে।

এখন আপনি যদি DNS, Flush করতে চান তাহলে নিচের কমান্ডটি দিন  
 ipconfig /flushdns

আপনার DNS Resolver Cache, ফ্লাস হয়ে গেছে।

আপনি যদি নির্দিষ্ট ওয়েবসাইটের DNS সংক্রান্ত তথ্য দেখতে চান তাহলে নিচের কমান্ডটি দিন।

nslookup techtunes.co

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_d4a924ae0b8868044b5aa0838f557197.png)

আপনি যদি DNS এড্রেস থেকে সার্ভার বের করতে চান তাহলে নিচের মত লিখতে পারেন

nslookup techtunes.co 8.8.8.8

যদি mx টাইপ বের করতে চান তাহলে লিখুন

nslookup -type=mx techtunes.co

txt দেখতে

nslookup -type=txt techtunes.co

ব্যবহার করতে পারেন

nslookup -type=ptr techtunes.co

স্ক্রিন ক্লিন করা

আপনি যদি Command Prompt এর পুরো স্ক্রিন ক্লিন করতে চান তাহলে নিচের কমান্ডটি দিন

cls

## ম্যাক এড্রেস

আপনি স্পেসিফিক ভাবে ম্যাক এড্রেস বের করতে চাইলে নিচের কমান্ডটি ব্যবহার করতে পারবেন

getmac /v

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_97e5dacf88f069a20a515720052e8a98.png)

## পাওয়ার এবং ব্যাটারি রিপোর্ট

আপনি যদি পাওয়ার এনার্জি নিয়ে রিপোর্ট দেখতে চান তাহলে নিচের কমান্ডটি দি

powercfg /energy

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_41df0618d3d108a5c9b98dca0b87d200.png)

যে এড্রেসটি আসবে ব্রাউজারে সেটা কপি করে  পেস্ট করে Enter দিন

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_a158bad961fc4324f03834d7ac3d2f23.png)

ব্যাটারি রিপোর্ট জানতে চাইলে নিচের কমান্ড ব্যবহার করুন

powercfg /batteryreport

যে এড্রেসটি আসবে সেটা কপি করে পেস্ট করে Enter দিন

## কোন ফাইল কোন অ্যাপে ওপেন হচ্ছে

কোন ফাইল এক্সটেনশন কোন অ্যাপ বা সফটওয়্যারে ওপেন হচ্ছে সেটা জনতে নিচের কমান্ডটি ব্যবহার করতে পারেন

assoc

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_02cb377964de66b3b6904064858b5802.png)

আপনার পিসি কি স্লো কাজ করছে? আপনি বুঝতে পারছেন না সমস্যা কোথায়? চলুন কিছু বিষয় চেক করে নেয়া যাক।

নিচের দুইটি কমান্ড দিয়ে ইস্যু চেক করতে পারেন  
 chkdsk /f  
 chkdsk /r

আপনি যদি সিস্টেম ফাইল চেক করতে চান তাহলে নিচের কমান্ডটি দিতে পারেন। sfc এর মানে হচ্ছে সিস্টেম ফাইল চেকার।

sfc /scannnow

আপন যদি সিস্টেম ইমেজ চেক করতে চান তাহলে নিচের কমান্ডটি দিন।

DISM /Online /Cleanup /CheckHealth

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_f022105cd6867959e61c70fd951ea479.png)

আরও ডিপ স্ক্যানের জন্য নিচের কমান্ড দিন

DISM /Online /Cleanup /ScanHealth

যদি কোন ইস্যু থাকে তাহলে নিচের কমান্ডটি দিয়ে সিস্টেম রিস্টোর করতে পারেন

DISM /Online /Cleanup /RestoreHealth

## অটো রান কিছু ডিজেবল

অটো রান ডিজেবল করতে নিচের পদক্ষেপ গ্রহণ করুন

প্রথমে আমাদের জানতে হবে কোন কোন টাস্ক রান হচ্ছে এজন্য নিচের কমান্ডটি দিন

tasklist | findstr script

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_a08ac6d7656d121076e66f3f2f6c3f59.png)

যে স্ক্রিপ্ট গুলো রান হচ্ছে সেটা এখানে দেখাবে, নাম্বার গুলো নোট করুন।

নির্দিষ্ট টাস্ক অফ করতে নিচের কমান্ড দিন

taskkill /f /pid 20184

## wlan রিপোর্ট

আপনি wlan এর বিস্তারিত রিপোর্ট পেতে নিচের কমান্ডটি ব্যবহার করতে পারেন

netsh wlan show wlanreport

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_349ac06295846cc9bd1aa075ce24251c.png)

এন্টার দেয়ার পর যে এড্রেসটি আসবে সেটা কমান্ড হিসেবে দিন অথবা ব্রাউজারে ওপেন করুন।

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_aa5e7961f4e687d66d48ce6665ae715c.png)

## পিসির নেটওয়ার্ক ইন্টারফেস

পিসিতে নেটওয়ার্ক ইন্টারফেস বা কিভাবে কানেক্ট আছে জানতে নিচের কমান্ডটি দিন

netsh interface show interface

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_8e006b5a1021f73b9887786b64aadbc2.png)

নেটওয়ার্ক ইন্টারফেসের আইপি দেখতে,

netsh interface ip show address | findstr “IP Address”

এবং DNS সার্ভার দেখতে নিচের কমান্ডটি দিন

netsh interface ip show dnsservers

## উইন্ডোজের Firewall স্ট্যাটাস

উইন্ডোজের Firewall স্ট্যাটাস চেক করতে নিচের কমান্ড দিন

netsh advfirewall set allprofiles state off

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_71d22f6ad0809853f080b4c12bdd38c6.png)

Firewall এনেভল করতে নিচের কমান্ড দিয়ে Enter করুন

netsh advfirewall set allprofiles state on

## ওয়েবসাইট Ping করা

আপনি যদি নির্দিষ্ট ওয়েবসাইট Ping করতে চান তাহলে নিচের কমান্ড ব্যবহার করুন

ping techtunes.co

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_64fb1af43de688dedc5a60bdcca61b03.png)

এক্ষেত্রে চার বার Ping হয়, আনলিমিটেড Ping করতে নিচের কমান্ড ব্যবহার করতে পারেন,

ping -t techtunes.co

আপনি যদি কোন ওয়েবসাইটের Tracing route দেখতে চান তাহলে নিচের কমান্ডটি দিন

Tracert techtunes.co

উপরের কামান্ডে কিছুটা স্লো হতে পারে, এটার স্পিড বাড়াতে নিচের কমান্ডটি দিন।

tracert -d techtunes.co

## কানেকশন প্রোটোকল

আপনার পিসির একটিভ কানেকশন গুলোর প্রোটোকল দেখতে নিচের কমান্ড দিন  
 netstat

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_1f0f72e08415839586ee9be1e23f5a0b.png)

আরও বিস্তারিত জানতে  
 netstat -af

একটিভ কানেকশন গুলো PID সহ দেখতে নিচের কমান্ড দিন

netstat -o

প্রতি ৫ সেকেন্ডে সেন্ড রিসিভ স্ট্যাট দেখতে নিচের কমান্ড দিন

netstat -e -t 5

## নেটওয়ার্ক Route

নেটওয়ার্কের Route সম্পর্কে জানতে নিচের কমান্ডটি দিন

route print

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_f19276e5fc135bb1e88dcd0541b53127.png)

Route যদি মাস্ক করতে চান তাহলে নিচের মত Route লিখুন

route add 192.168.40.0 mask 255.255.255.0 10.7.1.44

Route ডিলিট করতে ব্যবহার করুন

route delete 192.168.40.0

## Recovery Environment

আপনি যদি পিসিতে UEFI BIOS অথবা Windows 10 Recovery Environment ওপেন করতে চান তাহলে সরাসরি নিচের কমান্ডটি দিন।

shutdown /r /o /f /t 0

![](https://dnc.techtunes.io/tDrive/tuner/2023/05/techtunes_aeab32ef0bd233884fced6bf7cf72f85.png)

## শেষ কথা

পিসির বিভিন্ন কাজ দ্রুত সময়ের মধ্যে করতে Command Prompt এর বিকল্প নেই। উপরে উল্লেখিত কমান্ড গুলো দিয়ে সহজেই আপনি নির্দিষ্ট কাজ করে ফেলতে পারবেন। আশা করছি এই কমান্ড গুলো আপনার দারুণ কাজে আসবে।

তো আজকে এই পর্যন্তই পরবর্তী টিউন পর্যন্ত ভাল থাকুন আল্লাহ হাফেজ।
