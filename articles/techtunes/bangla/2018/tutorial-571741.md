---
archive_id: techtunes-571741
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 571741
title: 'jQuery for Web Design [পর্ব-০২] :: jQuery Integrate amp jQuery Events amp
  jQuery Methods নিয়ে কিছু কথা'
slug: tutorial-571741
language: bn
status: publish
published_at: '2018-03-31T06:47:00+00:00'
modified_at: '2018-03-31T06:47:00+00:00'
original_url: https://www.techtunes.io/tutorial/tune-id/571741
author: মোহাম্মদ রিয়াদ
author_url: https://www.techtunes.io/tuner/itorcenter
categories:
- ওয়েব ডিজাইন
tags:
- জেকোয়ারি
- টিউটোরিয়াল
- Bangla jquery tutorial
- Bangla Web Design Tutorial
- FREE WEB DESIGN TUTORIAL
- jquery
- web deisgn
- টিউটোরিয়াল
- টিপস এন্ড ট্রিকস
content_hash: 066b831f073178d12530a34628014dbdee80136e7d199a522c768d805ef53fe7
archived_at: '2026-11-12T12:32:27.466342+00:00'
---

আসসালামু আলাইকুম। সকলে কেমন আছে। আমি আলহামদুল্লিলাহ ভালই আছি। আপনাদের সকলকে জানাই **jQuery for Web Design** সিরিজে স্বাগতম। তো, আমাদের আজকের এই পর্ব থেকে আমরা জানবো **jQuery** কিভাবে আমাদের প্রোজেক্ট এ যুক্ত করতে পারি এবং এর **Event & Method** সম্পর্কে। তো চলুন শুরু করা যাক আমাদের আজকের পর্ব।

**jQuery কিভাবে আমাদের প্রোজেক্ট-এ যুক্ত করতে পারি?**

=> গত পর্বে আমরা দেখেছিলাম আমরা jQuery কোথা থেকে পেতে পারি। তো ওইখান থেকে আমরা jQuery টাকে লিংকের মাধ্যমে যুক্ত করতে পারি অথবা ফাইলটাকে আমাদের প্রোজেক্ট ফোল্ডারে js নামে একটা ফোল্ডার করে, তার ভেতর যেকোন নামে এক্ষেত্রে আমি ধরে নিচ্ছি jQuery.js নামে একটি ফাইল করে লিংক থেকে প্রাপ্ত ফাইলের সকল কোড সমূহ আমাদের তৈরি করা ফাইলে কপি এবং পেস্ট করে সেভ করে রাখতে পারি। এভার আমার প্রোজেক্টের মেইন ফাইল, মানে HTML ফাইলে যুক্ত করার পালা। আমরা যদি  লিংকের মাধ্যমে যুক্ত করি তাহলে নিচের দেওয়া পদ্ধতিতে যুক্ত করতে পারি।

`<script src="ফাইলের লিংক"></script>`

এই কোড টুকু ব্যবহার করে আমরা ফাইল যুক্ত করতে পারবো। উদাহরন স্বরূপ যদি আমরা দেখেতে চাই তাহল চলুন গুগল এর jQuery ফাইলে লিঙ্কের মাধ্যমে যুক্ত করার চেষ্টা করি।

**`<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>`**

তো আমরা দেখলাম লিঙ্কের মাধ্যমে আমরা কিভাবে jQuery ফাইল যুক্ত করতে পারি। কিন্ত আমরা এইভাবে ফাইল যুক্ত করবো না। তার কারণ হলো এইভাবে যদি যুক্ত করি আমাদের কম্পিউটারে সার্ভক্ষিন ইন্টারনেট সংযোগ রাখতে হবে।

এবার আমরা দেখবো আমাদের তৈরি করা জেস ফাইলে কিভাবে যুক্ত করতে পারি।

`<script src="folder name/file name.js"></script>`

এই পদ্ধতিতে আমরা প্রোজেক্ট ফোল্ডারে থাকা jQuery ফাইল যুক্ত করতে পারি। চলুন আমাদের তৈরি করা ফাইলটাই যুক্ত করি।

`<script src="js/jQuery.js"></script>`

তো আমরা দেখলাম কিভাবে আমরা jQuery ফাইল আমাদের প্রোজেক্টের মধ্যে যুক্ত করতে পারি।

**jQuery Events এবং Methods**

jQuery তে Event সমূহকে ৪ ভাগে ভাগ করে রাখা হয়েছে। সেগুলো হলঃ

- **Mouse Events**
- **Keyboard Events**
- **Form Events**
- **Documents / Windows Events**

তো চলুন জেনেনি এই ৪ ভাগে কি কি Events রয়েছে।

**Mouse Events**

- *click*
- *dblclick*
- *mouseenter*
- *mouseleave*

**Keyboard Events**

- *keypress*
- *keydown*
- *keyup*

**Form Events**

- *submit*
- *change*
- *fouce*
- *blur*

**Documents / Windows Events**

- *load*
- *unload*
- *resize*
- *scroll*

jQuery তে অনেক মেথড রয়েছে যা আমরা ব্যবহারের মাধ্যমে জানবো। তার আগে আমি আপনাদের এটা জানিয়ে রাখতে চাই আপনারা মেথড কিভাবে চিনবেন। আমরা আগের পর্বের jQuery সিন্টেক্স সম্পর্কে জেনেছি। তাও আবার দেখাচ্ছি.

`$(selector).action();`

এইটাই তো। তো এখানে action এর জায়গায় যে লিখাটি হবে সেটাই হচ্ছে মেথড। যেমনঃ `$(selector).hide();` এখানে hide() হল একটি মেথড।

আজ এই পর্যন্ত, আগামী পর্ব থেকে আমরা jQuery কোড লিখা আরম্ভ করবো এবং মেথডের ব্যবহার দেখে jQuery এর বিস্তারিত সম্পর্কে জানবো।
