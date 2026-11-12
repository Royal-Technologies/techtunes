---
archive_id: techtunes-684755
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 684755
title: সেরা দশটি ফ্রি ওপেন সোর্স DNS সার্ভার যেগুলো আপনি ব্যবহার করতে পারেন
slug: tips-and-tricks-684755
language: bn
status: publish
published_at: '2021-08-31T06:46:00+00:00'
modified_at: '2021-08-31T06:46:00+00:00'
original_url: https://www.techtunes.io/tips-and-tricks/tune-id/684755
author: সোহানুর রহমান
author_url: https://www.techtunes.io/tuner/sohanur-raihan
categories:
- টিপস এন্ড ট্রিকস
tags:
- ইনটারনেট
- ওয়েবসার্ভার
- টিপ্স এন্ড ট্রিকস
content_hash: 672f1a401e8acc36cb68df2b78258bd51111a7f3a812718b06004556f66eee9f
archived_at: '2026-11-12T12:12:33.812752+00:00'
---

আসসালামু আলাইকুম, কেমন আছেন সবাই? আশা করছি সবাই ভাল আছেন। বরাবরের মতই আজকে হাজির হলাম নতুন কিছু নিয়ে।

আজকের আলোচনার শুরুতেই আমাদের জেনে নিতে হবে DNS এর কাজ কি এবং DNS আসলে কি? DNS এর পূর্ণরূপ হচ্ছে Domain Name System। সহজ ভাষায় বলতে গেলে আপনার চাহিদা মত নির্দিষ্ট ওয়েবসাইটকে দ্রুত আপনার সামনে প্রদর্শন করতে সাহায্য করে DNS। চলুন বিষয়টি বিস্তারিত জেনে নিই।

## DNS কি এবং কেন?

