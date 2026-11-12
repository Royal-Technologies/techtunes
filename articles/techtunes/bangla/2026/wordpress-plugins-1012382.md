---
archive_id: techtunes-1012382
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 1012382
title: WordPress Search নিয়ে টেনশনে আছেন? স্প্যামিং অ্যাটাক থেকে বাঁচতে Disable Search
  Plugin! In-Depth গাইড
slug: wordpress-plugins-1012382
language: bn
status: publish
published_at: '2026-03-02T17:03:00+00:00'
modified_at: '2026-03-02T17:03:00+00:00'
original_url: https://www.techtunes.io/wordpress-plugins/tune-id/1012382
author: মো আতিকুর ইসলাম
author_url: https://www.techtunes.io/tuner/atikurofficial
categories:
- ওয়ার্ডপ্রেস প্লাগইনস
tags:
- অন্যান্য প্লাগইন্স
- ওয়ার্ডপ্রেস প্লাগইন
- ওয়ার্ডপ্রেস প্লাগইন টিউটোরিয়াল
content_hash: 4749181d1830965aa97f1fb45619d4285633146b1279feadac9b3d8afe9d36cd
archived_at: '2026-11-12T11:44:31.639995+00:00'
---

আসসালামু আলাইকুম বন্ধুরা! টেকটিউনস এর দুনিয়ায় আপনাদের স্বাগতম। কেমন আছেন সবাই? আশাকরি ভালো আছেন। আজ আমরা WordPress নিয়া কথা বলব। WordPress শুধু একটা প্লাটফর্ম না, এটা একটা Ecosystem। এখানে সবকিছুই আছে, কিন্তু Security নিয়া একটু Extra Care তো নিতেই হয়, তাই না? আজকের ব্লগটা WordPress Website নিয়া, তবে একটু অন্যরকম। আমরা দেখবো কিভাবে আপনার সাইটকে Spam Attack থেকে বাঁচাতে পারেন। তাহলে চলুন, আর দেরি না করে শুরু করি!

## স্প্যামিং অ্যাটাক: WordPress Search এর দুর্বল দিকগুলো

