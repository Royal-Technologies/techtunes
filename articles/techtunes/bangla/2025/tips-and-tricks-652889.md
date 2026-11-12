---
archive_id: techtunes-652889
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 652889
title: আপনার কম্পিউটারকে আরও Better করতে Windows Group Policy এর ১০টি টিপস
slug: tips-and-tricks-652889
language: bn
status: publish
published_at: '2025-04-05T03:45:00+00:00'
modified_at: '2025-02-23T03:48:00+00:00'
original_url: https://www.techtunes.io/tips-and-tricks/tune-id/652889
author: সোহানুর রহমান
author_url: https://www.techtunes.io/tuner/sohanur-raihan
categories:
- টিপস এন্ড ট্রিকস
tags:
- Tips টিপস
- উইন্ডোজে হোমগ্রুপ ব্যবহার করে
- কমান্ড প্রোমোট
content_hash: 264dc8e8ea78d32c607179379ab3a672fa6eb3f9d42d5efa3d261a0f74dd6db9
archived_at: '2026-11-12T12:24:45.521332+00:00'
---

আসসালামু আলাইকুম, কেমন আছেন টেকটিউনস কমিউনিটি? আশা করছি সবাই ভাল আছেন। আজকে আবার হাজির হলাম নতুন টিউন নিয়ে। কথা না বাড়িয়ে চলুন শুরু করা যাক।

আমাদের মাঝে অনেকে আছেন যারা আপনাদের উইন্ডোজকে আরও কাস্টমাইজড করতে চান, ডিফল্ট সেটিং থেকে বেশি কন্ট্রোল কর‍তে চান, মাঝে মাঝে হয়তো ভাবেন এমন কোন Tweaks বানাতে যা সেটিং এ নেই। তো আপনাদের জন্যই এই ধরনের দারুণ সুবিধা দিচ্ছে Windows Group Policy। Windows Group Policy এর মাধ্যমে আপনি আপনার কম্পিউটারের সেটিং নিয়ন্ত্রণ করতে পারবেন আরও এডভান্সড ওয়েতে। আপনার পিসিতে এমন অনেক Group Policy সেটিং আছে যার মাধ্যমে আপনি নিজের মত Tweak করে আপনার উইন্ডোজকে কন্ট্রোল করতে পারবেন। তাছাড়া এই Windows Group Policy এর চমৎকার ব্যবহার আছে Windows Domain কন্ট্রোলে।