![](https://dnc.techtunes.io/tDrive/tuner/2021/04/techtunes_b3a6539c95c9db8089228d0bedc673d4.png)

ইন্টারনেটে যত ধরনের Domain রয়েছে সব গুলোর একটি নির্দিষ্ট আইপি এড্রেস থাকে। যেমন [Google](https://www.google.com/) এর একটি আইপি এড্রেস আছে, [Facebook](https://www.facebook.com/) এর একটি আইপি এড্রেস রয়েছে। কম্পিউটার কিন্তু Domain Name চিনে না, কম্পিউটার আইপি এড্রেসের মাধ্যমে নির্দিষ্ট ওয়েবসাইটে কমিউনিকেট করে। আমরা যখন একটি ওয়েবসাইটের নাম লিখি তখন কম্পিউটার খুঁজে বের করার চেষ্টা করে এর আইপি এড্রেস কি, যখন খুঁজে পায় তখন সেই আইপি এড্রেসের ইনফরমেশন আমাদের সামনে তুলে ধরে। আর কম্পিউটারকে আইপি এড্রেস খুঁজে পেতে সহায়তা করে DNS। DNS একটি এড্রেস-বুকের মত কাজ করে, সেখানে সকল ওয়েবসাইটের আইপি এড্রেস গুলো লিপিবদ্ধ থাকে। সুতরাং আপনি যত ভাল DNS ব্যবহার করবেন আপনার ওয়েবসাইট তত দ্রুত ওপেন হবে। এছাড়াও আরও বিভিন্ন কারণে DNS ব্যবহার করা যেতে পারে।

তো আজকে আমি সেরা দশটি ওপেন সোর্স DNS সার্ভার নিয়ে কথা বলব যেগুলো ব্যবহার করে আপনি আপনার ব্রাউজিং অভিজ্ঞতা আরও উন্নত এবং দ্রুত করতে পারবেন।

## ১. Google Public DNS Server

![](https://dnc.techtunes.io/tDrive/tuner/2021/04/techtunes_20f795a4f3ec0fdfeb1a305d38926edc.png)

ইন্টারনেটের অসংখ্য DNS সার্ভারের মধ্যে অন্যতম হচ্ছে, [Google Public DNS Server](https://developers.google.com/speed/public-dns)। দ্রুত ব্রাউজিং এক্সপেরিয়েন্স পেতে আপনাকে দারুণ ভাবে সাহায্য করবে এটি। দ্রুত ব্রাউজিং ছাড়াও ইন্টারনেটের সিকিউরিটি বাড়াতে কাজ করে গুগলের এই পাবলিক DNS সার্ভার।

অধিকাংশ মানুষ তাদের DNS হিসেবে Google Public DNS Server ব্যবহার করে, চাইলে আপনিও আপনার DNS সার্ভারে গুগলের সার্ভার ব্যবহার করতে পারেন,

DNS Server : 8.8.8.8  
 বিকল্প সার্ভার : 8.8.4.4

## ২. OpenDNS

![](https://dnc.techtunes.io/tDrive/tuner/2021/04/techtunes_bf07919f12997b649079f58060cb65fe.png)

[OpenDNS](https://www.opendns.com/) একটি ক্লাউড ভিত্তিক DNS সার্ভার। এই সার্ভারটি আপনাকে অতিদ্রুত ব্রাউজিং অভিজ্ঞতা প্রদান করবে। দ্রুত ইন্টারনেট ব্রাউজ নিশ্চিতের পাশাপাশি বিশ্বস্ত একটি সার্ভার এটি। এটি একই সাথে ইন্টারনেটের বিভিন্ন সাইবার এটাক থেকেও ইউজারদের রক্ষা করতে পারে৷ [OpenDNS](https://www.opendns.com/) এর দারুণ একটি ফিচার হচ্ছে কন্টেন্ট ফিল্টারিং ফিচার।

DNS Server: 208.67.222.222  
 বিকল্প DNS server: 208.67.222.220

## ৩. Comodo Secure DNS

![](https://dnc.techtunes.io/tDrive/tuner/2021/04/techtunes_2a344a94ecec5f0d89efb6a0a60d5490.png)

আপনার ISP যে সার্ভার প্রদান করে তার চেয়ে দ্রুত এবং বিশ্বস্ত DNS সার্ভার প্রদান করতে পারে [Comodo Secure DNS](https://www.comodo.com/secure-dns/)। [Comodo Secure DNS](https://www.comodo.com/secure-dns/) সেটআপ করার জন্য আপনাকে বাড়তি কোন সফটওয়্যার বা হার্ডওয়্যারের দরকারের হবে না। অবশ্যই এটি নিরাপদ। [Comodo Secure DNS](https://www.comodo.com/secure-dns/) সেট করতে চাইলে নিচের ইনফো গুলো ব্যবহার করতে পারেন।

DNS Server: 8.26.56.26  
 বিকল্প DNS server: 8.20.247.20

## ৪. Level3

![](https://dnc.techtunes.io/tDrive/tuner/2021/04/techtunes_34142d27305ffdff3ba865ed15d1c680.png)

বিশ্বজুড়ে ব্যাপক ভাবে ব্যবহৃত হওয়া আরেকটি DNS সার্ভার হল [Level3](https://www.publicdns.xyz/public/level3.html)। বিভিন্ন সাইবার এটাক প্রতিহত করতে এটি মাল্টিপল লেয়ারের সিকিউরিটি মেথড ব্যবহার করে। আপনার ডোমেইন নেম সার্ভিসের জন্য যথেষ্ট নিরাপদ হবে এই [Level3](https://www.publicdns.xyz/public/level3.html) এর DNS সার্ভার।

DNS Server: 209.244.0.3  
 বিকল্প DNS server: 208.244.0.4

## ৫. DNS Advantage

![](https://dnc.techtunes.io/tDrive/tuner/2021/04/techtunes_5bb58a845a92640dce40eafb94786f53.jpg)

[DNS Advantage](https://www.dnsadvantage.com/) এর DNS সার্ভারগুলোর যেকোনো ওয়েবসাইট খোলার জন্য সেরা রাউটিং তথ্য রয়েছে। যেহেতু তাদের কাছে সর্বোত্তম রাউটিং তথ্য রয়েছে সুতরাং তারা বেশ দ্রুত এবং নির্ভরযোগ্য। একই সাথে [DNS Advantage](https://www.dnsadvantage.com/) আপনাকে ইন্টারনেটের বিভিন্ন এটাকের হাত থেকে রক্ষা করার জন্য অত্যন্ত শক্তিশালী সিকিউরিটি ব্যবস্থা নিশ্চিত করবে।

DNS Server: 156.154.70.1  
 বিকল্প DNS server: 156.154.71.1

## ৬. OpenNIC

![](https://dnc.techtunes.io/tDrive/tuner/2021/04/techtunes_21a2e3cef31c773c92f4f2ec00356efc.png)

আপনি যদি প্রাইভেসি নিয়ে খুব বেশি সচেতন হোন তাহলে আপনার জন্য সেরা হতে পারে [OpenNIC](https://www.opennic.org/)। ব্রাউজিং এ আপনি দারুণ স্পীড পাবেন তবে এখানে প্রাইভেসিকে বেশি গুরুত্ব দেয়া হয়। আপনি যদি দেশের সরকারের হাত থেকেও আপনার ডেটাকে নিরাপদ করতে চান তাহলে এই সার্ভারটি ব্যবহার করতে পারেন।

DNS Server: 46.151.208.154  
 বিকল্প DNS server: 128.199.248.105

## ৭. Dyn

![](https://dnc.techtunes.io/tDrive/tuner/2021/04/techtunes_103d6937568a5a11c9807f47e4d8b7c3.png)

আমাদের লিস্টের অন্যতম আরেকটি DNS সার্ভার হচ্ছে [Dyn](https://account.dyn.com/)। আপনি যদি ব্রাউজিং এ ভিন্ন অভিজ্ঞতা পেতে চান তাহলে আপনি [Dyn](https://account.dyn.com/) চেষ্টা করে দেখতে পারেন। ব্রাউজিং এ ইউনিক অভিজ্ঞতা পেতে নিচের সার্ভার গুলো ব্যবহার করুন।

DNS Server: 216.146.35.35  
 বিকল্প DNS server: 216.146.36.36

## ৮. SafeDNS

![](https://dnc.techtunes.io/tDrive/tuner/2021/04/techtunes_f7c1e886f976979046211e4faea074ab.png)

নামের মতই সবার জন্য নিরাপদ একটি DNS সার্ভিস হচ্ছে [SafeDNS](https://www.safedns.com/)। ক্লাউড ভিত্তিক এই সার্ভারটি আপনাকে ডেটা শেয়ার এবং এক্সেস করার নিরাপদ একটি প্ল্যাটফর্মের ব্যবস্থা করে দেবে। [SafeDNS](https://www.safedns.com/) সেট করতে নিচের ইনফো গুলো ব্যবহার করতে পারেন

DNS Server: 195.46.39.39  
 বিকল্প DNS server: 195.46.39.40

## ৯. Verisign Public DNS

![](https://dnc.techtunes.io/tDrive/tuner/2021/04/techtunes_ed560bab0552ac5cba02902611d637d8.png)

স্ট্যাবিলিটি এবং সিকিউরিটি বাড়াতে আপনার জন্য সেরা বিকল্প হতে পারে [Verisign Public DNS](https://www.verisign.com/en_US/security-services/public-dns/index.xhtml)। এটা ব্যবহার করলে আপনার ডেটা থার্ডপার্টির কাছে যাবে না এবং এড টার্গেটের জন্যও ব্যবহৃত হবে না। এই DNS সেট করতে নিচের ইনফো গুলো ব্যবহার করুন।

DNS Server: 64.6.64.6  
 বিকল্প DNS server: 64.6.65.6

## ১০. DNS.Watch

![](https://dnc.techtunes.io/tDrive/tuner/2021/04/techtunes_258d04db4f725563585e2473eb702cbe.png)

[DNS.Watch](https://dns.watch/) আজকের লিস্টের শেষ DNS সার্ভিস। এই সার্ভিসটি তাদের No Censorship পলিসির জন্য বিখ্যাত। এটিও বেশ বিশ্বস্ত, নিরাপদ এবং ফাস্ট একটি DNS সার্ভিস। [DNS.Watch](https://dns.watch/) সেট করতে নিচের ইনফো ব্যবহার করুন।

DNS Server: 84.200.69.80  
 বিকল্প DNS server: 84.200.70.40

## শেষ কথাঃ

আপনাদের কথা ভেবে বিভিন্ন সুবিধা বিবেচনা করে সেরা ১০ টি DNS নিয়ে আলোচনা করলাম৷ এবার আপনার পছন্দ মত DNS ব্যবহার করুন।

তো আজকে এই পর্যন্তই, পরবর্তী টিউন পর্যন্ত ভাল থাকুন আল্লাহ হাফেজ।
