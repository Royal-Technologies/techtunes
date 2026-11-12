---
archive_id: techtunes-501164
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 501164
title: কোন প্রকার  সফটওয়্যার ছাড়াই পাসওয়ার্ড দিয়ে আপনার অডিও বা ভিডিও বা যেকোন ফাইল
  লুকিয়ে রাখুন মাত্র দুই মিনিট এ
slug: computing-501164
language: bn
status: publish
published_at: '2017-07-07T01:25:00+00:00'
modified_at: '2017-07-09T12:00:00+00:00'
original_url: https://www.techtunes.io/computing/tune-id/501164
author: আসিফ পারভেজ
author_url: https://www.techtunes.io/tuner/asifparvezasif
categories:
- কম্পিউটিং
tags:
- file hide
- file hinde
content_hash: 4d10af16a872745c538decf34e8c5c83740075047d22e1494ac6554eb91dcdfb
archived_at: '2026-11-12T12:47:11.041822+00:00'
---

## ফাইল হাইড কি

ফাইল হাইড হল আপনার কোন গোপনীয় ফাইল কে লুকিয়ে রাখা। প্রায় সবাই কোন ফাইল হাইড সফটওয়্যার ব্যবহার করে প্রয়োজনীয় ফাইল হাইড করে রাখে তবে আমরা আজ দেখব কিভাবে কোন প্রকার  সফটওয়্যার ছাড়াই পাসওয়ার্ড দিয়ে  অডিও বা ভিডিও বা যেকোন ফাইল লুকিইয়ে রাখা যায়। প্রথমে নিচের মত করে একটি ফোল্ডার তৈরি করি।

![](https://dnc.techtunes.io/tDrive/tuner/asifparvezasif/501164/1_folder-create.png)

এখন একটি টেক্সট ডকুমেন্ট তৈরি করি নিছের মত করে।

![](https://dnc.techtunes.io/tDrive/tuner/asifparvezasif/501164/2_text_document.png)

টেক্সট ডকুমেন্ট ওপেন করে নিছের মত করে আমাদের মন মত password দেই

![](https://dnc.techtunes.io/tDrive/tuner/asifparvezasif/501164/3_password_name.png)

এখন টেক্সট ডকুমেন্টির এক্সটেন্সন পরিবর্তন করে .bat দেই।

![](https://dnc.techtunes.io/tDrive/tuner/asifparvezasif/501164/4_.bat_.png)

.bat ফাইল এ ডাবল ক্লিক করি তাহলে নিচের মত একটি ফোল্ডার তৈরি হবে private নামে।

![](https://dnc.techtunes.io/tDrive/tuner/asifparvezasif/501164/5_double_click.png)

আপনি যে অডিও  বা ভিডিও বা যে ফাইল লুকিইয়ে রাখতে চান সেই ফাইল কপি বা পেস্ট করেন এই  private নামের  ফোল্ডার এ। যেকোন ফাইল ই হাইড করা যাবে।

![](https://dnc.techtunes.io/tDrive/tuner/asifparvezasif/501164/6_file_copy.png)

আপনি আপনার .bat ফাইল্টা ডাবল ক্লিক করুন তাহলে নিছের মত আসবে আপনি y লেখে এন্টার প্রেস করুন।বেচ আপনার ফাইল হাইড হয়ে গেছে।

![](https://dnc.techtunes.io/tDrive/tuner/asifparvezasif/501164/7_y_enter.png)

এবার আপনার ফাইল দেখার জন্য আবার ওপেন করে আপনার দিয়ে এন্টার প্রেস করুন। আপনার ফাইল পেয়ে গেছেন তাই না।

![](https://dnc.techtunes.io/tDrive/tuner/asifparvezasif/501164/8_asif_enter.png)

## সহায়ক হিসেবে ভিডিওটি দেখুন

[Embedded External Content: https://www.youtube.com/embed/nBP1JhwTbbM?feature=oembed]

## কোড

```
cls
@ECHO OFF
title Folder Private
if EXIST "HTG Locker" goto UNLOCK
if NOT EXIST Private goto MDLOCKER
:CONFIRM
echo Are you sure you want to lock the folder(Y/N)
set/p "cho=>"
if %cho%==Y goto LOCK
if %cho%==y goto LOCK
if %cho%==n goto END
if %cho%==N goto END
echo Invalid choice.
goto CONFIRM
:LOCK
ren Private "HTG Locker"
attrib +h +s "HTG Locker"
echo Folder locked
goto End
:UNLOCK
echo Enter password to unlock folder
set/p "pass=>"
if NOT %pass%== asif goto FAIL
attrib -h -s "HTG Locker"
ren "HTG Locker" Private
echo Folder Unlocked successfully
goto End
:FAIL
echo Invalid password
goto end
:MDLOCKER
md Private
echo Private created successfully
goto End
:End
```

ধন্যবাদ।
