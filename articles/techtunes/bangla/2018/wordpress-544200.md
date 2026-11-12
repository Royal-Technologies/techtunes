---
archive_id: techtunes-544200
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 544200
title: আপনার ওয়ার্ডপ্রেস সাইটের স্পিড বাড়ান কয়েকগুন
slug: wordpress-544200
language: bn
status: publish
published_at: '2018-01-20T14:47:00+00:00'
modified_at: '2018-01-20T14:47:00+00:00'
original_url: https://www.techtunes.io/wordpress/tune-id/544200
author: শরিফুল ইসলাম
author_url: https://www.techtunes.io/tuner/shariful002
categories:
- ওয়ার্ডপ্রেস
tags: []
content_hash: 77052d0d72106901ee52b9278b7ed67740e133e180b3c01a4b1929849cab3a5e
archived_at: '2026-11-12T12:34:12.920171+00:00'
---

ওয়েব সাইটের স্পিড একটি গুরুত্বপূর্ণ বিষয় যে কোন সাইটের জন্য। সাইট লোড হতে এক সেকেন্ড বেশি সময় লাগলে:

- পেজ ভিউ কমে যাবে ১১%
- কাস্টমার সন্তুষ্টি কমে যাবে ১৬%
- কনভার্সন কমে যাবে ৭% (সূত্র: [এবার্ডিন গ্রুপ](http://www.aberdeen.com/research/5136/ra-performance-web-application/content.aspx))

যদি আপনার সাইট লোড হতে ২ সেকেন্ডের বেশী লাগে তাহলে বেশির ভাগ ভিজিটরই সাইট থেকে চলে যাবে এবং আপনি কোন সুযোগই পাবেন তাদের কাছে আপনার সাইটের কন্টেন্টকে তুলে ধরতে। এছাড়াও সাইট স্পিড এখন গুগলের একটি র‍্যাংকিং ফ্যাক্টর। তাই এটি SEO-তে গুরুত্বপূর্ণ ভূমিকা রাখে।

আমরা এই আর্টিকেলে একটি ওয়ার্ডপ্রেস সাইটকে কিভাবে [গুগল পেজস্পিড ইনসাইটে](https://developers.google.com/speed/pagespeed/insights/) ৯১-১০০ স্কোরে আনতে পারব তা দেখানোর চেষ্টা করবো।

ওয়ার্ডপ্রেস সাইটের গতি বাড়ানোর জন্য সাধারণত ২টি ক্যাশিং প্লাগ-ইন্স সবচেয়ে বেশি ব্যবহার করা হয়। এরা হল [W3 Total Cache](https://wordpress.org/plugins/w3-total-cache/) এবং [WP Super Cache](https://wordpress.org/plugins/wp-super-cache/)। যদিও বিভিন্ন ভাবে অপ্টিমাইজ করেও আমি তেমন আশানুরূপ ফল এই দুটি প্লাগ-ইন্স থেকে পাই নি। তাই এই দুটি বাদে অন্য ৩-৪টি ছোট প্লাগ-ইন্স ব্যবহার করে কিভাবে সাইটের স্পিড বাড়ানো যায় তা আমরা আজকে দেখবো।

**১। হোস্টিং:** সাইটের স্পিড কম হওয়ার সবচেয়ে বড় কারণ হোস্টিং। কিন্তু দুঃখজনক ব্যাপার হল কোন হোস্টিং কোম্পানিই আপনাকে বলবে না যে সমস্যাটা তাদের দিকের। তারা প্রথমে বলবে আপনার সাইট ওপ্টিমাইজ করা নাই। তারপরে বলবে, যদি আরও স্পিড দরকার হয় তবে তাদের অন্য কোন হোস্টিং প্যাকেজে আপগ্রেড হতে।

তবে বাস্তবতা হল আপনি শেয়ার্ড হোস্টংই ব্যবহার করেন আর ভিপিএস ই করেন, স্পিডে তেমন কোন পার্থক্য পাবেন না। তাই নেমচিপ, ব্লুহোস্ট বা ড্রিমহোস্ট যেকোনো কোম্পানি থেকেই হোস্টিং নিতে পারেন। এদের মধ্যে কোন পার্থক্য আমার নজরে পড়েনি। এমনকি আপনি দেশী রেপুটেড কোম্পানি থেকেও হোস্টিং নিতে পারেন। সেক্ষেত্রে পেমেন্টের ব্যাপারে ঝামেলা কমে যাবে।

**২। থিম:** ওয়ার্ডপ্রেস প্লাটফর্ম হিসাবে এমনিতেই একটু স্লো। তার উপরে এর থিম একে আরও স্লো করে তোলে। থিম ডেভেলপাররা সাধারণত স্পিডের চেয়ে এসথেটিক্সের উপর বেশি নজর দেন। তাই থিমগুলো হয়ে পরে ভারী। এক্ষেত্রে ফ্রি বা পেইড থিমে কোন পার্থক্য নাই। আমি দুটি সাইটে একটিতে ফ্রি থিম এবং একটিতে পেইড থিম নিয়ে কাজ করেছি। ফ্রি থিম হিসাবে আমি বেছে নিয়েছি [বেসিক থিম](https://wordpress.org/themes/basic/) এবং পেইড থিম হিসাবে নিয়েছি আল্টিমেট এজন।

**৩। এনাবল জিজিপ কমপ্রেশন:** বড় পেজ সাধারণত ১০০কেবি বা তার চেয়ে বড় হয়ে থাকে। ফলে এই পেজ ডাউনলোড হতে বেশী সময় লাগে। লোড টাইম কমানোর সবচেয়ে ভাল উপায় হল এদেরকে জিপ ফাইল হিসাবে বিতরণ করা। শেয়ার হোস্টিং-এ এটি সাধারণত সক্রিয় করা থাকে না। তাই আমাদেরকে.htaccess file এডিট করার মাধ্যমে ম্যানুয়ালি একে সক্রিয় করে নিতে হবে।

আপনার FTP একাউন্ট থেকে.htaccess file খুলুন। এর পরে নিচের কোডটিকে কপি/পেস্ট করুন।

# Compress HTML, CSS, JavaScript, Text, XML and fonts  
 AddOutputFilterByType DEFLATE application/javascript  
 AddOutputFilterByType DEFLATE application/rss+xml  
 AddOutputFilterByType DEFLATE application/vnd.ms-fontobject  
 AddOutputFilterByType DEFLATE application/x-font  
 AddOutputFilterByType DEFLATE application/x-font-opentype  
 AddOutputFilterByType DEFLATE application/x-font-otf  
 AddOutputFilterByType DEFLATE application/x-font-truetype  
 AddOutputFilterByType DEFLATE application/x-font-ttf  
 AddOutputFilterByType DEFLATE application/x-javascript  
 AddOutputFilterByType DEFLATE application/xhtml+xml  
 AddOutputFilterByType DEFLATE application/xml  
 AddOutputFilterByType DEFLATE font/opentype  
 AddOutputFilterByType DEFLATE font/otf  
 AddOutputFilterByType DEFLATE font/ttf  
 AddOutputFilterByType DEFLATE image/svg+xml  
 AddOutputFilterByType DEFLATE image/x-icon  
 AddOutputFilterByType DEFLATE text/css  
 AddOutputFilterByType DEFLATE text/html  
 AddOutputFilterByType DEFLATE text/javascript  
 AddOutputFilterByType DEFLATE text/plain  
 AddOutputFilterByType DEFLATE text/xml

# Remove browser bugs (only needed for really old browsers)  
 BrowserMatch ^Mozilla/4 gzip-only-text/html  
 BrowserMatch ^Mozilla/4\.0[678] no-gzip  
 BrowserMatch \bMSIE!no-gzip!gzip-only-text/html  
 Header append Vary User-Agent

খেয়াল রাখবেন কোডটি যেন.htaccess file-এ উপস্থিত কোডের নিচে থাকে।

আপনি যদি NGINX ব্যবহার করে থাকেন তবে নিচের কোডটি nginx.conf file-এ পেস্ট করুন।

36 gzip on;  
 37 gzip\_disable “MSIE [1-6]\.(?!.\*SV1)”;  
 38 gzip\_vary on;  
 39 gzip\_types text/plain text/css text/javascript application/javascript application/x-javascript;

**৪। ইমেজ অপ্টিমাইজেশন:** ইমেজ সাইটের লোডিং টাইমে একটা বড় প্রভাব ফেলে। তাই সাইটের সব ইমেজ অপটিমাইজ থাকা উচিৎ। এটি দুই ভাবে করা যায়। এক, ইমেজকে অপ্টিমাইজ করে সাইটে আপলোড করা এবং দুই, প্লাগ-ইন্স ব্যবহার করে সাইটে ইমেজ আপলোড করার সময় অপ্টিমাইজ করে নেয়া।

প্লাগ-ইন্সের ক্ষেত্রে **[ShortPixel](https://shortpixel.com/free-sign-up-referrer/referrer/120433)** ব্যবহার করা যায়।

ইমেজকে এডোবি ফটোশপ, জিম্প ইত্যাদি সফটওয়ার দিয়ে সাইটে আপলোড করার আগেই অপ্টিমাইজ করে নেয়া যায়। ইমেজের প্রস্থ সাইটের প্রস্থের সাথে সামঞ্জস্যপূর্ণ থাকা উচিত। যেমন, সাইটের প্রস্থ যদি 570px হয় তবে ইমেজকেও একই প্রস্থে নিয়ে আসতে হবে। ইমেজের ফরমেট JPEG হওয়া উচিৎ।

**৫। Above-the-fold Content হতে Render-blocking JavaScript and CSS দুর করা:** যখন একটি ব্রাউজার ওয়েবসাইট লোড করে, তখন সাধারণত JavaScript এবং CSS রিসোর্সগুলো সাইটকে ডিসপ্লে হতে বাধা দিতে থাকে যতক্ষণ না তারা নিজেরা ডাউনলোড হচ্ছে।

কিছু রিসোর্স অবশ্য প্রথমেই ডাউনলোড এবং প্রসেস হতে হবে কোন কিছু ডিসপ্লে হবার আগে। যাইহোক, কিছু CSS এবং JavaScript রিসোর্স Above-the-fold Content রেন্ডারিংএ কোন ভূমিকা রাখে না। তাই আপনার উচিৎ সকল Render-blocking CSS এবং JavaScript কে eliminate করা।

আমরা JavaScript-কে asynchronously লোড করে উপরের ফলাফল পেতে পারি। এজন্য আমাদের লাগবে একটি ফ্রি প্লাগ-ইন্স [Async JavaScript](https://wordpress.org/plugins/async-javascript/)।

- ইন্সটল করার পরে সেটিং-এ গিয়ে Async JavaScript-কে এনাবল করে নিন।
- এরপরে Async JavaScript Method-কে Async করে দিন।
- jQuery কে Defer করে দিন।
- Async JavaScript For Plugins এ Autoptimize Support এনাবল করে দিন এবং jQuery Method-কে Defer করে দিন।

[![Async JavaScript Setting](https://i1.wp.com/i67.tinypic.com/2usvlev.jpg?w=750)](http://tinypic.com/?ref=2usvlev)

**৬। Optimize CSS Delivery:** [Autoptimize](https://wordpress.org/plugins/autoptimize/) প্লাগ-ইন্স দিয়ে আপনি সহজেই এটি করতে পারবেন।

- Autoptimize প্লাগ-ইন্স করে একটিভেট করে নিন।
- সেটিং থেকে Autoptimize Settings এ যান।
- Show advanced setting সিলেক্ট করুন।
- HTML Options থেকে Optimize HTML Code সিলেক্ট করুন।
- JavaScript Options থেকে Optimize JavaScript Code এবং Also aggregate inline JS সিলেক্ট করুন।
- CSS Options থেকে Optimize CSS Code, Remove Google Fonts এবং Also aggregate inline CSS সিলেক্ট করুন।
- Save and empty cache চাপুন।

এখানে একটি কাজ বাকি থাকলো, সেটি হল “Inline and Defer CSS”-কে একটিভ করা। এটি একটিভ করতে হলে আমাদেরকে Critical Path CSS জেনারেট করতে হবে। এটি বের করার জন্য আপনার সাইটের যেকোনো স্থানে রাইট বাটন ক্লিক করে পেজ সোর্স দেখুন। পেজের প্রথম দিকেই আপনি আপনার পেজের CSS ফাইলটি পেয়ে যাবেন। ফাইলটি এমন ফর্মেটে পাবেন- <http://yoursite.com/wp-content/cache/autoptimize/css/autoptimize_42474faf5fd636c0e6bb9088050e6a2f.css।>

সাইটের CSS ফাইলের সকল কন্টেন্ট সিলেক্ট করে কপি করুন। এখন Critical Path CSS Generator-রে গিয়ে আপনার সাইটের নাম এবং কপি করা CSS কন্টেন্ট পেস্ট করুন এবং create Critical Path CSS বাটনটি চাপুন। আপনার above the fold CSS এখন তৈরি।

এটি কপি করে Autoptimize Settings এ চলে যান এবং CSS Options-এর Inline and Defer CSS-এ চেক দিন এবং পাশের খলি স্থানে above the fold CSS পেস্ট করুন। সেভ করে বেরীয়ে আসুন।

**৭। Leverage Browser Caching:** আমরা দুই ভাবে এটি করতে পারি। এক, ক্যাশ-কন্ট্রোল হেডার এবং দুই, এক্সপায়ার হেডার। তবে যেকোনো একটি মেথডই ব্যবহার করা উচিৎ। ক্যাশ-কন্ট্রোল হেডার নতুন পদ্ধতি এবং এটি সাধারণত রিকমেন্ডেড মেথড।

ক্যাশ-কন্ট্রোল হেডার Nginx-তে যুক্ত করা: নিচের কোডটি সার্ভার কনফিগ ফাইলের সার্ভার লোকেশন বা ব্লকে যোগ করুন।

location ~\* \.(js|css|png|jpg|jpeg|gif|ico)$ {expires 2d;  
 add\_header Cache-Control “public, no-transform”;}

এক্সপায়ার হেডার Nginx-তে যুক্ত করা: নিচের কোডটি সার্ভার ব্লকে যোগ করুন।

location ~\* \.(jpg|jpeg|gif|png)$ {expires 365d;}

location ~\* \.(pdf|css|html|js|swf)$ {expires 2d;}

ক্যাশ-কন্ট্রল হেডার এপাচিতে যুক্ত করা: নিচের কোডটি.htaccess ফাইলে যোগ করুন।

Header set Cache-Control “max-age=604800, public”

এক্সপায়ার হেডার এপাচিতে যুক্ত করা: নিচের কোডটি.htaccess ফাইলে যোগ করুন।

## EXPIRES HEADER CACHING ##

ExpiresActive On  
 ExpiresByType image/jpg “access 1 year”  
 ExpiresByType image/jpeg “access 1 year”  
 ExpiresByType image/gif “access 1 year”  
 ExpiresByType image/png “access 1 year”  
 ExpiresByType text/css “access 1 month”  
 ExpiresByType application/pdf “access 1 month”  
 ExpiresByType application/javascript “access 1 month”  
 ExpiresByType application/x-javascript “access 1 month”  
 ExpiresByType application/x-shockwave-flash “access 1 month”  
 ExpiresByType image/x-icon “access 1 year”  
 ExpiresDefault “access 2 days”

## EXPIRES HEADER CACHING ##

আপনাদের নিশ্চয় মনে আছে আমরা আগেও একবার.htaccess ফাইলে কোড যোগ করেছিলাম। ফলে এখন.htaccess ফাইলটি দেখতে নিচের ছবির মতো হবে।

[![expire headers code](https://i2.wp.com/i66.tinypic.com/28anf5u.jpg?w=750)](http://tinypic.com/?ref=28anf5u)

এখন যদি আমরা আমাদের সাইট Google PageSpeed Insights-এ দেখি তাহলে দেখব, Leverage Browser Caching-এর অধীনে শুধু Google Analytic-এর স্ক্রিপ্টটি আছে। এই স্ক্রিপ্টটি আমরা লোকালি হোস্ট করে এই ওয়ার্নিংটি দুর করতে পারি। তবে এটি অবশ্যই মাথায় রাখবেন যে [গুগল এই পদ্ধতিকে সাপোর্ট করে না](https://support.google.com/analytics/answer/1032389?hl=en)।

একটি অসাধারণ ফ্রি প্লাগ-ইন্স আছে যার নাম [Complete Analytics Optimization Suite](https://wordpress.org/plugins/host-analyticsjs-local/), যেটা দিয়ে আপনি Google Analytics-কে লোকালি হোস্ট করতে পারেন। প্লাগ-ইন্সটি ইন্সটল করে আপনার Google Analytics Tracking ID টি বসান। প্লাগ-ইন্সটি নিজেই ট্র্যাকিং কোড ডাউনলোড করে আপনার সার্ভারে রাখবে এবং শিডিউল স্ক্রিপ্টের মাধ্যমে এটি আপডেটেড থাকবে। সেটিংসে অবশ্যই এটিকে ফুটারে লোড হতে দেবেন। আর এই প্লাগ-ইন্সটি অন্য Google Analytics WordPress plugins-এর সাথে কাজ করতে পারে না।

**৮। রিডিউস সার্ভার রেসপন্স টাইম:** আমরা [Cache Enabler](https://wordpress.org/plugins/cache-enabler/) প্লাগ-ইন্সটি ব্যবহার করবো। এটি একটি হালকা প্লাগ-ইন্স যেটি স্ট্যাটিক HTML ফাইল জেনারেট করে সাইটকে দ্রুত লোড করে। এই প্লাগ-ইন্সটি পুরোপুরি Async JavaScript এবং Autoptimize-এর সাথে কম্প্যাটিবল।

- ইন্সটল করে একটিভ করুন।
- Cache Expiry তে ৭২ লিখুন।
- Cache Behavior-রে Clear the complete cache if a new post has been published এবং Pre-compression of cached pages অপশনে টিক দিন।
- Cache Minification ডিজেবল রাখুন।
- সেভ করুন।

আমাদের সাইটের বর্তমান অবস্থা:

[![PageSpeed Insight](https://i0.wp.com/i64.tinypic.com/24awt42.jpg?w=750)](http://tinypic.com/?ref=24awt42)

That’s it! আমরা আমাদের সাইটকে পুরোপুরি অপটিমাইজ করে ফেলেছি। আপনিও চেষ্টা করুন এবং আপনার ফলাফল আমাদেরকে জানান।
