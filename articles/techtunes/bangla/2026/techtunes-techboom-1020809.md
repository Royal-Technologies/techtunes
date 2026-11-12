---
archive_id: techtunes-1020809
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 1020809
title: Google-এর মহাপ্রলয় শুরু! চলে এলো Gemma 4 AI Model! যেখানে পাবেন Apache 2 License,
  128 Expert MoE, 256K Context Window আর Native Audio-Vision ফিচারের কম্বিনেশন যা
  পুরো AI মার্কেট জ্বালিয়ে খাক করে দিবে!
slug: techtunes-techboom-1020809
language: bn
status: publish
published_at: '2026-04-04T13:48:00+00:00'
modified_at: '2026-04-11T13:07:00+00:00'
original_url: https://www.techtunes.io/techtunes-techboom/tune-id/1020809
author: টেকটিউনস টেকবুম
author_url: https://www.techtunes.io/tuner/techboom
categories:
- টেকটিউনস টেকবুম
tags: []
content_hash: 6ddcce5b5b81510cc151b73a133b0dadae3fcbb0afdd9146a817f1abc509318b
archived_at: '2026-11-12T11:38:53.858439+00:00'
---

Text World-এ বর্তমানে আলোচনার কেন্দ্রবিন্দুতে রয়েছে Artificial Intelligence। আর এই আলোচনার পারদ আরও বাড়িয়ে দিয়ে Google বিশ্বজুড়ে রিলিজ করেছে তাদের সবথেকে শক্তিশালী এবং আধুনিক Open Model Series— Gemma 4। আপনারা যারা AI প্রযুক্তির খোঁজখবর রাখেন, তারা জানেন যে Google-এর আগের Models-গুলো নিয়েও অনেক এক্সাইটেড ছিল। কিন্তু এবারের Gemma 4 রিলিজের পর পরিস্থিতি পুরোপুরি বদলে গেছে। এটি শুধু একটি Model নয়, বরং চারটি ভিন্ন ভিন্ন Model-এর একটি শক্তিশালী Family, যা Multi-Modality, Internal Thinking, Function Calling এবং আরও অনেক অত্যাধুনিক Features-এ ভরপুর।

আজকের টিউনে এই Gemma 4 নিয়ে In-depth আলোচনা করব এবং বোঝার চেষ্টা করব কেন এটি Developers এবং সাধারণ Users-দের জন্য একটি বিশাল আশীর্বাদ।

## ১. Apache 2 License: এক ঐতিহাসিক স্বাধীনতার সূচনা

Gemma 4 নিয়ে কথা বলার শুরুতে সবচেয়ে বড় যে বিষয়টি সামনে আসে, তা Model-এর Performance নয় বরং এর License। অতীতে Google যখন Gemma Series-এর আগের Models-গুলো রিলিজ করেছিল, তখন সেগুলোতে কিছু জটিল Custom License এবং Restrictions ছিল। যেমন— "আমাদের সাথে প্রতিযোগিতা করা যাবে না" বা Model ব্যবহারের ক্ষেত্রে অনেক সীমাবদ্ধতা ছিল। এর ফলে অনেক Developer বাধ্য হয়ে Llama বা Qwen-এর দিকে ঝুঁকে পড়েছিলেন।

কিন্তু এবার Google পুরো Game বদলে দিয়েছে। Gemma 4 এখন সম্পূর্ণভাবে একটি প্রকৃত Apache 2 License-এর অধীনে বাজারে এসেছে। এর মানে হলো, এখন কোনো রকম শর্ত ছাড়াই আপনি Google-এর এই শক্তিশালী Model-টিকে নিজের মতো করে Modify করতে পারবেন, আপনার নিজস্ব Data দিয়ে Fine-Tune করতে পারবেন এবং সম্পূর্ণ Commercially Deploy করতে পারবেন। এই উদারতা প্রমাণ করে যে Google এখন অন্যান্য Open Model Providers-দের সাথে সমান তালে পাল্লা দিতে প্রস্তুত। মজার ব্যাপার হলো, যখন China-এর কিছু বড় বড় Company তাদের Models-গুলো সাধারণের জন্য বন্ধ করে দিচ্ছে, ঠিক তখনই Google তাদের সেরা প্রযুক্তি সবার জন্য উন্মুক্ত করে দিয়েছে।

