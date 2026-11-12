---
archive_id: techtunes-349719
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 349719
title: Laravel 5 এখন চলছে!! আসুন জেনে নিই নতুন কী কী আছে Laravel 5 এর ফিচারে
slug: programming-349719
language: bn
status: publish
published_at: '2015-05-14T21:15:00+00:00'
modified_at: '2015-05-14T21:15:00+00:00'
original_url: https://www.techtunes.io/programming/tune-id/349719
author: অরিন্দম পাল
author_url: https://www.techtunes.io/tuner/arindampaulripon
categories:
- প্রোগ্রামিং
tags:
- Laravel 5
- Laravel 5 New
- Laravel Tutorial
content_hash: 1f004a5c4a078c5da7d85ed4bdd88468e614955d32125fbb44c0e559a4ddb43f
archived_at: '2026-11-12T12:57:08.269113+00:00'
---

টেকটিউনরসের সবাইকে জানাই শুভেচ্ছা । আশা করি সবাই ভাল আছেন । আজ আমি আপনাদের সাথে PHP এর একটা খুবই লেটেস্ট ফ্রেমওয়ার্ক ল্যারাভেল নিয়ে কিছুটা আলোচনা করব । ল্যারাভেল হল PHP এর সবথেকে আপডেটেড ও সহজ এবং কার্যকরী একটা ফ্রেমওয়ার্ক যেটা বেশ কিছুদিন আগে রিলিজ হয়েছে। আর ইতিমধ্যেই ল্যারাভেল এর সবথেকে লেটেস্ট ভার্সন ৫.০.১ রিলিজ হয়েছে যেটা ছিল ল্যরাভেলের সবথেকে নতুন চমক ।

আর রিলিজ হবার সাথে সাথেই এটা ওয়েব ডেভলপমেন্ট এর জগতে ব্যাপকভাবে নাড়া ফেলতে পেরেছে এর সব নতুন ও আকর্ষণীয় ফিচার দ্বারা । আজ আমরা মূলত দেখব ল্যারাভেল ৪ ও ৫এর মধ্যে কিছু তুলনা এবং ল্যারাভেল ৫ এ নতুন যেসব ফিচার যুক্ত করা হয়েছে সেগুলো । তে চলুন , আর কথা বেশী না বাড়িয়ে কাজে যাওয়া যাক ।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/349719/fddf.png)

## **Directory Structure**

ল্যারাভেল ৫ এ সবথেকে যেটা বেশী চেঞ্জ হয়েছে সেটা হল ফ্রেমওয়ার্ক এর ফোল্ডার স্ট্রাকচার । ল্যারাভেল ৫ একটা সম্পূর্ণ PSR-4 অটোলোডিং স্ট্যান্ডার্ড এ ইমপ্লিমেন্ট করা হয়েছে , যেটার ফলে আপনার সবগুলো ক্লাস সম্পূর্ণ ভাবে নেমস্পেসড হয়ে যায় । এই নেমস্পেস জিনিস টা হল এমন কিছু , ধরুন আপনি একই নামের অনেকগুলো ক্লাস ইউজ করেছেন ।

এখন ল্যারাভের ৫ এ এই ক্লাসগুলো খুব সহজেই আপনি আলাদা করে ইউজ করতে পারবেন । আপনার ল্যারাভেল এ ডিফল্ট নেমস্পেস হল App , আর আপনি চাইলে এই নেমস্পেস চেঞ্জ করতে পারবেন php artisan app:name <your-app-name> কমান্ড দ্বারা ।এ্ই কমান্ডের সাথে ল্যারাভেল নিয়ে যারা হালকা পাতলা কাজ করেছেন তারা আশা করি পরিচিত । আপনি নতুন কেউ হয়ে থাকলে এটা জাস্ট দেখে স্কিপ করুন । পরে এই বিষয়ে বিস্তারিত আলোচনা করব ।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/349719/hQZwv.png)

ল্যারাভেল ৫ এ আপনার তৈরী বা লেখা মডেলগুলো app এর ভেতরেই থাকে এবং এটা app ফোল্ডারের ভেতরেই পাওয়া যায় । আপনার এ্যপ্লিকেশনের assets, views, ও language ফাইলগুলো রিসোর্স ফোল্ডারের ভেতর থাকে । vendor, public, ও bootstrap ল্যারাভেলএর আগের ভার্সনগুলোর মতই একই ফোল্ডারে রয়েছে ।

