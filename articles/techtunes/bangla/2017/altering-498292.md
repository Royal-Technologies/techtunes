---
archive_id: techtunes-498292
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 498292
title: 'Kali_Buntu: উবুন্তুতে কালির টুল কিভাবে ইউজ করবেন ?'
slug: altering-498292
language: bn
status: publish
published_at: '2017-06-15T04:30:00+00:00'
modified_at: '2017-06-15T04:30:00+00:00'
original_url: https://www.techtunes.io/altering/tune-id/498292
author: R!zwan B!n Sula!man
author_url: https://www.techtunes.io/tuner/rizuan611
categories:
- অল্টারিং
tags:
- kali
- katoolin
- Ubuntu.
content_hash: 6d646b65df766014f89e0d9f58ce363b6c66c5a905db2a4db4ed462ff04fc314
archived_at: '2026-11-12T12:48:57.026712+00:00'
---

পেনিট্রেশন টেস্টিং বেলেন আর হ্যাকিং বলেন, এটা বলতে দিধা নাই যে কালি একটা পার্ফেকট অপেরেটিং সিস্টেম, তাদের জন্য যারা এই লাইনে হাঁটেন। তবে আমার পার্সনাল মতামত হল, কালি যথেষ্ট Unstable, Dependencies শেষ নাই ! কোন একটা সফওয়ার Install দিতে গেলে বুঝা যায় কত ধানে কত চাল !

অনেকে ভাবের ঘোরে বসে কালি ইউজ করে ! লোকে বলবে "বাহ ! ছেলেটা কালি ইউজ করে "। ভাব দেখাইলে তো আমার কিচ্ছু করার নাই ! যারা কালি কালি করে খালি চিল্লায়, এরা একটু ঘাটা ঘাটি করলে কিন্তু অনেক ভাল সমাধান পাইতেন ! আমি যদি কালি এর সবগুলা টুলস আমার উবুন্তুতে Install করে ফেলি, তাহলে কিন্তু কালির Instability এবং Dependencies এর ঝামেলা থেকে রক্ষা পাই !

LionSec আমাদের জন্য Katoolin নামক একটা পাইথন script Develop করেছে ! এটা দিয়ে সহজেই Ubuntu-তে কালি এর সব টুলস Install করা যায়। আজকে আমি এই জিনিসটাই দেখাবো।

## Ubuntu-তে টার্মিনাল খুলে নিচের Command-গুলা ইউজ করেন:

- ১। sudo apt-get install python git
- ২। sudo su
- ৩। git clone <https://github.com/LionSec/katoolin.git> && cp katoolin/katoolin.py /usr/bin/katoolin
- ৪। chmod +x /usr/bin/katoolin

ব্যাস কাজ শেষ, এখন আপনার মেশিনে katoolin, Install হয়েছে।

## কিভাবে ব্যবহার করবেন

Terminal-এ katoolin লিখেন ! এমন কিছু একটা দেখবেন

![](https://dnc.techtunes.io/tDrive/tuner/rizuan611/498292/Screenshot_4.png.jpg)

এই লাইন গুলা একটু আলোচনা করি।

1. Add Kali repositories & update kat  এর পরে 1 type করলে  কালির repositories-গুলা এড হবে এবং আপডেট হবে। নিচের মত কিছু দেখতে পাবেন

```
1) Add Kali repositories & Update 
2) View Categories
3) Install classicmenu indicator
4) Install Kali menu
5) Help

kat >1
```

এখন আবার আমরা 1 type করব  !

- Then, type 2 to update the repositories
- Type 3 to if you want to remove the added kali-linux repositories, and type 4 to view the contents of sources.list file.
- To go back to the previous menu, type back and press ENTER.
- To go back to the main menu, type gohome and hit ENTER.

```
kat > gohome
1) Add Kali repositories & Update 
2) View Categories
3) Install classicmenu indicator
4) Install Kali menu
5) Help
To view all the list of available categories, type 2.
```

```
kat> 2
                           All Categories 
1) Information Gathering			8) Exploitation Tools
2) Vulnerability Analysis			9) Forensics Tools
3) Wireless Attacks				10) Stress Testing
4) Web Applications				11) Password Attacks
5) Sniffing & Spoofing				12) Reverse Engineering
6) Maintaining Access				13) Hardware Hacking
7) Reporting Tools 				14) Extra
0) All
Select a category or press (0) to install all Kali linux tools .
```

As you see in the above output, there are 14 categories are available. You can either install all of them at once, or install any specific category by entering the respective category number.

To install all kali Linux tools, type **0** (zero) and press ENTER key. This will install all tools. It will take a while depending upon the Internet speed. Also, make sure you have sufficient space in your hard drive. This is going to consume a lot of disk space.

Alternatively, just install what exactly you want. Say for example, to install tools under category Exploitation tools, type 8 and press ENTER.

![](https://dnc.techtunes.io/tDrive/tuner/rizuan611/498292/Screenshot_4.jpg)

It will display a sub menu and list all available packages in this category. You can install all tools in that category by typing 0 (zero), or type any specific number to install the particular tool under the Exploitation tools category.

Thats It ! you have successfully install kali tools in you Ubuntu machine !

write “gohome” and then, now you need to Install classicmenu indicator, type 3 and press ENTER and then type y to confirm and install it.

The last thing you need to do is, install kali tool menu, type 4 and type y to confirm the installation.

Thanx, if you liked it share it ! thanx

- [ফেবুতে আমাকে পাবেন](https://www.facebook.com/rizwanbinsulaiman)
- [ফেবুতে আমার পেইজ](https://www.facebook.com/pages/Rizwan-Bin-Sulaiman/636462423117510)
- [বাংলাদেশ ব্লেক হ্যাট হ্যাকারস এর পেইজ](https://www.facebook.com/BangladeshBlackHat)
