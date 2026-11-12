---
archive_id: techtunes-660942
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 660942
title: মাইক্রোসফট নোটপ্যাডে ৪টি প্রোগ্রামিং ট্রিকস
slug: tips-and-tricks-660942
language: bn
status: publish
published_at: '2020-07-13T04:28:00+00:00'
modified_at: '2020-07-13T04:29:00+00:00'
original_url: https://www.techtunes.io/tips-and-tricks/tune-id/660942
author: মোঃ রাকিবুল ইসলাম
author_url: https://www.techtunes.io/tuner/rakibulitopu
categories:
- টিপস এন্ড ট্রিকস
tags:
- Notepad
content_hash: 1cec5cfbcab1106ceb1f064bb57f40a847da31ddb74abf5a4b8a8d49bd2fadcc
archived_at: '2026-11-12T12:24:15.552935+00:00'
---

ওয়েব ডিজাইনার/প্রোগ্রামারদের কাছে মাইক্রোসফট নোটপ্যাড খুবই পরিচিত একটি সফটওয়্যার। বিশেষ করে প্রায় সকল ওয়েব ডিজাইনারাই তাদের কোড লিখা শুরু করে নোটপ্যাড দিয়ে। আর এই নোটপ্যাড দিয়েই মজার মজার বেশ কিছু প্রোগ্রামিং করে ফেলা যায়।

এই আর্টিকেলে ৪টি দুর্দান্ত প্রোগ্রাম রয়েছে যা যে কেউ তাদের পিসিতে সহজে রান করতে পারেন। আর এই সমস্ত স্ক্রিপ্টগুলি উইন্ডোজ 10 ক্রিয়েটর আপডেট ব্যবহার করে পরীক্ষা করা হয়েছিল আর আপনার উইন্ডোজ সেটআপে ভিন্নতার কারণে কিছুটা ভিন্নভাবে কাজ করতে পারে।

**1. Make Your Computer Talk**

আপনার কম্পিউটারকে কথা বলান নিচের ছোট্ট এই কোডটি লিখে!

1) নিম্নলিখিত কোডের লাইনগুলি কপি করুন এবং এগুলি নোটপ্যাডে পেস্ট করুন:

> Dim Message, Speak  
>  Message=InputBox("Enter text", "Speak")  
>  Set Speak=CreateObject("sapi.spvoice")  
>  Speak.Speak Message

2) "talk.vbs"এই নামে ফাইলটি সংরক্ষণ করুন (আপনি যেকোন নামে ফাইলটি সেভ করতে পারেন তবে ফাইলের এক্সেটেনশন.vbs ফাইল হিসাবে সংরক্ষণ করতে হবে)।

3) অ্যাকশন দেখতে ফাইলটিতে ডাবল ক্লিক করে ওপেন করুন।

**2. Guessing Game**

আপনি যদি কোন কারণে বিরক্ত হয়ে থাকেন তবে সময়টি কাটানোর একটি ভাল উপায় এই গেম।

1) নিম্নলিখিত কোডের লাইনগুলি কপি করুন এবং এগুলি নোটপ্যাডে পেস্ট করুন:

> [@echo](https://www.techtunes.io/techtuner/echo/) off  
>  color 0e  
>  title Guessing Game by seJma  
>  set /a guessnum=0  
>  set /a answer=%RANDOM%  
>  set variable1=surf33  
>  echo -  
>  echo Welcome to the Guessing Game!  
>  echo.  
>  echo Try and Guess my Number!  
>  echo -  
>  echo.  
>  :top  
>  echo.  
>  set /p guess=  
>  echo.  
>  if %guess% GTR %answer% ECHO Lower!  
>  if %guess% LSS %answer% ECHO Higher!  
>  if %guess%=%answer% GOTO EQUAL  
>  set /a guessnum=%guessnum% +1  
>  if %guess%=%variable1% ECHO Found the backdoor hey?, the answer is: %answer%  
>  goto top  
>  :equal  
>  echo Congratulations, You guessed right!  
>  echo.  
>  echo It took you %guessnum% guesses.  
>  echo.  
>  pause

2) "game.bat"এই নামে ফাইলটি সংরক্ষণ করুন (আপনি যেকোন নামে ফাইলটি সেভ করতে পারেন তবে ফাইলের এক্সেটেনশন.bat ফাইল হিসাবে সংরক্ষণ করতে হবে)।

