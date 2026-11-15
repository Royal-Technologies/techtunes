---
archive_id: techtunes-282547
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 282547
title: 'শিখেনিন C++ এর A to Z, [পর্ব-০৪] :: ভেরিয়েবল মেমোরি কনসেপ্ট'
slug: programming-282547
language: bn
status: publish
published_at: '2014-04-16T13:29:00+00:00'
modified_at: '2016-12-10T09:53:00+00:00'
original_url: https://www.techtunes.io/programming/tune-id/282547
author: মুসতাকিম বিল্লাহ
author_url: https://www.techtunes.io/tuner/hemel50
categories:
- প্রোগ্রামিং
tags: []
content_hash: 7d3c95bc40591d627a60aec1e13b96f607114363d87e16debe3ddb22d9ff0ae5
archived_at: '2026-11-15T04:53:24.332429+00:00'
---

### [শিখেনিন C++ এর A to Z](https://www.techtunes.io/chain-tunes/learn-c-a-to-z "শিখেনিন C++ এর A to Z")

- [শিখেনিন C++ এর A to Z, [পর্ব-০১] :: ব্যাসিক](https://www.techtunes.io/programming/tune-id/281114 "শিখেনিন C++ এর A to Z, [পর্ব-০১] :: ব্যাসিক")
- [শিখেনিন C++ এর A to Z, [পর্ব-০২] :: ব্যাসিক](https://www.techtunes.io/programming/tune-id/281435 "শিখেনিন C++ এর A to Z, [পর্ব-০২] :: ব্যাসিক")
- [শিখেনিন C++ এর A to Z,[পর্ব-০৩] :: ব্যাসিক ভেরিয়েবল](https://www.techtunes.io/programming/tune-id/281920 "শিখেনিন C++ এর A to Z,[পর্ব-০৩] :: ব্যাসিক ভেরিয়েবল")
- শিখেনিন C++ এর A to Z, [পর্ব-০৪] :: ভেরিয়েবল মেমোরি কনসেপ্ট
- [শিখেনিন C++ এর A to Z, [পর্ব-০৫] :: ইফ স্টেটমেন্ট](https://www.techtunes.io/programming/tune-id/282964 "শিখেনিন C++ এর A to Z, [পর্ব-০৫] :: ইফ স্টেটমেন্ট")
- [শিখেনিন C++ এর A to Z, [পর্ব- ০৬] :: ফাংশন](https://www.techtunes.io/programming/tune-id/283637 "শিখেনিন C++ এর A to Z, [পর্ব- ০৬] :: ফাংশন")
- [শিখেনিন C++ এর A to Z, [পর্ব-০৭] :: ফাংশনে প্যারামিটার এর ব্যবহার](https://www.techtunes.io/programming/tune-id/284200 "শিখেনিন C++ এর A to Z, [পর্ব-০৭] :: ফাংশনে প্যারামিটার এর ব্যবহার")
- [শিখেনিন C++ এর A to Z, [পর্ব-০৮] :: ফাংশনে মাল্টিপল প্যারামিটার এর ব্যবহার](https://www.techtunes.io/programming/tune-id/285899 "শিখেনিন C++ এর A to Z, [পর্ব-০৮] :: ফাংশনে মাল্টিপল  প্যারামিটার এর ব্যবহার")
- [শিখেনিন C++ এর A to Z, [পর্ব-০৯] :: ইফ স্টেটমেন্ট](https://www.techtunes.io/programming/tune-id/286430 "শিখেনিন C++ এর A to Z, [পর্ব-০৯] :: ইফ স্টেটমেন্ট")
- [শিখেনিন C++ এর A to Z, [পর্ব-১০] :: ইফ- এলস স্টেটমেন্ট](https://www.techtunes.io/programming/tune-id/287422 "শিখেনিন C++ এর A to Z, [পর্ব-১০] :: ইফ- এলস স্টেটমেন্ট")
- [শিখেনিন C++ এর A to Z, [পর্ব- ১১] :: হয়াইল লুপ](https://www.techtunes.io/programming/tune-id/304346 "শিখেনিন C++ এর A to Z, [পর্ব- ১১] :: হয়াইল লুপ")

হ্যালো বন্ধুরা কেমন আছো সবাই?? আশা করি নতুন কিছু শেখার আগ্রহ নিয়ে আমরা সবাই সামনের দিকে এগিয়ে  যাচ্ছি। আর একই ভাবে আশা করছি  আমার সাথে c++ কে সহজ ভাবে শিখতে সবার ই অনেক ভালো লাগছে।

তাহলে কথা না বাড়িয়ে আজকে চলো আরও নতুন কিছু শিখে নেওয়া যাক। আজকে আমার টিউটোরিয়ালটি  variable memory concept নিয়ে সাজানো। আশা করছি আজকের টিউটোরিয়ালটি  তোমাদের অনেক উপকারে আসবে। যদি তোমরা আমার পূর্বের টিউটোরিয়াল গুলো স্মরণ করো তাহলে এটা বুঝতে কোন সমস্যা নেই যে আমরা দুই ভাবে variable তৈরি করতে পারি।

প্রথমত আমরা variable তৈরি করতে পারি

int hemel=10;

অথবা আমরা অন্যভাবেও variable তৈরি করতে পারি।

int hemel;

hemel=10;

অর্থাৎ প্রথমে আমরা variable তৈরি করেছি তারপর variable এর  value বসিয়েছি; তোমরা ভালো করে খেয়াল করলে দেখতে পাবে যে প্রথমে আমি int hemel; লিখেছি। কিন্তু ২য় লাইনে int ব্যবহার করিনাই।

শুধু লিখেছি hemel=10;

কারন প্রথমে int hemel; লেখার সাথে সাথেই c++ বুঝে নিয়েছে যে তুমি একটা variable তৈরি করেছ যেটা integer data type। তাই ২য় লাইন এ নতুন করে int লেখার প্রয়োজন নাই।

তো আমরা দেখে নেই c++ এ দেখে নেই।

```
#include&lt;iostream&gt;

using namespace std;

int main()

{

int hemel;

hemel=10;

cout&lt;&lt;hemel&lt;&lt;endl;

cin.get();

return 0;

}
```

এখন প্রোগ্রামটিকে রান করলে আমরা ডিসপ্লে টে দেখতে পাবো

[![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F2.bp.blogspot.com%2F-TxWB0kN7znA%2FU0558ZcUbNI%2FAAAAAAAAAM0%2FL0mF3PKV5P8%2Fs1600%2Ftutorial4.JPG&container=blogger&gadget=a&rewriteMime=image%2F*)](https://2.bp.blogspot.com/-TxWB0kN7znA/U0558ZcUbNI/AAAAAAAAAM0/L0mF3PKV5P8/s1600/tutorial4.JPG)

ওকে এখন যদি আমরা এভাবে লেখি যে

প্রথমে লিখলাম

int hemel=10;

এবার ২য় লাইন এ লিখলাম

hemel=50;

তাহলে c++ কোন value টি গ্রহন করবে??

খুবই জটিল প্রশ্ন তাইনা??

না আসলে একটুও জটিল নয়। যখন তুমি একটি variable তৈরি করলে এবং তার মান দিলে ১০, তখন c++ বুঝে নিল যে তুমি একটি  variable তৈরি  করেছ যেটার মান ১০।

এরপরে তুমি যখন ২য় লাইনে একই  variable টি লিখে তার মান অন্য কিছু দিলে তখন c++ বুঝে নিল যে তুমি  variable টির নতুন মান দিয়েছো।যেটাকে বর্তমান মান হিসেবে  c++ গননা করবে।

তাহলে চলো দেখে নেই c++  আসলেই সেরকম করে কিনা।

```
#include&lt;iostream&gt;

using namespace std;

int main()

{

int hemel=10;

hemel=50;

cout&lt;&lt;hemel&lt;&lt;endl;

cin.get();

return 0;

}
```

এখন রান করলে দেখা যাবে

[![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F4.bp.blogspot.com%2F-hesyT7hVgbU%2FU058moO8yMI%2FAAAAAAAAANA%2FexkN_Uurn0E%2Fs1600%2Ftutorial4.1.JPG&container=blogger&gadget=a&rewriteMime=image%2F*)](https://4.bp.blogspot.com/-hesyT7hVgbU/U058moO8yMI/AAAAAAAAANA/exkN_Uurn0E/s1600/tutorial4.1.JPG)

হম আমরা দেখতে পেলাম আসলেই কাজ করে। তো বন্ধুরা আজকে আরও একটু শিখে নেব যে কিভাবে ডিসপ্লে টে কোন কিছু ইনপুট করা যায়। কোন কিছু ইনপুট করার জন্যে c++ এ cin>> ব্যবহার করা হয়। যেমন আমরা যদি একটা  স্ক্যাধারন লকুলেটর তৈরি করতে চাই ইনপুট সহ তাহলে

আমরা এভাবে তৈরি করতে পারি

```
#include&lt;iostream&gt;

using namespace std;

int main()

{

int x,y,z,i,p;

cout&lt;&lt;"enter your first number: ";

cin&gt;&gt;x;

cout&lt;&lt;"enter your second number: ";

cin&gt;&gt;y;

z= x+y;

i= x-y;

p=x*y;

cout&lt;&lt;"your addition result is: "&lt;&lt;z&lt;&lt;endl;

cout&lt;&lt;"your substraction result is: "&lt;&lt;i&lt;&lt;endl;

cout&lt;&lt;"your mulplication result is: "&lt;&lt;p&lt;&lt;endl;

cout&lt;&lt;endl&lt;&lt;" thanks for using me :)";

cin.get();

return 0;

}
```

এখন প্রোগ্রামটি রান করলে ডিসপ্লেতে তোমাকে নাম্বার বসাতে বলবে। তো আমি ১০ এবং ৫ বসিয়েছি

[![](https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=http%3A%2F%2F1.bp.blogspot.com%2F-dqDwxEpgIJc%2FU06BiSgUX3I%2FAAAAAAAAANQ%2FFgBYILiWo_s%2Fs1600%2Ftutorial4.2.JPG&container=blogger&gadget=a&rewriteMime=image%2F*)](https://1.bp.blogspot.com/-dqDwxEpgIJc/U06BiSgUX3I/AAAAAAAAANQ/FgBYILiWo_s/s1600/tutorial4.2.JPG)

আশা করি আজকের টিউটোরিয়ালটি  বুঝতে কারো কোন সমস্যা হয়নি। যেকোনো সমস্যা অথবা কোন প্রশ্ন থাকলেই টিউমেন্ট করে জানাবে ভালো থাকো আর প্রোগ্রামিং এর সাথেই থাকো 🙂

> সৌজন্যেঃ  **[Sciencetech](http://www.sciencetech.tk/)**
