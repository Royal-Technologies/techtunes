---
archive_id: techtunes-676876
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 676876
title: MAC Address কি? কিভাবে আপনার ডিভাইসের MAC Address বের করবেন
slug: tips-and-tricks-676876
language: bn
status: publish
published_at: '2024-04-08T11:15:00+00:00'
modified_at: '2024-03-07T11:22:00+00:00'
original_url: https://www.techtunes.io/tips-and-tricks/tune-id/676876
author: সোহানুর রহমান
author_url: https://www.techtunes.io/tuner/sohanur-raihan
categories:
- টিপস এন্ড ট্রিকস
tags:
- Tips টিপস
- ম্যাক অ্যাড্রেস কি?
- ম্যাক এড্রেস
content_hash: 8a7be8510acbacf2a5d5a20f9fb75a70bbe5677ab06d270245807c6a1983ca4c
archived_at: '2026-11-12T12:17:26.696792+00:00'
---

টেকটিউনস কমিউনিটি, কেমন আছেন সবাই? আশা করছি সবাই ভাল আছেন। বরাবরের মত চলে এসেছি নতুন কোন টিউন নিয়ে।

ওয়াইফাই নেটওয়ার্কের সাথে সংযুক্ত যেকোনো ডিভাইস নিজেকে সনাক্ত করতে একটি স্বতন্ত্র নেটওয়ার্ক আইডেন্টেকটিউনস ব্যবহার করে। সেই স্বতন্ত্র আইডেন্টেকটিউনস নাম্বারকে Media Access Control বা MAC এড্রেস বলে। এটি নেটওয়ার্ক এডমিনিস্ট্রেটর কে নেটওয়ার্কে যুক্ত সকল ডিভাইসের প্রোফাইল বা কার্যকলাপ ট্র‍্যাক করতে সাহায্য করে।

বেশির ভাগ ক্ষেত্রে আমাদের এই ম্যাক এড্রেস নিয়ে চিন্তা করতে হয় না তেমন কোন কাজে লাগে না আবার কখনো কখনো এটি জানা আমাদের জন্য জরুরি হয়ে যায়। যেমন আপনি আপনার রাউটারে কোন ডিভাইসের এক্সেস নিয়ন্ত্রণ করতে চাচ্ছেন সেক্ষেত্রে কিন্তু আপনার নির্দিষ্ট ডিভাইসটির ম্যাক এড্রেস প্রয়োজন হবে।

যাই হোক, চলুন দেখে নেয়া যাক কিভাবে Mac এবং Windows পিসির ম্যাক এড্রেস কিভাবে বের করবেন।

## MAC Address কি?

![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_d6f1a0efe7dd91613c216307f2d6b264.png)

Mac Address একটি অনন্য 17 অক্ষর বিশিষ্ট নাম্বার (উদাহরণস্বরূপ: 00: 1A: C2: 9B: 00: 68) যা আপনার কম্পিউটারের Network Interface Controller (NIC) কার্ডে এম্বেড থাকা একটি হার্ডওয়্যার সনাক্তকারী হিসাবে কাজ করে।

এই স্বতন্ত্র নাম্বারটি ডিভাইস প্রস্ততকারকের দ্বারা নির্ধারিত এবং স্থায়ীভাবে আপনার ডিভাইসে সেট করা থাকে। এটি মূলত কোন লোকাল নেটওয়ার্কের মধ্যে ডিভাইসগুলির সংযোগ করার জন্য অনুমতি দেয়।

প্রধানত দুটি ধরনের Mac Address রয়েছে, যেমন, Universally Administered Address (UAA) এবং Locally Administered Address (LAA)।

UAA হল প্রধান ম্যাক এড্রেস যা ডিভাইস প্রস্ততকারকের দ্বারা নির্ধারিত হয়। আপনি আপনার নেটওয়ার্ক ডিভাইসে LAA নির্ধারণ করতে পারেন এবং এটি নির্মাতার দ্বারা নির্ধারিত ঠিকানাটি ওভার-রাইড করবে।

