---
archive_id: techtunes-513634
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 513634
title: প্রোগ্রামিং করুন অ্যান্ড্র‍য়েডে (পর্ব ২)। দেখে নিন C,C++,python প্রোগ্রামিং
  এর জন্য চমৎকার কিছু  Application
slug: android-513634
language: bn
status: publish
published_at: '2017-09-10T12:03:00+00:00'
modified_at: '2017-09-10T12:25:00+00:00'
original_url: https://www.techtunes.io/android/tune-id/513634
author: মাকসুদুর রহমান জীবন
author_url: https://www.techtunes.io/tuner/maksudur
categories:
- অ্যান্ড্রয়েড
tags:
- Android
- এন্ড্রয়েড এ প্রোগ্রামিং
- টিপস এন্ড ট্রিকস
content_hash: 295d5b3243c541ce7f0ca2b681af018098a697a907cf993334de2d20abc3711e
archived_at: '2026-11-12T12:39:03.989873+00:00'
---

এর আগের টিউনটিতে আমি terminal emulator দিয়ে প্রোগ্রাম কম্পাইল করার কথা বলেছিলাম। তাই আজকে terminal emulator দিয়ে প্রোগ্রাম কম্পাইলের ধাপে চলে যাচ্ছি। প্রথমেই আমাদের দুটি app ডাউনলোড এবং ইন্সটল করে নিতে হবে।  
 app দুটি হলো :

## ১. Termux

Termux হলো একটি terminal app. এটি মূলত আ্যান্ড্রয়েডে linux environment তৈরি করে।  
 ডাউনলোড করতে [এখানে ক্লিক করুন](https://play.google.com/store/apps/details?id=com.termux&hl=en)

## ২.Hackers keyboard

এটি একটি কি বোর্ড যা মূলত terminal emulator এর জন্যই বিশেষভাবে বানানো।

ডাউনলোড করতে [এখানে ক্লিক করুন](https://play.google.com/store/apps/details?id=org.pocketworkstation.pckeyboard&hl=en) এবার hackers keyboard app টিকে ডিফল্ট কিবোর্ড করে নিতে হবে। Termux ওপেন করার পর আমাদের প্রথমে এর সকল pakage update এবং upgrade করে নিতে হবে। update করতে টাইপ করুন

★$ apt update

upgrade করতে টাইপ করুন এবং enter চাপুন।

★ $ apt upgrade

এরপর আপনাকে programming language pakage install করতে হবে। প্রত্যেকটি programing language এর জন্য আলাদা আলাদা প্যাকেজ আছে। আপনি আপনার প্রয়োজনীয় pakage টি ইন্সটল করে নিবেন। নিচে এর একটি তালিকা এবং তা ইন্সটল করার command দেওয়া হলো :  
 ১. c / c++  
 $ pkg install clang

২. python  
 $ pkg install python

৩. go  
 $ pkg install golang

৪. ruby  
 $ pkg install ruby

pakage ইন্সটল করা শেষ হলে আপনি প্রোগ্রাম কম্পাইল ও রান করাতে পারবেন।

কিন্তু প্রথমেই termux সম্পর্কে একটি basic ধারণা মাথায় থাকা লাগবে।

\* termux কখনোই এক directory তে থেকে অন্য directory তে কাজ করতে পারে না।  
 (বিষয়টি কিছুক্ষণ পরে আরো স্পষ্ট ভাবে বুঝতে পারবেন।)

\*কিছু গুরুত্বপূর্ণ command আপনাকে মনে রাখতে হবে।

directory পরিবর্তন করার জন্য = cd  
 directory তে কি কি ফাইল আছে তা দেখার জন্য = ls  
 termux এখন কোন directory তে আছে তা জানার জন্য = pwd

আমি একটি c++ প্রোগ্রাম লিখেছি যা আমাদের স্ক্রিনে hello world. লেখা দেখাবে। আর এটি আমার / ডিরেক্টরির sdcard ফোল্ডারের cpp সাবফোল্ডারের ভেতর hello.cpp নামে সেভ করা আছে। এটি কম্পাইল করতে হলে প্রথমে আমাদের termux এর directory থেকে hello.cpp এর ডিরেক্টরি তে যেতে হবে। এছাড়া termux কখনই hello.cpp কে খুঁজে পাবে না। directory পরিবর্তন করতে টাইপ করুন

$ cd sdcard/cpp

এখন directory পরিবর্তিত হয়ে গেছে।

প্রোগ্রাম কম্পাইল ও রান করার command গুলোর তালিকা নিচে দেওয়া হলো :

c++  
 compile: $ clang++ (file name.extension)  
 run. : $ ./a.out

c  
 compile: $ clang (file name.extension)  
 run. : $ ./a.out

python  
 compile: (কম্পাইলের প্রয়োজন পড়ে না)  
 run. : $ python (file name.extension)

ruby  
 compile: (কম্পাইলের প্রয়োজন পড়ে না)  
 run. : $ python (file name.extension)

go  
 compile: (কম্পাইলের প্রয়োজন পড়ে না)  
 run. : $ go run (file name.extension)

টিউন সংক্রান্ত কোনো প্রশ্ন থাকলে টিউনমেন্টে জানাবেন। টিউনটি পড়ার জন্য ধন্যবাদ

***বি.দ্র.: অনেক সময়ই sdcard এর ফাইল কম্পাইল করলেও termux তা run করতে পারে না। permission denied দেখায়। এই ক্ষেত্রে প্রোগ্রাম run করার জন্য তা termux এর নিজস্ব storage এ তা রাখা লাগে। ইনশাল্লাহ পরবর্তি টিউনে এই বেপারে বিস্তারিত জানিয়ে দিব।***
