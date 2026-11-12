---
archive_id: techtunes-367903
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 367903
title: টপ ২০ টি জাভাস্ক্রিপ্ট ফ্রেমওয়ার্ক যেগুলো সম্পর্কে না জানলে আপনার জীবনই বৃথা
slug: javascript-367903
language: bn
status: publish
published_at: '2019-08-20T13:18:00+00:00'
modified_at: '2019-08-20T13:18:00+00:00'
original_url: https://www.techtunes.io/javascript/tune-id/367903
author: অরিন্দম পাল
author_url: https://www.techtunes.io/tuner/arindampaulripon
categories:
- জাভাস্ক্রিট
tags:
- bangla javascript tutorial
- Top Javascript framework
- '`Top 20 Javascript framework'
content_hash: 6c68e6afd5f03f2c8f3884669fb483af55cc538aa6a8926fb14112b42cf0b51d
archived_at: '2026-11-12T12:56:42.746077+00:00'
---

টেকটিউনসের সবাইকে শুভেচ্ছা। আশা করি সবাই ভাল আছেন। আজ আমরা ওয়েব ডেভলপমেন্ট এর একটা বিষয় নিয়ে একটু আলোচনা করব। আমরা জানি এখন প্রতিদিনই অসংখ্য পরিমাণ ওয়েব অ্যাপ্লিকেশন তৈরী হচ্ছে। এবং সবথেকে গুরুত্বপূর্ণ কথা হল এখন প্রায় সব অ্যাপ্লিকেশনগুলোই বেশ জটিল এবং ফ্রন্ট এন্ড ডেভলপেমন্টের ক্ষেত্রে তো স্ট্যাটিক পেজের আর কোন স্থানই নেই। সবকিছুই হয়ে যাচ্ছে ডাইনামিক।

আপনার একটা ওয়েবসাইটে বা সার্ভারে প্রচুর পরিমাণ অবজেক্ট রয়েছে যেগুলো নিজেদের ভেতর বিভিন্ন ভাবে ইন্টারঅ্যাক্ট করছে, এবং এটা করানোও যে খুব সহজ সেটাও নয়। কিন্তু এই কাজগুলো সহজে করারও বিভিন্ন উপায় বের হচ্ছে প্রতিদিন। এর কঠিন কাজগুলো সহজ করে ফেলার একটা সবথেকে সহজ সমাধান হল জাভাস্ক্রিপ্ট এর বিভিন্ন ফ্রেমওয়ার্ক। ‌ তাই, আজ আমি আপনাদেরকে বেশ অনেকগুলো জাভাস্ক্রিপ্ট এর ফ্রেমওয়ার্কের সাথে পরিচয় করিয়ে দেব যেগুলোর মাধ্যমে আপনি ডাইনামিকলি বিভিন্ন কাজ করতে পারবেন।

এই ধরনের ফ্রেমওয়ার্কগুলো কেন প্রয়োজন

