---
archive_id: techtunes-373083
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 373083
title: Arduino শিখুন এক্সক্লুসিভ প্রজেক্ট তৈরি করুন [পর্ব-১৮] ::(ডিবাউন্সিং কৌশল)
  আসুন জেনে নেই কিবোর্ডের বাটন কিভাবে সুন্দরভাবে কাজ করে
slug: electronics-373083
language: bn
status: publish
published_at: '2015-07-19T15:21:00+00:00'
modified_at: '2015-07-19T15:30:00+00:00'
original_url: https://www.techtunes.io/electronics/tune-id/373083
author: অসীম কুমার পাল
author_url: https://www.techtunes.io/tuner/ashim
categories:
- ইলেক্ট্রনিক্স
tags:
- arduino
- Ashim Kumar
- আরডুইনো
content_hash: 59ab6e7114d984aeabb05bbb9fbeda17d33a2d0d3fd0c71e9e973afee4288319
archived_at: '2026-11-12T12:56:22.343199+00:00'
---

আমরা কিবোর্ডের বাটন গুলোতে চাপ দিয়ে সুন্দরভাবে লিখবে পারি,  এর পেছনের ইঞ্জিনিয়ারিংটা কিন্তু এতো সহজ নয়। আমরা যখন কিবোর্ডের একটা বাটন প্রেস করি তখন আশা করি একটা ক্যারেক্টার লেখা হবে বা কোন একটা নির্দিষ্ট কাজ হবে। কিবোর্ডের বোতামগুলো সহজভাবে বিশ্লেষণ করলে বলা যায় দুইটা কন্ডাক্টিং তলের মধ্যে স্পর্শ হওয়ার ম্যাকানিক্যাল সিস্টেম, যার মাধ্যমে ইলেকট্রিক্যাল সিগন্যাল ইনপুট হয়। এই  ম্যাকানিক্যাল সিস্টেম অতোটা সুক্ষ নয়, যে আমরা একবার বাটন প্রেস করলে এই দুটো তলের মধ্যে মাত্র একবারই কন্টাক্ট বা স্পর্শ হবে।

