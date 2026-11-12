---
archive_id: techtunes-613971
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 613971
title: 'অটোক্যাডে স্কেলিং [পর্ব-০২] :: বিভিন্ন ধরনের স্কেলিং ও তার সংশ্লিস্ট বিভিন্ন
  পদ্ধতি নিয়ে আলোচনা'
slug: autodesk-autocad-613971
language: bn
status: publish
published_at: '2019-02-25T15:51:00+00:00'
modified_at: '2019-03-04T07:10:00+00:00'
original_url: https://www.techtunes.io/autodesk-autocad/tune-id/613971
author: ইঞ্জিনিয়ার আলী কায়সার
author_url: https://www.techtunes.io/tuner/ali-kaiser
categories:
- অটোডেস্ক অটোক্যাড
tags:
- আটোক্যাড
content_hash: 8e94c66978ead38392bb5d1825f4373a9833e4814a436efdd84b1fcf584b105f
archived_at: '2026-11-12T12:28:31.642289+00:00'
---

[প্রথম পর্বঃ অটোক্যাডে বিভিন্ন ধরনের স্কেলিং ও তার সংশ্লিস্ট  বিভিন্ন পদ্ধতি নিয়ে আলোচনাঃ পর্ব ১](https://projuktiteam.com/5113/how-to-scale-in-autocad-1/)

অটোক্যাডের স্কেলিং এর বিভিন্ন বিষয় নিয়ে পর্ব ১ এ আমরা কিছু গুরুত্বপূর্ণ বিষয় আলোচনা করেছিলাম। এর ধারাবাহিকতায় আমরা পর্ব ২ এর আলোচনা শুরু করছি।

**Xrefs ও images এর স্কেলিং ঃ**

Xrefs অথবা external references হল  DWG files এর মত, PDF  অথবা images যা ড্রয়িং এ ইনসার্ট  করা যায় reference হিসেবে। আপনি Xrefs ইনসার্ট করার সময় তা স্কেল করতে পারেন অথবা আপনি ড্রয়িং এ ইনসার্ট করার পরও তাদের সাইজ পরিবর্তন করতে পারেন।

এই উদাহরণের জন্য, আমি  একটি DWG file ব্যবহার করব কিন্তু আপনি একই প্রক্রিয়া PDF file ও Images এর জন্যও ব্যবহার করতে পারেন।

টাইপ করুন ATTACH এবং press করুন  enter, এর ফলে attach window টি ওপেন হবে। নিচের ছবির মত format dropdown থেকে  DWG  সিলেক্ট করুন।

![9-800x702](https://i0.wp.com/projuktiteam.com/wp-content/uploads/2019/02/9-800x702.png?resize=300%2C263&ssl=1)

![](https://sourcecad-f5hmctaeshq3us.netdna-ssl.com/wp-content/uploads/2018/09/9-644x565.png)

এর ফলে Xref window টা ওপেন হবে যেখানে  বিভিন্ন axes এর জন্য বিভিন্ন scale নির্ধারণ করতে পারেন, এমনকি আপনি attached Xref এর অরিজিনাল  সাইজ রাখতে চাইলে সব axes এর জন্য মান 1 রাখতে পারেন।

![](https://sourcecad-f5hmctaeshq3us.netdna-ssl.com/wp-content/uploads/2018/09/10-644x474.png)

![10](https://i1.wp.com/projuktiteam.com/wp-content/uploads/2019/02/101.png?resize=300%2C221&ssl=1)

এমনকি Xref এড করার পর আপনি  property palette ব্যবহার করে এর scale পরিবর্তন করতে পারেন। এজন্য drawing area থেকে  সিলেক্ট করুন Xref, এরপর টাইপ করুন PR এবং press করুন enter। এর ফলে property palette ওপেন হবে,  palette এ scroll down করুন এবং property palette এর geometry tab  থেকে scale পরিবর্তন করুন।

[![11](https://projuktiteam.com/wp-content/uploads/2019/02/111-184x300.png)](https://projuktiteam.com/wp-content/uploads/2019/02/111.png)

Attached Xref এর overall scale পরিবর্তন করতে আপনি scale command ব্যবহার করতে পারেন। একইভাবে, আপনি attached images এবং PDF files এরও scale পরিবর্তন করতে পারেন। এখানে আমি উদাহরণ হিসেবে একটি ফ্লোর প্ল্যানের image কে  attach করব।

টাইপ করুন ATTACH এবং press করুন enter, তারপর সিলেক্ট করুন  একটি image এবং click করুন OK। তারপর ড্রয়িং এ একটি  point নির্দিষ্ট করুন এটি ইনসার্ট করার জন্য এবং default scale  1 কে গ্রহন করার জন্য enter প্রেস করুন।

আমার ড্রয়িং এ ইনসার্ট করার পর এটি দেখতে  এরকম দেখাচ্ছে।

![a-800x626](https://i0.wp.com/projuktiteam.com/wp-content/uploads/2019/02/a-800x626.png?resize=300%2C235&ssl=1)

![](https://sourcecad-f5hmctaeshq3us.netdna-ssl.com/wp-content/uploads/2018/09/a-644x504.png)এই image টা ঠিকভাবে  scaled না, যেমন image এ 10′ দৈর্ঘ্য আশাকরি এই ফ্লোর প্ল্যানের উপরের দিকে 10′ দৈর্ঘ্যের reference লাইনটি নিয়ে।

scale command এর কাজ শুরু করার জন্য  টাইপ করুন SC এবং press করুন enter। এখন সিলেক্ট করুন floor plan image এবং আবারো press করুন enter। base point হিসেবে image এর top left corner  সিলেক্ট করুন এবং তারপর command line থেকে reference option সিলেক্ট করুন।

এখন,  reference  কে specify করার জন্য প্রথমে point A তে click  করুন  এরপর point B তে এবং টাইপ করুন 10′ এবং আবারো press করুন enter। এখন,  AB এর দূরত্ব 10′  এ পরিবর্তিত হল এবং অন্যান্য দূরত্বও একইসাথে পরিবর্তিত হয়ে গেল।

[![b](https://projuktiteam.com/wp-content/uploads/2019/02/b-300x133.png)](https://projuktiteam.com/wp-content/uploads/2019/02/b.png)

এক্ষেত্রে, আমি ব্যবহার করেছি Architectural units, তাই  আপনি এই ড্রয়িং এ scale option ব্যবহারের পূর্বে unit পরিবর্তন করে architectural করে নিন। Architectural এ পরিবর্তন করার জন্য টাইপ করুন UN এবং press করুন enter এবং তারপর এই image এর মত Length drop-down থেকে select করুন Architectural।

[![c](https://projuktiteam.com/wp-content/uploads/2019/02/c-269x300.png)](https://projuktiteam.com/wp-content/uploads/2019/02/c.png)

**স্কেলিং হ্যাচঃ**

যখন আপনি কোন closed area তে  hatch ব্যবহার করেন তখন এটি দেখতে solid pattern এর মত দেখায় অথবা এটি দেখাই যায় না। এটা, মাঝে মাঝেই  hatch এর সাথে সামঞ্জস্যহীন scale সিলেকশনের জন্যই হয় যা ঠিক করতে চাইলে hatch creation panel  থেকে সহজেই adjust করা যায়।

Draw panel  থেকে hatch command সিলেক্ট করে কাজ শুরু করুন অথবা ব্যবহার করুন H command। একটি temporary hatch creation tab দেখা যাবে। hatch pattern সিলেক্ট করুন এবং যে area তে আপনি hatch টা  add করতে চান তা specify  করুন।

যদি hatch pattern এর size  খুব ই ছোট হয় অথবা খুব বড় হয় তখন নিচের image এর মত properties panel এর  scale field থেকে এর  scale পরিবর্তন করে নিন।

[![12](https://projuktiteam.com/wp-content/uploads/2019/02/121-300x27.png)](https://projuktiteam.com/wp-content/uploads/2019/02/121.png)

যদি pattern খুব ছোট হয় তবে  আপনি scale field এ মান বৃদ্ধি করতে পারেন এবং যদি  pattern অনেক widely spaced হয় তবে আপনি scale value হ্রাস করে দিতে পারেন।  এখানে আমরা দেখিয়েছি,  ANSI 31 hatch pattern বিভিন্ন স্কেলে (1, 0.05 and 50) দেখতে কেমন দেখায়।

![13-800x304](https://i1.wp.com/projuktiteam.com/wp-content/uploads/2019/02/13-800x304.png?resize=300%2C114&ssl=1)

![](https://sourcecad-f5hmctaeshq3us.netdna-ssl.com/wp-content/uploads/2018/09/13-644x244.png)

এমনকি,  hatch এড করার সময় আপনি যদি তা আবার সিলেক্ট করেন তবে তা hatch creation tab আবার ওপেন করবে যেখানে আপনি hatch scale অথবা অন্যান্য properties কে modify করতে পারবেন।

আপনি property palette থেকেও hatch scale পরিবর্তন করতে পারেন, এজন্য select করুন hatch pattern, তারপর, টাইপ করুন PR এবং press করুন enter। এর ফলে property palette ওপেন হবে,  scroll down করে Pattern section এ যান এবং নিচের image এর মত scale  পরিবর্তন করুন।

[![14](https://projuktiteam.com/wp-content/uploads/2019/02/141-184x300.png)](https://projuktiteam.com/wp-content/uploads/2019/02/141.png)

**স্কেলিং ভিউপোর্টঃ**

ড্রয়িং সাধারণত model space এ করা হয়, কিন্তু text, title blocks এবং ড্রয়িং সম্পর্কিত অন্যান্য information গুলো সাধারণত layout অথবা paper space এ এড করা হয়। এই সেকশনে, আমি paper space এ কিভাবে viewport তৈরি করা হয় এবং তাদের scale কিভাবে ড্রয়িং এর সাথে সামঞ্জস্যপূর্ণভাবে পরিবর্তন করা হয় তা আলোচনা করব।

আমি এই সিম্পল  elevation drawing  টা ব্যবহার করব এই ঘটনাটি ব্যখ্যা করার জন্য।

![15](https://i2.wp.com/projuktiteam.com/wp-content/uploads/2019/02/152.png?resize=300%2C166&ssl=1)

![](https://sourcecad-f5hmctaeshq3us.netdna-ssl.com/wp-content/uploads/2018/09/15-644x357.png)

এই ড্রয়িংটি আছে model space এ, কিন্তু আমরা  এটি layout এ different scale এর viewport এ ইনসার্ট করব। এটি শুরু করার জন্য bottom left tab এ  Layout 1 সিলেক্ট করুন, এছাড়াও আপনি + icon ক্লিক করেও  new layout tab ওপেন করতে পারেন।

[![16](https://projuktiteam.com/wp-content/uploads/2019/02/161.png)](https://projuktiteam.com/wp-content/uploads/2019/02/161.png)

এই layout space একটি default viewport নিয়ে ওপেন হবে এবং আপনার model space drawing টি এর সাথে automatically যুক্ত হয়ে যাবে। আগের যে viewport আছে, তা Delete করুন এবং তারপর,  image এ দেখানো উপায়ে Layout tab থেকে Page Setup option এ click করুন।

[![17](https://projuktiteam.com/wp-content/uploads/2019/02/171-300x36.png)](https://projuktiteam.com/wp-content/uploads/2019/02/171.png)

এরপরে page setup manager window তে Modify বাটনে Click করুন এবং layout এর বিভিন্ন settings যেমনঃ printer/plotter এবং page size প্রভৃতি পরিবর্তন করুন। আমি plotter এ সিলেক্ট করেছি DWG to PDF.pc3 এবং paper size এ ANSI A।

এসব পরিবর্তনের পর সব open windows থেকে বের হতে OK ক্লিক করুন। এখন, আমরা আমাদের viewport তৈরির জন্য প্রস্তুত।

টাইপ করুন -VPORTS এবং press করুন enter (VPORTS এর আগে  dash টাইপ করতে ভুলবেন না)।  এখন,  plotter margin এর ভিতরে layout এর  top left এর কাছাকাছি কোন point এ click করুন। এই command টা Repeat করুন এবং একই  layout view তে আরো ২ টি rectangular viewport তৈরি করুন।

সব viewport তৈরির পর আপনার layout space দেখতে নিচের ছবির মত দেখাবে।

![18-800x617](https://i1.wp.com/projuktiteam.com/wp-content/uploads/2019/02/18-800x617.png?resize=300%2C231&ssl=1)

![](https://sourcecad-f5hmctaeshq3us.netdna-ssl.com/wp-content/uploads/2018/09/18-644x497.png)

এখন,  viewport এর ভিতরে ড্রয়িং এর যে scale তা AutoCAD  স্বয়ংক্রিয়ভাবে ঠিক করে দিবে কিন্তু আপনি এটা manually পরিবর্তন করতে পারেন। scale  পরিবর্তনের জন্য প্রথমে viewport boundary সিলেক্ট করুন; তারপর image এ দেখানো status bar এ scale option থেকে  scale পরিবর্তন করুন।

![](https://sourcecad-f5hmctaeshq3us.netdna-ssl.com/wp-content/uploads/2018/09/19-644x371.png)

আপনি যে scale দিতে চাচ্ছেন তা  যদি viewport list এ ন থাকে, তবে আপনি আপনার নিজের custom scale ও এড করতে পারেন। custom scale এড করার জন্য প্রথমে  select করুন যেকোন viewport তারপর image এ দেখানো উপায়ে status bar এ scale option এ click করুন এবং scales  list থেকে Custom option সিলেক্ট করুন।

“Edit Drawing Scales” window টি ওপেন হবে। অনুমান করে নিই যে, আমরা এই লিস্টে 1:6 এই scale এড করতে চাই, এজন্য add button এ  click  করুন।

[![20](https://projuktiteam.com/wp-content/uploads/2019/02/201-300x282.png)](https://projuktiteam.com/wp-content/uploads/2019/02/201.png)

পরবর্তী window এর name field এ এড করুন 1:6 এবং তারপর paper unit এ 1  এবং drawing unit field এ 6 এড করুন। পরিবর্তনগুলি নিশ্চিত করতে OK  তে Click করুন এবং সব open windows ক্লোজ করে ফেলুন।

আপনি এখন আপনার নতুন scale টা এখন list এ add হয়েছে  এবং  আপনি এটা আপনার viewport এ ব্যবহার করতে পারছেন।

এর মাধ্যমেই আমাদের ২ পর্বব্যপী অটোক্যাডের স্কেলিং এর খুঁটিনাটি বিষয়ের আলোচনা শেষ হল। ধৈর্য্য সহকারে পড়ার জন্য আপনাদের জানাই অসংখ্য ধন্যবাদ।
