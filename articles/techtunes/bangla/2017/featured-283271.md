---
archive_id: techtunes-283271
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 283271
title: আপনি Android ইউজার? একদিন এই টিউনই হয়ত আপনি খুঁজবেন!!
slug: featured-283271
language: bn
status: publish
published_at: '2017-08-07T03:17:00+00:00'
modified_at: '2017-09-22T10:00:00+00:00'
original_url: https://www.techtunes.io/featured/tune-id/283271
author: অন্য মানুষ ফয়সাল
author_url: https://www.techtunes.io/tuner/onno-manush-foysal
categories:
- নির্বাচিত
tags:
- Android
- টিপস এন্ড ট্রিকস
content_hash: c1299197dd5bdf5abcca9281d520d24a2ec99cebbc46af92d23abc902e6a3d5f
archived_at: '2026-11-12T12:58:17.008311+00:00'
---

আসসালামুয়ালাইকুম।  
 গ্রীষ্মের প্রচণ্ড গরমে হয়ত ভাল থেকেও স্বস্তিতে নেই, স্বস্তিতে থাকার কথাও না ! তবুও আমি  লিখতে বসলাম।

মোবাইল Operating System হিসাবে Android এর প্রতিদ্বন্দ্বী নেই। তাই আজ Android ফোন Root, Unroot, Flash, Stock Room Install, Frameware Update করা দেখাব আমি। আমার এ সম্পর্কে জানার জ্ঞান খুবই সীমিত, তাই টিউনে ভুল থাকবেই, আশা করি এটা তেমন একটা আমলে নিবেন না।

