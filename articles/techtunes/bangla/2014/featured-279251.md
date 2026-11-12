---
archive_id: techtunes-279251
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 279251
title: বাড়িয়ে নিন আপনার Windows এর 100% Net Speed এবং Windows কে দেখিয়ে দিন বুড়ো
  আঙ্গুল আর উপভোগ করুন Full Speed এ Download এবং Browse। সব পদ্ধতি এখন আপনার হাতের
  মুঠোয়
slug: featured-279251
language: bn
status: publish
published_at: '2014-03-23T21:41:00+00:00'
modified_at: '2017-12-17T10:48:00+00:00'
original_url: https://www.techtunes.io/featured/tune-id/279251
author: Hit Regan
author_url: https://www.techtunes.io/tuner/hit-regan
categories:
- নির্বাচিত
tags:
- টিপস
- টিপস এন্ড ট্রিকস
- ডাউনলোড
content_hash: 78c85f8dd4d73e3a754186389fec7a051fb7076e6a69edf057a33af695cca121
archived_at: '2026-11-12T12:58:17.132623+00:00'
---

আসসালামু আলাইকুম,

কেমন আছেন সবাই। ব্যাবসার কারনে টিউন করার সময় বের করতে পারছি না। তারপরও যতটুকু সময় পাই টিউন করার চেষ্টা করি। আজকের টিউনে আমি আলোচনা করব কি ভাবে windows থেকে ১০০% নেট Speed পাওয়া যায়।

