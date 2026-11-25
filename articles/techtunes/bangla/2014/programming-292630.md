---
archive_id: techtunes-292630
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 292630
title: 'সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০২] :: নবীনদের জন্য  -২'
slug: programming-292630
language: bn
status: publish
published_at: '2014-06-28T11:30:00+00:00'
modified_at: '2014-08-18T17:07:00+00:00'
original_url: https://www.techtunes.io/programming/tune-id/292630
author: Hasnat Riaz
author_url: https://www.techtunes.io/tuner/hasnat_riaz
categories:
- প্রোগ্রামিং
tags: []
content_hash: ef94025dd1c7500a9c108d24c0a7fbf0266766b51cfc86ba448cbf1deff0b7dc
archived_at: '2026-11-25T07:04:51.381993+00:00'
---

### [ডেভেলপমেন্ট ইন C শার্প](https://www.techtunes.io/chain-tunes/software-development-in-c-sharp "ডেভেলপমেন্ট ইন C শার্প")

- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০১] :: নবীনদের জন্য -১](https://www.techtunes.io/programming/tune-id/292139 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০১] :: নবীনদের জন্য -১")
- সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০২] :: নবীনদের জন্য -২
- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০৩] :: নবীনদের জন্য-৩](https://www.techtunes.io/programming/tune-id/293018 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০৩] :: নবীনদের জন্য-৩")
- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০৪] :: নবীনদের জন্য-৪](https://www.techtunes.io/programming/tune-id/293412 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০৪] ::  নবীনদের জন্য-৪")
- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০৫] :: নবীনদের জন্য-৫](https://www.techtunes.io/programming/tune-id/294344 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০৫] ::  নবীনদের জন্য-৫")
- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব-০৬] :: User defined type -১](https://www.techtunes.io/programming/tune-id/297241 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব-০৬] :: User defined type -১")
- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব-০৭] :: User defined Type -২](https://www.techtunes.io/programming/tune-id/298299 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব-০৭] :: User defined Type -২")
- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব-০৮] :: Exception Handling -১](https://www.techtunes.io/tutorial/tune-id/290347 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব-০৮] :: Exception Handling -১")
- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব -০৯] :: Exception Handling -২](https://www.techtunes.io/tutorial/tune-id/290598 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব -০৯] :: Exception Handling -২")
- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব-১০] :: Exception Handling -৩](https://www.techtunes.io/programming/tune-id/291489 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব-১০] :: Exception Handling -৩")

পর্বটি শুরু করার আগে C শার্পের কিছু  data types , এদের range এবং মেমোরিতে কতটুকু জায়গা নিবে তা দেখে নিই:

![](https://dnc.techtunes.io/tDrive/tuner/hasnat_riaz/292630/dataTypeTable.png)

আমি ধরে নিচ্ছি, আপনারা আগে C ল্যাঙ্গুয়েজে কাজ করেছেন এবং ভেরিয়েবল কি তা জানেন।তারপরেও আমি যদি খুব অল্প কথায় বলি তাহলে, ভেরিয়েবল হল প্রোগ্রামিং ল্যাঙ্গুয়েজে ব্যবহৃত ডাটা ধারন করার স্থানের রুপক নাম। মেমোরিতে ডাটা রাখার জন্য প্রোগ্রামে সরাসরি মেমোরি এড্রেস ব্যাবহার না করে, কোন একটি এড্রেসের জন্য রুপক নাম ব্যাবহার করা হয় এবং প্রোগ্রামে ঐ নামের অধীনেই ডাটা রাখা হয়।

প্রত্যেক ভেরিয়েবল কিছু ডাটা টাইপ থাকে যা নির্ধারন করে সেই ভেরিয়েবল কি ধরনের ডাটা সংরক্ষন করবে এবং মেমোরিতে কতটুকু জায়গা রাখবে। উদাহরণস্বরূপঃ int aNumber; এই স্টেটমেন্টটির মানে হচ্ছে aNumber হচ্ছে int টাইপের অর্থাৎ পূর্ণ সংখ্যার ভেরিয়েবল। প্রোগ্রামটি রান করলে aNumber এর জন্য মেমোরিতে 4 byte (C শার্পে) জায়গা রাখবে। যাইহোক এই পর্বে আমি যোগ, বিয়োগ, গুন, ভাগের সাধারণ একটি ক্যালকুলেটর বানিয়ে Console Application এ দেখাবো।

প্রথমেই আমি নতুন একটি Console Application ওপেন করে প্রজেক্টের নাম দিলাম CalculatorApp. এরপর মেইন মেথডে নিচের মত কোডগুলো লিখলাম:

![](https://dnc.techtunes.io/tDrive/tuner/hasnat_riaz/292630/calculatorConsole1.png)

প্রথমেই firstNo, secondNo, addition, subtraction, multiplication, division নামে ছয়টি double টাইপ ভেরিয়েবল নিলাম। এরপর ConsoleWrite() মেথডটির মাধ্যমে ১ম নাম্বারটি ইনপুট দেয়ার জন্য ইউজারকে মেসেজ দেখালাম। firstNo = Convert.ToDouble(Console.ReadLine()); এর স্টেটমেন্টের মাধ্যমে ইউজারের কাছ থেকে ইনপুট নিলাম এবং সেটিকে ডাবলে কনভার্ট করে firstNo ভেরিয়েবলে রাখলাম। ব্যাপারটা আরেকটু ভালোভাবে খেয়াল করলে এইরকম, Console.ReadLine() মেথড ইউজারের কাছ থেকে string ইনপুট নেয়।

আমরা সেটিকে আবার Convert.ToDouble() এর মাধ্যমে double এ কনভার্ট করে নিলাম কারণ আমাদের firstNo ভেরিয়েবলটি double টাইপের। অনুরুপভাবে দ্বিতীয় নম্বরটি ইনপুট নিয়ে আমরা secondNo ভেরিয়েবলে রাখলাম। এরপর firstNo, seconNo এই দুই ভেরিয়েবলে থাকা  সংখ্যা দুইটির যোগ/বিয়োগ/গুন/ভাগকরে তা আরেকটি ভেরিয়েবলে (addition/ subtraction/ multiplication/ division) রাখলাম, পরবর্তীতে তা ইউজারকে দেখালাম। প্রোগ্রামটির আউটপুট নিচের মতো:

![](https://dnc.techtunes.io/tDrive/tuner/hasnat_riaz/292630/CalculatorConsole2.png)

পর্বটি এখানেই শেষ করলাম।আগামী পর্বে ইনশাআল্লাহ্‌ এই প্রোগ্রামটি Windows Forms Application, WPF Application এ দেখাবো।