আপনি APP ফোল্ডারের ভেতর ঢুকলে অনেক ক্লাস দেখতে পাবেন যেগুলো হয়ত আপনার কাছে অনেক নতুন ও অচেনা লাগছে । এগুলো এখন স্কিপ করে যান । আমি পরে এই ক্লাস ও ফাইলগুলো নিয়ে ডিটেইলসে আলোচনা করব ।

## **Method Injection**

ল্যারাভেল ৫ এ মেথড ইনজেকশনটা ব্যাপক ভাবে সহজ করে দেওয়া হয়েছে । ভার্সন ৪.২পর্যন্ত আপনাকে মেথড ইনজেকশনের জন্য the Inversion of Control (IoC) নামের একটি কনটেইনার ক্লাস রিকুয়েস্ট করতে হত অথবা আপনাকে নিজে থেকেই একটা ক্লাস লিখতে হত ক্লাস ইনট্যান্স প্রোভাইড করার জন্য । আর এখন ল্যারাভেল ৫ এ আপনাকে জাস্ট ক্লাস ইনট্যান্স এর টাইপটা বলে দিতে হবে , তারপর ল্যারাভেল ৫ নিজে থেকেই এর একটা ডিফল্ট কন্ট্রোলার দ্বারা এটার বাদ বাকী কাজ করে নেবে ।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/349719/knowing-laravel-5-the-most-popular-php-framework-15-638.jpg)

আসলে মেথড ইনজেকশনটা ল্যারাভেল ৫ এর অনেক ডিপের একটা বিষয় । হয়ত অনেক্ই বুঝবেন না । তাই , জাস্ট এটা পড়ে যান । পরে সব বিষয়গুলো বুঝিয়ে বলা হবে ।

```
&lt;/pre&gt;
&lt;?php

// your class at &quot;app/Classes/your_class.php&quot;

namespace App\Classes

class YourClass

{

// your class implementation

}

// somewhere in one of your controller actions

public function myAction(\App\Classes\YourClass $MyObject)

{

// use $MyObject just like any other object

}

?&gt;
&lt;pre&gt;
```

## **Route Caching**

রাউট কেসিং জিনিসটা ল্যারাভেলের একটা নতুন ফিচার । এটা আপনার রাউট রেজিস্ট্রেশনকে অনেক সহজ ও দ্রুত করে দেয় । আসলে ল্যারাভেলে রাউট জিনিসটা হল এমন কিছু , আপনি যে সব ক্লাস বা যা কিছুই লিখেন , সেটা রাউটে গিয়ে রেজিস্ট্রেশন না করা পর্যন্ত কাজ করে না । এটার সাথে এনড্রয়েড ডেভলপমেন্টের কিছুটা মিল আছে । আপনি যখন কম সংখ্যক রাউট নিয়ে কাজ করবেন , তখন রাউট কেসিংটা আপনার তেমন একটা কাজে লাগবে না । কিন্তু বড় কোন কাজ করতে গেলে যেখানে অনেক রাউট নিয়ে আপনাকে কাজ করতে হয় , সেখানে রাউট কেসিং আপনার কাজকে অনেক সহজ করে দেবে ।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/349719/laravel-5-annotations-restful-api-routing-53-638.jpg)

রাউট কেসিং চালু ও বন্ধ করার জন্য php artisan route:cache  ও php artisan route:clear কমান্ড ইউজ করা হয় । আপনি যদি রাউট কেসিং অন করে দেন , তাহলে আপনি আপনার রাউট এডিট বা মোডিফাই করলেও সেগুলো কোন ইফেক্ট ফেলবে না ।

## **Route Middleware**

মিডল ও্য়্যানগুলো সাধারণত আপনার HTTP রাউটে একস্ট্রা লেয়ার এড করার জন্য ইউজ হয় । আপনি যদি প্রত্যেক রাউট অথবা কোন কোন স্পেসিফিক রাউট এর আগে কোন কোড এক্সিকিউট করাতে চান , তাহলে আপনাকে ল্যারাভেল ৫ এ জাস্ট নীচের মত একটা কোড লিখতে হবে । এই কোড দ্বারা আপনি অনেক কিছু ফিল্টার করে নিতে পারেন । ল্যারাভেল ৫ এ এটা ফিল্টার নামে পরিচিত ছিল । আর র‌ল্যারাভেল ৫ এ এটা হয়ে গিয়েছে মিডলওয়্যার ।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/349719/middleware.png)

