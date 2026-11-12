---
archive_id: techtunes-1005989
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 1005989
title: 'কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০২] :: Curl-এর
  নতুন Function'
slug: programming-1005989
language: bn
status: publish
published_at: '2025-08-20T12:40:00+00:00'
modified_at: '2025-08-20T15:27:00+00:00'
original_url: https://www.techtunes.io/programming/tune-id/1005989
author: সোহানুর রহমান
author_url: https://www.techtunes.io/tuner/sohanur-raihan
categories:
- প্রোগ্রামিং
tags: []
content_hash: 4c896b2ad452dd733f7c8ea1cf100cd232c01c9796868aa2253d70fea6d86319
archived_at: '2026-11-12T11:50:14.992735+00:00'
---

### [PHP 8.5! নতুন ফিচার](https://www.techtunes.io/chain-tunes/php-8-5-new-features "PHP 8.5! নতুন ফিচার")

- [কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০১] :: পাইপ Operator](https://www.techtunes.io/programming/tune-id/1005969 "কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০১] :: পাইপ Operator")
- কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০২] :: Curl-এর নতুন Function
- [কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০৩] :: PHP BUILD DATE Constant](https://www.techtunes.io/programming/tune-id/1005990 "কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০৩] :: PHP BUILD DATE Constant")
- [কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০৪] :: আরও স্বচ্ছ Error Handling](https://www.techtunes.io/programming/tune-id/1006349 "কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০৪] :: আরও স্বচ্ছ Error Handling")

যারা PHP দিয়ে Complex Network Operations বা Multiple HTTP Request একবারে Handle করেন, তাদের জন্য Curl Extension একটি অপরিহার্য Tool। এটি Asynchronous Request পাঠানোর একটি শক্তিশালী উপায়, যা Web Scraper, API Client এবং Microservices Communication-এর জন্য খুবই কার্যকর। PHP 8.5 সেই Tool-কে আরও শক্তিশালী করছে নতুন Function **`curl_multi_get_handles`** দিয়ে।

## Curl-এর জন্য নতুন বন্ধু: `curl_multi_get_handles` Function

![কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে!](https://dnc.techtunes.io/tDrive/tuner/2025/08/techtunes_e168d34c1b3d52175fb89d6d15b8a3b5.jpg)

এই Function-টি একটি `CurlMultiHandle` Object-এর সাথে যুক্ত সমস্ত `CurlHandle` Objects-এর একটি Array Return করে।

### কেন এটি এত দরকারি?

আগে, যখন আপনি `curl_multi_add_handle()` দিয়ে একটি `CurlMultiHandle`-এ একাধিক `CurlHandle` যোগ করতেন, তখন কোন `CurlHandle`-গুলো বর্তমানে `multi_handle`-এর সাথে যুক্ত আছে তা জানার কোনো সহজ উপায় ছিল না। ডেভেলপারদের সাধারণত একটি আলাদা Array বা `WeakMap` (যদি PHP 8.0+ ব্যবহার করেন) ব্যবহার করে তাদের `CurlHandle` Objects-এর List নিজেদেরই বজায় রাখতে হতো। এটি ছিল অতিরিক্ত Code, সম্ভাব্য Memory Leak (যদি `WeakMap` ব্যবহার না করা হয়) এবং Potential Bug-এর কারণ। `curl_multi_get_handles()` এই Manual Tracking-এর প্রয়োজনীয়তা দূর করে, আপনার Code-কে Simplified করে তোলে এবং এর Robustness বাড়ায়। `WeakMap` এখানে বিশেষভাবে উপযোগী কারণ এটি `CurlHandle` Objects-কে `reference` হিসাবে ধরে রাখে না, ফলে Object-টি প্রয়োজন না থাকলে স্বয়ংক্রিয়ভাবে Destroy হতে পারে, কিন্তু নতুন Function-টি আরও সরাসরি এবং Built-In উপায় প্রদান করে।

### উদাহরণ

```
$cm = curl_multi_init(); // একটি নতুন CurlMultiHandle তৈরি করা হলো
print_r(curl_multi_get_handles($cm)); // শুরুতে Empty Array দেখাবে, কারণ কোনো Handle যোগ করা হয়নি।
$ch1 = curl_init('https://example.com/foo'); // প্রথম CurlHandle তৈরি করা হলো
$ch2 = curl_init('https://example.com/bar'); // দ্বিতীয় CurlHandle তৈরি করা হলো
curl_multi_add_handle($cm, $ch1); // Handle গুলি MultiHandle এ যোগ করা হলো
curl_multi_add_handle($cm, $ch2);
print_r(curl_multi_get_handles($cm)); // এখন [$ch1, $ch2] এর মতো একটি Array দেখাবে, যেখানে যুক্ত Handle গুলো আছে।
```

### Function Synopsis

```
function curl_multi_get_handles(CurlMultiHandle $multi_handle): array {}
```

এই Function-টি Global Namespace-এ Declared এবং যদি `CurlMultiHandle`-এ কোনো `CurlHandle` Object যুক্ত না থাকে, তবে একটি Empty Array Return করে।

### Backward Compatibility Impact

এটি একটি সম্পূর্ণ নতুন সংযোজন, তাই আপনার Application-এ যদি ইতিমধ্যেই `curl_multi_get_handles` নামে কোনো User-Defined Function না থাকে, তবে কোনো Backward Compatibility Issue হবে না। `libcurl` 8.4 বা পরের Versions-এ একই নামের একটি `C Function` থাকলেও, PHP-এর Implementation সরাসরি সেই `libcurl` Function-এর উপর নির্ভরশীল নয়। এটি PHP-এর নিজস্ব Implementation। যদিও User-Land PHP ব্যবহার করে এটিকে সম্পূর্ণরূপে Polyfill করা কঠিন, `WeakMap` বা Array ব্যবহার করে এর কার্যকারিতা Mimic করা সম্ভব।

এই পর্বে আমরা আলোচনা করলাম PHP এর নতুন পাইপ `curl_multi_get_handles` Function, আগামী পর্বে PHP 8.5 এর আরেকটি নতুন ফিচার নিয়ে আলোচনা করবো।
