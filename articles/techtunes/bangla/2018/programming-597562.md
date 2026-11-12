---
archive_id: techtunes-597562
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 597562
title: 'বাংলায় PHP Laravel Framework [পর্ব-০৫] :: Laravel Controller'
slug: programming-597562
language: bn
status: publish
published_at: '2018-09-07T04:00:00+00:00'
modified_at: '2018-09-07T04:41:00+00:00'
original_url: https://www.techtunes.io/programming/tune-id/597562
author: ফজলে রাব্বি
author_url: https://www.techtunes.io/tuner/rabbiit
categories:
- প্রোগ্রামিং
tags:
- bangla laravel 5 tutorial
content_hash: f4b3911da7ac95c9d960c5963cee5240b49e293f8871df6bbc559f31e5f8c207
archived_at: '2026-11-12T12:30:04.327026+00:00'
---

### [বাংলায় PHP Laravel Framework](https://www.techtunes.io/chain-tunes/php-laravel-framework-in-bangla "বাংলায় PHP Laravel Framework")

- [বাংলায় PHP Laravel Framework [পর্ব-০১] :: Laravel পরিচিতি](https://www.techtunes.io/programming/tune-id/594968 "বাংলায় PHP Laravel Framework [পর্ব-০১] :: Laravel পরিচিতি")
- [বাংলায় PHP Laravel Framework [পর্ব-০২] :: Laravel Project তৈরি](https://www.techtunes.io/programming/tune-id/595339 "বাংলায় PHP Laravel Framework [পর্ব-০২] :: Laravel Project তৈরি")
- [বাংলায় PHP Laravel Framework [পর্ব-০৩] :: Laravel Project পরিচিতি](https://www.techtunes.io/programming/tune-id/597110 "বাংলায় PHP Laravel Framework [পর্ব-০৩] :: Laravel Project পরিচিতি")
- [বাংলায় PHP Laravel Framework [পর্ব-০৪] :: Laravel Basic Route পরিচিতি](https://www.techtunes.io/programming/tune-id/597185 "বাংলায় PHP Laravel Framework [পর্ব-০৪] :: Laravel Basic Route পরিচিতি")
- বাংলায় PHP Laravel Framework [পর্ব-০৫] :: Laravel Controller

আশাকরি সবাই আছেন। বাংলায় PHP Laravel Framework টিউটোরিয়াল পর্ব ৫ আবারও চলে আসলাম। যারা এখনও আগের পর্ব গুলো দেখেন নাই তারা উপরের এর লিংক গুলো থেকে ঘুড়ে আসলে এই পর্ব টা বুজতে সুবিধা হবে। আর কথা না বাড়িয়ে Laravel Controller কি ভাবে কাজ করে বা কি ভাবে আপনি Controller এ কাজ করবেন চলুন জেনে নেওয়া যাক।

MVC framework মধ্যে অক্ষর 'C' কন্ট্রোলার জন্য দাঁড়িয়েছে। এটি Views  এবং Models গুলির মধ্যে একটি নির্দেশক ট্র্যাফিক হিসাবে কাজ করে।

আপনি ব্যবহার করছেন কোন অপারেটিং সিস্টেম তার উপর ভিত্তি করে কমান্ড প্রম্পট বা টার্মিনাল খুলুন এবং Artisan CLI (কমান্ড লাইন ইন্টারফেস) ব্যবহার করে Controller তৈরি করতে নিম্নলিখিত কমান্ড টাইপ করুন।

```
php artisan make:controller <controller-name>
```

### Syntax

```
Route::get(‘base URI’, ’controller@method’);
```

উদাহরন: UserController তৈরি করতে নিম্নলিখিত কমান্ডটি চালান

```
php artisan make:controller UserController
```

Controller successful তৈরির পর এটি নিচের লোকেশনে পাবেন

```
app/Http/Controller/UserController.php
```

```
<?php
namespace App\Http\Controllers;
use Illuminate\Http\Request;
use App\Http\Requests;
use App\Http\Controllers\Controller;
class UserController extends Controller {//}?>
```

এরকম ভাবে পাবেন।

এখন User Controller  function তৈরি করে আমাদের কাজ করতে হবে। এবং function টি রাউটের মাধ্যমে ভিউ একসেস করতে হবে।

practical কাজটি ভিডিও  তে দেখুন

[Embedded External Content: https://www.youtube.com/embed/YCDTzx9\_QDM?feature=oembed]

আজ এ পর্যন্তই ভাল লাগলে জানাবেন। আপর পরের পর্ব পর্যন্ত সাথে থাকবেন।

আল্লাহ হাফেজ।
