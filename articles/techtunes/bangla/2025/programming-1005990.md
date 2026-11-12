---
archive_id: techtunes-1005990
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 1005990
title: 'কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০৩] :: PHP BUILD
  DATE Constant'
slug: programming-1005990
language: bn
status: publish
published_at: '2025-09-03T02:17:00+00:00'
modified_at: '2025-09-03T02:17:00+00:00'
original_url: https://www.techtunes.io/programming/tune-id/1005990
author: সোহানুর রহমান
author_url: https://www.techtunes.io/tuner/sohanur-raihan
categories:
- প্রোগ্রামিং
tags: []
content_hash: 4b260ad79beab1e4828515b89a89b4597b212699503b2226a80561356f463d93
archived_at: '2026-11-12T11:50:15.026129+00:00'
---

### [PHP 8.5! নতুন ফিচার](https://www.techtunes.io/chain-tunes/php-8-5-new-features "PHP 8.5! নতুন ফিচার")

- [কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০১] :: পাইপ Operator](https://www.techtunes.io/programming/tune-id/1005969 "কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০১] :: পাইপ Operator")
- [কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০২] :: Curl-এর নতুন Function](https://www.techtunes.io/programming/tune-id/1005989 "কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০২] :: Curl-এর নতুন Function")
- কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০৩] :: PHP BUILD DATE Constant
- [কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০৪] :: আরও স্বচ্ছ Error Handling](https://www.techtunes.io/programming/tune-id/1006349 "কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০৪] :: আরও স্বচ্ছ Error Handling")

আপনি কি কখনও জানতে চেয়েছেন আপনার PHP Binary টি ঠিক কোন দিন Built হয়েছিল? Debugging, Environment Setup Verification, বা Security Audits-এর জন্য এই তথ্যটি খুবই মূল্যবান হতে পারে। এটি আপনাকে জানতে সাহায্য করে যে আপনার PHP Installation কতটা আপডেটেড, কোন Version-এর Build-টি আপনি ব্যবহার করছেন, যা Troubleshooting-এর সময় খুবই দরকারি। PHP 8.5 এই কাজটি খুব সহজ করে দিচ্ছে নতুন Global Constant **`PHP_BUILD_DATE`** যোগ করে। এটি PHP Binary তৈরি হওয়ার সময় এবং তারিখ ধারণ করে।

## `PHP_BUILD_DATE` Constant - আপনার PHP Binary-এর জন্ম-পরিচয়!

![কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে!](https://dnc.techtunes.io/tDrive/tuner/2025/08/techtunes_b0c3f0d4fd02f0f3d4b4ff3b2fb90be0.jpg)

## কেন এটি দরকারি ছিল?

আগে, `PHP_VERSION` এবং `PHP_VERSION_ID`-এর মতো Constants থাকলেও, Build Date/Time শুধুমাত্র `phpinfo()` Function থেকে পাওয়া যেত। `phpinfo()` Function সরাসরি Standard Output-এ (CLI-তে Plain-Text বা Web-এ HTML Format-এ) Text Print করে, তাই এই তথ্য Programmatically ভাবে Access করা এবং Parse করা ছিল বেশ Unwieldy এবং সময়সাপেক্ষ। উদাহরণস্বরূপ, যদি আপনি একটি Monitoring Script চালান যা স্বয়ংক্রিয়ভাবে PHP Build Date চেক করবে, তবে `phpinfo()` Output Parse করাটা একটা জটিল Regular Expression লেখার কাজ ছিল। এখন, `PHP_BUILD_DATE` Constant-এর মাধ্যমে এটি সরাসরি এবং সহজে Accessible, যা Automation Script-এর জন্য খুবই কার্যকর।

### উদাহরণ:

```
echo "আমার PHP Binary Built হয়েছিল: ". PHP_BUILD_DATE;
// আউটপুট হতে পারে: আমার PHP Binary Built হয়েছিল: Sep 3 2025 10:44:26
```

### Date এবং Time Format

`PHP_BUILD_DATE` Constant-এর মান PHP-এর `M j Y H:i:s` Format-এ থাকে। একটি ছোট Nuance হলো, মাসের তারিখ (`j`) যদি 10-এর কম হয়, তবে এটি Single Digit হিসাবে থাকে এবং Space-Prefixed হয় (যেমন, `Sep 3 2025` বনাম `Sep 12 2025`)। এই Format-টি `phpinfo()` Output-এর সাথে সামঞ্জস্যপূর্ণ।

এই Value-কে আপনি `DateTimeImmutable` Object-এ Parse করে আরও সহজে Manipulation করতে পারবেন:

```
$buildDateString = PHP_BUILD_DATE;
$dt = DateTimeImmutable::createFromFormat('M j Y H:i:s', $buildDateString);
if ($dt) {echo "Unix Timestamp: ". $dt-&gt;format('U'). "\n" echo "Formatted Date: ". $dt-&gt;format('Y-M-d'). "\n"} else {echo "Date Parsing Failed.\n"}
```

### Backward Compatibility Impact

এটি একটি সম্পূর্ণ নতুন Constant। যদি আপনার Application-এর Global Namespace-এ একই নামে কোনো Constant Declared না থাকে, তবে কোনো Backward Compatibility Issue হবে না। পুরোনো PHP Versions-এ এই তথ্য `phpinfo()` থেকে Regular Expression ব্যবহার করে Extract করা যেত, যেমনটি মূল আর্টিকেলে দেখানো হয়েছে। তবে নতুন Constant-টি এই কাজটি অনেক বেশি Cleaner এবং Reliable উপায়ে করে, যা Developer-দের জন্য একটি সহজলভ্য সুবিধা।

এই পর্বে আমরা আলোচনা করলাম PHP এর নতুন PHP\_BUILD\_DATE Constant, আগামী পর্বে PHP 8.5 এর আরেকটি নতুন ফিচার নিয়ে আলোচনা করবো।