আপনি যদি জাভাস্ক্রিপ্ট এর ফ্রেমওয়ার্ক বলতে শুধুমাত্র [জেকুয়েরি](https://jquery.com/) কে বুঝে থাকেন তাহলে আমি বলব আাপনি এখনও অনেক কিছুই জানেন না। আসলে রেসপনন্সিভ, ফ্লুইড এবং সহজে মেইনটেইনেবল ওয়েব অ্যাপ তৈরী করা খুুব একটা সহজ কাজ না। এসব কাজের জন্য আপনাকে ব্যাকএন্ডে সার্ভারে ডাটা সেন্ড, আপডেট, রিড এবং বিভিন্ন ভাবে একসেস করতে হবে। আসলে একটা ওয়েবসাইটের ব্যাকগ্রাউন্ডে যে কতটা কাজ এবং সেটাকে ফ্রন্ট এন্ডে এনে রিপ্রেজেন্ট করাটাও যে খুব একটা সহজ না সেটাও বুঝতে পারছেন। আসলেই একজন ওয়েব ডেভলপার এর কাজটা অনেক জটিল ও সময়সাপেক্ষ। তাদের ওয়েবসাইটকে ঠিকঠাক রাখার কারণে অনেক খাটুনি পড়ে।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/url.jpg)

এখন ডেভলপারদের কাজগুলো বিভিন্ন ফ্রেমওয়ার্ক অনেক সহজ করে দিয়েছে। বিভিন্ন ফ্রেমওয়ার্কের সাহায্যে অনেক জটিল ও কঠিন কাজ অত্যান্ত দ্রুত করে ফেলা সম্ভ হচ্ছে যেটা করতে ডেভলপাররা অনেক কষ্ট করতেন। তাই, এটা সময়ও অনেক বাচিয়ে দিচ্ছে এবং সেই সাথে কোড লেখার পরিমাণও। আজ আমরা এমন কিছু জাভাস্ক্রিপ্ট এর ফ্রেমওয়ার্ক সম্পর্কে জানব যেগুলোর মাধ্যমে আপনারা খুব সহজেই ফ্রন্ট এন্ড এবং ব্যাক এন্ড এর কাজগুলো করে ফেলতে পারবেন এবং সেগুলো বেশ জনপ্রিয়ও। যদিও এর ভেতর এমন অনেক ফ্রেমওয়ার্ক রয়েছে যেগুলো অনেক পুরানো,   কিন্তু সেগুলো থেকেও অনেক কিছু শেখার আছে।

## [**Sproutcore**](http://www.sproutcore.com/)

[**Sproutcore**](http://www.sproutcore.com/) হল একটা হাই প্রোফাইল অ্যাপ ডেভলপমেন্টের জন্য পারফেক্ট ফ্রেমওয়ার্ক। এটা দিয়ে ‌ [MobileMe](https://en.wikipedia.org/wiki/MobileMe) এর মত অ্যাপ ডেভলপ করা হয়েছে। এটা শেখাটা একটু সময় সাপেক্ষ কিন্তু একবার শিখতে পারলে এটার মাধ্যমে অনেক কিছু ই করা সম্ভব যেটা অন্য ফ্রেমওয়ার্ক দিয়ে করাটা অনেক কঠিন। এটার একটা UI ফ্রেমওয়ার্ক ও রয়েছে এবং এটা [MVC](https://en.wikipedia.org/wiki/Model–view–controller) টাইপের একটা ফ্রেমওয়ার্ক। আর সেই সাথে এটার একটা খুবই সমৃদ্ধ API ডকুমেন্টেশন রয়েছে।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/sc.png)

**শিক্ষণীয় রিসোর্স****:**

- [Using SproutCore 2.0 with jQuery UI](http://yehudakatz.com/2011/06/11/using-sproutcore-2-0-with-jquery-ui/)
- [Build a Micro-Blog with SproutCore](http://net.tutsplus.com/tutorials/javascript-ajax/how-to-build-a-micro-blog-with-sproutcore-new-on-premium/)
- [When To Use SproutCore, and When Not To](http://blog.sproutcore.com/when-to-use-sproutcore-and-when-not-to/)

## [**Cappuccino**](http://cappuccino.org/)

[**Cappuccino**](http://cappuccino.org/) প্রথম ডেভলপ করা হয় ‌ ‌280North team এর থেকে। এটা বর্তমাতে [MOTOROLA](http://www.motorola.com/) এর একটা ফ্রেমওয়ার্ক।

এই ফ্রেমওয়ার্ক টা এমনভাবে ডেভলপ করা যে এটা নিয়ে কাজ করতে হলে আপনাকে HTML, CSS, DOM এসব না জানলেও চলবে। আপনাকে শুধুমাত্র জানতে হবে এই ফ্রেমওয়ার্কটা সম্পর্কে। তাহলেই আপনি এটা দিয়ে সবকিছু করতে পারবেন।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/cp.png)

**শিক্ষণীয় রিসোর্স****:**

- [Cappuccino Casts](http://suitmymind.com/blog/category/cappuccino-casts/)
- [Building rich web application in Objective-J](http://www.nice-panorama.com/Programmation/cappuccino/)
- [Learning Objective-J](http://cappuccino.org/learn/tutorials/objective-j-tutorial.php)

## [**JavaScriptMVC**](http://javascriptmvc.com/)

[**JavaScriptMVC**](http://javascriptmvc.com/) এটা মূলত জেকুয়েরী দিয়ে লেখা। এটা ওয়েবসাইটের ফ্রন্ট এন্ড এর কাজের জন্য একটা পারফেক্ট ফ্রেমওয়ার্ক। এটা ডেভলপ করা হয় ২০০৮ সালে। MVC আর্কিটেকচারের একটা ফ্রেমওয়ার্ক। ফ্রেমওয়ার্কটি কোড জেনারেটর, টেস্টিং এবং ডিপেন্ডেন্সি ম্যানেজমেন্ট ফিচারসহ সব ধরনের কাজের জন্য বেশ ভাল।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/3.png)

**শিক্ষণীয় রিসোর্স****:**

- [JavaScriptMVC Documentation](http://javascriptmvc.com/docs.html)
- [Quick Overview of JavaScriptMVC](https://gist.github.com/989117)

## [**Asana Luna**](https://asana.com/luna/)

[**Luna**](https://asana.com/luna/) একটা বেশ ভাল প্রাইভেট ফ্রেমওয়ার্ক এবং বেশ হইচই ফেলা একটা ফ্রেমওয়ার্ক। এটা দিয়ে আপনি কেসিং, রাউটিং, অথেনটিকেশন সহ আরও অনেক কাজ করতে পারবেন। এটাও একটা MVC ফ্রেমওয়ার্ক।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/4.png)

**শিক্ষণীয় রিসোর্স****:**

- [HackerNews Discussion](http://news.ycombinator.com/item?id=2191800)
- [Quora Discussion](https://www.quora.com/Web-Application-Frameworks/What-is-Asanas-Luna-technology-framework)

## [**Backbone.js**](https://documentcloud.github.com/backbone/)

[**Backbone.js**](https://documentcloud.github.com/backbone/) মূলত জাভাস্ক্রিপ্ট দিয়ে অনেক বড় বড় ও ভারী অ্যাপ্লিকেমন লেখার কাজে ইউজ হয়। এটা দিয়ে আপনি একটা সাইটের ব্যাক এন্ড ও ফ্রন্ট এন্ড উভয় ধরনের কাজই করতে পারবেন। এটার মাধ্যমে আপনি কী ভ্যালু দিয়ে কাষ্টম ইভেন্ট বাইন্ড করতে পারবেন। এটার একটা অনেক বড় API ডকুমেন্টেশন রয়েছে।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/5.png)

**শিক্ষণীয় রিসোর্স****:**

- [Getting Started with Backbone.js](http://net.tutsplus.com/tutorials/javascript-ajax/getting-started-with-backbone-js/)
- [Hello Backbone.js](http://arturadib.com/hello-backbonejs/)
- [Backbone.js Tips : Lessons from the trenches](http://devblog.supportbee.com/2011/07/29/backbone-js-tips-lessons-from-the-trenches/)

## [**qooxdoo**](http://qooxdoo.org/)

[qooxdoo](http://qooxdoo.org/) একটা ইউনিভার্সাল জাভাস্ক্রিপ্ট ফ্রেমওয়ার্ক এবং এটা বহু প্লাটফর্মে আপনাকে এপ্লিকেশন তৈরী করা সুযোগ করে দিবে। এটার অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিং এর মাধ্যমে আপনি অনেব বড় ও ইন্টারএকটিভ অ্যাপ্লিকেশনগুলো তৈরী করতে পারবেন। এটা দিয়ে আপনি মোবাইল ডিভাইসের জন্য বা ছোটখাট ট্রেডিশনাল ওয়েব অ্যাপ তেকে শুরু করে এমন অ্যাপও তৈরী করতে পারবেন যেগুলো ব্রাউজারের বাইরেও রান করা সম্ভব।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/6.png)

**শিক্ষণীয় রিসোর্স****:**

- [A Developer Looks at the qooxdoo 1.4 JavaScript Framework](http://www.htmlgoodies.com/beyond/javascript/a-developer-looks-at-the-qooxdoo-1.4-javascript-framework.html)
- [Working with Qooxdoo and PHP](http://greg.chiaraquartet.net/working-with-qooxdoo-and-php)

## [**Spine**](https://maccman.github.com/spine/)

Spine হল লাইট ওয়েট ফ্রেমওয়ার্ক যেটা আপনাকে সব ধরনের জাভাস্ক্রিপ্ট অ্যাপ্লিকেশন তৈরী সম্ভব। এটা একটা MVC ফ্রেমওয়ার্ক এবং এটার মাধ্যমে আপনি অসাম সব ওয়েব অ্যাপ্লিকেশন তৈরী করতে পারবেন।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/7.png)

**শিক্ষণীয় রিসোর্স****:**

- [Building JavaScript Web Apps With MVC & Spine.js](http://addyosmani.com/blog/building-apps-spinejs/)
- [Meet Spine.JS](http://kazimanzurrashid.com/posts/meet-spine-dot-js-my-framework-of-choice-for-client-side-mvc-part-1)

## [**ActiveJS**](http://www.activejs.org/)

[**ActiveJS**](http://www.activejs.org/) হল এমন একটা ফ্রেমওয়ার্ক যেটা লোকাল এবং রেস্ট বেসড ডাটা মডেলিং এবং পিওর DOM ভিউ কনস্ট্রাকশন এর জন্য ইউজ হয়। এটা এক্সটারনাল ডিপেডেন্সি মুক্ত একটা ফ্রেমওয়ার্ক।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/8.png)

**শিক্ষণীয় রিসোর্স****:**

- [Example of a Simple View in Action](http://activejs.org/samples/simple_view.html)
- [Github Repo](https://github.com/aptana/activejs)

## [**Eyeballs**](https://github.com/paulca/eyeballs.js)

[**Eyeballs**](https://github.com/paulca/eyeballs.js) একটা স্লিম জাভাস্ক্রিপ্ট ফ্রেমওয়ার্ক এবং এটা জাভাস্ক্রিপ্ট এর ফ্রেমওয়ার্কের ভেতর বেশ উপরের দিকেই রয়েছে। এটা ভাল ও বড় মাপের অ্যাপ্লিকেশন ডেভলপমেন্টের জন্য বেশ ভাল। এটা স্ট্যান্ডএ্যলোন জাভাস্ক্রিপ্ট অ্যাপস গুলো তৈরীর জন্য পারফেক্ট যেগুলো HTML দিয়ে তৈরী এবং CouchDB টাইপের ডাটাবেস দিয়ে সাপোর্ট দেওয়া।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/9.png)

**শিক্ষণীয় রিসোর্স****:**

- [Github repo](https://github.com/paulca/eyeballs.js)
- [HackerNews Discussion](http://news.ycombinator.com/item?id=2981159)

## [**Sammy**](http://sammyjs.org/)

[**Sammy**](http://sammyjs.org/) একটা ছোটখাট ফ্রেমওয়ার্ক যেটা হালকা ওয়েব অ্যাপ তৈরীর জন্য ভাল এবং এটা জাভাস্ক্রিপ্ট অ্যাপ্লিকেশন গুলোর জন্য একটা বেসিক স্ট্রাকচার তৈরী করতে পারে। এটা খুব ছোট একটা কোর নিয়ে বিভিন্ প্লাগিন এর সাহায্যে বিভিন্ন স্পেসিফিক ফাংশনালিটি প্রোভাইড করে থাকে।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/10.png)

**শিক্ষণীয় রিসোর্স****:**

- [Introduction to Sammy.js](http://net.tutsplus.com/tutorials/javascript-ajax/quick-tip-an-introduction-to-sammy-js/)

## [**Choco**](https://github.com/ahe/choco)

[**Choco**](https://github.com/ahe/choco) এর একটা বিরাট সাফল্য হল MVC কে ক্লায়েন্ট সাইডে নিয়ে আসা। এটার অ্যাপগুলো মূলত HTML পেজ এর সাথে তৈরী করা হয় এবং এটার ব্যাক এন্ড এর কাজ করা হয়ে থাকে জাভাস্ক্রিপ্ট দিয়ে। এটার মাধ্যমে ডেভলপিং এর সময় আপনাকে শুধুমাত্র HTML এবং CSS ইউজ করতে হবে।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/choco.png)

**শিক্ষণীয় রিসোর্স****:**

- [Github Repo](https://github.com/ahe/choco)

## [**Agility**](http://agilityjs.com/)

[**Agility**](http://agilityjs.com/)  একটা জাভাস্ক্রিপ্ট এর MVC লাইব্রেরী এবং এটা আপনাকে মেইনটেইনএবল এবং রিইউজেবল ওয়েব তৈরীর সুযোগ করে দেয়। এটার মেন লক্ষ হল ওয়েব অ্যাপগুলো যত কম সময়ের ভেতর লিখে ফেলা এবং এটার লং টার্ম মেইটেইন্স MVC এর মাধ্যমে সহজ ও দ্রুত করা।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/12.png)

**শিক্ষণীয় রিসোর্স****:**

- [HackerNews Discussion](http://news.ycombinator.com/item?id=2793634)
- [JSBin Playground](http://jsbin.com/agility/edit#javascript, html, live)
- [Github Repo](https://github.com/arturadib/agility)

## [**Angular**](http://angularjs.org/#/)

[**Angular**](http://angularjs.org/#/) আপনাকে পুরোপুরি একটা ফুল ডেভলপমেন্ট এনভায়রনমেন্ট প্রোভাইড করে, আপনার ওয়েব অ্যাপসের জন্য একটা ভাল স্ট্রাকচারও তৈরী করে। এটা সব ভাল জাভাস্ক্রিপ্ট লাইব্রেরী গুলোর সাথে কাজ করতে পারে। এটা ডিরেক্ট HTML এর ট্যাগের বেতর লেখা যায় এবং এটা অনেক ছোট ও ফাস্ট। এটার সাইজ মাত্র ৬০ কিলোবাইট।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/13.png)

**শিক্ষণীয় রিসোর্স****:**

- [Quora Discussion](https://www.quora.com/JavaScript/How-do-Angular-js-and-Backbone-js-compare)
- [Github repo](https://github.com/angular/angular.js)
- [angular: A Radically Different Way of Building AJAX Apps](http://misko.hevery.com/2010/07/29/a-radically-different-way-of-building-ajax-apps/)

## [**ExtJS**](http://www.sencha.com/products/extjs/)

[**ExtJS**](http://www.sencha.com/products/extjs/) ক্লায়েন্ট সাইড অ্যাপ ডেভলপিং এর ক্ষেত্রে একটা সম্পূর্ণ নতুনরাস্তা তৈরী করেছে। এটা মূলত একটা MVC ফ্রেমওয়ার্ক। এটা আলাদা ভাবে ডাটা ম্যানেজমেন্ট, লজিক ইসপ্লিমেন্ট ও ইন্টারফেস ডিজাইনের কাজ করার সুযোগ দেয়। এটা বড় একটা ডেভলপমেন্ট টীমকে একসাথে কাজ করার একটা সুযোগ করে দিয়েছে এবং এক্ষেত্রে ডেভলপারদের অন্যদের কাজ সম্পর্কে কোন চিন্তা ভাবনা করা লাগে না।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/14.png)

**শিক্ষণীয় রিসোর্স****:**

- [What's New in Ext Js 4](http://www.sencha.com/products/extjs/whats-new-in-ext-js-4/)
- [Migrating from Ext JS 3 to 4](http://www.sencha.com/forum/showthread.php?132530-ExtJS-3-to-ExtJS-4-MVC)

## [**Knockout**](http://knockoutjs.com/)

[**Knockout**](http://knockoutjs.com/) এমন একটা লাইব্রেরী যেটা দিয়ে আপনি বড় মাপের রেসপন্সিভ ডিসপ্লে এবং এডিটর, ইউজার ইন্টারফেস সহ ক্লিন ডাটা মডেলের সব অ্যাপ তৈরী করতে পারবেন। আপনি এটার মাধ্যমে খুব সহজেই ডাইনামিক কনটেন্ট তৈরী করতে পারবেন।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/15.png)

**শিক্ষণীয় রিসোর্স****:**

- [Into the Ring with knockout.js](http://net.tutsplus.com/tutorials/javascript-ajax/into-the-ring-with-knockout-js/)
- [Creating Rich Interactive Web Apps With KnockoutJS](http://blog.monnet-usa.com/?p=354)
- [Build Dynamic Pages with Knockout.js](http://thinkvitamin.com/code/javascript/build-dynamic-pages-with-knockout-js/)

## [**Jamal**](http://jamal-mvc.com/)

[**Jamal**](http://jamal-mvc.com/) হল ছোটখাট একটা জাভাস্ক্রিপ্ট ফ্রেমওয়ার্ক। এটা আপনাকে আপপনার ওয়েব এ্যপ এর HTML, CSS ও JAVASCRIPT ফাইল গুলো সম্পূর্ণ আলাদাভাবে ম্যানেজমেন্ট এর ক্ষেত্রে অনেক বড় একটা সুবিধা দেয়। এটা মূলত জেকুয়েরী দিয়ে লেখা এবং MVC ফ্রেমওয়ার্ক।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/16.png)

**শিক্ষণীয় রিসোর্স****:**

- [Github](https://github.com/adcloud/jamal/)
- [Integration Examples](http://jamal-mvc.com/wiki/IntegrationExamples)

## [**PureMVC**](http://puremvc.org/)

[**PureMVC**](http://puremvc.org/) একটা লাইটওয়েট ফ্রেমওয়ার্ক যেটা মডেল ভিউ ও কন্ট্রোলার বেসড অ্যাপ ডেভলপমেন্ট এর জন্য ভুবই ভাল। এটা একটা ওপেনসোর্স ফ্রেমওয়ার্ক এটা মূলত ActionScript 3 ল্যাংগুয়েজ থেকে ইমপ্লিলমেন্টেড এবং এ্যডোবি ফ্লেক্স ফ্লাস ও এয়ার নিয়ে কাজ করার জন্য তৈরী করা।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/17.jpg)

**শিক্ষণীয় রিসোর্স****:**

- [Understanding the PureMVC Open Source Framework](http://active.tutsplus.com/tutorials/workflow/understanding-the-puremvc-open-source-framework/)
- [PureMVC Best Practices](http://puremvc.org/component/option, com_wrapper/Itemid, 174/)

## [**TrimJunction**](https://code.google.com/p/trimpath/wiki/TrimJunction)

[**TrimJunction**](https://code.google.com/p/trimpath/wiki/TrimJunction) একটা ওপেনসোর্স ফ্রেমওয়ার্ক এবং MVC ফ্রেমওয়ার্ক। এটা মূলত একটা পোর্ট বা জংশন যেটা রুবি অন রেইলস এর বিভিন্ন বৈশিষ্ঠ ও কাজকে জাভাস্ক্রিপ্ট এর মাধ্যমে করার একটা সুযোগ করে দিয়েছে।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/18.png)

**শিক্ষণীয় রিসোর্স****:**

- [Google Code](https://code.google.com/p/trimpath/wiki/TrimJunction)

## [**CorMVC**](http://www.bennadel.com/projects/cormvc-jquery-framework.htm)

[**CorMVC**](http://www.bennadel.com/projects/cormvc-jquery-framework.htm) হল জেকুয়েরী দিয়ে তৈরী করা একটা MVC ফ্রেমওয়ার্ক যেটা সিঙ্গেল পেজ এর

ওয়েব বেসড অ্যাপ্লিকেশন তৈরীর জন্য ইউজ করা হয়ে থাকে। এটার ফুল মিনিং হল **client-only-required model-view-controller** **‌** এবং এটা এমনভাবে তৈরী করা যাতে করে খুব কম সময়ের ভেতর এটা শিখে যে কেউ সিঙ্গেল পেজ অ্যাপ্লিকেশন তৈরী করতে পারে।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/19.png)

**শিক্ষণীয় রিসোর্স****:**

- [corMVC: An jQuery-based MVC Framework](http://javascriptly.com/2009/12/coremvc-an-jquery-based-mvc-framework/)
- [Online demo](http://www.bennadel.com/resources/projects/cormvc/demo/index.htm)

## [**batman**](http://batmanjs.org/)

[**batman**](http://batmanjs.org/) হল ফুল স্টাক মাইক্রোফ্রেমওয়ার্ক যেটা রিয়েল ইউজের জন্য তৈরী এবং ডেভলপার এবং ডিজাইনারের মনমত করে তৈরী করা।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/367903/20.png)

**শিক্ষণীয় রিসোর্স****:**

- [How Batman can Help you Build Apps](http://www.shopify.com/technology/4080092-how-batman-can-help-you-build-apps)
- [HackerNews discussion](http://news.ycombinator.com/item?id=3014434)
- [Github](https://github.com/Shopify/batman)

## শেষকথা

আমরা জাভাস্ক্রিপ্ট এর অনেকগুলো ফ্রেমওয়ার্ক নিয়েই আলোচনা করলাম। এগুলোর মাধ্যমে আপনারা বিভিন্ন ফ্রেমওয়ার্কের কাজ এবং এদের ভেতর বেসিক পার্থক্যগুলো নিশ্চই খুঁজে বের করতে পেরেছেন। আর এই বিভিন্ন ফ্রেমওয়ার্কগুলো বিভিন্ন ধরনের কাজের জন্য ইউজ হয়ে থাকে।

আর এই ফ্রেমওয়ার্কগুলো সম্পর্কে আরও কিছূ জানতে চাইলে বা আপনার কোন কনফিউশন থাকলে টিউমেন্ট করতে ভুলবেন না। আজ এই পর্যন্তই। সবাই ভাল থাকবেন। ধন্যবাদ।