ধরুন , আপনি আপনার ওয়েবসাইটে একটা রেঞ্জ থেকে আপপি ব্লক করে দিতে পান , সেক্ষেত্রে আপনাকে আগে একটা কন্ট্রোলার ক্লাস লিখতে হত । কিন্তু , এখন জাস্ট একটা মিডলওয়্যার ইউজ করেই আপনি এই কাজটা খুবই সহজে করে ফেলতে পারবেন । নীচের কোডটা একটা স্যাম্পল কোড মিডলওয়্যার এর জন্য ।

এর জন্য app/Http/Middleware/RegionMiddleware.php  তে গিয়ে php artisan make:middleware "RegionMiddleware". কমান্ড এর মাধ্যমে একটা মিডলওয়্যার ক্লাস তৈরী করলেই কাজ শেষ ।

```
&lt;/pre&gt;
&lt;?php

namespace app\Http\Middleware;

use Closure;

class RegionMiddleware {

/**

* Handle an incoming request.

*

* @param  \Illuminate\Http\Request  $request

* @param  \Closure  $next

* @return mixed

*/

public function handle($request, Closure $next)

{

// perform some IP logic on $request

// and redirect to appropriate

// page based on results

// everything went well

// this will resume normal flow

return $next($request);

}

}

?&gt;
```

## **Authentication**

অথেনটিকেশন সব ওয়েব এ্যাপ্লিকেশন এর একটা খুবই গুরুত্বপূর্ণ কাজ । এর জন্য ডেভলপাররা সাধারণত অনেক সময় ব্যায় করেন । কিন্তু ল্যারাভেল ৫ এ এটা কোন বিষয়ই না । আপনাকে এটার জন্য জাস্ট আপনার ডাটাবেস , মডেল , কন্ট্রোলার এবং ভিউগুলো জাস্ট কনফিগার করতে হবে । তারপর ল্যারাভেল এই কাজটা নিজে থেকেই করে নেবে ।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/349719/url.png)

## **Events**

আপনার এ্যাপ্লিকেশনের ইভেন্টগুলো স্ট্রিং আকারে লিখে কাজ করার দিন শেস করে দিয়েছে ল্যারাভেল ৫ । এখন আপনি ল্যারাভেল ৫ এ php artisan make:event <event-name> এই কোডটা লিখে যেকোন ইভেন্ট ক্রিয়েট করতে পারবেন এবং ইভেন্ট হ্যান্ডেলার অবজেক্ট php artisan handler:event <handler-name> কোডটা লিখে ক্রিয়েট করতে পারবেন । আপনার সব ইভেন্ট ও ইভেন্ট হ্যান্ডেলারগুলো app/Events এবং app/Handlers/Events ফোল্ডারে থাকবে । এটা ক্রিয়েট করার পর আপনি Event::fire(new Event(params))কমান্ড দ্বারা ইভেন্টগুলো ইউজ করতে পারবেন ।

## **Commands**

ল্যারাভেল ৫ এ আপনি বিভিন্ন বিজনেজ লজিক খুব সহজেই সিম্পল কমান্ডের মাধ্যমে করে ফেলতে পারবেন । ধরুন , আপনার একটা অনলাইন শপ রয়েছে এবং এটাতে ইউজারের ইমেইল ও ক্রেডিট কার্ড ভেরিফাই করার দরকার পড়ে । এখন , এর জন্য কন্ট্রোলার একশন লেখাটা খুবই ভাল একটা উপায় , কিন্তু যখন শুধুমাত্র কমান্ড লিখেই আপনি এই কাজটা করে ফেলতে পারছেন , তাহলে কেন আবার ঝামেলা বাড়াবেন ?

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/349719/laravel-5-in-depth-45-638.jpg)

## **Queue and Task Scheduling**