কখনো কখনো আপনার ডিভাইসের Mac Address এবং আইপি এড্রেস আপনাকে বিভ্রান্ত করতে পারে কারণ উভয়ই ইন্টারনেটে আপনার ডিভাইস সনাক্ত করতে ব্যবহৃত হয়, তবে এদের মধ্যে বড় পার্থক্য রয়েছে।

Mac Address স্থায়ীভাবে ডিভাইস প্রস্ততকারকের দ্বারা অন্যদের কাছ থেকে আপনার মেশিনটি সনাক্ত করার জন্য নির্ধারিত হয়। অন্যদিকে আইপি অ্যাড্রেস আপনার ডিভাইস এবং নেটওয়ার্কগুলি থেকে লজিকাল রুটেবল সংযোগ পরিচালনা করে এবং এটি অবস্থানের ভিত্তিতে পরিবর্তিত হয়।

যেখানে আপনার ডিভাইসের ম্যাক এড্রেস আপনার লোকাল নেটওয়ার্কের মধ্যে ব্যবহার করা হয়, সেখানে আইপি এড্রেস সারা বিশ্বে নেটওয়ার্ক ডিভাইসগুলি সনাক্ত করতে ব্যবহার করা হয়।

## কেন আমাদের ম্যাক এড্রেস বের করতে হবে

![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_83c054a2cc30726ebecb5d6b1d9f8cc2.jpg)

আপনার মনে প্রশ্ন আসতে পারে কি কি কারণে MAC Address আমাদের প্রয়োজন হতে পারে চলুন কারণ গুলো দেখে নেয়া যাক।

- আপনার ডিভাইস ট্র‍্যাক করতে
- অপ্রত্যাশিত নেটওয়ার্ক এক্সেস রোধ করতে
- নেটওয়ার্কে রিসিভার এবং সেন্ডার খুঁজে বের করতে
- ডিভাইস সার্ভিস করতে কখনো কখনো Mac Address লাগতে পারে
- কিভাবে আপনার Windows এবং Mac কম্পিউটারের ম্যাক এড্রেস বের করবেন

আপনি Windows 10 পিসির ক্ষেত্রে Settings, Control Panel, System Information, Command Prompt, এবং PowerShell এর মাধ্যমে ম্যাক এড্রেস বের করতে পারবেন। যদি আপনার Windows 10 না থাকে সেক্ষেত্রে Setting ছাড়া মেথড গুলো উপকারে আসবে।

## Settings ব্যবহার করে Mac Address বের করা,

প্রথমে Start > Settings > Network & Internet যান

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_a4719ef6d4bf28dc8df13cca22f478e9.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_a4719ef6d4bf28dc8df13cca22f478e9.webp)

আপনার নেটওয়ার্ক কানেকশন অনুযায়ী Ethernet অথবা WiFi সিলেক্ট করুন

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_e480b10db615195215453bb2dcc0734c.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_e480b10db615195215453bb2dcc0734c.webp)

এবার Hardware Properties এ ক্লিক করুন

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_4f8d1e96c7268300d558cf0cfef79595.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_4f8d1e96c7268300d558cf0cfef79595.webp)

নিচে আপনার Mac Address দেখাচ্ছে

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_fca764d22c1847f0ae653d30087d00b0.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_fca764d22c1847f0ae653d30087d00b0.webp)

## কিভাবে Control এর মাধ্যমে Mac Address চেক করবেন

প্রথমে Control Panel > Network & Internet এ যান

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_25fc431903046d88303890ed3f8969f9.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_25fc431903046d88303890ed3f8969f9.webp)

Network and Sharing Center এ ক্লিক করুন

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_3c7de2b270c4849ab56bf15efea4293d.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_3c7de2b270c4849ab56bf15efea4293d.webp)

বাম পাশ থেকে Change adapter settings সিলেক্ট করুন

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_54fec6b843eeceb13844db6a71cc9ede.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_54fec6b843eeceb13844db6a71cc9ede.webp)

আপনার কানেকশন কি সেটার উপর ভিত্তি করে Ethernet অথবা WiFi এ ডাবল ক্লিক করুন।

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_abd9c23d8873029c165a24bb24a90b45.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_abd9c23d8873029c165a24bb24a90b45.webp)

