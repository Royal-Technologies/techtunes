---
archive_id: techtunes-99354
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 99354
title: 'Visual Basic খুব সহজে [পর্ব-০৪] :: GPA বের করার প্রোগ্রাম'
slug: programming-99354
language: bn
status: publish
published_at: '2011-11-29T15:54:00+00:00'
modified_at: '2011-11-29T19:10:00+00:00'
original_url: https://www.techtunes.io/programming/tune-id/99354
author: গোলাম মুক্তাদির
author_url: https://www.techtunes.io/tuner/web-developer
categories:
- প্রোগ্রামিং
tags: []
content_hash: 8c4f11c3d4f8d60881b91cb232a46dcd74de3fdf8a8ed8eac620dfc12b8e6be4
archived_at: '2026-11-17T06:38:15.845921+00:00'
---

### [Visual Basic খুব সহজে](https://www.techtunes.io/chain-tunes/visual-basic-%e0%a6%96%e0%a7%81%e0%a6%ac-%e0%a6%b8%e0%a6%b9%e0%a6%9c%e0%a7%87 "Visual Basic খুব সহজে")

- [Visual Basic খুব সহজে [পর্ব-০২] :: প্রোগ্রাম লেখা – কোন সংখ্যার বর্গমূল বের করা](https://www.techtunes.io/programming/tune-id/95220 "Visual Basic খুব সহজে [পর্ব-০২] :: প্রোগ্রাম লেখা – কোন সংখ্যার বর্গমূল বের করা")
- [Visual Basic খুব সহজে [পর্ব-০৩] :: সফটওয়্যার তৈরি](https://www.techtunes.io/programming/tune-id/98029 "Visual Basic খুব সহজে [পর্ব-০৩] :: সফটওয়্যার তৈরি")
- Visual Basic খুব সহজে [পর্ব-০৪] :: GPA বের করার প্রোগ্রাম
- [Visual Basic খুব সহজে [পর্ব-০৫] :: Stop Watch তৈরি](https://www.techtunes.io/programming/tune-id/100938 "Visual Basic খুব সহজে [পর্ব-০৫] :: Stop Watch তৈরি")
- [Visual Basic শিখুন খুব সহজে [পর্ব-০৬] :: ঘড়ি তৈরি](https://www.techtunes.io/mobileo/tune-id/105877 "Visual Basic শিখুন খুব সহজে [পর্ব-০৬] :: ঘড়ি তৈরি")
- [Visual Basic শিখুন খুব সহজে [পর্ব-০৭] :: সাধারণ হিসাব](https://www.techtunes.io/programming/tune-id/107157 "Visual Basic শিখুন খুব সহজে [পর্ব-০৭] :: সাধারণ হিসাব")
- [Visual Basic শিখুন খুব সহজে [পর্ব-০৮] :: মিডিয়া প্লেয়ার ডিজাইন!](https://www.techtunes.io/programming/tune-id/107440 "Visual Basic শিখুন খুব সহজে [পর্ব-০৮] :: মিডিয়া প্লেয়ার ডিজাইন!")

Visual Basic প্রগ্রামে আপনারা অনেক দূর এগিয়ে গেছেন ! তবে অনেক কাজ হুবহু কপি পেস্ট করেছেন কিন্তু বুঝতে পারেননি ! ।

কিন্তু এখন থেকে বুঝে কাজ করবেন , না হলে শিখে লাভ নাই । তবে মাঝে মাঝে মজার প্রোজেক্ট নিয়ে আসব না হলে এক ঘেয়েমিতে পেয়ে বসবে এটা স্বাভাবিক প্রগ্রামিং জগতটায় এমন !! ।

## আজ শিখবেন GPA বের করার প্রোগ্রাম .....................

প্রথমে Visual Basic ওপেন করে standard EXE সিলেক্ট করি

[![](https://dnc.techtunes.io/tDrive/tuner/web-developer/99354/ScreenHunter_06-Oct.-27-16.11.jpg)](https://www.techtunes.io/programming/tune-id/99354/screenhunter_06-oct.27-16.11-3/)

এবার আপনি তিনটি Lebel ও তিনটি Text box নিয়ে চিত্র অনুসারে সাজাবেন

[![](https://dnc.techtunes.io/tDrive/tuner/web-developer/99354/jpiblog.tk-vb.jpg)](https://www.techtunes.io/programming/tune-id/99354/jpiblog.tk-vb/)

[![](https://dnc.techtunes.io/tDrive/tuner/web-developer/99354/vb11.gif)](https://www.techtunes.io/programming/tune-id/99354/vb11/)

প্রথম lebel এর নাম Marks ২য় টি হবে Grade Point , ৩য় টি হবে Letter Grade

এবার একটি Command Button নিন এবং নাম দিন Result

আপনার ডিজাইন এর কাজ শেষ ! এখন কোড বসাতে হবে ।

এবার Command Buttton এ ডাবল ক্লিক করে

```
Private Sub Command1_Click()

End Sub
```

মাঝে নিচের কোড টুকু লিখুন

```
Dim Subject1, Subject2, Subject3, Subject4, Subject5

Subject1 = Val(Text1)

If Subject1 >= 80 And Subject 1<= 100 Then

Text2 = 5

Text3 = "A+"

ElseIf Subject1 >= 70 And Subject1 <= 79 Then

Text2 = 4

Text3 = "A"

ElseIf Subject1 >= 60 And Subject1 <= 69 Then

Text2 = 3.5

Text3 = "A-"

ElseIf Subject1 >= 50 And Subject1 <= 59 Then

Text2 = 3

Text3 = "B"

ElseIf Subject1 >= 40 And Subject1 <= 49 Then

Text2 = 2

Text3 = "C"

Else

Text2 = 0

Text3 = "F"

End If
```

সর্বশেষ F5 চেপে Run করুন ।

## Code বিশ্লেষণ

এখন আপনাকে বুঝতে হবে কি কি কাজ সংগঠিত হয়েছে

প্রথমে Dim দিয়ে Subject1, Subject2, Subject3, Subject4, Subject5 মোট পাঁচটি Variable ঘোষণা করলাম

এবং এখানে IF  Else Else if statement ব্যবহার করেছি ,

এখন এটি দ্বারা কি বুঝায় ?

```
Subject1 = Val(Text1)
```

Value Text1 কে ধরা হয়েছে অর্থাৎ আপনি Text 1 এ যা বসাবেন সেটি নিবে এবং দেখবে সেটি ৮০ এর সমান না বড় হয় তবে এটি Text2 তে A+   grade এবং Text3 তে 5 দেখাবে । এভাবে ক্রমান্বয়ে compile করবে ।

বুঝতে না পারলে মন্তব্য করবেন ।

[Download](http://www.mediafire.com/?5rrp6dgnn8w1wyr) করে দেখে নিতে পারেন ।

Password : jpiblog

> সবাইকে কষ্ট করে পড়ার জন্য ধন্যবাদ .........
>
> পূর্বে প্রকাশিত [http://jpiblog.tk](http://jpiblog.tk/)