## ২. মডেল ফ্যামিলি পরিচিতি: Workstation এবং Edge Tier

Google মূলত Gemma 4-কে দুটি প্রধান স্তরে বা Tiers-এ ভাগ করেছে যাতে Professional থেকে শুরু করে সাধারণ শখের বশে AI ব্যবহারকারী—সবাই উপকৃত হতে পারেন।

### Workstation Models (প্রফেশনাল কাজের জন্য)

এই Models-গুলো মূলত শক্তিশালী PC বা Server-এ চালানোর জন্য Design করা হয়েছে।

- **31 Billion Parameter Dense Model:** এটি একটি অত্যন্ত শক্তিশালী Model। এতে আগের Versions-গুলোর চেয়ে Layer কম থাকলেও অনেক গুরুত্বপূর্ণ Architectural Upgrades করা হয়েছে। এটি মূলত Coding এবং জটিল Data Processing-এর জন্য সেরা।
- **26 Billion Parameter Mixture of Experts (MoE) Model:** এটি মূলত বুদ্ধিমত্তা এবং সাশ্রয়—এই দুইয়ের এক অপূর্ব সংমিশ্রণ। এর মোট Parameter 26 Billion হলেও একই সময়ে মাত্র 3.8 Billion Active থাকে। এতে 128 Tiny Experts রয়েছে, যেখানে প্রতি Token-এর জন্য মাত্র ৮টি Expert সক্রিয় হয় এবং সাথে একটি Shared Always-on Expert কাজ করে। এর ফলে আপনি একটি 27B Model-এর বুদ্ধিমত্তা পাবেন মাত্র একটি 4B Model-এর সমপরিমাণ Compute খরচে। এই Models-গুলোর Context Window হলো অবিশ্বাস্য— 256K।

### Edge Models (স্মার্টফোন এবং ছোট ডিভাইসের জন্য)

এগুলো হলো **E2B** (2 Billion) এবং **E4B** (4 Billion) Model। এগুলো এতটাই ছোট যে আপনি অনায়াসেই আপনার Phone, Raspberry Pi, বা Jetson Nano-তে চালাতে পারবেন। এগুলোর Context Window হলো 128K। সবথেকে বড় চমক হলো, এই ছোট Models-গুলোতেই মূলত Native Audio Support রাখা হয়েছে।

## ৩. Gemini 3 Research: ফ্ল্যাগশিপ প্রযুক্তির ছোঁয়া

অনেকেই হয়তো ভাবছেন Gemma 4-এর এই অসাধারণ শক্তির উৎস কী? Google পরিষ্কার জানিয়েছে যে, এই Models-গুলো তৈরি করা হয়েছে তাদের Flagship Gemini 3 Research-এর ওপর ভিত্তি করে। অর্থাৎ Google তাদের সবচেয়ে দামী এবং শক্তিশালী Commercial Models-এ যেসব উদ্ভাবন ব্যবহার করে, সেগুলোই এখন তারা এই Open Weights Models-এর ভেতরে দিয়ে দিয়েছে।

বর্তমান বাজারে অনেক Model রয়েছে যেগুলো মূলত Text-Only অথবা বড়জোর Text Plus Vision। আপনি যদি আগে Audio ব্যবহার করতে চাইতেন, তবে আপনাকে আলাদা করে Whisper বা অন্য কোনো External ASR Pipeline যোগ করতে হতো। কিন্তু Gemma 4-এর বিশেষত্ব হলো— এর Vision, Audio, Thinking, এবং Function Calling সবকিছুই Model-এর Architecture-এর ভেতরে সরাসরি গেঁথে দেওয়া হয়েছে (Natively Built-in)। এটি কোনো আলাদাভাবে জুড়ে দেওয়া বা Bolted on কোনো ফিচার নয়, বরং এটি একদম ভেতর থেকে তৈরি।

## ৪. মাল্টি-মোডালিটি এবং Long Chain of Thought Reasoning

