---
archive_id: techtunes-505167
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 505167
title: VLSM (Variable Length Subnet Mask)
slug: networking-505167
language: bn
status: publish
published_at: '2017-07-31T05:15:00+00:00'
modified_at: '2017-10-11T10:35:00+00:00'
original_url: https://www.techtunes.io/networking/tune-id/505167
author: জামাল হোসেন
author_url: https://www.techtunes.io/tuner/jh1337-cse
categories:
- নেটওয়ার্কিং
tags:
- কম্পিউটার নেটওয়ার্ক
- ভিএলএসএম
- সিসিএনএ
content_hash: e65a8455ddb312d3b136baf79adfbec7b1f61d6d087a840bc13805a311257ccf
archived_at: '2026-11-12T12:44:56.310490+00:00'
---

VLSM নেটওয়ার্কিং এর একটি অত্যন্ত গুরুত্বপূর্ণ টপিক। যারা CCNA করছো অথবা ইউনিভার্সিটিতে "কম্পিউটার নেটওয়ার্কিং" পড়ছো তাদের জন্য VLSM না জানলেই নয়। এখন কথা কথা হচ্ছে আমরা কেন VLSM করবো??? উত্তর হচ্ছে, যখন একটি আইপি এড্রেস দিয়ে কয়েকটি নেটওয়ার্কের হোস্টের/কম্পিউটারের সংখ্যা অনুযায়ী আইপি এসাইন করতে হয় ঠিক তখনই VLSM করতে হয় যেন যতটা পারা যায় আইপি গুলোর সদ্ব্যবহার করা যায়। তো চল শুরু করি।

প্রথমে একটি প্রবলেম দিয়েই শুরু করি। ধরা যাক, কোন এক প্রতিষ্ঠানের বিভিন্ন Department এ নিচের তালিকা অনুযায়ী কম্পিউটার রয়েছে এবং আমাদের এ সবগুলো কম্পিউটারে IP Address দিতে হবে। একই সাথে সেই প্রতিষ্ঠানে থেকে আমাকে একটি IP Address Block 172.12.0.0/16 দিয়ে দেওয়া হয়েছে যা দিয়ে প্রত্যেক Department এর জন্য আলাদা আলাদা LAN (Network) গঠন করতে হবে।