[![](https://dnc.techtunes.io/tDrive/tuner/onno-manush-foysal/283271/are-you-android-user_bg_featured.jpg)](https://dnc.techtunes.io/tDrive/tuner/onno-manush-foysal/283271/are-you-android-user_bg_featured.jpg)

ছবি - [Shutter Stock](http://www.shutterstock.com)

Android একটা ফোন (Samsung-GT-s5282) কিনার পর যখন দেখলাম আজেবাজে এই সেই application দিয়ে ফোন ভর্তি, যা ফোনকে স্লো করে রাখে, আর  Always RAM এর ৮০%-৮৫% Use হয়ে পড়ে থাকে, তখনই মূলত ফোনটা ROOT করে ওইসব ও-প্রয়োজনী Application রিমুভ করার জন্যই আমি আমার ফোনটা ROOT করি। ROOT করার পর ও-প্রয়োজনী Application  রিমুভ করায় কি হল জানি না, তবে ভাল একটা ফল পেলাম RAM useing আর ব্যাটারি'র স্থায়িত্ব এর ক্ষেত্রে। ও-প্রয়োজনীয় সেই সব Application যেহেতু ব্যবহার হচ্ছে না, তাই RAM free থাকে, Always Use হয় ৪০%-৫০% ! কিন্তু জানেন, সেই সুখ বেশী টিকল না, কি করলাম? আরও বেশী লাভের আশায় বড় সাইজ দেখে কয়েকটা System File ও Delete করে দিলাম :O অতি লোভে তাঁতি নষ্ট, তাই যা হওয়ার তাই হল। ফোনটা সেই যে অফ হল, অন তো হয় না :(:cry:

তার পরের গল্পটা আরও কষ্টের, দয়াল বাবা Google এ মাথা বেঁধে লেগে গেলাম, কিন্তু এই সমস্যার সহজ সমাধান নেই। যা আছে, সেটা হল এই- নতুন করে Stock Room Install দিতে হবে। মানে ফোন ফ্ল্যাশ... :(কিন্তু আমার কাছে তো Frameware নেই :O ভাল মানের Fremeware Download এর সাইট ও পাচ্ছিলাম না, পরে টেকটিউনসে টিউন করে ভাল একটা লিঙ্ক পেলাম। আর দয়াল বাবার সার্চক্রীত রেজাল্ট দেখে দেখে ভাল একটা সাইট এর অনুকরণে Odin নামক একটা সফটওয়্যারের সাহায্যে Stock Room re-Install করে সেই যাত্রায় রক্ষা পেলাম 😀 কিন্তু যাত্রার অনবদ্য অভিজ্ঞতা নিজের মাথায় ভাল করে পুরে নিলাম। আর সেটাই আজ সুন্দর ভাবে আপনাদের সামনে উপস্থাপন করব ! জানি না কতটুকু সুন্দরভাবে লিখতে পারব, তার পরও চেষ্টা করলাম... তাতে তো দুষ নাই? কি বলেন? 😀

## ডিভাইস ROOT করা :

আপনার ফোন কি ভাবে ROOT করবেন, সেটা নিয়ে একবার টেকটিউনসে একবার সার্চ দিন। আশা করি এত রেজাল্ট পাবেন, সেখান থেকে ভাল ভাবেই আপনার ফোনটি ROOT করতে পারবেন, কিন্তু এর পরও আমার খুঁজে পাওয়া ROOT করার সিস্টেমটা Share করছি-

প্রথমে Impector নামের software টি Dawnload করে নিন --->> https://cydia.saurik.com/api/latest/2  [Direct Download]

এইবার মন দিয়ে পড়ুন। প্রথমে আপনার ফোনের Driver টা PC তে Install দিন। যদি Driver খুঁজে পেতে সমস্যা হয়, তাহলে টিউমেন্টে বলবেন, আমি চেষ্টা করব ভাল Download Link দিতে। Driver Install দেয়ার পর ফোনটি Data Cable এর সাহায্যে PC তে Connect করুন। নিচের ছবির মত উইন্ডো আসবে-

![](https://dnc.techtunes.io/tDrive/tuner/onno-manush-foysal/283271/2.jpg)

এবার আপনি RAR ফাইল থেকে নিচের ছবির মত Impector নামক Softwere টি Run করুন, এবং "Start" এ ক্লিক করুন।

![](https://dnc.techtunes.io/tDrive/tuner/onno-manush-foysal/283271/1.jpg)

সব কিছু টিকটাক থাকলে নিচের ছবির মত উইন্ডোতে কিছু  Installing Command দেখবেন-

![](https://dnc.techtunes.io/tDrive/tuner/onno-manush-foysal/283271/Final.jpg)

সব শেষে আবার প্রথম লেখাটা আসবে, তার মানে আপনার ফোনটি এখন ROOT করা ! 😀 কি বিশ্বাস হল না?  
 আপনার ফোনটি Successful ভাবে ROOT হয়েছে কি না, এ জন্য নিচের APK টা install করে Chack করে নিন।  
 APK Link--->> [http://www13.zippyshare.com/d/83719607/69535/Root%20Checker%20Pro.apk](https://www13.zippyshare.com/d/83719607/69535/Root%20Checker%20Pro.apk  ) [Direct Download]

শেষ হয়ে গেল ROOT করার কাজ, এখন চাইলে ভাল মানের একটা Uninstaller দিয়ে ও-প্রয়োজনী Application রিমুভ করে নিতে পারেন। ও ভাল কথা, রিমুভ করার আগে Backup রাখতে ভুলবেন না... তা না হলে আমার মত ভুগতে হবে। Backup রাখা ও Uninstall এর জন্য নিচের লিঙ্ক থেকে APK টা নামিয়ে নিতে পারেন, আমি এটাই Use করি।  
 APK Link--->> [http://www38.zippyshare.com/d/18701808/17549/Root%20Uninstaller%20Pro%20v.4.0.apk](https://www38.zippyshare.com/d/18701808/17549/Root%20Uninstaller%20Pro%20v.4.0.apk  ) [Direct Download]

শেষ হল ROOT এর সাতকাহন ! 😀

## Unroot, Flash, Stock Room Install, Frameware Update করা :

আমার মতে Unroot, Flash,Stock Room Install, Frameware Update সবই এক সুতায় বাঁধা। আপনি টিউনটা পড়ছেন, So আপনি টেকটিউনসের Membar না হউন, অন্তত Visitor তো ? So আপনি কেন এর যেকোন একটা কাজের জন্য মোবাইল সার্ভিসিং সেন্টারে যাবেন ??? চেষ্টা করুন, আপনি ও পারবেন। আমি পারব না বলে বসে থাকলে সত্যিই আপনি পারবেন না, আপনাকে চেষ্টা করতে হবে। আর টেকটিউনস শিখার জায়গা, এখানে শিখতে আসলে আপনি ফিরত যাবেন, এটা টিটির কেও মানবে না। টিটির সাম্প্রতিক একটা জরিপে দেখেছিলাম দিনের শুরুতে বেশির ভাগ মানুষ ফেসবুক Chack করে, Than টেকটিউনস 😀 আমার মনে হয় যারা টেকটিউনস কে মনের মত ভালবাসেন, যারা প্রযুক্তি-কে ভালবাসেন, তারা আগে টিটি Chack না করে শান্তি পান না 😀 anyway, কাজের কথায় আসি। Unroot, Flash, Stock Room Install, Frameware Update এর যেকোন একটি করতে নিচের ধাপগুলু অনুসরন করুন, আশা করি নিরাশ হয়ে ফিরবেন না 😀 🙂

### কি কি প্রয়োজন হবে ?

- ফোনের Driver,
- Odin নামক Software
- আর আপনার ফোনের Stock Room বা Frameware

প্রথমে Odin Download করে নিন -->> [http://samsung-updates.com/Odin307.zip](http://samsung-updates.com/Odin307.zip  ) [Direct Download]

এবার আপনার ফোনের নাম model লিখে দয়াল বাবা Google এ সার্চ দিয়ে Frameware টা নামিয়ে নিন। অথবা আপনার ফোনের নাম মডেল লিখে টিউমেন্ট করুন, আমি আপনার Device এর Frameware এর লিঙ্ক দেয়ার Try করব।

কাজ শুরু করে দেই, কি বলেন ? খুব সাবধান, কাজে উল্টাপাল্টা হয়ে বা বিদ্যুৎইক গোলযোগের জন্য যদি আপনার Device টি ব্রিক বা স্পট ডেড হয়, এ ক্ষেত্রে আমাকে কোন দায়ী করবেন না।

প্রথমে আপনার ফোনটি অফ করে নিন, Than অন করার সময় Vol Down+Home+Power বাটনে ধরতে হবে, যার ফলে ফোন Downloading Mode এ অন হবে। কিন্তু এটা আমার ফোনের Downloading Mode এ যাওয়ার পদ্ধতি, Brand অন্যটা হলে এটা পরিবর্তনীয়, কিন্তু আপনি যদি আপনার ফোনের Downloading Mode যেতে না পারেন, তাহলে টিউমেন্ট করুন। আমি বলে দিব ইনশাআল্লাহ্‌। Anyway, নিচের ছবিতে দেখুন আমার Device এ আমি Downloading Mode এ গেছি-

![](https://dnc.techtunes.io/tDrive/tuner/onno-manush-foysal/283271/4-HH.jpg)

Odin ওপেন করুন। আর আপনার ফোনটি Data Cable এর সাহায্যে PC তে Connect করুন এবার নিচের ছবির দিকে তাকান-

- Auto Reboot এ টিক বসিয়ে ক্লিক করুন।
- F.Reset Time এ টিক বসিয়ে ক্লিক করুন।
- দেখুন ফোন Add হয়েছে বলে বার্তা দেখাচ্ছে।

![](https://dnc.techtunes.io/tDrive/tuner/onno-manush-foysal/283271/11.jpg)

4. এবার PDA তে ক্লিক করুন-

![](https://dnc.techtunes.io/tDrive/tuner/onno-manush-foysal/283271/22.jpg)

PDA তে ক্লিক করার সাথে সাথে Open নামে একটা উইন্ডো ওপেন হবে।  
 5. আপনি আপনার ফোনের জন্য Dawnload করা Fremeware বা Stock Room এর Location এ গিয়ে MD5 ফাইল-টা  
 সিলেক্ট করুন।  
 6. এবং Open এ ক্লিক করুন।

![](https://dnc.techtunes.io/tDrive/tuner/onno-manush-foysal/283271/3.jpg)

এবার লক্ষ করুন, PDA তে MD5 ফাইলটা লোড দেয়ার পর কিছু সময় লাগবে, এমনকি Program "Not Responding" ও Show করতে পারে। কিন্তু Program ক্লোজ করবেন না, ২-৩ মিনিট Wait করুন, একটু পরে সব টিকটাক হয়ে যাবে।

7. এবার "Start" এ ক্লিক করুন।

![](https://dnc.techtunes.io/tDrive/tuner/onno-manush-foysal/283271/4.jpg)

দেখুন আবার লোডিং শুরু হয়েছে-

![](https://dnc.techtunes.io/tDrive/tuner/onno-manush-foysal/283271/5.jpg)

আর অন্য দিকে ফোনে ও Downloading হচ্ছে, মানে Load হচ্ছে-

![](https://dnc.techtunes.io/tDrive/tuner/onno-manush-foysal/283271/5-HH.jpg)

কিছু সময় পর নিচের ছবির মত বার্তা Show করে "Reset" লেখা উঠবে-

![](https://dnc.techtunes.io/tDrive/tuner/onno-manush-foysal/283271/6.jpg)

পরে ফোনে এ রকম একটা লোডিং হয়ে ফোনটি Restart হবে।

![](https://dnc.techtunes.io/tDrive/tuner/onno-manush-foysal/283271/6-HH.jpg)

অপেক্ষা করুন, সবশেষে কত সময় লাগল তার হিসাব সমেত "Pass" লেখা উঠবে-

![](https://dnc.techtunes.io/tDrive/tuner/onno-manush-foysal/283271/7.jpg)

আপনার কাজটি যদি ফ্রেমওয়ার Update হয়, তাহলে আপনার কাজ শেষ। দেখুন আপনার Download ক্রিত Fremeware Install হয়ে নতুন কিছু পরিবর্তন হয়েছে। আর যদি Unroot বা  Flash করার উদ্দেশে কাজটি করে থাকেন, তাহলে আপনাকে আরও ছোট্ট একটা কাজ করতে হবে। সেটা হল ফোনটা আবার অফ করুন, আগে Downloading Mode যাওয়ার জন্য Vol Down+Home+Power বাটন ধরেছিলেন না? এবার আপনাকে Vol UP+Home+Power একত্রে ধরতে হবে। একটু wait করুন, দেখবেন PC'র BOIS মেনুর মত একটা মেনু এসেছে। আপনি ভলিউম কী'র সাহায্যে "Wipe data/factory reset" এ যান-

![](https://dnc.techtunes.io/tDrive/tuner/onno-manush-foysal/283271/23.jpg)

এখন Home কী-তে prass করুন, দেখবেন ৫ বার "No" than একবার "Yes -- Delete all user data" লেখা আরও একটা পেজ আসবে, আপনি "Yes -- Delete all user data" এ প্রেস করুন Home বাটনের সাহায্যে।

![](https://dnc.techtunes.io/tDrive/tuner/onno-manush-foysal/283271/12.jpg)

এখন  "Reboot System Now" এ প্রেস করে ফোনটি রিস্টার্ট করে নিন 😀 কাজ শেষ বস...  
 মার্কেট থেকে কিনার পর প্রথম অন করার সময় যে সমস্ত কাজ করেছিলেন, মানে Language সেট, Google ID Login Or Create, Samsung ID Log-In Or Create Etc Etc... এগুলো সম্পন্ন করে ধীর হয়ে বসে পড়ুন আর আমার জন্য হাল্কা গরম এক কাপ লাল চায়ের অর্ডার করুন, আমি আবার গরম খেতে পারি না, তাই টাণ্ডা লাল চা খাই  😀

[বিশ্বাস করুন আর নাই করুন, শুধু মাত্র টেকটিউনসে এই টিউনটি করার জন্যই গতকাল ফোনটা ফ্ল্যাশ করলাম। কারো উপকার হলেই আমার প্রচেষ্টা সফল।]

ভাল থাকবেন, দোয়া করবেন আমার জন্য। আল্লাহ হাফেজ।