Gemma 4-এর অন্যতম শক্তিশালী দিক হলো এর Thinking বা চিন্তা করার সক্ষমতা। এটি এখন কোনো জটিল প্রশ্নের উত্তর দেওয়ার আগে মানুষের মতো করে গভীরভাবে ভাবতে পারে, যাকে প্রযুক্তির ভাষায় Long Chain of Thought Reasoning বলা হয়। এর সবথেকে আধুনিক দিকটি হলো, এই Reasoning শুধু Text-এর মধ্যে সীমাবদ্ধ নয়। এটি এখন Images এবং প্রথমবারের মতো Audio-এর ওপর ভিত্তি করেও Reasoning করতে পারে।

এই সক্ষমতার কারণেই এটি MMU Pro এবং SweetBench Pro-এর মতো অত্যন্ত কঠিন সব Benchmarks-এ অবিশ্বাস্য ফলাফল দেখাতে সক্ষম হয়েছে। ব্যবহারকারীরা যখন Model-টি ব্যবহার করবেন, তখন চাইলে Model-এর Chat Template-এ খুব সহজেই Enable Thinking = True বা False করে এই সুবিধাটি নিয়ন্ত্রণ করতে পারবেন।

## ৫. উন্নত ফাংশন কলিং এবং এজেন্টিক ফ্লো

আপনি যদি AI দিয়ে কোনো অটোমেশন বা Agentic কাজ করাতে চান, তবে আপনার জন্য Function Calling অত্যন্ত জরুরি। Gemma 4-এ Google তাদের গত বছরের জনপ্রিয় Function Gemma Model-এর সব গবেষণাকে একীভূত করেছে। এটি এখন শুধু Instruction ফলো করে না, বরং Model-এর ভেতরেই Function Calling করার ক্ষমতা গেঁথে দেওয়া হয়েছে। এটি Multi-Turn Agentic Flows এবং একাধিক Tools ব্যবহারের ক্ষেত্রে অসাধারণ পারফরম্যান্স দেখায়। এটি মূলত Production Level-এর কাজের জন্য একদম Perfect।

## ৬. অডিও এবং ভিশন প্রযুক্তির বিস্ময়কর উন্নতি

### শক্তিশালী ও সাশ্রয়ী অডিও এনকোডার

Gemma 4-এর ছোট Models-গুলোতে (E2B এবং E4B) চমৎকার Audio Support দেওয়া হয়েছে। এটি আগের Gemma 3N-এর চেয়ে অনেক গুণ ভালো। Google এর Audio Encoder-কে 50% ছোট করে ফেলেছে— 681 মিলিয়ন Parameter থেকে কমিয়ে মাত্র 305 মিলিয়ন করা হয়েছে। এর ফলে Disk Space 390 মেগাবাইট থেকে কমিয়ে মাত্র 87 মেগাবাইট হয়ে গেছে। এছাড়া এর Frame Duration 160 মিলিসেকেন্ড থেকে কমিয়ে 40 মিলিসেকেন্ড করার ফলে এটি এখন অনেক দ্রুত গতিতে এবং নিখুঁতভাবে Transcription বা ASR করতে পারে। এর মাধ্যমে আপনি সরাসরি Speech to Translated Text (যেমন English ভাষায় কথা বলে Japanese Text Output পাওয়া) সুবিধা পাবেন।

### আধুনিক ভিশন এনকোডার

মডেলটির Vision Encoder এখন আগের চেয়ে অনেক হালকা এবং দ্রুত (মাত্র 150 মিলিয়ন Parameter)। এতে Native Aspect Ratio Processing যুক্ত করা হয়েছে, যার ফলে এটি Image বা Document-এর সঠিক Size এবং Dimension নিজেই Handle করতে পারে। এটি OCR (Optical Character Recognition) এবং Document Understanding-এর জন্য অত্যন্ত কার্যকর। যেহেতু এটি Interleaved Multi-Image Inputs সমর্থন করে, তাই আপনি চাইলে এটি দিয়ে Video বিশ্লেষণ বা একই সাথে অনেকগুলো Image নিয়ে চিন্তা করার কাজও করাতে পারেন।

## ৭. কোডিং এবং বহুভাষিক সক্ষমতা: এক বিশাল ভাণ্ডার

