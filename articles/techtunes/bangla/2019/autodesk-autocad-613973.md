---
archive_id: techtunes-613973
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 613973
title: 'অটোক্যাডে স্কেলিং [পর্ব-০১] :: বিভিন্ন ধরনের স্কেলিং ও তার সংশ্লিস্ট  বিভিন্ন
  পদ্ধতি নিয়ে আলোচনা'
slug: autodesk-autocad-613973
language: bn
status: publish
published_at: '2019-02-25T15:46:00+00:00'
modified_at: '2019-03-04T07:13:00+00:00'
original_url: https://www.techtunes.io/autodesk-autocad/tune-id/613973
author: ইঞ্জিনিয়ার আলী কায়সার
author_url: https://www.techtunes.io/tuner/ali-kaiser
categories:
- অটোডেস্ক অটোক্যাড
tags:
- অটোক্যাড
content_hash: 9720d20063b7878f6242dd79e6602b2282703c13b753b4d17061824a7c3b3c36
archived_at: '2026-11-12T12:28:31.659896+00:00'
---

এই আর্টিক্যালে আমরা  বিভিন্ন ধরনের স্কেলিং নিয়ে আলোচনা করব। অটোক্যাডে স্কেলিং এর কাজ অনেক বিশাল ব্যপ্তি জুড়ে আছে। তাই আমরা বিস্তারিত আলোচনার সুবিধার্থে এই টপিকটিকে দুই পর্বে ভাগ করেছি। এটি হল আমাদের স্কেলিং নিয়ে আলোচনার প্রথম পর্ব। আলোচনার বিভিন্ন পর্যায়ে বিষয়গুলো সহজে অনুধাবনের জন্য আমরা কিছু উদাহরণের সাহায্যও নিয়েছি।

**সাধারণ স্কেল কমান্ড**

অটোক্যাডে Scale কমান্ড  ব্যবহার করে আপনি  একটি অবজেক্টের সাইজ পরিবর্তন করতে পারেন। scale command ব্যাখ্যা করার জন্য আমি একটি সাধারণ window block ব্যবহার করব যার  X-axis বরাবর দৈর্ঘ্য 10  ইউনিট এবং Y-axis বরাবর দৈর্ঘ্য 15 ইউনিট।