![](https://dnc.techtunes.io/tDrive/tuner/jh1337-cse/505167/vlsm1.jpg)

তো আমাদের এখানে কি কি কাজ করতে হবে??? তেমন বেশী কিছু না। শুধু মাত্র নিচের টেবিলটি তৈরি করতে পারলেই আমাদের কাজ শেষ।

![](https://dnc.techtunes.io/tDrive/tuner/jh1337-cse/505167/vlsm2.jpg)

(i) প্রথমে আমরা এই Department & Required IP Column টি পূরণ করবো। পূরণ করার আগে একটি কথা মনে রাখতে হবে আমাদের যে required IP দেওয়া আছে তার সাথে 2 যোগ করতে হবে কেননা এই 2 টি IP এর একটি হবে Network Address অন্যটি Broadcast Address.

Ex: CSE Dept. এ required IP হলো 4000, কিন্তু আমরা এর সাথে 2 যোগ করে লিখবো 4002. এভাবে সম্পূর্ণ Column টি পূর্ণ করতে হবে।

![](https://dnc.techtunes.io/tDrive/tuner/jh1337-cse/505167/vlsm3-1.jpg)

(ii) এবার আমাদের Host bit (n) এর Column টি পূর্ণ করার পালা। সবসময় মনে রাখতে হবে required IP যতই হোক না কেন তা 2 এর Power (2n) হতে হবে।

Ex: CSE Department এর required IP হচ্ছে 4002 টি। আমরা যদি 211 দেই তাহলে এতে IP Address এর সংখ্যা হয় 2048 টি, যা আমাদের requirement fulfil করে না। কিন্তু আমরা যদি 212 দেই তাহলে এতে IP Address এর সংখ্যা হয় 4076 টি, যা আমাদের requirement fulfil করেও কিছু IP বেশী রয়ে যায়। মনে রাখতে হবে IP Assigning সবসময় 100% fill up করা যায় না। সুতরাং আমাদের এখানে n এর value হচ্ছে 12 যা Host bit সংখ্যা নির্দেশ করে। এভাবে সম্পূর্ণ Column টি পূর্ণ করতে হবে।

(iii) এবার আসি Network Address কিভাবে নির্ণয় করা যায়। Network Address এর Column টি পূর্ণ করার আগে চল দেখে নেই কিভাবে Broadcast Address নির্ণয় করতে হয়।

## (ক) পদ্ধতি-১

আমরা জানি, কোন একটি IP Address এ Network bit গুলো 1 থাকে এবং Host bit গুলো 0 থাকে।

Host bit এ যেহেতু সবগুলো 0 থাকে। তাই শূন্যের পরিবর্তে সবগুলো 1 বসিয়ে যে Binary সংখ্যা পাওয়া যায়, সেই বাইনারি সংখ্যাকে Decimal এ পরিবর্তন করে মূল আইপি এর সাথে যোগ করতে হয়।

Ex: ধরা যাক, Host bit সংখ্যাঃ 12 (11110000.00000000)

![](https://dnc.techtunes.io/tDrive/tuner/jh1337-cse/505167/vlsm4.jpg)

4095 = 256×15+255. যেহেতু প্রত্যেক 256 এর জন্য 1 bit পরিবর্তন হবে সুতরাং CSE Dept. এর Broadcast address হবে 172.12.15.255

## (খ) পদ্ধতি-২

এছাড়াও আরও সহজে এবং তাড়াতাড়ি Broadcast Address নির্ণয় করা যায়। শুধুমাত্র Host bit কে 2 এর Power ধরে সেখান থেকে 1 বিয়োগ করতে হয়।

212-1=4095 (using calculator)

4095 থেকে 256 করে বিয়োগ করতে থাকবো যত পর্যন্ত না তা 256 এর কম চলে আসে। একই সাথে মনে রাখতে হবে কতবার আমি 256 বিয়োগ করেছি। এবং সে সংখ্যাটি হচ্ছে 15. অর্থাৎ আমি 15 বার 256 বিয়োগ করেছি।

এবার ফিরে যাই Network Address এর Column এ। প্রথম Network Address (CSE Dept.) হবে আমাদের যে IP block টি দেওয়া আছে সেটি। তারপর Broadcast Address নির্ণয় করবো। এবার পরবর্তী Network Address(EEE Dept.) হবে পূর্বের Broadcast Address(CSE Dept.) থেকে 1 বেশী। তারপর আবার Broadcast Address(EEE Dept.) নির্ণয় করবো। এভাবে পরপর দুটি column (Network & Broadcast) একই সাথে পূরণ করতে হবে।

![](https://dnc.techtunes.io/tDrive/tuner/jh1337-cse/505167/vlsm5-2.jpg)

(iv) First Usable IP হবে Network Address থেকে 1 বেশী এবং Last Usable IP হবে Broadcast Address থেকে 1 কম।

![](https://dnc.techtunes.io/tDrive/tuner/jh1337-cse/505167/vlsm6-2.jpg)

(v) আমাদের সর্বশেষ ধাপ Subnet Mask নির্ণয়

## পদ্ধতি-১

আমরা জানি IPv4 Address হচ্ছে 32 bit. তাই বলা যায় CSE Dept. এ যেহেতু Host bit সংখ্যা 12 তাই এর Network bit সংখ্যা হবে 32-12=20. অর্থাৎ এর Network Address এ 20 টি 1 রয়েছে এবং একই সাথে Host Address এ 12 টি 0 আছে। নিচে তা দেখানো হলো-

11111111.11111111.11110000.00000000 এই বাইনারী সংখ্যাটিকে Decimal এ পরিবর্তন করলেই Subnet Mask পাওয়া যায়।

255            255              240              0

অর্থাৎ 255.255.240.0 ই হচ্ছে আমাদের কাঙ্ক্ষিত CSE Dept. এর Subnet Mask.

## পদ্ধতি-২

আরও সহজে এবং তাড়াতাড়ি Subnet Mask নির্ণয় করা যায়। শুধুমাত্র খেয়াল করতে হবে কোন Bit টি আসলে change হচ্ছে। CSE Dept. এ Network bit হচ্ছে 32-12=20. 1st  8 bit + 2nd 8 bit =16 bit, বাকি 4 bit নিতে হবে 3rd 8 bit থেকে। কাজেই বলা যায় 3rd Octet change হচ্ছে। শেষ bit গুলো যেহেতু Host bit, তাই 4th Octet অপরিবর্তনীয় অর্থাৎ 0 ই থাকবে।

11111111.11111111.11110000.00000000

Bit:            8               8                 8                 8

255        255               ?                 0

এবার 3rd Octet (11110000) এর Decimal value হচ্ছে 240. সুতরাং Subnet Mask হচ্ছে 255.255.240.0। নিচের Table টি মনে রাখলে খব তাড়াতাড়ি Subnet Mask নির্ণয় করা যায়।

![](https://dnc.techtunes.io/tDrive/tuner/jh1337-cse/505167/vlsm7-1.jpg)

এভাবে সম্পূর্ণ Column পূরণ করতে হবে।

![](https://dnc.techtunes.io/tDrive/tuner/jh1337-cse/505167/vlsm.jpg)

ভিডিও টিউটোরিয়ালঃ <https://www.youtube.com/watch?v=YCz4ADTsIO0&index=14&list=PL5SsUwhEEVyg3n5UrNFj8EGds3DVEW0-J>
