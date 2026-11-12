---
archive_id: techtunes-634070
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 634070
title: সলিডওয়ার্কসে অটো ডাইমেনশনিং এর ব্যবহার!
slug: autodesk-autocad-634070
language: bn
status: publish
published_at: '2019-10-27T06:58:00+00:00'
modified_at: '2019-10-27T06:58:00+00:00'
original_url: https://www.techtunes.io/autodesk-autocad/tune-id/634070
author: ইঞ্জিনিয়ার আলী কায়সার
author_url: https://www.techtunes.io/tuner/ali-kaiser
categories:
- অটোডেস্ক অটোক্যাড
tags:
- Tips টিপস
content_hash: f7701d90414a9e173d51b8012ae5cd878ffa8c920337a2b1c6e340482963641a
archived_at: '2026-11-12T12:27:17.587701+00:00'
---

# সলিডওয়ার্কসে অটো ডাইমেনশনিং

ডাইমেনশনিং যেকোন ড্রয়িং বা ড্রাফটিং ইঞ্জিনিয়ারের জন্য একটি সাধারণ কাজ। প্রত্যেক ৩ ডি মডেলের [ম্যানুফ্যাকচারিং](https://projuktiteam.com/5853/tutorial-solidworks/)এর জন্য এর সাথে একটি ২ ডি ড্রয়িং সংশ্লিস্ট থাকে; তাই ডাইমেনশনিং খুব সঠিকভাবে করতে হয়। অনেক বড় বা কমপ্লেক্স ডিজাইনের জন্য,   এটি অনেক সময় নিয়ে নেয়; কিন্তু সলিডওয়ার্কসে একটি ফিচার আছে যার মাধ্যমে আপনি কিছু ক্লিক করেই এই কাজটি খুব সহজেই করে ফেলতে পারেন।

আসল ফাংশন এবং এটি কিভাবে ব্যবহার করতে হয়, তা দেখার পূর্বে, আমরা কিছু ছবির সিরিজ দেখে নিই। আপনি ডাইমেনশনিং এর বিষয়টা একটু দেখবেন যাতে আমরা এটি পরবর্তীতে খুব সহজেই পুণঃস্থাপন করতে পারি।

[![Draw a rectangle on the top plane.](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/a-1024x520.png)](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/a.png)

[![Extrude the object and create a solid block.](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/b-1024x545.png)](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/b.png)

[![Add a few features (here we add two holes), with customized positions (25 mm from their adjacent faces).](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/c-1024x540.png)](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/c.png)

এখন আমরা একটি ৩ ডি [ড্রয়িং](https://projuktiteam.com/5853/tutorial-solidworks/) নিতে যাচ্ছি এবং একটি ২ ডি ড্রয়িং জেনারেট করব, যাতে আমরা পরবর্তীতে ডাইমেনশন যুক্ত করতে পারি। এজন্য নিচের ধাপগুলো অনুসরণ করুনঃ

[![Bring the view into the 2D drawing](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/d-1024x574.png)](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/d.png)

“View Palette” ব্যবহার করে আমরা ২ ডি ড্রয়িং এ ৩ ডি ডিজাইনের [ভিউ](https://projuktiteam.com/5853/tutorial-solidworks/) যোগ করতে পারি। দেখুন এখানে কিভাবে “Top” অপশন মিসিং আছে, যেহেতু আমরা ইতিমধ্যেই তা ড্রয়িং এ যোগ করেছি। ভবিষ্যৎ নোট এবং অতিরিক্ত অপশন প্রদর্শনীর জন্য, আমি এখানে আরেকটি ফেস যোগ করছি।

[![Adding an extra view for future practices](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/f-1024x523.png)](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/f.png)

front view যুক্ত অবস্থায়, আমি সামনে এগিয়ে যাচ্ছি এবং ফিচারগুলো ডাইমেনশনসহ যুক্ত করার জন্য annotation ট্যাবের নিচে “Model Items” অপশন ব্যবহার করছি। ঠিক যেমন আপনি নিচের ছবিতে দেখছেন, উইন্ডো আপনাকে একটির বেশি অপশন সিলেক্ট করতে সাহায্য করছে, যা হল [“Entire model”](https://projuktiteam.com/5853/tutorial-solidworks/) এবং [“Selected feature”](https://projuktiteam.com/5853/tutorial-solidworks/).

[![Source options: Entire Model or Selected Feature](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/g-1024x525.png)](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/g.png)

প্রথমে, আমরা ডাইমেনশনিং এর জন্য সমগ্র মডেল সিলেক্ট করি এবং অন্যান্য অপশনগুলো চেক করি। ঠিক নিচে যে অপশনটি আছে, যা শেষটির পূর্বের স্ক্রিনশটে দৃশ্যমান, তাই আপনাকে ডাইমেনশনাল ফাংশনালিটি আনতে সাহায্য করে যা আপনার পছন্দের ভিউ এর বদলে শিটের সব ভিউতে প্রযোজ্য হবে। ডাইমেনশন ট্যাবের বাটন ইতিমধ্যে সিলেক্টেড আছে এবং এগুলো হল বিবিধ বিষয়, যা আমরা কিছুক্ষণের মাঝেই দেখব। নিচে আছে  [annotations](https://projuktiteam.com/5853/tutorial-solidworks/) ট্যাব এবং আরো অনেক কিছু। এখন ডাইমেনশনিং এর জন্য সব মডেল সিলেক্টেড থাকা অবস্থায়, চলুন আমরা যা শিখতে চাই তাতে ফোকাস করি।  
  নিচের বৃত্তাকার মার্কের জায়গায় একটি সিংগেল ক্লিক করলেই আমরা ডিফল্ট ডাইমেনশন দেখতে পাব। ডাইমেনশন ট্যাবের নিচে আমরা যেভাবে সিলেক্ট করেছি, সেভাবেই ডাইমেনশন প্রদর্শিত হবে।  
 [![Using the selected options, clicking the "checkmark" annotates the features with the dimensions](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/h-1024x516.png)](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/h.png)

এইতো! আপনার ২ ডি ড্রয়িং এর প্রত্যেক ভিউ এবং ফিচারের ডিফল্ট ডাইমেনশন আপনি যেভাবে সুনির্দিষ্ট করেছেন সেভাবেই লেভেলিং হল। এখন, চলুন আমরা অন্য কিছু অপশন দেখে নিই।

---

## বিবিধ এবং অতিরিক্ত ফিচারগুলোঃ

### শুধুমাত্র Wholes অথবা Particular ফিচার সিলেক্ট করা

ডাইমেনশনিং এর জন্য শুধুমাত্র একটি সিংগেল ফিচার সিলেক্টেড হয়েছে তা নিশ্চিত করতে, আমরা প্রথমে “Model Items” এ যাব এবং সিলেক্ট করব [“Selected Feature”](https://projuktiteam.com/5853/tutorial-solidworks/)  অপশন সোর্স প্রেফারেন্সের জন্য। এর সাথে, আপনি ফিচার ছাড়া কিন্ত আর কিছু সিলেক্ট করবেন না। সিলেকশনের ক্ষেত্রে, ফিচারের কমলা আউটলাইন নীলে রূপান্তরিত হবে; যার অর্থ হলো ফিচারটি সিলেক্টেড হয়েছে এবং ফাংশনটি একটিভ হয়েছে ঠিক যেমন নিচে দেখা যাচ্ছে।

[![Selecting only the wholes or particular features](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/i-1024x399.png)](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/i.png)

### মার্কড ডাইমেনশন ব্যতীর কল আউট এনোটেশন

যদি আপনি শুধু একটি কল আউট ব্যবহার করতে চান, এবং [ডাইমেনশন মার্কিং](http://www.cadtutor.net/tutorials/autocad/dimensioning.php) বাদ দিতে চান; এটি “Dimensions” অপশন সিলেক্টেড থাকা অবস্থায়  সম্ভব যেমন আপনি বামের কলামে দেখতে পাচ্ছেনঃ

[![Call out annotations without marked dimensions](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/j-1024x526.png)](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/j.png)

দেখুন এখানে শুধু একটি অপশন সিলেক্টেড অবস্থায় আছে। এটিকে কল আউট অপশন বলে। অন্য অপশনগুলো ডিজেবল অবস্থায় আছে এবং বিপরীত সিলেকশন আপনাকে পরিবর্তিত ভিউ দিবে।

### সব এভেইলেভল ভিউতে ডাইমেনশন ইম্পোর্ট করা

যখন একটি জায়গায় বহু সংখ্যক ভিউ থাকবে, একটি দ্রুত এবং সব ভিউতে সব ডাইমেনশন প্রদর্শনের আবশ্যক উপায় হল [“Import items into all views”](https://projuktiteam.com/5853/tutorial-solidworks/)অপশন ব্যবহার করা। কিন্ত এক্ষেত্রে, আপনি শুধু কিছু ভিউতে ডাইমেনশন প্রদর্শন করতে চান, এই ভিউগুলো একবার সিলেক্ট করুন এবং (যেমন নিচে দেখছেন) বামদিকে সব ভিউ হাইলাইটেড হয়েছে। একটি বা রা বেশি ভিউ এখানে সিলেক্ট করুন, সব ভিউ এর বদলে শুধু এই ভিউগুলো সিলেক্ট করার জন্য।

[![k](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/k-1024x579.png)](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/k.png)

### ডাইমেনশন ড্র্যাগ এবং কপি করা

আপনি একটি ভিউতে ডাইমেনশন যোগ করার পর, কোন কারণে অন্য ভিউগুলো ডাইমেনশনহীন থাকলে, আপনি অরিজিনাল [ভিউ](https://projuktiteam.com/5853/tutorial-solidworks/)এর ডাইমেনশনগুলো কপি অথবা ড্র্যাগ করে আনতে পারেন। এখানে বলছি কিভাবে আপনি কাজটি করবেনঃ

কপি (Copy) – CTRL + ডাইমেনশন ড্যাগিং করে

মুভ (Move) – SHIFT + ডাইমেনশন ড্যাগিং করে

নিচের দুইটি স্ক্রিনশটে, প্রথমটি ডাইমেনশন কপি করা অবস্থাটি প্রদর্শন করছে ; যেখানে দ্বিতীয়টি ডাইমেনশন কিভাবে মুভ করেছে তা প্রদর্শন করছে।

[![l-1](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/l-1.png)](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/l-1.png)

[![l-2](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/l-2.png)](https://www.computeraideddesignguide.com/wp-content/uploads/2016/05/l-2.png)

---

## প্রান্তকথন

আপনি হয়তো অনুপযুক্ত ডাইমেনশনের ব্যবহার দেখেছেন যেখানে এর কিছু অন্য ডাইমেনশনের সাথে ইন্টারফেয়ারিং অবস্থায় দেখা যাচ্ছে। সব ডাইমেনশন এলাইন আছে তা নিশ্চিত করতে, আপনি যখন  [“Model Items”](https://projuktiteam.com/5853/tutorial-solidworks/) কমান্ড ব্যবহার করবেন, তখন ৩ ডি মডেলিং এর সাথে একই আয়োজনে একই ডাইমেনশন ব্যবহারের চেষ্টা করুন; কারণ এগুলোই হলো সেই ডাইমেনশন যা ২ডি ড্রয়িং এ স্থান পাবে [“Model Items”](https://projuktiteam.com/5853/tutorial-solidworks/) কমান্ড ব্যবহারের সময়। এবং সেখানে আপনি ঠিক তখনি, সলিডওয়ার্কসে অটো ডাইমেনশনিং ব্যবহার করতে পারবেন। এই অপশনগুলি ব্যবহার করে আপনি আরো অনেক কিছুই অর্জন করতে পারবেন; কিন্তু এটি নিশ্চিত যে প্রত্যেক ফেস ও এইজ ধরে কষ্টকর ম্যানুয়েল পদ্ধতিতে ডাইমেনশনিং এর দিন ফুরালো!

লেখাটি পূর্বে প্রযুক্তি টিমের ওয়েবসাইটে প্রকাশিত হয়েছে যার লিংকঃ

<https://projuktiteam.com/6540/solidworks-auto-dimension/>