3) অ্যাকশন দেখতে ফাইলটিতে ডাবল ক্লিক করে ওপেন করুন।

**3. Password Generator**

আপনি যদি একটি সাধারণ (সংখ্যাগত) এলোমেলো পাসওয়ার্ড জেনারেটর তৈরি করতে চান তবে এটি আপনাকে সাহায্য করবে। মূলত, এটি পিন জেনারেট করতে বেশি সাহায্য করবে।

1) নিম্নলিখিত কোডের লাইনগুলি কপি করুন এবং এগুলি নোটপ্যাডে পেস্ট করুন:

> [@echo](https://www.techtunes.io/techtuner/echo/) off  
>  :Start2  
>  cls  
>  goto Start  
>  :Start  
>  title Password Generator  
>  echo I will make you a new password.  
>  echo Please write the password down somewhere in case you forget it.  
>  echo -¬-  
>  echo 1) 1 Random Password  
>  echo 2) 5 Random Passwords  
>  echo 3) 10 Random Passwords  
>  echo Input your choice  
>  set input=  
>  set /p input= Choice:  
>  if %input%=1 goto A if NOT goto Start2  
>  if %input%=2 goto B if NOT goto Start2  
>  if %input%=3 goto C if NOT goto Start2  
>  :A  
>  cls  
>  echo Your password is %random%  
>  echo Now choose what you want to do.  
>  echo 1) Go back to the beginning  
>  echo 2) Exit  
>  set input=  
>  set /p input= Choice:  
>  if %input%=1 goto Start2 if NOT goto Start 2  
>  if %input%=2 goto Exit if NOT goto Start 2  
>  :Exit  
>  exit  
>  :B  
>  cls  
>  echo Your 5 passwords are %random%, %random%, %random%, %random%, %random%.  
>  echo Now choose what you want to do.  
>  echo 1) Go back to the beginning  
>  echo 2) Exit  
>  set input=  
>  set /p input= Choice:  
>  if %input%=1 goto Start2 if NOT goto Start 2  
>  if %input%=2 goto Exit if NOT goto Start 2  
>  :C  
>  cls  
>  echo Your 10 Passwords are %random%, %random%, %random%, %random%, %random%, %random%, %random%, %random%, %random%, %random%  
>  echo Now choose what you want to do.  
>  echo 1) Go back to the beginning  
>  echo 2) Exit  
>  set input=  
>  set /p input= Choice:  
>  if %input%=1 goto Start2 if NOT goto Start 2  
>  if %input%=2 goto Exit if NOT goto Start 2

2) "pg.bat"এই নামে ফাইলটি সংরক্ষণ করুন (আপনি যেকোন নামে ফাইলটি সেভ করতে পারেন তবে ফাইলের এক্সেটেনশন.bat ফাইল হিসাবে সংরক্ষণ করতে হবে)।

3) অ্যাকশন দেখতে ফাইলটিতে ডাবল ক্লিক করে ওপেন করুন।

**4. A Virtual Calculator**

সাধারণ একটি ক্যাল্কুলেটর তৈরি করার জন্য এই কোডটি ব্যবহার করতে পারেন!

1) নিম্নলিখিত কোডের লাইনগুলি কপি করুন এবং এগুলি নোটপ্যাডে পেস্ট করুন:

> [@echo](https://www.techtunes.io/techtuner/echo/) off  
>  title Batch Calculator by seJma  
>  color 1f  
>  :top  
>  echo -  
>  echo Welcome to Batch Calculator  
>  echo -  
>  echo.  
>  set /p sum=  
>  set /a ans=%sum%  
>  echo.  
>  echo = %ans%  
>  echo -  
>  pause  
>  cls  
>  echo Previous Answer: %ans%  
>  goto top  
>  pause  
>  exit

2) "calculator.bat"এই নামে ফাইলটি সংরক্ষণ করুন (আপনি যেকোন নামে ফাইলটি সেভ করতে পারেন তবে ফাইলের এক্সেটেনশন.bat ফাইল হিসাবে সংরক্ষণ করতে হবে)।

3) অ্যাকশন দেখতে ফাইলটিতে ডাবল ক্লিক করে ওপেন করুন।

# লেখাটি পূর্বে TechFAQBD-এর ওয়েবসাইটে প্রকাশিত হয়েছে যার লিংকঃ <https://www.techfaqbd.com/2020/07/4-programming-tricks-inside-microsoft-notepad.html>
