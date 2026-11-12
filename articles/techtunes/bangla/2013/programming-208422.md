---
archive_id: techtunes-208422
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 208422
title: লিনাক্সে রুবি অন রেইলস ইন্সটলেশন পদ্ধতি, অপারেটিং সিস্টেম উবুন্টু
slug: programming-208422
language: bn
status: publish
published_at: '2013-05-19T11:14:00+00:00'
modified_at: '2020-12-05T15:40:00+00:00'
original_url: https://www.techtunes.io/programming/tune-id/208422
author: Mashpy Says
author_url: https://www.techtunes.io/tuner/shadhin
categories:
- প্রোগ্রামিং
tags:
- উবুন্টু
- রুবি অন রেইলস
- লিনাক্স
content_hash: 91598bfe56319567a0e66b66136eca9352efa1bee4afef8c296a8a1966a2ea34
archived_at: '2026-11-12T12:58:29.979212+00:00'
---

রুবি একটি প্রোগ্রামিং ল্যাঞ্জুয়েজ, যার জনপ্রিয় MVC ফ্রেমওয়ার্ক হল রুবি অন রেইলস। ওয়েব সাইট তৈরির ক্ষেত্রে এই ফ্রেমওয়ার্কটির জনপ্রিয়তার মূল কারন এর শক্তিশালী সিকিউরিটি। ভাসিটিতে একবার রুবি অন রেইলসের উপর ওয়ার্কশপ হয়েছিল, সেখান থেকেই এর উপর ধারনা আসে। বলা হয়েছিল রুবি অন রেইলস লিনাক্সে ভাল সাপোর্ট দেয়, উইন্ডোজে বিভিন্ন ক্ষেত্রে সমস্যা করে। আমি চেয়েছিলাম উইন্ডোজেই এই ফ্রেমওয়ার্ক নিয়ে কাজ করব। কাজ করার সময়ে উইন্ডোজে তেমন কোন প্রবলেম করছিল না। কিন্তু ডাটাবেজ চাপ্টারে আসার পর বিভিন্ন কোড কাজ করছিল না।

শেষ পর্যন্ত রুবি অন রেইলসে থাকার জন্য লিনাক্সেই ব্যাক করতে হল। লিনাক্সে ফ্রেমওয়ার্কটি ইন্সটলেশন পদ্ধতি আমার কাছে একটু জটিল মনে হয়েছে। কারন এটা করতে গিয়ে অনেক গুলো ইংরেজী টিউটরিয়াল দেখতে হয়েছে। কোন টিউটরিয়ালই পরিপূর্ণভাবে করা নেই। তার জন্যই এই লেখা।

**১.** অপারেটিং সিস্টেম উবুন্টু ১২.১০ ইন্সটল পিসিতে টার্মিনালে গিয়ে নিচের কমান্ডটি লিখে রিপোজটরি আপডেট করে নিন। আপডেট করতে প্রায় ১৮ মেগাবাইট নিবে এটা।

**sudo apt-get update**

**২.** আপনার সিস্টেমে curl না থাকলে ইন্সটল করে নিন।

**sudo apt-get install curl**

**৩.** রুবি ভার্সন ম্যানেজার ইন্সটল করে নিন।

```
curl -L get.rvm.io | bash -s stable
```

**৪.** এটি ইন্সটল হওয়ার পর টার্মিনাল বন্ধ করে দিন। তারপর আবার চালু করুন। নিচের কমান্ডটি দিন।

**source ~/.rvm/scripts/rvm**

**৫.** আবার টার্মিনালটি অফ করুন। নিচের কমান্ডটি দিন।

**type rvm | head -n 1**

তারপর এখানে এরকম এরর দেখাতে পারে-  "You should get: RVM is a function as a reply"

এই মূহূর্তে আপনি টার্মিনালটি ফুল স্ক্রীন করুন। Edit - Profile Preferences- Run command as a login shell এ টিক চিহ্ন দিয়ে বেরিয়ে আসুন।  
 [![](http://1.bp.blogspot.com/-LmNw73eS8uc/UZeycy9VeXI/AAAAAAAAAoI/PxyBH8HLYGI/s640/Title_and_Command.jpg)](https://1.bp.blogspot.com/-LmNw73eS8uc/UZeycy9VeXI/AAAAAAAAAoI/PxyBH8HLYGI/s1600/Title_and_Command.jpg)  
 আবার কমান্ডটি এপ্লাই করুন।

**type rvm | head -n 1**

**৬.** নিচের কমান্ডটি চালিয়ে rvm এর যা যা ডিপেন্ডেন্সি দরকার লাগে আপডেট করে নিন।

**rvm requirements**

**৭.** রুবি এর ভার্সন আপডেট করে নিন। এখন লেটেস্ট ভার্সন ১.৯.৩ চলছে।

**rvm install 1.9.3**

**৮.** এই ভার্সনকেই ডিফল্ট হিসেবে করে নিন। তবে নিচের কোডটা কাজও না করতে পারে। তাহলে টার্মিনাল আবার রিস্টার্ট দিয়ে নিন।

```
rvm use 1.9.3 -default
```

**৯.** রুবি জেমসগুলো ইন্সটল করে নিন।

**rvm rubygems current**

**১০.** এখন রেইলস ইন্সটল করে নিন।

```
gem install rails
```

**১১.** পরে যা যা কমান্ড চালাতে হবে তার লিস্ট দিয়ে দিচ্ছি পর পর এপ্লাই করুন।

**gem install "therubyracer"**  
 **sudo apt-get install nodejs**  
 **rails new demo\_app**  
 **cd demo\_app**  
 **rails server**

এখানে rubyracer এবং nodejs জাভাস্ক্রীপ্ট ইঞ্জিন যোগ করা হচ্ছে। তারপর rails এর নতুন এপ তৈরি করা হচ্ছে, এটা তৈরি করতে একটু সময় লাগে। তারপর রেইলস সার্ভার চালু করা হচ্ছে।

**১২.** সর্বশেষ <http://localhost:3000/> তে ভিজিট করুন। নিচের মত আসলে আপনার রেইলস এপ্লিকেশনটি ঠিকভাবে সার্ভারে রান হয়েছে।  
 [![](http://2.bp.blogspot.com/-rYegrDM5nG8/UZe_YmGY4RI/AAAAAAAAAoY/YjVzDx6JTRg/s640/localhost.jpg)](https://2.bp.blogspot.com/-rYegrDM5nG8/UZe_YmGY4RI/AAAAAAAAAoY/YjVzDx6JTRg/s1600/localhost.jpg)

## রুবি অন রেইলস শেখার জন্য যে বইগুলো কালেক্ট করতে পারেন -

**১.** book of ruby  
 **২.** Ruby on Rails 3 Tutorial  
 **৩.** Pragmatic Agile Web Development with Rails