ধরে নিলাম আপনি ওয়াইফাই ব্যবহার করছেন সুতরাং WiFi ডাবল ক্লিক করুন এবং Details এ ক্লিক করুন

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_204faf69e425c6a3994a8f6b66fe1320.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_204faf69e425c6a3994a8f6b66fe1320.webp)

এবার Physical address আন্ডারে আপনার Mac Address দেখতে পাবেন

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_7395ccf8c24b6f8f5515b6d070329b87.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_7395ccf8c24b6f8f5515b6d070329b87.webp)

## কিভাবে Command Prompt এর মাধ্যমে আপনার Mac Address বের করবেন

প্রথমে সার্চ বক্সে CMD লিখুন এবং Command Prompt কে Run as administrator এ ওপেন করুন

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_f00980e1773da608f1dcf6ec5268f279.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_f00980e1773da608f1dcf6ec5268f279.webp)

ipconfig /all লিখে এন্টার দিন। এভাবে আপনি পিসিতে ইন্সটল করা সকল নেটওয়ার্ক কার্ডের ম্যাক এড্রেস দেখতে পাবেন।

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_4b0158b41a874e8691e1161f8963edf5.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_4b0158b41a874e8691e1161f8963edf5.webp)

Physical address ফিল্ডে আপনার Mac Address দেখতে পারবেন।

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_7b1cc8a657a4a51d7684b453ae1820fd.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_7b1cc8a657a4a51d7684b453ae1820fd.webp)

আপনি শুধু মাত্র একটিভ নেটওয়ার্ক কার্ডের ম্যাক এড্রেস দেখতে চাইলে getmac /v লিখে Enter দিন।

## Windows PowerShell এর মাধ্যমে কিভাবে Mac Address বের করবেন

প্রথমে Start > Windows PowerShell এ যান

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_67c438e1225a300057f0b4a9f1208f5b.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_67c438e1225a300057f0b4a9f1208f5b.webp)

Get-NetAdapter কমান্ডটি দিন এবং Enter প্রেস করুন

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_785bbdf1ba761640291e5cbc5e5b2fb7.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_785bbdf1ba761640291e5cbc5e5b2fb7.webp)  
 এবার আপনি প্রতিটি Network Adapter এর Mac Address দেখতে পারবেন

## কিভাবে System Information ব্যবহার করে Mac Adress বের করবেন

সার্চ বারে System Information সার্চ করুন এবং System Information এ প্রবেশ করুন

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_c8819547c049b33831e3e95d980e457e.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_c8819547c049b33831e3e95d980e457e.webp)

প্রথমে Components সেকশনটি এক্সপান্ড করুন এবং পরে Networks সেকশনটি এক্সপান্ড করুন।

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_9f45bbcd644f05f013078d63bdcda4e9.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_9f45bbcd644f05f013078d63bdcda4e9.webp)

Adapter এ ক্লিক করুন এবার ডান পাশে আপনার Mac Address দেখতে পাবেন

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_1d9cee27203d38c83ad5d76e23ff9b55.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_1d9cee27203d38c83ad5d76e23ff9b55.webp)

## কিভাবে ম্যাক-বুকের Mac Address বের করবেন

প্রথমে Menu > System Preferences > Network যান।

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_a943b90005903252b40189f743718c3b.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_a943b90005903252b40189f743718c3b.webp)

এবার Advanced সিলেক্ট করুন

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_aa767fdbb24fae050e80eb3371eb0e4c.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_aa767fdbb24fae050e80eb3371eb0e4c.webp)

এবার Info থেকে আপনার Mac Address দেখতে পাবেন। চাইলে WiFi এ ক্লিক করেও দেখতে পারেন।

[![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_840f131eaf024d33e78bbe8de397fbde.webp)](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_840f131eaf024d33e78bbe8de397fbde.webp)

## শেষ কথাঃ

আশা করছি উপরে বর্ণিত মেথড গুলো ফলো করে আপনি আপনার ডিভাইসের ম্যাক এড্রেস বের করে ফেলতে পারবেন।

কেমন হল আজকের টিউন জানাতে অবশ্যই টিউমেন্ট করুন। পরবর্তী টিউন পর্যন্ত ভাল থাকুন। আল্লাহ হা-ফেজ।
