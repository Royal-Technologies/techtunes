---
archive_id: techtunes-298299
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 298299
title: 'সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব-০৭] :: User defined Type -২'
slug: programming-298299
language: bn
status: publish
published_at: '2014-08-12T06:49:00+00:00'
modified_at: '2014-08-12T08:44:00+00:00'
original_url: https://www.techtunes.io/programming/tune-id/298299
author: Hasnat Riaz
author_url: https://www.techtunes.io/tuner/hasnat_riaz
categories:
- প্রোগ্রামিং
tags: []
content_hash: 878e64af9b5283c691c12070d5718c2dee3fdb0d29d737c90660ff894fdc4218
archived_at: '2026-11-22T05:10:51.396797+00:00'
---

### [ডেভেলপমেন্ট ইন C শার্প](https://www.techtunes.io/chain-tunes/software-development-in-c-sharp "ডেভেলপমেন্ট ইন C শার্প")

- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০১] :: নবীনদের জন্য -১](https://www.techtunes.io/programming/tune-id/292139 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০১] :: নবীনদের জন্য -১")
- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০২] :: নবীনদের জন্য -২](https://www.techtunes.io/programming/tune-id/292630 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০২] :: নবীনদের জন্য  -২")
- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০৩] :: নবীনদের জন্য-৩](https://www.techtunes.io/programming/tune-id/293018 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০৩] :: নবীনদের জন্য-৩")
- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০৪] :: নবীনদের জন্য-৪](https://www.techtunes.io/programming/tune-id/293412 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০৪] ::  নবীনদের জন্য-৪")
- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০৫] :: নবীনদের জন্য-৫](https://www.techtunes.io/programming/tune-id/294344 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C# )- [পর্ব-০৫] ::  নবীনদের জন্য-৫")
- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব-০৬] :: User defined type -১](https://www.techtunes.io/programming/tune-id/297241 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব-০৬] :: User defined type -১")
- সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব-০৭] :: User defined Type -২
- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব-০৮] :: Exception Handling -১](https://www.techtunes.io/tutorial/tune-id/290347 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব-০৮] :: Exception Handling -১")
- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব -০৯] :: Exception Handling -২](https://www.techtunes.io/tutorial/tune-id/290598 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব -০৯] :: Exception Handling -২")
- [সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব-১০] :: Exception Handling -৩](https://www.techtunes.io/programming/tune-id/291489 "সফটওয়্যার ডেভেলপমেন্ট ইন C শার্প (C#)- [পর্ব-১০] :: Exception Handling -৩")

গতপর্বে আমরা User defined Type কি তা আলোচনা করেছিলাম। অল্পস্বল্প কিছু বেসিক কথাবার্তাও বলেছিলাম।গতপর্বে যেই প্রোগ্রামটা দেখিয়েছিলাম সেখানে বুঝানোর সুবিধার্থে Object Oriented এর কিছু rules  violate করেছিলাম।এই পর্বে আরেকটি প্রোগ্রাম দিয়ে Object Oriented এর data must be private এই rules দিয়ে কোড করে দেখাবো।শুরুতেই Person নামে নতুন একটা টাইপ বানালাম অর্থাৎ Person.cs নামে একটি ক্লাস নিলাম। ক্লাসের মধ্যে তিনটি private  ভেরিয়েবল, দুইটি constructor এবং একটি মেথড নিচের মতো করে লিখলাম।

![](https://dnc.techtunes.io/tDrive/tuner/hasnat_riaz/298299/personClass.png)

এবার প্রোগ্রামটির UI দেখে নিই:

![](https://dnc.techtunes.io/tDrive/tuner/hasnat_riaz/298299/PersonUI.png)

Save এবং Show Full Name বাটনের ক্লিক ইভেন্টে নিচের মতো করে কোড লিখলাম:

![](https://dnc.techtunes.io/tDrive/tuner/hasnat_riaz/298299/UI-Class.png)

এরপর প্রোগ্রামটি রান করিয়ে ইউজার নাম ইনপুটদিয়ে Save বাটনে ক্লিক করলে নামগুলো সেইভ হবে।

![](https://dnc.techtunes.io/tDrive/tuner/hasnat_riaz/298299/PersonUI-having-input.png)

এরপর show Full Name বাটনে ক্লিক করলে person টির Full Name দেখতে পাবেন।

![](https://dnc.techtunes.io/tDrive/tuner/hasnat_riaz/298299/Output.png)

এই পর্ব আপাতত এতোটুকুই।
