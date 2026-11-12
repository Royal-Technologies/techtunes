---
archive_id: techtunes-676837
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 676837
title: Android Code এর বিস্তারিত ব্যবহার
slug: sci-tech-676837
language: bn
status: publish
published_at: '2023-11-25T04:00:00+00:00'
modified_at: '2023-11-20T06:02:00+00:00'
original_url: https://www.techtunes.io/sci-tech/tune-id/676837
author: মো তানজিন প্রধান
author_url: https://www.techtunes.io/tuner/tanzin-2
categories:
- বিজ্ঞান ও প্রযুক্তি
tags: []
content_hash: 5d5fec3ac9ba9b5ff18e16eff2bb3fc13dbfd547ccccf86caeedc783b2ff6ea6
archived_at: '2026-11-12T12:17:26.746064+00:00'
---

টেকটিউনস কমিউনিটির সদস্যরা, কেমন আছেন সবাই?

আশা করছি সবাই ভালো আছেন। বরাবরের মত চলে এসেছি নতুন কোন টিউন নিয়ে।

আজ আমি আপনাদেরকে Android  মোবাইল এর কয়েকটা গুরুত্বপূর্ণ কোড নিয়ে আলোচনা করব। তাহলে চলুন শুরু করা যাক।

## গুরুত্বপূর্ণ Android কোড

আমরা অনেক সময় কোন গুরুত্বপূর্ণ কাজ বা মীটিং এ থাকি। সেখানে আমরা কোন ফোন কল আশাকরি না। আমরা যদি incoming call বন্ধ করতে চাই তবে Dial pad এ গিয়ে dial করব \*21# অথবা \* 61#.আবার এই সার্ভিস বন্ধ করতে dial করব যথাক্রমে #21# ও #61#।

![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_572dc66ef073def2901e8c76a3435241.jpg)

আবার যখন আমাদের ফোন কাউকে কিছুক্ষন এর জন্য দেই তখন আমরা কেউ কেউ চাইনা কেউ আমাদের ফোন কারো সাথে কথা বলার জন্য কব্যহার করুক। তখন আমরা outgoing call বন্ধ করব। এজন্য dial করতে হবে \*31# এবং এই সার্ভিস বন্ধ করতে dial করতে হবে #31#।

![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_4a1b4646ac44cdcf7c57bf0af7f90eb6.jpg)

আবার আমরা যখন অন্য কারো সাথে কথা বলি তখন অন্য অনেকেই ফোন দেয় কিন্তু আমরা বুঝতে পারি না কে ফোন দিলো। এই সমস্যা দূর করতে dial pad এ dial করতে হবে \* 43#.কোডটি dial করলে কথা বলা অবস্থায় অন্য ব্যক্তির কল ঢুকবে এবং আপনি চাইলে রিসিভ করতে পারবেন। সার্ভিস টি বন্ধ করতে dial #43#.

![](https://dnc.techtunes.io/tDrive/tuner/2020/12/techtunes_09f59fd9260486e1008cace80bbb6b3d.jpg)

আপনার ব্যবহার কৃত ফোনের IMEI (International Mobile Equipment Identity) নাম্বার বের করতে চাইলে dial \*#06#.

আপনার ফোনের সম্পুর্ণ তথ্য জানতে dial \*#\*#4636#\*#\*.যেমন; uses status, battary life etc.

\*#\*#7780#\*#\* এই কোডটি ফোন এর factory data reset এর জন্য। যারা বোঝেন তাড়াই factory data reset দেবার সময় dial করবেন।

ফোন বন্ধ করার সময় power button এ চাপ দিলে অনেক গুলো অপশন আসে। অনেক সময় এটা আমাদের বিরক্তি লাগে। power button দিয়ে ফোন সরাসরি বন্ধ করতে চাইলে dial \*#\*#7594#\*#\*.

টিউন টি কাজে আসলে জোসস দিতে ভুলবেন না। মন্তব্য থাকলে টিউমেন্ট এ আমাকে জানাতে ভুলবেন না।
