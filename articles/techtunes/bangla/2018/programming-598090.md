---
archive_id: techtunes-598090
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 598090
title: 'আরডুইনো দিয়ে খেলাধুলা [পর্ব-০২] ::'
slug: programming-598090
language: bn
status: publish
published_at: '2018-09-07T11:02:00+00:00'
modified_at: '2018-09-10T00:15:00+00:00'
original_url: https://www.techtunes.io/programming/tune-id/598090
author: আবদুল মুকিত
author_url: https://www.techtunes.io/tuner/abdulmukit-2
categories:
- প্রোগ্রামিং
tags:
- আরডুইনো
- আরডুইনো টিউটোরিয়াল
content_hash: d2eafb50afae67995748af2d4a32a56e683878795f207af12483dc0c8846457b
archived_at: '2026-11-12T12:30:04.182935+00:00'
---

আরডুইনো দিয়ে খেলাধুলার দ্বিতীয় পর্বে সবাইকে স্বাগতম।

আজ আমরা বেসিক জিনিসেরো বেসিক কাজ গুলো দেখব

প্রত্যেকেই আরডুইনো নিয়ে কাজ শুরু করলে সবার প্রথমে এই কাজটি করে।  একটা ভিজুয়াল ইফেক্ট যা সর্বপ্রথম আরডুইনোর প্রতি আকর্ষণ তৈরি করে।

Project name : LED Sequential Control

কাজ তেমন কিছুই না। শুধু স্কিমেটিক দেখে হার্ডওয়্যার কানেকশন দিন। কোড লেখে আপ্লোড দিন। মজা নিন।

## স্কিমেটিক:

![](https://dnc.techtunes.io/tDrive/tuner/2018/09/techtunes_9aaa9e0c4686c49c655e4610f21e49be.png)

## কোড কিভাবে লিখব:

আজকে শুধু ডিজিটাল কমান্ড ইউজ করব। তাই কোন ঝামেলাই নাই।

digitalWrite(pin\_number, HIGH/LOW);

এই ফাংশন দিয়েই সব খেলা হবে।

## বিস্তারিত কোড:

```
#define LED1 11 //declare LED at pin 11
#define LED1 12
#define LED1 13

void setup() {pinMode(11, OUTPUT);
pinMode(12, OUTPUT);
pinMode(13, OUTPUT);// set pin 11 as output
pinMode(3, OUTPUT);}

void loop() {digitalWrite(11, HIGH);
delay(200);
digitalWrite(12, HIGH);
delay(200);
digitalWrite(13, HIGH);
delay(1000);
digitalWrite(11, LOW);
delay(200);
digitalWrite(12, LOW);
delay(200);
digitalWrite(13, LOW);
delay(1000);}
```

## ডেমো:

[<https://dnc.techtunes.io/tDrive/tuner/2018/09/techtunes_5fa321b87b24d75e3deef6ac1f4a92b4.mp4>](https://dnc.techtunes.io/tDrive/tuner/2018/09/techtunes_5fa321b87b24d75e3deef6ac1f4a92b4.mp4?_=1)

ভবিষ্যতে আমরা ট্রাফিক লাইট ম্যানেজমেন্ট (নরমাল + এডভান্সড) এর প্রয়োগ দেখব।

Abdul Mukit  
 CSE 46  
 JU
