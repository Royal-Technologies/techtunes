---
archive_id: techtunes-486856
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 486856
title: কিভাবে একটি সার্ভার বানাবেন? আসুন জেনে নেই
slug: networking-486856
language: bn
status: publish
published_at: '2017-04-02T18:20:00+00:00'
modified_at: '2017-04-03T05:56:00+00:00'
original_url: https://www.techtunes.io/networking/tune-id/486856
author: আশরাফুল ফিরোজ
author_url: https://www.techtunes.io/tuner/ashraful1004
categories:
- নেটওয়ার্কিং
tags:
- how to guide
- how to make nas
- টিউটোরিয়াল
content_hash: d8815084e8c057a188ab362273258e2a3362af5c84c21bd9b512cbea9f372c31
archived_at: '2026-11-12T12:55:04.616248+00:00'
---

আমরা সবাই আমাদের সাধের ডাটাগুলকে কখনো হারাতে চাই না। তাই অনেকেই এক ডাটা অনেক জায়গায় সেভ করে রাখি কখন জানি কোন জায়গা থেকে ডিলিট হয়ে যায়। আমার নিজের সাথেই এরকম অনেকবার হয়েছে যে ডাটা রেখে ভুলে ফোল্ডার ডিলিট করে দিয়েছি। এতে আমার যেমন ক্ষতি হয়েছে তেমনি গুরুত্বপূর্ণ ডাটা আর ফেরত পাওয়া যাবে না। এসকল সমস্যার একটি সহজ সমাধান হল একটি সার্ভার বানানো।

## সার্ভার কি?

সার্ভার শুনেই ভয় পাবার কিছুই নাই। সার্ভার বলতে আমরা বুঝি বিশাল বড় একটি কম্পিউটার। আসলে সেরকম কিছুইনা। যে কম্পিউটার আপনাকে কিছু সারভ করে অর্থাৎ আপনাকে কোনো প্রকার সুবিধা দেয় তাই সার্ভার। সার্ভার বড় যেমন হতে পারে তেমন খুব ছোটও হতে পারে। তো ডাটা হারানোর ভয় থেকেই মূলত আমি সার্ভারটি বানাই। আমি আজকে আপনাদের দেখাবো কিভাবে এটি বানাতে হয়।

## যা যা লাগবেঃ

- ১।একটি রাস্পবেরি পাই
- ২।একটি হার্ড ড্রাইভ বা পেনড্রাইভ(ডাটা রাখার জন্য)
- ৩।একটি ৮ জিবি মেমোরি কার্ড
- ৪।একটি পাওয়ার সাপলাই

তো চলুন টিউটোরিয়াল শুরু করা যাক। আশা করি নিচের ভিডিও টিউটোরিয়ালটি দেখলে সহজেই একটি সার্ভার বানাতে পারবেন।  
[Embedded External Content: https://www.youtube.com/embed/q17uivROxR8?feature=oembed]
  
 এর পরেও যদি কোন প্রকার সমস্যা হয় তাহলে অবশ্যই টিউমেন্ট করবেন

## Commands:

sudo apt-get install samba samba-common-bin  
 sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.old  
 sudo mkdir /media/storage  
 sudo mount -t auto /dev/sda1 /media/storage  
 sudo nano /etc/samba/smb.conf

[Storage]  
 comment = Storage  
 path = /media/storage  
 valid users = @users  
 force group = users  
 create mask = 0660  
 directory mask = 0771  
 read only = no

Remove the # symbol from the security = user line

sudo /etc/init.d/samba restart  
 sudo useradd nas -m -G users  
 sudo passwd nas  
 sudo smbpasswd -a nas  
 sudo nano /etc/fstab  
 dev/sda1 /media/storage auto noatime 0 0
