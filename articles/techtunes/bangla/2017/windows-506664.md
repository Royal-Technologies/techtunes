---
archive_id: techtunes-506664
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 506664
title: কোন প্রকার সফটওয়্যার ছাড়াই পেনড্রাইভটি Bootable করুন।
slug: windows-506664
language: bn
status: publish
published_at: '2017-08-03T04:24:00+00:00'
modified_at: '2017-08-03T07:24:00+00:00'
original_url: https://www.techtunes.io/windows/tune-id/506664
author: টেক হান্টার
author_url: https://www.techtunes.io/tuner/madesk-com
categories:
- উইন্ডোস
tags:
- bootable
- OS bootable
- pendrive bootable
content_hash: dcef64fde00b205ccbd832fc087ff4e88f79d3b212dbb9b2b90507a5e41afb6b
archived_at: '2026-11-12T12:44:01.365113+00:00'
---

আসসালামু আলাইকুম

শিরোনার দেখেই নিশ্চয় বুঝে গেছেন যে আমি কি বিষয়ে টিউন করতে যাচ্ছি হ্যা আজকে আমি আপনাকে দেখাবে যে কিভাবে আপনি অতি সহজেই কোন প্রকার সফটওয়্যার ছাড়াই আপনার পেনড্রাইভটি Bootable করবে পারবেন।

![TechsBD](https://dnc.techtunes.io/tDrive/tuner/madesk-com/506664/thumbnail.jpg)

এ বিষয়ে অনেকেরই একটি কমন প্রশ্ন থাকবে পারে যে, ভাইয়া অনেক ফ্রি সফটওয়্যার দিয়েই তো অতি সহজেই পেনড্রাইভ Bootable করা যায় তাহলে আপনার পদ্ধতি ফলো করতে হবে কেন।

উত্তরঃ- হ্যা, অনেক Freeware Software আছে যার মাধ্যমে আপনি সহজেই কয়েক ক্লিকেই আপনার পেনড্রাইভটি  Bootable করতে পারবেন কিন্তু একবার ভাবুন তো যদি কোন কারণে আপনার কাছে সফটওয়্যার না থকে তখন আপনি  কি করবেন। আবার হয়তো দেখা যায় যে আপনার কোন বন্ধুর বাসায় গিয়েছেন ওর কম্পিউটারে উইন্ডোজ দিতে হবে কিন্তু ওর তো নেট কানেকশন ও সফটওয়্যার কোনটাই নেই তখন আপনি এই পদ্ধতিটি কাজে লাগাতে পারবেন এককথায় আমার পরার্মশ হল যেই কাজটি সফটওয়্যার ছাড়াই হচ্ছে সেই কাজের জন্য আপনি শুধু শুধু সফটওয়্যারের উপর ভরসা করবেন কেন।

## এখন নতুনদের জন্যঃ-

পেনড্রাইভ Bootable আসলে কিঃ- সহজ কথায় আপনি যখন আপনার কম্পিউটারে উইন্ডোজ দেবার জন্য সিডি বা ডিভিডি আপনার রোমে প্রবেশ করান তখন তা সেটা BIOS এর সাহায্যে Boot হয় এবং আপনি আপনার কম্পিউটারে উইন্ডোজ দিতে পারেন। সেই একই কাজটি আপনার পেনড্রাইভ থেকে করা সম্ভব। অর্থাৎ আপনি আপনার পেনড্রাইভ কেও DVD Writer এর মত Bootable Device বানাতে পারেন।

কোন কোন ক্ষেত্রে এটি প্রয়োজন পড়েঃ- DVD Writer নেই, উইন্ডেজ ডিক্স নেই, কোন Bootable সিডি বুথ করার জন্য যেমন: Ultimate Boot Disk।

তো শুরু করা যাক, প্রথমেই আপনার Pendrive টিতে যদি কোন দরকারি ফাইল থাকে তার হার্ডড্রাইভে কপি করে রাখুন। মোটকথা Pendrive টি ফাকা করে রাখুন। এবার আপনার কম্পিউটারে Pendrive টি প্রবেশ করান। এবং নিচের কমান্ডগুলি ভালোভাবে Follow করুন।

**Start Command Prompt (CMD)**

1. Insert your USB Flash Drive to your running windows computer. As the first step, we need to run Command Prompt as Administrator. To do this, we need to find cmd by typing 'cmd' in the search box on Windows Start Menu. After search result for 'cmd' appears, right click on it and select "Run as Administrator".

2. Type "**diskpart"** on Command Prompt and press Enter. Wait for a while until the **DISKPART** program run.

3. Type "**list disk"** to view active disks on your computer and press Enter. There would be seen that the active disks shown as Disk 0 for the hard drive and Disk 1 for your USB Flash Drive with its total capacity. **[Remember: Disk 1 as USB Flash Drive will change when you use multiple disks to your computer.]**

4. Type "**select disk 1"** to determine that disk 1 would be processed in the next step then press Enter.

5. Type '**clean**' and press Enter to remove all of data in the drive.

6. Type '**create partition primary**' and press Enter. Creating a primary partition and further recognized by Windows as 'partition 1'.

7. Type '**select partition 1**' and press Enter. Choosing the 'partition 1' for setting up it as an active partition.

8. Type '**active**' and press Enter. Activation current partition.

9. Type '**format fs=ntfs quick**' and press Enter. Formatting current partition as NTFS file system quickly.

10. Type '**exit**' and press Enter. After leaving **DISKPART** program just close the Command Prompt Program.

**End Command Prompt (CMD)**

ব্যাস কাজ শেষ আপনার পেনড্রাইভটি Bootable জন্য Assign হয়েছে। এখন আপনি যেই যা Bootable করতে চান যেমন Windows 7, 8, 10 অথবা, অন্যকোন Boot Disk যেমন Ultimate Boot Disk, Hiren's.BootCD, Kaspersky Rescue Disk, Magic Boot Disk ইত্যাদি ইত্যাদি। শুধুমাত্র তা যদি .zip, .rar, .iso ফাইলে তা Extract করে সমস্ত ফাইলগুলো আপনার পেনড্রাইভে কপি করুন। ব্যাস হয়ে গেল আপনার Bootable Pendrive. ব্যবহার করার জন্য আপনার পিসি টি একবার রিস্টার্ট দিন ও Press any key অধবা Boot Menu থেকে কাঙ্খিত পেনড্রাইভটি Run করান। তারপর কি অবস্থা উপভোগ করুন।

**নোটঃ-** এটি একটি সাধারণ টিউটোরিয়া হয়তো আপনি এই পদ্ধতিটি জানেন কিন্তু অনেকেই জানেনা সুতরাং বাজে টিউমেন্ট করবেননা দয়া করে। কারো বুঝতে সমস্যা হলে নিচে টিউমেন্ট করুন অথবা আমাকে ফেসবুকে নক করতে পারেন।

ফেসবুকে আমি : [http://www.facebook.com/drmabaki](https://www.facebook.com/drmabaki)

যারা ভিডিও টিউটোরিয়াল দেখতে পছন্দ করেন তারা নিচে এই টিউটোরিয়াটি ভিডিও আকারে দেখেতে পারেন।

[Embedded External Content: https://www.youtube.com/embed/KziE\_mcTisY?feature=oembed]
