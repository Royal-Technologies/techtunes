---
archive_id: techtunes-659392
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 659392
title: লোকেশন ট্র্যাক করুন ভিন্ন উপায়ে
slug: tips-and-tricks-659392
language: bn
status: publish
published_at: '2020-06-29T16:39:00+00:00'
modified_at: '2020-07-05T12:18:00+00:00'
original_url: https://www.techtunes.io/tips-and-tricks/tune-id/659392
author: আহমাদ উল্লাহ
author_url: https://www.techtunes.io/tuner/1234asdffff
categories:
- টিপস এন্ড ট্রিকস
tags:
- find location
- how to find location
- Location Track
content_hash: 302a2a90aec6cef1432a073fc196c456b3445488d219cf57136cba3399e8e331
archived_at: '2026-11-12T12:24:16.394216+00:00'
---

প্রিয় ভিজিটর আপনি কি গোপনে কারো লোকেশন ট্র্যাক করতে চান! আপনি কি IP এড্রেস ব্যবহার করে পায়ের ঘাম মাথায় ফেলে সঠিক লোকেশন খুঁজে পাচ্ছেন না!রাতদিন ইন্টারনেট ঘাটাঘাটি করায় চোখের পাওয়ার কমে যাচ্ছে! তাহলে এই টিউনটি  
 শুধুমাত্র আপনার জন্য। চলুন শুরু করা যাক।

আজকে যে পদ্ধতির কথা বলবো একে বলা হয় GSM METHOD এর জন্য আমাদের ৪টি কোড বা নাম্বার প্রয়োজন হবে।

1. Mobile Country Code (MCC)
2. Mobile Network Code (MNC)
3. Location Area Code (LAC)
4. Cell ID (CID)

কোড গুলো পাবেন কিভাবে? কয়েক ভাবেই এই কোড গুলি বের করা যায়, যেমন location finder and GSM mapper অ্যাপস ব্যবহার করে যা আপনি প্লেস্টোরে পেয়ে যাবেন। লিনাক্স ব্যবহার করে, যার জন্য আপনাকে প্রোগ্রামিং সম্পর্কে ভালো ধারনা থাকতে হবে। ৩য় পদ্ধতিটি খুবি সহজ আপনার ফোনের ডায়াল প্যাড ব্যবহার করে, কিভাবে?

### ১ম ধাপ

#### প্রথমে আপনার ডায়াল প্যাডে টাইপ করুন \*#\*#4636#\*#\*

![dialpad](https://dnc.techtunes.io/tDrive/tuner/2020/06/techtunes_3f2ce6c15f3a2b68179b135324940085.jpg)

নতুন একটি সেকশন আসবে নিচের মত।

![phone information](https://dnc.techtunes.io/tDrive/tuner/2020/06/techtunes_4056752ad8749fb1b49956941ce733c8.jpg)

এবার phone information এ গিয়ে উপড়ে স্লাইড করে একদম নিচে গেলে আপনার কাঙ্খিত কোড গুলো পেয়ে যাবেন।

![gsm](https://dnc.techtunes.io/tDrive/tuner/2020/06/techtunes_3eb20fc24436b0dd675fe0d0c7d4e23e.jpg)

### ২য় ধাপ

MCC এবং MNC কোড সহজে জানা যায়। নিচের ছবিটি দেখুন।

![lac and cid code](https://dnc.techtunes.io/tDrive/tuner/2020/06/techtunes_5d26610d0355e9be5e52ddb70fe6fa3a.jpg)

আপনার প্রিয় ব্রাউজারটি ওপেন করুন এবং টাইপ করুন (cellphonetrackers.org>gsm) নিচের মত একটি ইন্টারফেস আসবে।

![gsmtracker](https://dnc.techtunes.io/tDrive/tuner/2020/06/techtunes_c322256416f2ca22ce3c0a4131fa86da.jpg)

এবার ঘর গুলোতে আপনার বা ভিকটিমের কোড গুলো বসান এবং Track it এ ক্লিক করুন।

Lat=60.208511 Lon=24.752884 নিচে এমন দুটি সংখ্যা আসবে, latitude এবং longitude সংখ্যা দুটি কমা দিয়ে পাশাপাশি বসান। যেমন 60.208511, 24.752884 এবার সংখ্যা দুটি কপি করুন।

![lat and long](https://dnc.techtunes.io/tDrive/tuner/2020/06/techtunes_ebc35aa5822cd87056b8b663b80f91bf.jpg)

এখন গুগল ম্যাপ ওপেন করে সংখ্যা দুটি পেস্ট করুন নিচের মত।

![map](https://dnc.techtunes.io/tDrive/tuner/2020/06/techtunes_92bbfcdeb03a0906881bcff996816b43.jpg)

মোটামুটি আপনার কাজ শেষ। চাইলে এই ভাবে আপনি যে কারো লোকেশন ট্র্যাক করতে পারেন। অবস্থান অনুযায়ী আপনার মোবাইলের  
 LAC এবং Cell id পরিবর্তন হবে।

এমন চমৎকার ও ইন্টারেস্টিং টিউন পেতে টেকটিউনসের সাথে থাকুন। আর কি কি বিষয় নিয়ে লেখা যায় চাইলে টিউমেন্ট করে জানাতে পারেন। সবাই ভালো থাকুন, সুস্থ থাকুন, পরিবেশকে নিরাপদ রাখুন। খোদা হাফেজ।