ল্যারাভেল ৫ এ আর একটা বিশেষ জিনিস হল এর ফ্রেমওয়ার্কের ভেতরই ডিফল্টভাবে queue অপশনটা দেওয়া আছে । ফলে এটার জন্য আপনাকে কোন থার্ড পার্টি প্যাকেজ ইউজ করার প্রয়োজন নেই । আপনাকে জাস্ট যেটা করতে হবে সেটা হল queue টাকে ভালভাবে কনফিগার করে নিতে হবে । তারপর এটা এর কাজ নিজে থেকেই করে নেবে । আপনার app/Commands ফোল্ডারের ভেতর queue সম্পর্কিত সবকিছু ই রয়েছে । একবার আপনি কোন queue কমান্ড ক্রিয়েট করলে Queue::push(new Command($params)) কমান্ডের মাধ্যমে ইউজ করতে পারবেন ।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/349719/queue-your-work-4-638.jpg)

ল্যারাভেল ৫ এ টাস্ক সিডিউলিং এও অনেক পরিবর্তন এসেছে । আপনাকে আগের ভার্সনগুলোতে প্রত্যেক কনসোল কমান্ডের জন্য একটা করে CROB সেট করতে হত । কিন্তু , এখন একটা সিঙ্গেল CRON এর মাধ্যমেই এটা করা সম্ভব ।

## **Multiple File Systems**

ল্যরাভেল ৫ বর্তমানে মাল্টিপল ফাইলসিস্টেম সাপোর্ট করে একং এটার জন্য ফাইলসিস্টেম নামের একটা থার্ডপার্টি প্যাকেচ এর দরকার হয় । আপনার এপ্লিকেশর যেকোন লোকাল বা ক্লাউড স্টোরেজ খুব সহজভাবে জাস্ট ফাইলসিস্টেমকে ভালভাবে কনফিগার করেই ইউজ করতে পারবে । আপনাকে শুধুই এই ফাইলসিস্টেম এর সাথে কিছু কাজ করতে হবে , আর বাদ বাকী কাজ ল্যারাভেল ৫ অটোমেটিকলি করে নিবে । আপনি আপনার স্টোরেজ অপশনconfig/filesystems.php ফাইলে গিয়ে কনফিগার করে নিতে পারেন ।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/349719/upload_multiple.png)

## **Request Object**

রিকুয়েস্ট অবজেক্ট মুলত আপনার বিভিন্ন অথেনটিকেশন ও ডাটা ভ্যালিডেশন এর কাজে ইউজ হয়ে থাকে । আপনি যদি একবার আপনার লজিকটা লিখে ফেলেন তারপর আপনাকে জাস্ট কন্ট্রোলার একশনে গিয়ে হিন্ট টা টাইপ করতে হবে । এটা অনেকটা মেথড ইনজেকশনের মতই বলা যায় ।

![](https://dnc.techtunes.io/tDrive/tuner/arindampaulripon/349719/laravel-form-validation-custom-error-messages.png)

নিচের কোডটা ভালভাবে দেখুন , জাস্ট দেখুন , ট্রাই করবেন না ,। এখানে যে কোডটা লেখা হয়েছে সেটার কাজ হল আপনি যদি ভ্যালিড ইমেইল ও কমপক্ষে ৮ ক্যারেকটারের পাসওয়ার্ড না দেন তাহলে এটা আপনাকে অন্য একটা পেজে রিডিরেক্ট করবে ।

```
&lt;/pre&gt;
&lt;?php

namespace App\Http\Requests;

use App\Http\Requests\Request;

class TutsPlusRequest extends Request {

/**

* Determine if the user is authorized to make this request.

*

* @return bool

*/

public function authorize()

{

return true;

}

/**

* Get the validation rules that apply to the request.

*

* @return array

*/

public function rules()

{

return [

'email' =&gt; 'required|email',

'password' =&gt; 'required|min:8'

];

}

}

// in your controller action

public function postLogin(\App\Http\Requests\TutsPlusRequest $request)

{

// code here will not fire

// if the validation rules

// in the request fail

}

?&gt;
&lt;pre&gt;
```

এইরকম আরও অনেক চমক রয়েছে ল্যরাভেল ৫ এ নতুন ভাবে । আর এইসব বিষয়ে আপনাদের সাথে পরে আলোচনা করব । সেই পর্যন্ত সবাই ভাল থাকবেন । ধন্যবাদ ।
