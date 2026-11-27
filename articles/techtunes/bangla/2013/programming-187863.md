---
archive_id: techtunes-187863
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 187863
title: 'Microsoft Small Basic প্রোগ্রামিং [পর্ব-০৪] :: লুপ ও ব্রাঞ্চিং'
slug: programming-187863
language: bn
status: publish
published_at: '2013-02-20T17:21:00+00:00'
modified_at: '2013-02-22T20:19:00+00:00'
original_url: https://www.techtunes.io/programming/tune-id/187863
author: সাকিব
author_url: https://www.techtunes.io/tuner/sakib2010
categories:
- প্রোগ্রামিং
tags: []
content_hash: d8e2445bdff2f25293ff98e783620fb672822b15edd86bb72539e73beb13a7c8
archived_at: '2026-11-27T06:49:27.288043+00:00'
---

### [Microsoft Small Basic প্রোগ্রামিং](https://www.techtunes.io/chain-tunes/microsoft-small-basic-programming "Microsoft Small Basic প্রোগ্রামিং")

- [Microsoft Small Basic প্রোগ্রামিং [পর্ব-০১] :: প্রাথমিক আলোচনা](https://www.techtunes.io/programming/tune-id/186667 "Microsoft Small Basic প্রোগ্রামিং [পর্ব-০১] :: প্রাথমিক আলোচনা")
- [Microsoft Small Basic প্রোগ্রামিং [পর্ব-০২] :: আরও একটু এডভান্স](https://www.techtunes.io/programming/tune-id/187019 "Microsoft Small Basic প্রোগ্রামিং [পর্ব-০২] :: আরও একটু এডভান্স")
- [Microsoft Small Basic প্রোগ্রামিং [পর্ব-০৩] :: কন্ডিশনাল স্টেটমেন্ট](https://www.techtunes.io/programming/tune-id/187276 "Microsoft Small Basic প্রোগ্রামিং [পর্ব-০৩] :: কন্ডিশনাল স্টেটমেন্ট")
- Microsoft Small Basic প্রোগ্রামিং [পর্ব-০৪] :: লুপ ও ব্রাঞ্চিং
- [Microsoft Small Basic প্রোগ্রামিং [পর্ব-০৫] :: গ্রাফিক্স উইন্ডো](https://www.techtunes.io/programming/tune-id/188277 "Microsoft Small Basic প্রোগ্রামিং [পর্ব-০৫] :: গ্রাফিক্স উইন্ডো")
- [Microsoft Small Basic প্রোগ্রামিং [পর্ব-০৬] :: Shapes Object Part 1](https://www.techtunes.io/programming/tune-id/189289 "Microsoft Small Basic প্রোগ্রামিং [পর্ব-০৬] :: Shapes Object Part 1")
- [Microsoft Small Basic প্রোগ্রামিং [পর্ব-০৭] :: Shapes Object Part 2](https://www.techtunes.io/programming/tune-id/189643 "Microsoft Small Basic প্রোগ্রামিং [পর্ব-০৭] :: Shapes Object Part 2")
- [Microsoft Small Basic প্রোগ্রামিং [পর্ব-০৮] :: Program, Sound এবং Text অবজেক্ট](https://www.techtunes.io/programming/tune-id/191046 "Microsoft Small Basic প্রোগ্রামিং [পর্ব-০৮] :: Program, Sound এবং Text অবজেক্ট")
- [Microsoft Small Basic প্রোগ্রামিং [পর্বঃ ৯] :: Clock ও Desktop অবজেক্ট](https://www.techtunes.io/programming/tune-id/191568 "Microsoft Small Basic প্রোগ্রামিং [পর্বঃ ৯] :: Clock ও Desktop অবজেক্ট")

আপনাকে বলা হলো ১ থেকে ১০ পর্যন্ত কনসোলে দেখান। তাহলে আপনি কোড লেখা শুরু করবেন যে,

TextWindow.WriteLine(“1”) এভাবে 10 পর্যন্ত। কিন্তু আপনাকে যদি 1 থেকে 100 পর্যন্ত লিখতে বলা হয় তখন কি করবেন??

এই কাজগুলো আপনি মাত্র তিন লাইনের কোড দিয়েই করতে পারবেন। কারণ প্রতিটি প্রোগ্রামিং ল্যাংগুয়েজের মতোই Microsoft Small Basic এ লুপ আছে। লুপ দিয়ে সহজেই একাধিক স্টেটমেন্ট লেখা যায়। MS Small Basic এ দুধরনের লুপ আছে। For লুপ এবং While লুপ। আমরা For লুপের ব্যাবহার নিয়ে আজকের পর্ব শুরু করছি।

## For Loop

সাধারনত For.. EndFor লুপ ব্যাবহার করে থাকি একটি নির্দিষ্ট সময়ের জন্য কোড এক্সিকিউট করার জন্য। লুপ চালানের জন্য একটি ভেরিয়েবলে সীমা যুক্ত কর দিবো। ভালোভাবে বোঝার জন্য নিচের উদাহরনটি দেখুন।

```
For a = 1 To 10
TextWindow.WriteLine(a)
EndFor
```

প্রোগ্রামটি রান করে দেখুন আউটপুটে 1 থেকে 10 দেখতে পারবেন। প্রোগ্রামটি মূলত প্রতিবার এক করে মান বৃদ্ধি করে থাকে। আপনি যদি এক এর পরিবর্তে অন্য হারে মান পরিবর্তন করতে চান তাহলে আপনাকে Step নামক কীওয়ার্ডটি ব্যাবহার করতে হবে। নিচের উদাহরনটি লক্ষ্যনীয়।

```
For a = 1 To 10 Step 2
TextWindow.WriteLine(a)
EndFor
```

আউটপুট এরকম আসবেঃ

1

3

5

7

9

এবার চলুন For লুপ দিয়ে একটা নামতা লিখে ফেলি। আমরা 5 এর ঘরের নামতা লিখব।

```
number = 5
For a = 1 To 10
TextWindow.WriteLine(number + " X " + a + " = " + number * a)
EndFor
```

প্রোগ্রামটি আসলে কিভাবে কাজ করছে? প্রথমে আমরা number নামক ভেরিয়েবলে আমরা 5 অ্যাসাইন করছি। এরপর আমরা লুপের ভিতর number এর সাথে a গুন করে প্রতি লাইনে দেখাচ্ছি। a এর মান প্রতিবার যেহেতু এক করে বৃদ্ধি পাচ্ছে তাই আমাদের রেজাল্টও প্রতি লাইনে পরিবর্তিত হচ্ছে।

## While Loop

While Loop এর Syntax হলোঃ

**While** (condition)

‘some codes to be executed

**EndWhile**

আগে একটি উদাহরন তারপরে বিস্তারিত While Loop সম্পর্কে বলছি।

```
x = 10
While (x <= 100)
TextWindow.WriteLine(x)
x = x + 10
EndWhile
```

এখন প্রোগ্রামটি কিভাবে কাজ করলো তা জেনে নিই। প্রথমে আমরা x এর মান 10 অ্যাসাইন করলাম। এরপর আমরা while লুপে একটা শর্ত জুড়ে দিলাম যে  যতক্ষন পর্যন্ত x এর মান ১০০ এর সমান বা ছোট থাকবে ততক্ষণ পর্যন্ত লুপের ভিতরের কাজগুলো চলতে থাকবে। এখন লুপের ভিতর প্রথম স্টেটমেন্ট হলো কনসোল উইন্ডোতে x এর মান লেখা অর্থাৎ আউটপুট দেওয়া। এর পর আছে x = x + 10 এর মানে হলো x এর মান ১০ বৃদ্ধি করা। এখন x এর মান হলো ২০ । যেহেতু সে ১০০ এর ছোট তাই স্ক্রীনে x এর নতুন মান ২০ প্রিন্ট করবে। এভাবে ১০০ হওয়া পর্যন্ত লুপ চলতে থাকবে। আমরা বিষয়টাকে নিচের ফ্লো-চার্টের মাধ্যমে দেখাতে পারি।

[![](https://dnc.techtunes.io/tDrive/tuner/sakib2010/187863/algo-loop.png)](https://www.techtunes.io/programming/tune-id/187863/algo-loop)

## ব্র্রাঞ্চিং ( Branching )

আপনারা এতোক্ষনে জানেন যে প্রোগ্রাম লাইন বাই লাইন কাজ করে। আপনারা অনেকেই হয়তো প্রোগ্রাম শেষ না করে পূর্বের কোন স্টেটমেন্টে চলে যেতে চান। এজন্য **Goto** আমরা কীওয়ার্ড ব্যবহার করবো। এর এই **Goto** কীওয়ার্ড ব্যবহার করে পূর্বে স্টেটমেন্টে ফিরে যাওয়াকে Branching বলে। একটি উদাহরনের মাধ্যমে চলুন বিষয়টি দেখে নিই।

```
j = 1

start:

TextWindow.WriteLine(j)

j =  j + 1

If j < 10 Then

Goto start

EndIf
```

এখানে start হলো একটি লেবেল। আমরা বলেছি যদি j এর মান ১০ এর চেয়ে ছোট হয় তাহলে। start এ চলে যাও। লেবেল লেখার নিয়মটি ভালো করে দেখুন। আমরা লেবেলের পর একটি কোলন দিয়েছি।

Goto এর ব্যবাহার আমরা একটি প্রোগ্রামের মেনু তৈরী করে তাতে ফিরে যাওয়ার কাজে লাগাতে পারি। নিচের প্রোগ্রামটি উদাহরনসরূপ দিলাম।

```
TextWindow.Title = "Multifunction Calculator"
Start:
TextWindow.WriteLine("Enter the number of program you want to run: ")
TextWindow.WriteLine("1. Addition")
TextWindow.WriteLine("2. Subtraction")
TextWindow.WriteLine("3. Exit")
choice = TextWindow.ReadNumber()

If (choice = 1) Then
    TextWindow.WriteLine("Enter a number: ")
    x = TextWindow.ReadNumber()
    TextWindow.WriteLine("Enter another number: ")
    y = TextWindow.ReadNumber()
    ans = x + y
    TextWindow.WriteLine("The sum of entered numbers is " + ans)
    Goto Start
ElseIf (choice = 2) Then
    TextWindow.WriteLine("Enter a number: ")
    x = TextWindow.ReadNumber()
    TextWindow.WriteLine("Enter another number: ")
    y = TextWindow.ReadNumber()
    ans = x- y
    TextWindow.WriteLine("The subtraction of entered numbers is " + ans)
    Goto Start
ElseIf (choice = 3) Then
    TextWindow.WriteLine("Thanks for using this app.")
    'program will end here
Else
    TextWindow.WriteLine("Invalid Number. Try again!")
    Goto Start
EndIf
```

আজ এতোটুকুই থাক। আগামী পর্বে আমরা সাবরুটিন তৈরী ও একটি গ্রাফিকাল উইন্ডো তৈরী করা শিখবো।