Windows Domain  সম্পর্কে আরও জানুন। [Windows Domain কি? Windows Domain এর সুবিধা কী? কীভাবে ব্যবহার করা হয় এই Windows Domain!](https://www.techtunes.io/windows/tune-id/652980)

এবার জানব Windows Group Policy সম্পর্কে

## Windows Group Policy কি?

![](https://dnc.techtunes.io/tDrive/tuner/2020/07/techtunes_3aa1ea982e12a352796e4dddff62770c.png)

Group Policy হচ্ছে কম্পিউটারের যাবতীয় সেটিং কনফিগারেশন করার একটি কেন্দ্রীয় মাধ্যম, যার মাধ্যমে নেটওয়ার্ক ডিরেক্টরিতে একটিভ সকল Windows Domain বা কম্পিউটার গুলোকে নিয়ন্ত্রণ করা যায়।  সেটিং গুলো ডোমেইন কন্ট্রোলার এর মাধ্যমে মেইনটেইন করা হয় এবং যাতে করে সকল কম্পিউটার গুলোতে একই সেটিং কাজ করে এবং কোন কম্পিউটার এর বাইরে যেতে পারে না।

এখানে একটি কথা হয়তো বলার দরকার নেই তারপরেও বলে নিচ্ছি, এই পদ্ধতিতে যেসব কম্পিউটার শুধু মাত্র নেটওয়ার্ক ডিরেক্টরিতে থাকে শুধু মাত্র সেসব কম্পিউটারটাকেই নিয়ন্ত্রণ করা যায়।

তো আজকের এই টিউনে চলুন দেখে নেয়া যাক সেরা কিছু Group Policy সেটিং যার মাধ্যমে আপনি আপনার সিস্টেমকে করে ফেলতে পারবেন আরও এডভান্সড এবং কার্যকরী।

Control Panel এর কথাই ধরুন, আপনি Group Policy এর মাধ্যমে ইউজারদের শুধুমাত্র নির্দিষ্ট সেটিং ব্যবহারের সুযোগ দিতে পারবেন। সকল পিসির জন্য একই হোমপেজ সেট করে দিতে পারবেন এমনকি আপনি নিজেই সেটআপ করে দিতে পারবেন পিসি অফ বা অন হলে ডেক্সটপে কি দেখাবে।

## Group Policy কিভাবে কাজ করে?

আমরা সাধারণত আমাদের প্রয়োজনীয় কমান্ড গুলো Group Policy Editor এ দেব এবং Group Policy Editor, Windows Registry তে নির্দিষ্ট Tweaks তৈরি করবে। যার মাধ্যমে সেটিং গুলো পরিবর্তিত হবে।

Group Policy Editor আপনাকে একটি ইউজার ফ্রেন্ডলি ইন্টারফেস দেবে যার মাধ্যমে আপনি কোন ধরনের Registry এডিট করার ঝামেলা ছাড়াই সমস্ত কাজ করতে পারবেন।

তবে মনে রাখতে হবে Group Policy শুধু মাত্র Windows 10 Professional এবং এর উপরের ভার্সন গুলোতে সাপোর্ট করবে। সুতরাং আপনার Windows Home থাকলে সেটা আপগ্রেড করে নিতে হবে।

## কিভাবে ব্যবহার করবেন Group Policy

আপনি যতটা কঠিন ভাবছেন এটা মোটেও এতটা কঠিন নয়। চলুন দেখে নেয়া যাক কিভাবে ব্যবহার করবেন Windows Group Policy। আপনি এই এডিটর ব্যবহার করে শত শত সেটিং করতে পারবেন তবে সব গুলো এই টিউনে দেখানো অবশ্য সম্ভব না তাই আমি বিশেষ বিশেষ সেটিং গুলোই এখানে দেখানোর চেষ্টা করব।

*বিঃদ্রঃ কাজ শুরু করার আগে আমি বলে নিতে চাই, আপনি নিজে থেকে কনফিডেন্ট হলেই কেবল এটা ট্রাই করুন কারণ কোন  Tweaks ভুল হলে আপনার পিসিতে বিভিন্ন ধরনের সমস্যা দেখা দিতে পারে।*

যাক তাহলে আমরা শুরু করি, যাবতীয় কাজ করতে হলে প্রথমে আমাদের Group Policy Editor ওপেন করতে হবে,

প্রথমে চলে যান স্টার্টবারে, সার্চ দিন **group policy**লিখে

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_1ce7024db3d88426ba9088fb93060d5a.png)

এবং **Edit group policy**তে ক্লিক করুন।

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_8a6fe27c8640678330af41a0b1f5841d.png)

## ১. Control Panel ও Settings রে-স্ট্রিক্ট করা

কন্ট্রোল প্যানেল রেস্ট্রিকশন যেকোনো বিজনেস, স্কুল, কলেজ কম্পিউটার নেটওয়ার্ক এর জন্য জরুরী এর মাধ্যমে আপনি যেকোনো ইউজারকে কন্ট্রোল প্যানেলে ঢুকা থেকে বিরত করতে পারবেন। এটি চাইলে বাসার মাল্টি ইউজারদের ক্ষেত্রেও ব্যবহার করতে পারেন যাতে করে শিশুরা সেটিং চেঞ্জ করে আপনাকে বিপদে ফেলতে পারবে না।

কন্ট্রোল প্যানেল একেবারে বন্ধ করে দিতে চাইলে নিচের নির্দেশনা ফলো করুন এবং শেষ অবজেক্টটি এনে-ভল করে দিন।

```
 User Configuration &gt; Administrative Templates &gt; Control Panel &gt; Prohibit access to Control Panel and PC Settings
```

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_e6ba31d897c16382983778cdc60bdfae.png)  
 আপনি যদি কন্ট্রোল প্যানেলের নির্দিষ্ট কিছু সেটিং বন্ধ করতে চান তাহলে নিচের নির্দেশনা ফলো করুন

```
User Configuration &gt; Administrative Templates &gt; Control Panel &gt; Hide specified Control Panel items
```

```
User Configuration &gt; Administrative Templates &gt; Control Panel &gt; Show only specified Control Panel Item
```