![Disable Search](https://dnc.techtunes.io/tDrive/tuner/2025/12/techtunes_b7de3e627d007667e67683bb929aac55.png)

WordPress Website এ Spam Attack একটা খুব কমন সমস্যা। নতুন ব্লগার হোন বা পুরাতন, এই সমস্যার মুখোমুখি হননি এমন মানুষ খুঁজে পাওয়া কঠিন। Attack এর মূল Technique টা হলো Search Keyword ব্যবহার করে Spam Link Index করা।

বিষয়টাকে একটু ভেঙে বলি। ধরুন, আপনার Website এর Built-in Search এর Path ফিক্সড করা, যেখানে `?s=` প্রিফিক্স হিসেবে ব্যবহার করা হয়। এখন কিছু অসাধু Individuals বিভিন্ন Advertisement, Spam Link অথবা Promotion Related Term আপনার Search Link এর মধ্যে ঢুকিয়ে দেয়। এতে কী হয়? এতে প্রচুর URL তৈরি হয়, আর Search Crawler গুলো সেগুলোকে Crawl করতে থাকে।

বিষয়টা দেখতে নিরীহ মনে হলেও, এর Consequences কিন্তু মারাত্মক হতে পারে। Default ভাবে Search Result গুলো Search Engine Index না করলেও, আপনার Normal Website এর উপর এটা Negative Impact ফেলতে পারে। নিচের ছবিটা দেখলে ব্যাপারটা আরও ক্লিয়ার হবে:

Google Search Console-এ এই Record গুলো আপনারা সহজেই খুঁজে পাবেন। যদি দেখেন Link গুলো "NotFound (404)" Error Record-এ আছে, তাহলে আপাতত চিন্তার কিছু নেই। কিন্তু অন্য কোনো কারণে দেখলে একটু Attention দেওয়া উচিত। Google Search Engine প্রতিটি Website-কে Crawl করার জন্য একটা নির্দিষ্ট "Quota" দেয়। এই Spam Link Attack-এর কারণে আপনার Website-এর Indexing Ability কমে যেতে পারে। শুধু তাই না, আপনার Website এর Ranking ও কমে যেতে পারে।

বিষয়টা এমন, আপনার Website এ ভালো Content থাকা সত্ত্বেও Google মনে করতে পারে আপনার Website টি Spam Website.

### Disable Search

অফিসিয়াল ওয়েবসাইট @ [Disable Search](https://wordpress.org/plugins/disable-search/)

## Disable Search: সমস্যার সহজ সমাধান

![Disable Search: সমস্যার সহজ সমাধান](https://dnc.techtunes.io/tDrive/tuner/2025/12/techtunes_5e87e062cece2e071893bba360e5bae6.jpg)

যদি দুর্ভাগ্যবশত আপনার WordPress Search Spam Attack-এর শিকার হয়, তাহলে শুরুতে Search-এ Protection Mechanism যোগ করা (যেমন Cloudflare ব্যবহার করে Genuine কিনা তা যাচাই করা) ছাড়া এর সমাধান করা কঠিন। কিন্তু একটা Permanent Solution আছে। সেটা হলো WordPress Search বন্ধ করে দেওয়া এবং অন্য Search Functionality ব্যবহার করা। এক্ষেত্রে Programmable Search Engine (আগে Google Custom Search নামে পরিচিত ছিল) অথবা Algolia ব্যবহার করতে পারেন। এই Search Engine গুলো অনেক Powerful এবং Customize করার অনেক সুযোগ আছে।

তবে আমি আজ আপনাদের সাথে যে Plugin টা নিয়ে কথা বলব, সেটার নাম "Disable Search"। যারা Coding নিয়ে মাথা ঘামাতে চান না, তাদের জন্য এটা Best Solution হতে পারে।

## Disable Search Plugin এর Functionality: খুঁটিনাটি

![Disable Search Plugin এর Functionality](https://dnc.techtunes.io/tDrive/tuner/2025/12/techtunes_c4027c67f1d031b01c9692f19e681ac0.jpg)

এই Plugin-টির প্রধান Function হলো আপনার Website-এর Front-end-এর Search Request গুলো Block করা। Specifically বললে, এটা আপনার WordPress Website-এর Front-end-এর Search Field টি সরিয়ে দেয়, এবং Link-এর মাধ্যমে Website-এ Search করাও Block করে (সম্পূর্ণরূপে Search Functionality সরিয়ে দেয়)। Front-end Search এর সাথে জড়িত সবকিছু সরাসরি 404 Error Return করে।

সবচেয়ে গুরুত্বপূর্ণ বিষয় হলো, এটা আপনার Back-end-এর Search Functionality-তে কোনো Impact ফেলে না। তার মানে আপনি Article, Category অথবা Plugin এবং Theme Search করা আগের মতোই করতে পারবেন।

Search Functionality বন্ধ করার আরও একটা Benefit আছে। Search বেশিরভাগ সময় Cache এড়িয়ে সরাসরি Database থেকে Real-time Data নিয়ে আসে। তাই Attack হলে Server-এর Load বেড়ে যেতে পারে, যা Normal User-দের Browsing Experience-কে Impact করতে পারে। Server Load বেশি থাকলে Website Slow হয়ে যায়, যা User দের জন্য খুবই বিরক্তিকর।

## কেন Disable Search Plugin ব্যবহার করবেন? যুক্তিগুলো জেনে নিন

![কেন Disable Search Plugin ব্যবহার করবেন?](https://dnc.techtunes.io/tDrive/tuner/2025/12/techtunes_33814aedc3090fc2904ffc90e5e314bb.jpg)

আপনি Spam Attack-এর শিকার হন বা না হন, অথবা আপনি যদি আপনার WordPress Front-end Search Functionality-টা পুরোপুরি Remove করতে চান, তাহলে "Disable Search" Plugin Install করার মাধ্যমে খুব সহজেই সেটা করতে পারবেন। এই Plugin-টির তেমন কোনো Option নেই, তাই এটা ব্যবহার করা খুবই Easy। অনেক Website-এ এটা Install করা হয়েছে, এবং Developer-রা নিয়মিত Update করছেন (Plugin-টি ২০২১ সালের দিকে Launch করা হয়েছিল)। তার মানে বুঝতেই পারছেন, Plugin টি Trusted.

এখানে কিছু Reasons দেওয়া হলো কেন আপনি Disable Search Plugin ব্যবহার করবেন:

- **Website Security:** WordPress Security নিশ্চিত করতে এটা খুব Important।
- **Spam Attack প্রতিরোধ:** Keyword ব্যবহার করে Spam Link Index Attack হওয়ার সম্ভাবনা কমিয়ে দেয়।
- **সহজ ব্যবহার:** কোনো Coding Knowledge ছাড়াই এটা ব্যবহার করা যায়।
- **Performance Improvement:** Search বন্ধ করার মাধ্যমে Website এর Speed বাড়ানো যায়।
- **Negative Impact কমানো:** Search Link-এর জন্য 404 Error Return করে, যা Website-এর উপর Negative Impact কমায়।

## Disable Search Plugin: কিভাবে ব্যবহার করবেন? Step by Step গাইড

![Disable Search Plugin: কিভাবে ব্যবহার করবেন?](https://dnc.techtunes.io/tDrive/tuner/2025/12/techtunes_ec7e6aa5c7bc1d545d8aba6a74a1d711.jpg)

নিচে Plugin টি ব্যবহার করার Procedure step by step দেওয়া হলো:

১. **WordPress Search Functionality:** Generally, WordPress Website গুলোতে Default ভাবে একটা "Search" Functionality থাকে, যা Website এর Article, Page অথবা যেকোনো Category এবং Tag Search করার জন্য ব্যবহার করা হয়। কিন্তু Search Functionality খুব Accurate না ও Website এ Extra Load ও তৈরি করতে পারে।

![Install Now](https://dnc.techtunes.io/tDrive/tuner/2025/12/techtunes_3e5624c33afd4d68ab9d413b26c88ad6.png)

২. **Install Disable Search Plugin:** আপনার WordPress Control Panel থেকে "Install Plugin" Page-এ যান, Search Field-এ "Disable Search" লিখে Plugin-টি খুঁজে বের করুন এবং "Install Now"-তে Click করে Website-এ Download করুন ও Activate করুন।

![](https://dnc.techtunes.io/tDrive/tuner/2025/12/techtunes_289fecc88c4b05b281ef383a0e1e1e7a.png)

৩. **Activate করার পর Front-end Search বন্ধ:** Activate করার পরে দেখবেন Front-end-এর Search Functionality টি সম্পূর্ণরূপে Disable এবং Remove করা হয়েছে। Front end বলতে User রা যা দেখে। অথবা রিমুভ না হলেও, এটি কাজ করা বন্ধ করে দিয়েছে।

![Activate করার পর Front-end Search বন্ধ](https://dnc.techtunes.io/tDrive/tuner/2025/12/techtunes_f228a5fb33339fcad1fa98c6ac396c18.png)

৪. **Search করলে 404 Error:** এখন কেউ যদি আপনার Website-এ Search করার চেষ্টা করে, তাহলে 404 Error Page দেখতে পাবে। এটা নিশ্চিত করে যে কোনো Spam Bot আপনার Website Index করতে পারবে না এবং আপনার Website Secure থাকবে।

৫. **Back-end Search অক্ষত:** "Disable Search" Plugin ব্যবহার করার ফলে Front-end-এর Search Functionality বন্ধ হয়ে গেলেও WordPress Control Panel-এর Search Mechanism-এ কোনো Impact পড়বে না। আপনি আপনার Article, Category সবকিছু Back-end থেকে Search করতে পারবেন। Content Management এর জন্য এটা খুবই দরকারি।

![Back-end Search](https://dnc.techtunes.io/tDrive/tuner/2025/12/techtunes_3dac2df5383100df9abeaf6f72edaddc.png)

## Disable Search: কিছু অতিরিক্ত টিপস

![Disable Search: কিছু অতিরিক্ত টিপস](https://dnc.techtunes.io/tDrive/tuner/2025/12/techtunes_6b161f27a1178b2459d6f547f5982e2c.jpg)

এখানে কিছু Additional Tips দেওয়া হলো, যা আপনার WordPress Website কে Secure রাখতে সাহায্য করবে:

- নিয়মিত আপনার WordPress Version Update করুন। পুরাতন Version এ Security Flaw থাকতে পারে।
- Strong Password ব্যবহার করুন। Password যত Strong হবে, Hack হওয়ার সম্ভাবনা তত কম।
- Two-Factor Authentication ব্যবহার করুন। এটা Extra Security Layer যোগ করে।
- Security Plugin ব্যবহার করুন। যেমন Wordfence Security, Sucuri Security ইত্যাদি।
- নিয়মিত আপনার Website এর Backup নিন। কোনো Accident ঘটলে Backup থেকে Restore করতে পারবেন।
- আপনার Website এর Theme এবং Plugin গুলো নিয়মিত Update করুন।
- আপনার Hosting Provider এর Security Feature গুলো সম্পর্কে জানুন।
- Suspicious Link এ Click করা থেকে বিরত থাকুন।
- আপনার Computer কে Virus মুক্ত রাখুন।

## Disable Search ব্যবহারের তিনটি প্রধান কারণ সংক্ষেপে

![Disable Search ব্যবহারের তিনটি প্রধান কারণ](https://dnc.techtunes.io/tDrive/tuner/2025/12/techtunes_8e3d6241424e8c0c549ba8f5ccbe1843.jpg)

1. WordPress Search Functionality-তে Keyword ব্যবহার করে Spam Link Index Attack হওয়ার সম্ভাবনা থাকে।
2. "Disable Search" Plugin Front-end-এর Search Functionality-টা সম্পূর্ণরূপে Disable করে দেয়।
3. Search Link-এর জন্য 404 Error Return করে, যা Website-এর উপর Negative Impact কমায়।

আজকের টিউনটি কেমন লাগলো, টিউমেন্ট করে জানাতে ভুলবেন না। আপনার মতামত খুবই মূল্যবান। আর হ্যাঁ, "Disable Search" Plugin ব্যবহার করে আপনার Website-কে Spam Attack থেকে Safe রাখতে পারেন। নিরাপদে ব্লগিং করুন, ভালো থাকুন। আল্লাহ হাফেজ! 👋