Workstation Models-গুলো মূলত Developers-দের ব্যক্তিগত Coding Assistant হিসেবে কাজ করার জন্য তৈরি। এটি Code Generation, Completion এবং Correction-এ অত্যন্ত দক্ষ। যারা Coding শিখছেন বা Professional Developers, তাদের জন্য এটি একটি IDE Copilot হিসেবে কাজ করবে। এছাড়া এটি সম্পূর্ণ Multilingual; এর Pre-Training-এ 140টি ভাষা এবং Post-Training বা Instruction Fine-Tuning-এ 35টি ভাষা ব্যবহার করা হয়েছে। ফলে ভাষার বৈচিত্র্য নিয়ে আপনাকে একদম চিন্তা করতে হবে না।

## ৮. হার্ডওয়্যার রিকোয়ারমেন্ট এবং বাস্তব অভিজ্ঞতা

আপনি যদি এই Models-গুলো নিয়ে হাতে-কলমে কাজ করতে চান, তবে আপনার জন্য ভালো খবর আছে। ছোট Models-গুলো (যেমন E2B) আপনি সাধারণ একটি T4 GPU-তেই অনায়াসেই চালাতে পারবেন। বড় Models-গুলোর জন্য আপনাকে কিছুটা শক্তিশালী Hardware যেমন H100 বা RTX 6000 Pro ব্যবহার করতে হতে পারে।

Google তাদের QAT Checkpoints (Quantized Aware Training) রিলিজ করছে, যাতে কম Memory খরচ করেও Model-এর গুণগত মান একদম ঠিক থাকে। বাস্তব পরীক্ষায় দেখা গেছে, এটি একটি মেয়ের সাথে কুকুরের Image বা জটিল কোনো Audio File থেকে অত্যন্ত নিখুঁতভাবে তথ্য বের করে আনতে পারে। এমনকি একটি Audio File-এ নারী ও পুরুষের আলাদা আলাদা কণ্ঠস্বরও এটি নিখুঁতভাবে সনাক্ত করতে পারে।

## ৯. ক্লাউড এবং ডেপ্লয়মেন্টের সহজ উপায়

Gemma 4 এখন Hugging Face এবং Google Cloud-এ সহজলভ্য। যারা বড় Models সার্ভারে চালাতে চান, তাদের জন্য একটি দুর্দান্ত ফিচার হলো Serverless Cloud Run। Google Cloud-এর মাধ্যমে এখন আপনি G4 GPU (Nvidia RTX Pro 6000) ব্যবহার করে এই Models-গুলো চালাতে পারবেন, যেখানে 96GB VRAM পাওয়া যাবে। এর সবথেকে বড় সুবিধা হলো, আপনার কাজ শেষ হওয়ার পর এটি নিজে থেকেই বন্ধ হয়ে যাবে (Spin Down to Zero), যার ফলে অহেতুক বিল আসার কোনো ভয় নেই।

## AI বিপ্লবের এক নতুন সূর্যোদয়

পরিশেষে বলা যায়, Gemma 4 রিলিজের মাধ্যমে Google AI দুনিয়ায় এক বিশাল মাইলফলক স্থাপন করল। এর Open Weights এবং স্বচ্ছ Apache 2 License Developers এবং Innovators-দের জন্য এক বিশাল স্বাধীনতার দুয়ার খুলে দিয়েছে। আপনি যদি আপনার নিজস্ব কোনো App, Chatbot বা Coding Project-এ একটি শক্তিশালী এবং সাশ্রয়ী AI Model ব্যবহার করতে চান, তবে Gemma 4 হতে পারে আপনার শ্রেষ্ঠ হাতিয়ার।

সামনে হয়তো এই Family-র আরও নতুন Model আসবে, তবে এই চারটি Version-ই আমাদের AI ব্যবহারের ধারণা বদলে দেওয়ার জন্য যথেষ্ট। এখনই সময় এই Models-গুলো নিয়ে Experiment করার এবং নতুন কিছু উদ্ভাবন করার! আপনার এই Model-টি কেমন লাগল বা ভবিষ্যতে এটি দিয়ে কী করতে চান, তা জানাতে ভুলবেন না। আজকের মতো এখানেই শেষ করছি, দেখা হবে নতুন কোনো প্রযুক্তির গল্প নিয়ে! বিদায়!