![](https://dnc.techtunes.io/tDrive/tuner/ashim/373083/1.jpg)

আমরা প্রতিবার যখন কিবোর্ডের একটা বোতাম প্রেস করি, তখন দুইটা তলের মধ্যে কয়েকবার কন্টাক্ট হতে পারে যাকে বাউন্সিং বলে এবং বাউন্সিং ঘটতে কয়েক মিলি সেকেন্ড সময় লাগতে পারে। গিগাহার্জ টেকনোলজির এই যুগে কয়েক মিলিসেকেন্ড অনেক বেশি সময়। তাই কোন বিশেষ ব্যবস্থা না নিলে আমরা যদি কিবোর্ডে একবার "A" বাটন প্রেস করি তাহলে কয়েকটি "A" ক্যারেক্টার স্ক্রিনে লেখা হয়ে যেতে পারে এবং কয়টা ক্যারেক্টার লেখা হবে তাও কিন্তু আমরা নিশ্চিৎভাবে বলতে পারবো না। কি ভয়ংকর ব্যপার তাই না !

তাই এই সমস্যার সমাধান হিসেবে বাটনে ডিবাউন্সিং কৌশল ব্যবহার করা হয়। এটা একটা সহজ তত্বের উপর প্রতিষ্ঠিত। আমাদের কোন বাটন প্রেস করতে প্রায় হাফ সেকেন্ডের মতো সময় লাগে যাকে মিলিসেকেন্ডে নিলে ৫00  মিলিসেকেন্ড হয়। আমরা যখন কোন বাটন প্রেস করি তখন সেটা ইনপুট হিসেবে গৃহিত হয়, এবং তার উপর ভিত্তি করে নির্দিষ্ট কোন প্রোগ্রাম সক্রিয় হয় বা আউটপুট পাওয়া যায়। বাটন প্রেস করার সাথে সাথেই যদি ইনপুট গ্রহণ করা না হয় এবং ৫০ থেকে ১০০ মিলিসেকেন্ড অপেক্ষা করে আবার যদি চেক করে নেয়া হয় প্রকৃতপক্ষেই বাটনটি প্রেস করা হয়েছে কিনা তাহলে কিন্তু সমস্যাটি এড়ানো যাবে আর এটাই হলো ডিবাউন্সিং কৌশল। আজ আমরা ডিবাউন্সিং কৌশল সম্পর্কে জানার চেষ্টা করবো।

![](https://dnc.techtunes.io/tDrive/tuner/ashim/373083/1.png)

## যে সকল উপকরণ লাগবে

- বাটন সুইচ
- Male to Female jumper wires
- একটা Arduino uno
- 10k ohm রেজিস্টর

## 

## আরডুইনো এর সাথে সুইচের সংযোগ এবং ডিবাউন্সিং কৌশল

আমরা এমনভাবে সার্কিটি তৈরি করবো যাতে করে 10k ohm রেজিস্টরটি সংযুক্ত হবে GND এবং D2 এর মধ্যে। আর সুইচটাকে লাগাতে হবে D2 এবং VCC এর মধ্যে। এতে করে সুইচটি Open থাকলে D2 লজিক LOW হবে এবং সুইচ Close থাকলে D2 লজিক HIGH হবে।

![](https://dnc.techtunes.io/tDrive/tuner/ashim/373083/1.png)

## প্রোগ্রাম কোড

```
const int buttonPin = 2;    
const int ledPin = 13;      

int ledState = HIGH;         
int buttonState;             
int lastButtonState = LOW;   

long lastDebounceTime = 0;  
long debounceDelay = 50;    

void setup() {
  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);

  digitalWrite(ledPin, ledState);
}

void loop() {
 
  int reading = digitalRead(buttonPin);

  if (reading != lastButtonState) {

    lastDebounceTime = millis();
  }
 
  if ((millis() - lastDebounceTime) > debounceDelay) {

    if (reading != buttonState) {
      buttonState = reading;

      if (buttonState == HIGH) {
        ledState = !ledState;
      }
    }
  }

  digitalWrite(ledPin, ledState);
  lastButtonState = reading;
}
```

## 

## প্রোগ্রাম পর্যবেক্ষণ

![](https://dnc.techtunes.io/tDrive/tuner/ashim/373083/21.png)

এর মাধ্যমে কনস্ট্যান্ট এবং প্রয়োজনীয় ভেরিয়েবল সমূহকে ডিক্লেয়ার করা হয়েছে।

![](https://dnc.techtunes.io/tDrive/tuner/ashim/373083/3.png)

pinMode(buttonPin, INPUT); এর buttonPin এর ভ্যালু 2; তাই D2 পিনকে এই ইন্সট্রাকশন ব্যবহার করে ইনপুট হিসেবে নির্দেশ করা হয়েছে।

pinMode(ledPin, OUTPUT); এর ledPin এর ভ্যালু 13 ; তাই D13 পিনকে এই ইন্সট্রাকশন ব্যবহার করে আউটপুট হিসেবে নির্দেশ করা হয়েছে।

![](https://dnc.techtunes.io/tDrive/tuner/ashim/373083/4.png)

int reading = digitalRead(buttonPin); এর মাধ্যমে D2 এর সাথে যে সুইচ লাগানো আছে তার ডিজিটাল অবস্থা রিড করে reading ভেরিয়েবলের ভ্যালু হিসেবে জমা রাখা হবে। সুইচ OPEN থাকলে reading এর ভ্যালু হবে 0 আর CLOSE থাকলে হবে 1।

if (reading != lastButtonState) {

lastDebounceTime = millis();  
 }

lastButtonState এর প্রাথমিক ভ্যালু ছিলো  LOW, তাই প্রগ্রামটি যখন প্রথম রান হবে তখন ঠিক যেমূহর্তে বাটন সুইচটি Close করা হবে তখন

reading =1 হবে এবং lastButtonState =LOW=০ তাই উপরের if এর কন্ডিশনাল reading != lastButtonState সত্য হবে এবং if এর কন্ডিশনাল স্টেটমেন্টস কার্যকর হবে।

lastDebounceTime = millis();  এখানে millis() ফাংশনের কাজ হলো যখন প্রোগ্রামটি রান হওয়া শুরু হবে তখন থেকে একটা কাউন্টার চালু হবে এবং মিলিসেসেন্ডে ভ্যালু দেবে। lastDebounceTime = millis(); এর মাধ্যমে কাউন্টারের মিলিসেসেন্ড ভ্যালুকে lastDebounceTime ভেরিয়েবলে জমা রাখবে।

![](https://dnc.techtunes.io/tDrive/tuner/ashim/373083/5.png)

debounceDelay এর প্রাথমিক ভ্যালু ছিলো 50 ;

if ((millis() - lastDebounceTime) > debounceDelay) এর ক্ষেত্রে আমরা প্রথমে বিবেচনা করি যে প্রোগ্রামটি রান হওয়ার ঠিক ৫০০ মিলি সেকেন্ড পর সুইচটি প্রথম Close করা হয়েছিলো, তাহলে lastDebounceTime=500। এক্ষেত্রে millis() এর ভ্যালু যখন 551 হবে তখন if ((millis() - lastDebounceTime) > debounceDelay) এর কন্ডিশন সত্য হবে এবং if এর কন্ডিশনাল স্টেটমেন্টস কার্যকর হবে।

কারণ (551-500)>50।

![](https://dnc.techtunes.io/tDrive/tuner/ashim/373083/6.png)

(reading != buttonState) এখন  যদি reading এবং buttonState এর ভ্যালু যদি একই না হয় তাহলে if এর কন্ডিশনাল reading != buttonState সত্য হবে এবং if এর কন্ডিশনাল স্টেটমেন্ট কার্যকর হবে অর্থাৎ buttonState = reading; হবে।

if (buttonState == HIGH) {  
 ledState = !ledState;  
 }

যদি buttonState == HIGH হয় তাহলে ledState = !ledState; হবে বা টগোল করবে, অর্থাৎ আগে HIGH থাকলে LOW হবে বা উল্টা ঘটনা ঘটবে।।

digitalWrite(ledPin, ledState); এর মাধ্যমে ১৩ নং পিন D13  তে ledState এর ভ্যালু আউটপুট দেয়া হবে।  
 lastButtonState = reading; reading ভেরিয়েবলের ভ্যালু  lastButtonState  এ জমা হবে।

আশা করছি সবাই সফলভাবে কাজটি করতে পারবেন।

## কোর্স শেষে পাবেন টেকটিউনসসস ভেরিফায়েড সার্টিফিকেট!

এই কোর্সটি আপনি সফলভাবে এবং সক্রিয় অংশগ্রহণের মাধ্যমে সমাপ্ত করে এই কোর্সের টেকটিউনস ভেরিফায়েড সার্টিফিকেট গ্রহণ করতে পারবেন। এজন্য অংশগ্রহণকারীদের জন্য প্রতি পর্বে যে যে সকল প্রশ্ন, প্রজেক্ট এবং করণীয় থাকবে তা সঠিকভাবে সম্পাদন করুন এবং কোর্স শেষে আপনাদেরকে টেকটিউনসসের নির্দেশনা অনুযায়ী এক বা একাধিক সিমুলেশন প্রজেক্ট সাবমিট করতে হবে। যেগুলো টেকটিউনসসস কতৃপক্ষ বিশ্লেষণ করে দেখবেন, এবং এর উপর ভিত্তি করে সার্টিফিকেট প্রদান করা হবে।

![](https://dnc.techtunes.io/tDrive/tuner/ashim/283338/77.jpg)

আশা করছি এরই মধ্যে অনেকেই Arduino নিয়ে কাজ শুরু করেছেন। আবার অনেকেই Arduino বোর্ড সংগ্রহ করা সহ, বেশ কিছু সমস্যার কারণে কাজ শুরু করতে পারেন নি। আমি প্রায়ই অনেকের কাছ থেকে ম্যাসেজ পাই, চেষ্টা করি সবাইকে আমার সাধ্যে অনুযায়ী সাপোর্ট দেয়ার। Arduino শেখার সাথে সম্পর্কযুক্ত যে কোন বিষয় যেমন Arduino বোর্ড এবং অন্যান্য যন্ত্রাংশ সংগ্রহ করা, কোর্সের কোন পার্ট সম্পর্কে বা প্রোগ্রাম সম্পর্কে কোন বিষয় আমাকে জানানোর জন্য টিউমেন্ট করার পাশাপাশি আমাকে [[email protected]](/cdn-cgi/l/email-protection#4b2a38232226203e262a397e7b0b322a23242465282426) এ মেইল করতে পারেন বা <https://www.facebook.com/pages/Ashim-Kumar/1530502553863914> ফেসবুকে ম্যাসেজ দিতে পারেন। সবার জন্য শুভকামনা রইলো।