[![Figure 1](https://projuktiteam.com/wp-content/uploads/2019/02/110-233x300.png)](https://projuktiteam.com/wp-content/uploads/2019/02/110.png)

Home tab এর Modify panel থেকে scale tool সিলেক্ট করুন অথবা কমান্ড লাইনে টাইপ করুন SC

[![Figure 2](https://projuktiteam.com/wp-content/uploads/2019/02/24-300x82.png)](https://projuktiteam.com/wp-content/uploads/2019/02/24.png)

এখন,  window drawing এর মাধ্যমে অবজেক্ট সিলেক্ট করুন এবং enter প্রেস করুন। একটি অবজেক্ট যখন স্কেল করা হয় তখন Base-point টা fixed  থাকবে, এক্ষেত্রে আমি  window এর lower left corner কে  Base-point সিলেক্ট করলাম।

command line এ তখনি আপনাকে  scale factor টি specify করতে বলবে। এই scale factor আসলে আপনার window এর final size নির্ধারণ করবে।

scale factor যদি ০ থেকে 1 হয়, তবে তা আপনার অবজেক্ট এর size টা ছোট করবে (এক্ষেত্রে window)। যেমনঃ scale factor যদি 0.5  হয় তবে তা আপনার ড্রয়িং এর অরিজিনাল সাইজের সাপেক্ষে অর্ধেক সাইজে কমিয়ে আনবে,  scale factor যদি 0.25 হয়, তবে তা আপনার আসল অবজেক্ট এর এক-চতুর্থাংশে সাইজ কমিয়ে আনবে।

একইভাবে,  scale factor যদি 1 এর চাইতে বড় হয়, তখন ড্রয়িং এর সাইজ অরিজিনালের চেয়ে বড় হয়। যেমনঃ scale factor যদি 2 হয়, সাইজ আসল ড্রয়িং এর দ্বিগুন হয় এবং scale factor যদি 3 হয়, তবে ড্রয়িং এর সাইজ  অরিজিনালের তিনগুন হয়।

scale factor  টাইপ করে Enter প্রেস করুন। এক্ষেত্রে আমি  scale factor ব্যবহার করলাম 2, অবজেক্ট এর final size দাঁড়াবেঃ X-axis বরাবর দৈর্ঘ্য 20 unit এবং Y-axis বরাবর দৈর্ঘ্য 30 unit।

অন্যান্য টিপস ঃ যদি আপনি আপনার অরিজিনাল অবজেক্ট scale পরিবর্তনের পরও রেখে দিতে চান, তবে যখন  scale factor আপনাকে ইনপুট করতে বলবে তখন  command line  থেকে “Copy” option টি সিলেক্ট করতে পারেন।

[![Figure 3](https://projuktiteam.com/wp-content/uploads/2019/02/31-300x15.png)](https://projuktiteam.com/wp-content/uploads/2019/02/31.png)

**রেফারেন্স ব্যবহার করে স্কেলিংঃ**

একটি অবস্থা  বিবেচনা করি, আমাদের পূর্ববর্তী উদাহরণে যে window ব্যবহার করেছি  ঠিক সেরকম ই যার দৈর্ঘ্য X-axis বরাবর 10 units ও উচ্চতা 15 units। এখন আমরা চাচ্ছি যে,  X-axis বরাবর দৈর্ঘ্য পরিবর্তন করে 17 unit  করতে আর উচ্চতা  যেন সমানুপাতে নির্ধারিত হয় তা নিশ্চিত করতে।

এখন, এক্ষেত্রে আপনি ব্যবহার করতে পারেন scale command এর “Reference” option যা আপনার অবজেক্ট এর সাইজকে সমানুপাতে পরিবর্তিত করবে।

আপনি আবারো scale command টা দিয়ে শুরু করুন  এবং window সিলেক্ট করে enter প্রেস করুন। এখন,  window এর lower left corner কে  base point হিসেবে সিলেক্ট করুন, আপনি চাইলে অন্য কোন পয়েন্ট কেও base point হিসেবে সিলেক্ট  করতে পারেন।

এখন,  command line আপনাকে আপনার scale factor সিলেক্ট করতে বলবে, এই সিলেকশনের সময় আপনি command line থেকে Reference option টা সিলেক্ট করুন।

[![Figure 4](https://projuktiteam.com/wp-content/uploads/2019/02/41-300x15.png)](https://projuktiteam.com/wp-content/uploads/2019/02/41.png)

এখন command line -এই আপনাকে reference length টা specify করতে বলবে। টাইপ করুন 10 ও প্রেস করুন enter, এটা হল X-axis বরাবর window এর বর্তমান দৈর্ঘ্য।

এখন,  command line আপনাকে বলবে, আপনি window এর 10 unit লাইনের জন্য যে নতুন দৈর্ঘ্য নির্ধারণ করতে চাচ্ছেন তা টাইপ করতে। এক্ষেত্রে টাইপ করুন 17  এবং আবারো প্রেস করুন enter

এখন,  window এর base পরিবর্তিত হয়ে হবে দৈর্ঘ্যে  17 units এবং window এর উচ্চতা automatically সমানুপাতে পরিবর্তিত হয়ে যাবে।

কাজেই, আপনি বুঝতে পারছেন যে, এক অবজেক্ট এর সাপেক্ষে আরেক অবজেক্ট এর সাইজ পরিবর্তন করতে চান অথবা  আমাদের এই উদাহরণের মত একটি reference length এর সাপেক্ষে  কাজটি করতে চান, তবে এই কমান্ডটি বেশ উপকারী। কারণ, এক্ষেত্রে আপনাকে scale factor নির্ধারণ করে দেয়া লাগবে না।

**স্কেলিং ব্লকসঃ**

উপরে বর্ণিত স্কেল কমান্ড block references এর জন্য ও কাজ করবে  এবং আপনার ব্লককে scale করার জন্য  কোন বিশেষ টুল দরকার হবে না। তা যাই হোক, আপনি X, Y এবং Z axis বরাবর আপনার ব্লককে ভিন্ন স্কেলে রাখতে পারেন যা আমি  এখানে ব্যখ্যা করবে। আমি এখানে একটি সিম্পল chair এর ড্রয়িং দিয়ে তা ব্যখ্যা করব।

![5](https://projuktiteam.com/wp-content/uploads/2019/02/5-300x172.png)

প্রথমে, আমাদেরকে  এই সিম্পল অবজেক্টকে ব্লকে পরিবর্তন করতে হবে এবং  এজন্য, আপনি ব্যবহার করতে পারেন B command।

আপনি শুধু এটা নিশ্চিত করবেন যে, ব্লক তৈরি করার সময় “Scale Uniformly” box কে image এর মতো **unchecked**রেখেছেন।

![6](https://projuktiteam.com/wp-content/uploads/2019/02/61-300x198.png)

![](https://sourcecad-f5hmctaeshq3us.netdna-ssl.com/wp-content/uploads/2018/09/6-644x426.png)

একবার আপনার ব্লক তৈরি হয়ে গেলেই আপনি আপনার scales  পরিবর্তন করতে পারবেন এবং তারপর আপনার ড্রয়িং ইনসার্ট করতে পারবেন। ব্লক ইনসার্ট করার জন্য I command ব্যবহার করুন।

টাইপ করুন I এবং press করুন  enter, Insert window এখন স্ক্রিনে দেখাবে।

চলুন, আমরা X-axis  বরাবর scale factor ব্যবহার করি 1,  Y-axis বরাবর  1.5  এবং আমি  Z axis বরাবর রাখলাম 1.

![](https://sourcecad-f5hmctaeshq3us.netdna-ssl.com/wp-content/uploads/2018/09/7-644x291.png)

![7-800x362](https://projuktiteam.com/wp-content/uploads/2019/02/7-800x362-300x136.png)

এখন ক্লিক করুন OK এবং block ইনসার্ট করার জন্য একটি point এ ক্লিক করুন। এই ব্লকটি দেখতে image B এর মতো হবে যেখানে image A  হল overall scale 1 এ অরিজিনাল ব্লকটি।

![8-800x349](https://projuktiteam.com/wp-content/uploads/2019/02/8-800x349-300x131.png)

![](https://sourcecad-f5hmctaeshq3us.netdna-ssl.com/wp-content/uploads/2018/09/8-644x281.png)

এক্ষেত্রে যেহেতু আপনি block টা পরিষ্কারভাবে দেখতে পাচ্ছেন, এক্ষেত্রে Y direction এ  factor  1.5 হবে শুধু, অন্য  direction এ কোন পরিবর্তন হবে না।

এই পর্বে আমাদের আলোচনা এখানেই সীমাবদ্ধ রাখলাম। দ্বিতীয় পর্বে আমরা অটোক্যাডে স্কেলিং এর বাকি বিষয়গুলি নিয়ে আলোচনা করব। আপনারা  এই আর্টিক্যালের ইন্সট্রাকশনগুলি অনুসরণ করে খুব সহজেই আশা করি স্কেলিং এর কাজগুলি করে ফেলতে পারবেন। আপনাদের সবার জন্য থাকলো শুভকামনা।

[দ্বিতীয় পর্বঃ অটোক্যাডে বিভিন্ন ধরনের স্কেলিং ও তার সংশ্লিস্ট বিভিন্ন পদ্ধতি নিয়ে আলোচনাঃ পর্ব ২](https://projuktiteam.com/5156/how-to-scale-in-autocad/)
