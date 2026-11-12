---
archive_id: techtunes-1006349
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 1006349
title: 'কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০৪] :: আরও স্বচ্ছ
  Error Handling'
slug: programming-1006349
language: bn
status: publish
published_at: '2025-09-03T02:55:00+00:00'
modified_at: '2025-09-03T07:21:00+00:00'
original_url: https://www.techtunes.io/programming/tune-id/1006349
author: সোহানুর রহমান
author_url: https://www.techtunes.io/tuner/sohanur-raihan
categories:
- প্রোগ্রামিং
tags: []
content_hash: e1617dae068c33f82eca1f81bb0205f9d5a63594ad6dd639fae66f9dcc9d024c
archived_at: '2026-11-12T11:49:37.410651+00:00'
---

### [PHP 8.5! নতুন ফিচার](https://www.techtunes.io/chain-tunes/php-8-5-new-features "PHP 8.5! নতুন ফিচার")

- [কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০১] :: পাইপ Operator](https://www.techtunes.io/programming/tune-id/1005969 "কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০১] :: পাইপ Operator")
- [কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০২] :: Curl-এর নতুন Function](https://www.techtunes.io/programming/tune-id/1005989 "কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০২] :: Curl-এর নতুন Function")
- [কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০৩] :: PHP BUILD DATE Constant](https://www.techtunes.io/programming/tune-id/1005990 "কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০৩] :: PHP BUILD DATE Constant")
- কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে! [পর্ব-০৪] :: আরও স্বচ্ছ Error Handling

PHP তে আমাদের Application-এর Robustness নিশ্চিত করার জন্য রয়েছে Error এবং Exception Handling-এর জন্য শক্তিশালী Mechanism। আপনি Custom Handlers সেট করতে পারেন, যা PHP কোনো Error Trigger করলে বা কোনো Exception Uncaught থাকলে Called হবে। কিন্তু, যদি আপনার কোড বিভিন্ন Libraries বা Frameworks ব্যবহার করে, তবে একটি Handler দ্বারা অন্য Handler-কে Override করা অস্বাভাবিক নয়। PHP 8.5 পর্যন্ত, বর্তমানে কোন Handler Active আছে তা সরাসরি জানার কোনো Built-In উপায় ছিল না, যা Debugging এবং Complex Application-এর Layered Error Handling-এ সমস্যা সৃষ্টি করতো। এই গ্যাপ পূরণ করতে PHP 8.5 দুটি নতুন Function যোগ করেছে: **`get_error_handler`** এবং **`get_exception_handler`**।

## `get_exception_handler` এবং `get_error_handler` Functions - Error Handling হবে আরও স্বচ্ছ!

![কোডিং জগৎ কাঁপাতে আসছে PHP 8.5! নতুন ফিচার কী কী থাকছে!](https://dnc.techtunes.io/tDrive/tuner/2025/08/techtunes_7e40d06f9358f1d0d6c7b35d24951ca8.jpg)

### কেন এটি গুরুত্বপূর্ণ?

`set_error_handler()` এবং `set_exception_handler()` Functions পূর্ববর্তী Handler-কে Return করে। কিন্তু এই Return Value-টি শুধুমাত্র সেই Call-এর জন্য প্রযোজ্য ছিল। ধরুন, আপনার Application একটি Third-Party Library ব্যবহার করে যা তার নিজস্ব Error Handler সেট করে (যেমন একটি Logging Library)। এরপর আপনি আপনার কোডে Temporarily একটি Custom Handler সেট করলেন শুধুমাত্র একটি নির্দিষ্ট Task-এর জন্য, এবং সেই Task শেষ হওয়ার পর পূর্ববর্তী Handler-কে Restore করতে চান। এই নতুন Functions আপনাকে যেকোনো সময় জানতে দেবে বর্তমানে কোন Handler Active আছে, যা আপনাকে সঠিক Handler-কে Restore করতে বা Current Handler-এর সাথে Adjust করতে সাহায্য করবে। এটি বিশেষ করে Dynamic Error Handling Scenarios-এর জন্য খুবই কার্যকর, যেখানে আপনি Error Handling Behavior-কে Run-Time-এ Modify করতে চান।

## নতুন `get_error_handler` Function

```
function get_error_handler():?callable {}
```

- যদি কোনো Custom Error Handler সেট না থাকে (অর্থাৎ Default PHP Error Handling Active থাকে), এটি `null` Return করে।
- যদি একটি Custom Handler সেট করা থাকে, এটি সেই `Callable` Return করে (যেমন, Function Name String, Array for Class Method, বা Closure Object)।

```
var_dump(get_error_handler()); // আউটপুট: null (যদি কোনো Handler সেট না থাকে)

// একটি কাস্টম Error Handler সেট করা হলো
set_error_handler(function($errno, $errstr, $errfile, $errline) {echo "Custom Error Handler Activated!\n" // এই handler কিছু করে না বা শুধু Log করে return true; // true রিটার্ন করলে PHP এর Default Error Handler কল হবে না});

var_dump(get_error_handler()); // আউটপুট: Closure Object এর তথ্য দেখাবে

restore_error_handler(); // কাস্টম handler সরিয়ে আগেরটা পুনরুদ্ধার করা হলো

var_dump(get_error_handler()); // আউটপুট: null (যদি আগেরটি null হয়)
```

## নতুন `get_exception_handler` Function:

`get_exception_handler` Function-টিও `get_error_handler`-এর মতোই কাজ করে, তবে এটি Exception Handler-এর জন্য:

```
function get_exception_handler():?callable {}
```

- যদি কোনো Exception Handler সেট না থাকে, এটি `null` Return করে।
- যদি একটি Custom Handler সেট করা থাকে, এটি সেই `Callable` Return করে।

```
var_dump(get_exception_handler()); // আউটপুট: null (যদি কোনো Handler সেট না থাকে)

// একটি কাস্টম Exception Handler সেট করা হলো
set_exception_handler('my_exception_logger');

function my_exception_logger(Throwable $e): void {echo "Caught an exception: ". $e-&amp;gt;getMessage(). "\n"}

var_dump(get_exception_handler()); // আউটপুট: 'my_exception_logger' String দেখাবে

restore_exception_handler(); // কাস্টম handler সরিয়ে আগেরটা পুনরুদ্ধার করা হলো

var_dump(get_exception_handler()); // আউটপুট: null (যদি আগেরটি null হয়)
```

## PHP Polyfill (পুরোনো PHP Versions-এর জন্য)

PHP-এর এই নতুন Functions-কে আগের Versions-এর জন্য Polyfill করা তুলনামূলকভাবে সহজ, কারণ `set_error_handler()` এবং `set_exception_handler()` নিজেই পূর্ববর্তী Handler-কে Return করে। এই Polyfill গুলি `function_exists()` চেক ব্যবহার করে নিশ্চিত করে যে Function-টি ইতিমধ্যেই Declared না থাকলে তবেই Define করা হবে।

```
if (!function_exists('get_error_handler')) {function get_error_handler():?callable {$handler = set_error_handler(null); // বর্তমান handler নিয়ে এসে null সেট করে restore_error_handler(); // আগের handler পুনরুদ্ধার করে

return $handler;}

if (!function_exists('get_exception_handler')) {function get_exception_handler():?callable {$handler = set_exception_handler(null); // বর্তমান handler নিয়ে এসে null সেট করে restore_exception_handler(); // আগের handler পুনরুদ্ধার করে return $handler;}
```

## Backward Compatibility Impact

`get_error_handler` এবং `get_exception_handler` নতুন Functions। যদি আপনার Application-এর Global Namespace-এ একই নামে কোনো Function Declared না থাকে, তবে কোনো Backward Compatibility Issue হবে না। Polyfill-এর মাধ্যমে পুরোনো Versions-এও এটি ব্যবহার করা যাবে, যা আপনাকে Smooth Transition-এর সুবিধা দেবে। এটি Error এবং Exception Handling Behavior-কে Trace করা এবং Management করাকে আরও শক্তিশালী করে তুলবে।

এই পর্বে আমরা আলোচনা করলাম PHP এর নতুন `get_exception_handler` এবং `get_error_handler` Functions নিয়ে, আগামী পর্বে PHP 8.5 এর আরেকটি নতুন ফিচার নিয়ে আলোচনা করবো।