আপনি অবজেক্ট এনে-বল করার পর যে সেটিং গুলো হাইড করতে চান সেটা অবশ্যই এড করে দিতে হবে। উইন্ডোজ এর সব গুলো কন্ট্রোল প্যানেল Applets দেখতে এই লিংকে চলে যান [Microsoft’s Canonical Names of Control Panel Items](https://docs.microsoft.com/en-us/windows/win32/shell/controlpanel-canonical-names)।

আপনাকে একটি বিষয় মনে রাখতে হবে যখন নতুন কোন সেটিং এনে-বল করবেন তখন অবশ্যই আপনার পিসি একবার রিবুট দিতে হবে। তবে রিবুট দেয়া ছাড়া সেটিং এনে-বল করতে চাইলে Command Prompt এ নিচের কমান্ড দিন।

```
gpupdate /force
```

## ২. Command Prompt ব্লক করা

কখনো কখনো ভুল ভাবে Command Prompt ব্যবহারের ফলে পড়তে পারেন বিভিন্ন ঝামেলায় তাই আপনার ইউজারদের থেকে বন্ধ করে দিতে Command Prompt।

Command Prompt ব্লক করতে নিচের ভ্যালু ব্যবহার করুন,

```
User Configuration &gt; Administrative Templates &gt; System &gt; Prevent access to the command prompt
```

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_ade949cc0568f4f792ee540d29549a0f.png)

## ৩. সফটওয়্যার ইন্সটল ব্লক করা

আপনার ইউজাররা ভুল করে থার্ড পার্টি সফটওয়্যার ইন্সটল দিয়ে পিসির নিরাপত্তা ব্যবস্থা নাজুক করে দিতে পারে এজন্য আপনি সফট ওয়ার ইন্সটল বন্ধ রাখতে পারেন।

নিচের ভ্যালুটি ব্যবহার করুন

```
 Computer Configuration &gt; Administrative Templates &gt; Windows Components &gt; Windows Installer &gt; Turn off Windows Installer
```

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_963e8718ce22231404b68fa4c32da17d.png)

## ৪. Forced Restarts বন্ধ করা

মাঝে মাঝে আমাদের আপডেটের জন্য পিসি অটো restart নিয়ে নিতে পারে। চাইলে এটিও বন্ধ করে দিতে পারেন।

এজন্য নিচের কমান্ড ব্যবহার করুন,

```
 Computer Configuration &gt; Administrator Templates &gt; Windows Components &gt; Windows Update &gt; No auto-restart with logged on users for scheduled automatic update installations
```

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_3ac36d2545c64800d9225d1f58372df6.png)

## ৫. ডিজেবল ড্রাইভার আপডেট

আমরা জানি কখনো কখনো আমাদের ব্যবহৃত ড্রাইভার গুলো আপডেট হয় এবং এটি একদিক থেকে ভাল যে আপডেট ড্রাইভার ব্যবহার করছেন। তবে যদি আপনি কোন কাস্টম ড্রাইভার ব্যবহার করেন তাহলে অবশ্যই চাইবেন না যে ড্রাইভার আপডেট হোক। মাঝে মাঝে নতুন ড্রাইভারের মধ্যেও বিভিন্ন বাগ থাকতে পারে। চলুন দেখে নিই কিভাবে ড্রাইভার আপডেট বন্ধ করা যায়।

```
 Computer Configuration &gt; Administrative Templates &gt; System &gt; Device Installation &gt; Device Installation Restrictions &gt; Prevent installation of devices that match any of these device IDs
```

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_eed0124f8e0790779271c8aa9ab40bb5.png)

আপডেট বন্ধ করতে হলে আপনাকে ড্রাইভারের আইডিটি লাগবে যা Device Manager থেকে পেতে পারেন

## ৬. Removable Media ডিজেবল করা

আমরা বিভিন্ন ফাইল বা ডাটা আদানপ্রদান করার জন্য রিমুভেবল ডিস্ক বা পেন-ড্রাইভ ব্যবহার করি কিন্তু কখনো কখনো এই রিমুভেবল ডিস্ক আপনার পিসির সমস্ত তথ্য লিক করে দিতে পারে, পিসিতে ছড়িয়ে পড়তে পারে ম্যালওয়্যার।

আপনার ব্যবসায়ী ব্যবহৃত পিসির নিরাপত্তার জন্য ডিজেবল করে দিতে পারেন রিমুভেবল ডিস্ক।

নিচের ভ্যালু টি ব্যবহার করুন

```
 User Configuration &gt; Administrative Templates &gt; System &gt; Removable Storage Access &gt; Removable Disks: Deny read access
```

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_8e2f4f23bd77da7710ded026a550b28d.png)

## ৭. Balloon ও Toast Notifications হাইড করা

