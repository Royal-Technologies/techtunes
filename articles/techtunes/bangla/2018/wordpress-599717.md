---
archive_id: techtunes-599717
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 599717
title: ওয়ার্ডপ্রেস এর RSS Feed এ থাম্বনেইল দেখান কোড এর মাধ্যমে
slug: wordpress-599717
language: bn
status: publish
published_at: '2018-09-29T04:20:00+00:00'
modified_at: '2018-09-29T04:20:00+00:00'
original_url: https://www.techtunes.io/wordpress/tune-id/599717
author: সিহাব সুমন
author_url: https://www.techtunes.io/tuner/shihab-sumon
categories:
- ওয়ার্ডপ্রেস
tags:
- Classified ওয়ার্ডপ্রেস থিম
content_hash: 5fd08f4107a8c751194174aa242a0b576c22d23e7cef9f9318ce2a34531b1adf
archived_at: '2026-11-12T12:29:28.705566+00:00'
---

আমরা জানি যে, ডিফল্ট ভাবে ওয়ার্ডপ্রেস আরএসএস ফীড থাম্বনেইল দেখায় না। যে বিষয় টা শুধু আমার কাছে না অন্যসব ইউজার যারা ওয়ার্ডপ্রেস ব্যবহার করে তাদের কাছেও কোন ভাবে গ্রহণযোগ্যতা পায় না। আরএসএস ফীড এ থাম্বনেইল দেখালে সেটা দেখতে যেমন ভালো লাগে তেমনি অন্যান্য সুবিধাও আছে। তাই আমি এখন আপনাদের সাথে একটা কোড শেয়ার করছি যেটা ব্যবহার করলে আপনার ওয়ার্ডপ্রেস ব্লগ এর আরএসএস ফীড এ থাম্বনেইল দেখাবে।

```
add_filter('the_content_feed', 'rss_post_thumbnail');
function rss_post_thumbnail($content) {global $post; if(has_post_thumbnail($post-&gt;ID)) $content = '&lt;p&gt;'. get_the_post_thumbnail($post-&gt;ID, 'thumbnail'). '&lt;/p&gt;'. $content; return $content;}
```

উপরের কোডটা কপি করে আপনি আপনার ওয়ার্ডপ্রেস থিম এর functions.php ফাইলে পেস্ট করে সেভ করুন। ব্যাস কাজ শেষ এখন থেকে আপনার ওয়ার্ডপ্রেস আরএসএস ফীড এ থাম্বনেইল দেখাবে।  
 ধন্যবাদ সবাইকে।

এই টিউন টি প্রথম প্রকাশিত: [‘আইটি বাতায়ন‘](http://itbatayan.com/)