[![](https://dnc.techtunes.io/tDrive/tuner/hit-regan/279251/Increase-your-Windows-speed-to-100_fetured_bg1.jpg)](https://dnc.techtunes.io/tDrive/tuner/hit-regan/279251/Increase-your-Windows-speed-to-100_fetured_bg1.jpg)

ছবি - [Shutter Stock](http://www.shutterstock.com)

windows বিভিন্ন ভাবে bandwidth কেটে রেখে আমাদের নেট Speed কমিয়ে দেয়। এখন কি ভাবে  Windows কে  বুড়ো আঙ্গুল দেখিয়ে Full Speed এ Download এবং Browse করার যায়?

![](http://www.dbadesigns.com/wp-content/uploads/2013/09/HS_internet1.jpg)

এর জন্য কিছু পদ্ধতি রয়েছে। পদ্ধতি গুলো আমি ধাপে ধাপে তুলে ধরব। আমি নিজে এ পদ্ধতি গুলো ব্যবহার করে আমার windows থেকে ১০০% নেট Speed পাচ্ছি। তাই আপনাদের কাছে শেয়ার করলাম।

![](http://1.bp.blogspot.com/-9CjsKSOkq7I/UNS7T3GLWnI/AAAAAAAACPE/0vtCVL4-JEk/s1600/bandwidth-growth.jpg)

এ পদ্ধতিতে যাওয়ার আগে আপনার নেট Speed দেখেনিন। পদ্ধতি শেষ করার পর আপানার পিসি টি Restart দিন এবং নেট Speed চেক করে দেখুন, তাহলেই বুঝতে পারবেন আপনার নেট Speed বেরছে কিনা?

![](http://www.imboni.com/IMG/arton735.jpg)

## পদ্ধতি ১ Drain out DNS Cache

এ পদ্ধতি টি খুবই সহজ।নিচে তুলে ধরলাম।

- প্রথমে আপনি CMD অপেন করুন Run as administrator দিয়ে।(Cmd লিখে windows যে drive এ আছে সেখানে Search দিন।তাহলে cmd পাবেন)
- এখন টাইপ করুন IPCONFIG /FLUSHDNS এবং ইন্টার চাপুন।
- নিচের ছবির মত হলে Close করে দিন।

![](http://www.registryrecycler.com/blog/wp-content/uploads/2013/06/How-to-CMD-Flush-DNS-Windows8.png)

## পদ্ধতি ২ Disable Unnecessary Services

এ পদ্ধতি টি একটু ভাল ভাবে বুঝে করবেন।কিছু service আছে যে গুল আপনার নেট Speed কমিয়ে দেয়।

তাই সে গুল কে নিয়ন্তন করার পদ্ধতি নিচে দিয়ে দিলাম।

- Run গিয়ে services.msc লিখে Enter চাপুন।
- নিচের ছবির মত আসবে

![](http://blog.randait.com/wp-content/uploads/services.msc_.png)

- এখন নিচের service গুলতে right click করে properties এ click করুন।

এখন নিচের ছবির মত automatic থেকে Manual করে ok দিয়ে বের হয়ে যান।

![](http://www.registryrecycler.com/blog/wp-content/uploads/2013/06/Disable-Windows-8-Services-to-Speedup-Internet.png)

service গুলোর নাম।সব গুল service কে উপরের নিয়মে করতে হবে।

Diagnostic Policy Service, Distributed Link Tracking Client, Offline Files, Performance Logs & Alerts, Program Compatibility Assistant Service, Secondary Logon, Windows Error Reporting Service, Windows Image Acquisition (WIA)

## পদ্ধতি ৩ Reset WinSock

WinSock  রিসেট দিলে আপনার ইন্টারনেট এর গতি  বেরে যায়। তাই মঝে মাঝে WinSock  রিসেট দিবেন। কি ভাবে WinSock  রিসেট দেবেন নিচে তুলে ধরলাম।

- CMD অপেন করুন Run as administrator দিয়ে।
- এখন NETSH INT IP RESET C:\RESETLOG.txt লিখে ইন্টার চাপুন
- নিচের ছবির মত আসলে Cmd Close করুন।ব্যাস এটুকুই।

![](http://rumy.alghazzawigroup.netdna-cdn.com/wp-content/uploads/2013/09/How-to-reset-damaged-or-corrupted-TCPIP-connection12.jpg)

## পদ্ধতি ৪ Update Network Card Driver

এ পদ্ধতিতে আপনার  Network Card Driver সফট টি Update করে নিতে হবে। আমাদের motherboard সিডি তে নতুন Network Card Driver থাকে না। তাই এটিও নেট speed কম হওয়ার কারন।

কিভাবে নতুন Network Card Driver সফট টি আপডেট করব তা নিচে দিলাম।

- device manager ওপেন করুন।
- Network adapters এ ভিতরে ঢুকুন।
- আপনার Network Card Driver right click করে Update Driver Software click করুন।
- নিচের ছবির মত আসলে Search automatically for updated driver software এ click করে

আপনার Network Card Driver সফট টি আপডেট করে নিন।

![](http://www.registryrecycler.com/blog/wp-content/uploads/2013/06/Update-Windows-8-Lan-Drivers-to-Speedup-Internet.png)

## পদ্ধতি ৫ Disable Bandwidth Reserves

এ পদ্ধতিটি দুই ভাগে ভাগ করা হয়েছে। এ পদ্ধতি টি হয়ত অনেকেই জানেন। যারা জানেন না তাদের জন্য কঠিন।

### পদ্ধতি 1

- Run গিয়ে gpedit.msc টাইপ করে ইন্টার চাপুন।নিচে ছবির মত আসবে

![](http://3.bp.blogspot.com/-Zh02iP2-tPo/T2yK4J5IVBI/AAAAAAAAABc/pFjjoaLAtI4/s1600/image001.jpg)

- এবার এভাবে ধাপে ধাপে যান  Local Computer Policy\Computer Configuration\Administrative Templates\Network\QoS Packet Scheduler
- এবার Limit reservable bandwidth  এ  right click করে Edit এ click করুন।
- নিচের ছবির মত আসলে enabled এ click করুন এবং  Bandwidth limit to”0 লিখে ok দিয়ে বের হয়ে যান।

![](http://www.registryrecycler.com/blog/wp-content/uploads/2013/06/Increase-Windows-8-Internet-Speed-By-Limiting-Bandwidth.png)

### পদ্ধতি 2

- Run গিয়ে regedit.exe টাইপ করে ইন্টার চাপুন।নিচে ছবির মত আসবে

![](http://0.tqn.com/d/pcsupport/1/0/t/8/-/-/registry-editor-windows-7.jpg)

- এবার এভাবে ধাপে ধাপে যান HKEY\_LOCAL\_MACHINE\SOFTWARE\Policies\Microsoft\Windows
- এবার Pshed click করুন।দেখবেন ডান পাশে এই লিখাটি আছে NonBestEffortLimit।
- NonBestEffortLimit right click করে Modify এ ঢুকুন।

![](http://cdn1.dottech.org/wp-content/uploads/2012/01/2012-01-22_1746551.png)

- এখন Decimal এ click করুন এবং  Value data 1 থেকে 100 দিন।তারপর ok দিন।

![](http://www.registryrecycler.com/blog/wp-content/uploads/2013/08/Disable-Bandwidth.jpg)

সব গুল ধাপ শেষ করে আপনার  computer টি Restart দিন। এখন উপভোগ করুন আপনার windows এ ১০০% Bandwidth। দেখবেন আপনার নেট অনেক খানি ফাস্ট হয়েছে। সব গুল পদ্ধতি আপনি ভাল ভাবে শেষ করতে পারলে windows এ ১০০% Bandwidth পারবেন।

আপনাদের সুবিধার জন্য আমি ভিডিও টিউট্রিয়াল দিয়ে দিচ্ছি

[Embedded External Content: https://www.youtube.com/embed/SLKA1NRXTJE?feature=oembed]

কার যদি কোন যায়গায় বুঝতে সমস্যা হয় তাহলে আমাকে যানাতে পারেন আমি সাহায্য করতে চেষ্টা করব।

যদি কোন ভুল হয়ে থাকে তাহলে আমাকে জানাবেন আমি ঠিক করে দেব।

আজ এখানেই শেষ করছি।

আমার জন্য দোয়া করবেন, আমার ব্যাবসার জন্য দোয়া করবেন।

আল্লাহ্‌ হাফেজ।

> Hit Regan এর সাথে থাকুন আর  All time Hit থাকুন।  ![:mrgreen:](https://dnc.techtunes.io/wp-includes/images/smilies/mrgreen.png) ![:mrgreen:](https://dnc.techtunes.io/wp-includes/images/smilies/mrgreen.png) ![:mrgreen:](https://dnc.techtunes.io/wp-includes/images/smilies/mrgreen.png)