আমি মনে করি নোটিফিকেশন বিষয়টি ফোনের জন্যই উপযুক্ত, পিসিতে নোটিফেকশনে তেমন কোন গুরুত্ব ব্যক্তিগত ভাবে আমি পাই নি। ধরুন আপনি কাজের মধ্যে আছেন এমন সময় উইন্ডোজ এর যেকোনো এডভারটাইজমেন্ট নোটিফিকেশন আপনার মনোযোগ নষ্ট করে দিতেই পারে।

balloon notifications এর জন্য

```
 User Configuration &gt; Administrative Templates &gt; Start Menu and Taskbar &gt; Turn off all balloon notifications
```

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_b0a64972374b8be34cca31f18cbafd71.png)

Toast notifications এর জন্য

```
 User Configuration &gt; Administrative Templates &gt; Start Menu and Taskbar &gt; Notifications &gt; Turn off toast notifications
```

### ৮. OneDrive রিমুভ করা

আমরা জানি উইন্ডোজ ডিফল্ট ভাবেই পিসিতে OneDrive ইন্সটল দিয়ে দেয়। আপনি অন্য সফটওয়ারের মত এটি আনইন্সটল করতে পারেন অথবা৷ Group Policy এর মাধ্যমেও ডিজেবল করতে পারেন।

চলে যান এই অবজেক্টে

```
 Computer Configuration &gt; Administrative Templates &gt; Windows Components &gt; OneDrive &gt; Prevent the usage of OneDrive for file storage
```

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_aea4990829fa78057ebd67645eea5f12.png)

### ৯. Defender অফ করা

সাধারণ একজন উইন্ডোজ ব্যবহারকারীর কাছে আমি মনে করি Defender যথেষ্ট তবে যদি বিজনেস লেভেলে পিসি ব্যবহার করতে চান তাহলে আপনার আরও অধিক নিরাপত্তার জন্য আলাদা এন্টিভাইরাস ব্যবহার করতে পারেন। সেক্ষেত্রে কিভাবে Defender অফ করবেন বা ডিজেবল করবেন।

চলুন দেখে নেয়া যাক কোথায় আছে defender এর সেটিং

```
 Computer Configuration &gt; Administrative Templates &gt; Windows Components &gt; Windows Defender &gt; Turn off Windows Defender
```

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_48b260df7382643c7818097628c2cf46.png)

### ১০. Logon/Startup/Shutdown স্ক্রিনে স্ক্রিপ্ট রান করানো

আমাদের শেষ সেটিং। আপনি যদি batch ফাইল অথবা power shell script রাইটিং এ পারদর্শিনী হোন তাহলে এটি আপনার জন্য।

আপনি যদি আপনার গ্রুপের সমস্ত পিসি অন হবার সময় নিজস্ব কোন স্ক্রিপ্ট রান করাতে চান নিচের ধাপ গুলো দেখুন,

startup/shutdown script,

```
Computer Configuration &gt; Windows Settings &gt; Scripts (Startup/Shutdown)
```

logon অথবা logoff script,

```
 User Configuration &gt; Windows Settings &gt; Scripts (Logon/Logoff)
```

![](https://dnc.techtunes.io/tDrive/tuner/2020/05/techtunes_e814f45b7b05896bfe845b7bc78e0f06.png)

এর মাধ্যমে আপনি স্ক্রিপ্ট সিলেক্ট করতে পারবেন এবং প্রয়োজনীয় প্যারামিটার দিতে পারবেন। চাইলে একাধিক স্ক্রিপ্টও রান করাতে পারবেন।

## শেষ কথা

Windows 10 আসলে যেভাবে কাজ করে, আশা করছি এর সমস্ত কিছু কন্ট্রোল করতে পারবেন Group Policy এর মাধ্যমে। আমরা দেখতেই পেলাম এটি ব্যবহার করে কিভাবে আপনার নেটওয়ার্ককে রাখতে পারবেন নিরাপদ এবং কার্যকরী। আমি এই টিউনে জরুরী কিছু সেটিং দেখেছি কিন্তু এখানে আপনি আরও অনেক কনফিগারেশন পাবেন।

কেমন হল আজকের টিউন তা অবশ্যই টিউমেন্টের মাধ্যমে জানাবেন।

পরবর্তী টিউন পর্যন্ত ভাল থাকুন। আমাদের সমসাময়িক যে সংকট চলছে এর থেকে রক্ষা পেতে সবাই সচেতন থাকবেন কারণ আপনার সচেতনতাই পারে আমাদের সবাইকে খারাপ অবস্থা থেকে বাঁচাতে। সবাই বাসায় থাকুন আর আল্লাহর উপর ভরসা রাখুন, আল্লাহ হা-ফেজ।
