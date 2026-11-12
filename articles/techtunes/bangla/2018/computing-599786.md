---
archive_id: techtunes-599786
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 599786
title: 'অ্যামাজন ওয়েব সার্ভিসেস [পর্ব-০৩] :: আপনার কম্পিউটার থেকে কিভাবে ক্লাউড কম্পিউটারে
  কানেক্ট হবেন'
slug: computing-599786
language: bn
status: publish
published_at: '2018-11-02T20:26:00+00:00'
modified_at: '2018-11-02T20:26:00+00:00'
original_url: https://www.techtunes.io/computing/tune-id/599786
author: মোনারুল ইসলাম
author_url: https://www.techtunes.io/tuner/kazipurit
categories:
- কম্পিউটিং
tags:
- Amazon
- cloud computing
- cloud file transfer
content_hash: 2e7bb9b0b617a578505888148282707f4406c07ea2e8957de65b67a7dfbe1039
archived_at: '2026-11-12T12:29:28.660834+00:00'
---

টিউনের শুরুতে সবাইকে সালাম ও শুভেচ্ছা রইল। আমার টিউনে কোন ভুল হলে ক্ষমার দৃষ্টিতে দেখবেন। গত পর্বে আমরা দেখে ছিলাম কিভাবে অ্যামাজন ক্লাউডে একটি কম্পিউটার বানাতে হয়। আজ আমরা শিখব কিভাবে সেই কম্পিউটারে কানেক্ট হব আমাদের লোকাল কম্পিউটার থেকে। এই জন্য আপনাকে কিছু টুলস লাগবে। প্রথমে সেই টুলস গুলো ডাউনলোড করে ইন্সটল করে নিবেন।

টুলস লিঙ্কঃ

WinSCP  
 Web Site:<https://winscp.net/eng/download.php>  
 Download Link Direct: <https://winscp.net/download/files/20180926071294ed76f7679852c244b5bc67448c86a4/WinSCP-5.13.4-Setup.exe>

PuTTY  
 Web Site Link: <https://www.putty.org/>  
 Direct Download Link:  
 32 Bit Operating System: <https://the.earth.li/~sgtatham/putty/latest/w32/putty.exe>  
 64 Bit Operating System: <https://the.earth.li/~sgtatham/putty/latest/w64/putty.exe>

আমরা সবাই কম বেশি পুটি (PuTTy)  টুলসের কথা জানি। যেটা দিয়ে আপনি রিমোট কানেক্ট হতে পারেন। আপনি হয়ত উপরের টুলস গুলো ইন্সটল করে ফেলেছেন। আপনি যখন পুটি ইন্সটল দেন তখন তার সাথে একটি টুলস অটো ইন্সটল হয়ে থাকে যেটা পুটিজেন নামে। আপনাকে প্রথমে পুটিজেন দিয়ে আপনার PEM ফাইল কে কনভার্ট করে PPK ফাইল করতে হবে। কেননা আপনি যখন রিমোট কানেক্ট হবেন তখন অথেনটিক জন্য আপনার পাসওয়ার্ড লাগবে সেই পাসওয়ার্ড আপনার PPK ফাইলের মধ্যে রয়েছে। ছবিতে দেখুন অথেনটিক কোথায় দিতে হয়।

![](https://dnc.techtunes.io/tDrive/tuner/2018/09/techtunes_244314855110e355d026b06d992e69b6.jpg)

ব্রাউজ করে PPK ফাইল দেয়ার পর ওপেন করলে আপনার একটি পপআপ আসতে পারে অবশ্যই আপনি ইয়েস করে দিবেন। আপনার হয়ত বার বার মনে হতে পারে আপনার লগইনের জন্য কি ইউজার ব্যবহার করবেন। আপনি যখন ব্যবহারের জন্য সেল পাবেন সেখানে আপনার ইউজার দেখা যায় অথবা আপনি নিচের ইউজার গুলো ব্যবহার করতে পারেন।

Get the default user name for the AMI that you used to launch your instance

For Amazon Linux 2 or the Amazon Linux AMI, the user name is ec2-user.  
 For a Centos AMI, the user name is centos.  
 For a Debian AMI, the user name is admin or root.  
 For a Fedora AMI, the user name is ec2-user or fedora.  
 For a RHEL AMI, the user name is ec2-user or root.  
 For a SUSE AMI, the user name is ec2-user or root.  
 For an Ubuntu AMI, the user name is ubuntu.  
 Otherwise, if ec2-user and root don't work, check with the AMI provider.

এই ইউজার গুলো আমাজনের ডক ফাইলে থেকে নেয়া। আপনি চাইলে গুগলে সার্চ করে পেতে পারেন। আজ এই পর্যন্ত আগামীতে আমরা উইন্ডোজ সার্ভার ইন্সটল ও লোকাল কম্পিউটার থেকে কিভাবে রিমোট ডেস্কটপে কানেক্ট হবে সেটা দেখব। উপরের স্টেপ কোন ভুল করলে বা বুঝতে না পারলে টিউমেন্ট করতে পারেন। আপনি এই ভিডিও একবার দেখে নিতে পারেন হয়ত আরো সহযোগী হবে।

[Embedded External Content: https://www.youtube.com/embed/SGJBVPsLp-E?feature=oembed]

সর্বপরি আজ এইখানে শেষ। আপনি ভালো থাকুন। আল্লাহ্‌ হাফেজ
