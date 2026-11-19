---
archive_id: techtunes-1025785
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 1025785
title: Google AI Studio দিয়ে তৈরি করুন চমৎকার একটি এআই চ্যাটবট অ্যাপ
slug: android-apps-1025785
language: bn
status: publish
published_at: '2026-11-18T06:08:00+00:00'
modified_at: '2026-11-18T06:08:00+00:00'
original_url: https://www.techtunes.io/android-apps/tune-id/1025785
author: আয়ান কিং
author_url: https://www.techtunes.io/tuner/ayanbepari
categories:
- অ্যান্ড্রয়েড Apps
tags: []
content_hash: 0c30bf292cd3bfd6cce32e0846462cb7c9fdab998805926ce8f61f2268b46582
archived_at: '2026-11-19T05:58:17.986846+00:00'
---

পর্ব ১: গুগল এআই স্ট

‎পর্ব ১: গুগল এআই স্টুডিও (Google AI Studio) দিয়ে অ্যাপ তৈরির এ-টু-জেড গাইড (প্রাথমিক ধারণা ও সেটআপ)

‎​বর্তমান সময়ে কৃত্রিম বুদ্ধিমত্তা বা এআই (AI) ব্যবহার করে সফটওয়্যার ও মোবাইল অ্যাপ তৈরি করা প্রযুক্তির সবচেয়ে বড় বিপ্লব। আগে যেখানে একটি চ্যাটবট বা স্মার্ট অ্যাপ তৈরি করতে মাসের পর মাস মেশিন লার্নিং এবং জটিল অ্যালগরিদম নিয়ে কোডিং করতে হতো, সেখানে Google AI Studio এবং Gemini API সেই কাজটিকে মাত্র কয়েক ঘণ্টার ব্যাপার করে দিয়েছে।

‎​আপনি যদি মোবাইল বা ওয়েব অ্যাপ তৈরি করে গুগল প্লে-স্টোর, অ্যাপ স্টোর কিংবা কোডক্যানিয়ন (CodeCanyon)-এর মতো মার্কেটপ্লেসে বিক্রি করতে চান, তবে গুগল এআই স্টুডিও হতে পারে আপনার সেরা হাতিয়ার।

‎​১. গুগল এআই স্টুডিও কী এবং কেন এটি সেরা?

‎​গুগল এআই স্টুডিও হলো গুগলের একটি ব্রাউজার-ভিত্তিক ডেভেলপমেন্ট প্ল্যাটফর্ম বা প্রোটোটাইপিং টুল। এর মাধ্যমে ডেভেলপাররা সরাসরি গুগলের শক্তিশালী জেমিনি (Gemini) এআই মডেলগুলো ব্যবহার করে নিজের অ্যাপের জন্য কাস্টম লজিক, চ্যাট সিস্টেম, ইমেজ অ্যানালাইসিস এবং কোড জেনারেট করতে পারেন।

‎​সহজ ইন্টিগ্রেশন: কোনো ভারী সার্ভার বা সুপার কম্পিউটার ছাড়াই শুধুমাত্র একটি API Key ব্যবহার করে আপনার সাধারণ অ্যান্ড্রয়েড বা ওয়েব অ্যাপকে সুপার-স্মার্ট এআই অ্যাপে রূপান্তর করা যায়।

‎​ফ্রি টিয়ার (Free Tier): নতুন ডেভেলপারদের জন্য গুগল প্রতি মিনিটে নির্দিষ্ট সংখ্যক রিকোয়েস্ট একদম বিনামূল্যে (Free) ব্যবহারের সুযোগ দেয়, যা দিয়ে আপনি অনায়াসেই অ্যাপ তৈরি ও টেস্ট করতে পারবেন।

‎​মাল্টিমোডাল ক্ষমতা: এটি শুধু টেক্সট নয়, বরং ছবি, অডিও, ভিডিও এবং পিডিএফ ফাইল পড়েও উত্তর দিতে পারে।

‎​২. অ্যাপ তৈরির জন্য প্রয়োজনীয় প্রস্তুতি ও টুলস

‎​গুগল এআই স্টুডিও দিয়ে একটি পূর্ণাঙ্গ অ্যাপ বানানোর জন্য আপনার নিচের জিনিসগুলো প্রয়োজন হবে:

‎​একটি গুগল অ্যাকাউন্ট (Gmail): এআই স্টুডিওতে লগইন করার জন্য।

‎​কোড এডিটর বা আইডিই (IDE): ওয়েব অ্যাপের জন্য VS Code এবং অ্যান্ড্রয়েড মোবাইল অ্যাপের জন্য Android Studio (অথবা মোবাইলে টেস্ট করার জন্য Acode / WebView বিল্ডার)।

‎​বেসিক কোডিং জ্ঞান: HTML, CSS, JavaScript (ওয়েব অ্যাপের জন্য) অথবা Kotlin/Java/Flutter (মোবাইল অ্যাপের জন্য)। তবে এআই-এর সাহায্য নিয়ে কোড কপি-পেস্ট করেও কাজ করা সম্ভব।

‎​৩. ধাপে ধাপে প্রজেক্ট সেটআপ ও API Key তৈরি

‎​অ্যাপ তৈরির একদম প্রথম ধাপে আপনাকে গুগলের সার্ভারের সাথে আপনার অ্যাপের সংযোগ স্থাপন করতে হবে:

‎​১. প্ল্যাটফর্মে প্রবেশ: ব্রাউজারে গিয়ে aistudio.google.com ওপেন করুন এবং জিমেইল দিয়ে সাইন-ইন করুন।

1. ‎নতুন প্রজেক্ট তৈরি: ড্যাশবোর্ডে প্রবেশ করার পর বাম পাশের মেনু থেকে "Get API key" অপশনে ক্লিক করুন।

2. ‎API Key জেনারেট: এখানে "Create API key" বাটনে ক্লিক করুন। গুগল ক্লাউডের একটি নতুন প্রজেক্ট সিলেক্ট করে কী-টি তৈরি করুন। এটি দেখতে অনেকটা AIzaSyD-9x8c7v6b5n4m. এমন লম্বা কোডের মতো হবে।

3. ‎নিরাপত্তা সতর্কতা: এই API Key-টি কখনোই পাবলিক জায়গায় বা সরাসরি গিটহাবে (GitHub) শেয়ার করবেন না। কেউ এটি পেয়ে গেলে আপনার অ্যাকাউন্টের লিমিট ব্যবহার করে ফেলতে পারে।

‎​৪. সঠিক জেমিনি মডেল নির্বাচন (Model Selection)

‎​অ্যাপ তৈরির সময় আপনাকে ঠিক করতে হবে আপনার অ্যাপের কাজের ধরন অনুযায়ী কোন মডেলটি সবচেয়ে ভালো কাজ করবে:

‎​Gemini 1.5 Flash / 2.0 Flash: আপনার অ্যাপে যদি খুব দ্রুত (Fast Response) উত্তরের প্রয়োজন হয়—যেমন লাইভ চ্যাটবট, কাস্টমার সাপোর্ট বা গেমিং অ্যাসিস্ট্যান্ট—তবে এই মডেলটি সেরা। এটি অনেক হালকা এবং দ্রুত কাজ করে।

‎​Gemini 1.5 Pro / 2.0 Pro: আপনার অ্যাপটি যদি জটিল কোডিং, বড় কোনো আর্টিকেল লেখা, ডকুমেন্ট বিশ্লেষণ বা গাণিতিক সমাধানের জন্য তৈরি হয়, তবে Pro মডেলটি ব্যবহার করা উচিত।

‎​৫. সিস্টেম ইনস্ট্রাকশন (System Instructions) সেট করা

‎​আপনার অ্যাপের এআই কীভাবে কথা বলবে, তা নির্ধারণ করার সবচেয়ে গুরুত্বপূর্ণ অংশ হলো System Instructions।

‎ধরুন, আপনি একটি "বাংলা কন্টেন্ট রাইটিং অ্যাপ" বানাচ্ছেন। সেক্ষেত্রে System Instructions বক্সে আপনাকে লিখে দিতে হবে:

‎​"তুমি একজন পেশাদার বাংলা কন্টেন্ট রাইটার। ব্যবহারকারী যেকোনো বিষয় দিলে তুমি সেটিকে সহজ, প্রাঞ্জল ও আকর্ষণীয় বাংলা ভাষায় পয়েন্ট আকারে সাজিয়ে লিখবে। কোনো ইংরেজি অক্ষর বা অপ্রয়োজনীয় তথ্য দেবে না। "

‎​এই নির্দেশনাটি সেট করে দিলে আপনার অ্যাপের ভেতর এআই কখনোই তার মূল চরিত্রের বাইরে যাবে না।

‎পর্ব ২: অ্যাপের ফ্রন্টএন্ড ডিজাইন এবং বাস্তব প্রজেক্ট কোডিং (সম্পূর্ণ এআই চ্যাটবট অ্যাপ তৈরি)

‎​গুগল এআই স্টুডিও থেকে আপনার API Key এবং System Instructions ঠিক করার পর, এবার সময় এসেছে একটি বাস্তব ও কার্যকরী অ্যাপ তৈরি করার। এই পর্বে আমরা দেখব কীভাবে HTML, CSS এবং JavaScript ব্যবহার করে একটি আধুনিক, ডার্ক-থিম যুক্ত এআই অ্যাপ (ওয়েব অ্যাপ, যা পরবর্তীতে সহজেই অ্যান্ড্রয়েড APK-তে রূপান্তর করা যায়) তৈরি করা হয়।

‎​১. অ্যাপের কাঠামো বা আর্কিটেকচার (App Architecture)

‎​যেকোনো আধুনিক এআই অ্যাপের তিনটি মূল স্তর বা লেয়ার থাকে:

‎​1. ইউজার ইন্টারফেস (Frontend - HTML/CSS): ব্যবহারকারী যা স্ক্রিনে দেখতে পান (যেমন: চ্যাট বক্স, মেসেজ টাইপ করার জায়গা, সেন্ড বাটন এবং রেসপন্স দেখানোর কার্ড)।

‎​2. লজিক ও এপিআই হ্যান্ডলার (JavaScript): ব্যবহারকারীর লেখা প্রশ্নটি সংগ্রহ করে গুগলের জেমিনি (Gemini) সার্ভারে পাঠানো এবং সার্ভার থেকে আসা উত্তরটি স্ক্রিনে দেখানোর কাজ করে।

‎​3. এআই ইঞ্জিন (Google Gemini API): গুগলের ক্লাউড সার্ভার, যেখানে মূল প্রসেসিং হয় এবং বুদ্ধিমান উত্তর তৈরি হয়।

‎​২. পূর্ণাঙ্গ প্রজেক্ট কোড (Complete Source Code)

‎​নিচে একটি পূর্ণাঙ্গ "AI Content & Chat Assistant" অ্যাপের কোড দেওয়া হলো। আপনি কম্পিউটারে VS Code অথবা মোবাইলে Acode অ্যাপ ব্যবহার করে index.html নামে একটি ফাইল তৈরি করে নিচের সম্পূর্ণ কোডটি পেস্ট করলে সাথে সাথেই আপনার অ্যাপটি কাজ করা শুরু করবে।

‎​(নোট: কোডের ভেতর YOUR\_API\_KEY\_HERE লেখা জায়গায় গুগল এআই স্টুডিও থেকে নেওয়া আপনার আসল API Key-টি বসাতে হবে। )

‎

‎<!DOCTYPE html>

‎<html lang="bn">

‎<head>

‎ <meta charset="UTF-8">

‎ <meta name="viewport" content="width=device-width, initial-scale=1.0">

‎ <title>Smart AI Assistant</title>

‎ <style>

‎ /\* অ্যাপের আধুনিক ডার্ক ডিজাইন \*/

‎ \* {‎ box-sizing: border-box;

‎ margin: 0;

‎ padding: 0;

‎ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

‎}

‎

‎ body {‎ background-color: #0f172a;

‎ color: #f8fafc;

‎ display: flex;

‎ flex-direction: column;

‎ height: 100vh;

‎}

‎

‎ header {‎ background-color: #1e293b;

‎ padding: 16px 20px;

‎ text-align: center;

‎ border-bottom: 1px solid #334155;

‎ box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);

‎}

‎

‎ header h1 {‎ font-size: 1.3rem;

‎ color: #38bdf8;

‎ letter-spacing: 0.5px;

‎}

‎

‎ header p {‎ font-size: 0.8rem;

‎ color: #94a3b8;

‎ margin-top: 4px;

‎}

‎

‎ #chat-container {‎ flex: 1;

‎ overflow-y: auto;

‎ padding: 20px;

‎ display: flex;

‎ flex-direction: column;

‎ gap: 15px;

‎}

‎

‎.message {‎ max-width: 82%;

‎ padding: 12px 16px;

‎ border-radius: 14px;

‎ line-height: 1.5;

‎ font-size: 0.95rem;

‎ word-wrap: break-word;

‎ white-space: pre-wrap;

‎}

‎

‎.user-message {‎ background-color: #2563eb;

‎ color: #ffffff;

‎ align-self: flex-end;

‎ border-bottom-right-radius: 4px;

‎}

‎

‎.ai-message {‎ background-color: #1e293b;

‎ color: #e2e8f0;

‎ align-self: flex-start;

‎ border: 1px solid #334155;

‎ border-bottom-left-radius: 4px;

‎}

‎

‎.loading {‎ font-style: italic;

‎ color: #38bdf8;

‎ font-size: 0.85rem;

‎ align-self: flex-start;

‎}

‎

‎ #input-area {‎ background-color: #1e293b;

‎ padding: 12px 15px;

‎ display: flex;

‎ gap: 10px;

‎ border-top: 1px solid #334155;

‎}

‎

‎ #user-input {‎ flex: 1;

‎ background-color: #0f172a;

‎ border: 1px solid #475569;

‎ color: #f8fafc;

‎ padding: 12px 15px;

‎ border-radius: 25px;

‎ font-size: 0.95rem;

‎ outline: none;

‎}

‎

‎ #user-input:focus {‎ border-color: #38bdf8;

‎}

‎

‎ #send-btn {‎ background-color: #38bdf8;

‎ color: #0f172a;

‎ border: none;

‎ padding: 0 22px;

‎ border-radius: 25px;

‎ font-weight: bold;

‎ font-size: 0.95rem;

‎ cursor: pointer;

‎ transition: background 0.2s;

‎}

‎

‎ #send-btn:hover {‎ background-color: #0284c7;

‎ color: #ffffff;

‎}

‎

‎ #send-btn:disabled {‎ background-color: #475569;

‎ cursor: not-allowed;

‎}

‎ </style>

‎</head>

‎<body>

‎

‎ <header>

‎ <h1>AI Smart Studio</h1>

‎ <p>Powered by Google Gemini API</p>

‎ </header>

‎

‎ <div id="chat-container">

‎ <div class="message ai-message">স্বাগতম! আমি আপনার এআই অ্যাসিস্ট্যান্ট। আজ আপনাকে কীভাবে সাহায্য করতে পারি?</div>

‎ </div>

‎

‎ <div id="input-area">

‎ <input type="text" id="user-input" placeholder="এখানে আপনার প্রশ্ন বা বিষয় লিখুন." autocomplete="off">

‎ <button id="send-btn">পাঠান</button>

‎ </div>

‎

‎ <script>

‎ // আপনার Google AI Studio API Key এখানে বসান

‎ const API\_KEY = "YOUR\_API\_KEY\_HERE";

‎ const API\_URL = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${API\_KEY}`;

‎

‎ const chatContainer = document.getElementById('chat-container');

‎ const userInput = document.getElementById('user-input');

‎ const sendBtn = document.getElementById('send-btn');

‎

‎ // স্ক্রিনে মেসেজ যোগ করার ফাংশন

‎ function appendMessage(text, className) {‎ const msgDiv = document.createElement('div');

‎ msgDiv.classList.add('message', className);

‎ msgDiv.textContent = text;

‎ chatContainer.appendChild(msgDiv);

‎ chatContainer.scrollTop = chatContainer.scrollHeight;

‎ return msgDiv;

‎}

‎

‎ // এআই-এর সাথে যোগাযোগ করার মূল ফাংশন

‎ async function sendMessage() {‎ const promptText = userInput.value.trim();

‎ if (!promptText) return;

‎

‎ // ইউজারের মেসেজ দেখানো

‎ appendMessage(promptText, 'user-message');

‎ userInput.value = '';

‎ sendBtn.disabled = true;

‎

‎ // লোডিং ইন্ডিকেটর দেখানো

‎ const loadingDiv = document.createElement('div');

‎ loadingDiv.classList.add('loading');

‎ loadingDiv.textContent = 'এআই উত্তর তৈরি করছে.';

‎ chatContainer.appendChild(loadingDiv);

‎ chatContainer.scrollTop = chatContainer.scrollHeight;

‎

‎ try {‎ const response = await fetch(API\_URL, {‎ method: 'POST',

‎ headers: {‎ 'Content-Type': 'application/json'

‎},

‎ body: JSON.stringify({‎ system\_instruction: {‎ parts: [{text: "তুমি একজন বুদ্ধিমান ও সাহায্যকারী বাংলা এআই অ্যাসিস্ট্যান্ট। সবসময় স্পষ্ট ও গোছানো ভাষায় উত্তর দেবে। "}]

‎},

‎ contents: [{‎ parts: [{text: promptText}]

‎}]

‎})

‎});

‎

‎ const data = await response.json();

‎ chatContainer.removeChild(loadingDiv);

‎

‎ if (data.candidates && data.candidates[0].content) {‎ const aiReply = data.candidates[0].content.parts[0].text;

‎ appendMessage(aiReply, 'ai-message');

‎} else if (data.error) {‎ appendMessage(`ত্রুটি: ${data.error.message}`, 'ai-message');

‎} else {‎ appendMessage('দুঃখিত, কোনো উত্তর পাওয়া যায়নি। ', 'ai-message');

‎}

‎

‎} catch (error) {‎ chatContainer.removeChild(loadingDiv);

‎ appendMessage('ইন্টারনেট সংযোগ বা সার্ভার সমস্যা হয়েছে। আবার চেষ্টা করুন। ', 'ai-message');

‎ console.error(error);

‎} finally {‎ sendBtn.disabled = false;

‎ userInput.focus();

‎}

‎}

‎

‎ sendBtn.addEventListener('click', sendMessage);

‎ userInput.addEventListener('keypress', (e) => {‎ if (e.key = 'Enter') sendMessage();

‎});

‎ </script>

‎

‎</body>

‎</html>

‎

‎৩. কোডটি কীভাবে কাজ করছে? (বিস্তারিত ব্যাখ্যা)

‎​ডিজাইন অংশ (<style>): এখানে অ্যাপটির ব্যাকগ্রাউন্ড গাঢ় নীল (#0f172a) রাখা হয়েছে যাতে ব্যবহারকারীর চোখে চাপ না পড়ে। মেসেজগুলো ডান ও বাম পাশে সুন্দর বাবলের (Bubble) মতো সাজানো হয়েছে।

‎​এপিআই কানেকশন (fetch): জাভাস্ক্রিপ্টের fetch মেথড ব্যবহার করে গুগলের gemini-2.5-flash মডেলে POST রিকোয়েস্ট পাঠানো হয়েছে। এটি কোনো থার্ড-পার্টি লাইব্রেরি ছাড়াই সরাসরি ব্রাউজার বা মোবাইল অ্যাপে কাজ করে।

‎​সিস্টেম ইনস্ট্রাকশন (system\_instruction): কোডের ভেতরেই এআই-কে বলে দেওয়া হয়েছে যে সে যেন বাংলায় এবং গুছিয়ে উত্তর দেয়।

‎​এরর হ্যান্ডলিং (try.catch): যদি ইন্টারনেট চলে যায় বা API Key ভুল থাকে, তবে অ্যাপটি ক্র্যাশ না করে ব্যবহারকারীকে সুন্দরভাবে একটি ত্রুটি বার্তা দেখাবে।

‎​৪. এই কোডটিকে মোবাইল অ্যাপ (APK) বানাবেন কীভাবে?

‎​আপনার তৈরি এই index.html ফাইলটিকে সরাসরি অ্যান্ড্রয়েড মোবাইল অ্যাপে রূপান্তর করার দুটি সহজ উপায় আছে:

‎​1. Android Studio (WebView): অ্যান্ড্রয়েড স্টুডিওতে একটি নতুন প্রজেক্ট খুলে assets ফোল্ডারে এই index.html ফাইলটি রেখে একটি WebView কম্পোনেন্ট দিয়ে লোড করলেই এটি পূর্ণাঙ্গ APK হয়ে যাবে।

‎​2. মোবাইল অ্যাপ বিল্ডার (Website 2 APK / Median.co): আপনার কোডটি গিটহাব পেজে (GitHub Pages) বা নেটলিফাইতে (Netlify) ফ্রি হোস্ট করে সেই লিংকটি দিয়ে কয়েক মিনিটের মধ্যেই অ্যান্ড্রয়েড অ্যাপ বানিয়ে নিতে পারেন।

‎

‎পর্ব ৩: অ্যাডভান্সড ফিচার যুক্ত করা (চ্যাট হিস্ট্রি সেভ রাখা, কপি বাটন, ভয়েস ইনপুট এবং ছবি আপলোড করে প্রশ্ন করার ফিচার)

‎​পর্ব ২-এ আমরা একটি বেসিক এআই চ্যাটবট অ্যাপ তৈরি করেছি। কিন্তু ব্যবহারকারীরা যখন একটি অ্যাপ প্লে-স্টোর থেকে ডাউনলোড করেন বা মার্কেটপ্লেস থেকে কেনেন, তখন তারা অ্যাপটিতে প্রফেশনাল কিছু ফিচার আশা করেন। যেমন: অ্যাপ বন্ধ করে আবার চালু করলে আগের চ্যাট যেন মুছে না যায়, এআই-এর লেখা উত্তর এক ক্লিকেই কপি করা যায়, মুখে বলে প্রশ্ন করা যায় (Voice Input), এবং গ্যালারি থেকে ছবি আপলোড করে সেই ছবির বিষয়ে প্রশ্ন করা যায় (Multimodal Vision)।

‎​এই পর্বে আমরা আমাদের আগের অ্যাপটিকে আপগ্রেড করে এই চারটি প্রফেশনাল ফিচার যুক্ত করব।

‎​১. অ্যাডভান্সড ফিচারগুলো কীভাবে কাজ করবে?

‎​চ্যাট হিস্ট্রি সেভ রাখা (localStorage): ব্রাউজার বা ওয়েবভিউ-এর নিজস্ব মেমোরি (localStorage) ব্যবহার করে প্রতিটি মেসেজ সেভ রাখা হবে। এর ফলে অ্যাপ রিলোড দিলেও আগের কথোপকথন থেকে যাবে এবং প্রয়োজনে "Clear Chat" বাটনে ক্লিক করে সব মুছে ফেলা যাবে।

‎​ওয়ান-ক্লিক কপি বাটন (navigator.clipboard): এআই-এর প্রতিটি উত্তরের নিচে একটি ছোট "Copy" বাটন থাকবে, যাতে ক্লিক করলে পুরো উত্তরটি কপি হয়ে যাবে।

‎​ভয়েস ইনপুট (Web Speech API): টাইপ করার ঝামেলা এড়াতে একটি মাইক্রোফোন (🎤) বাটন থাকবে, যাতে ক্লিক করে বাংলায় বা ইংরেজিতে কথা বললে তা অটোমেটিক টেক্সট হয়ে ইনপুট বক্সে বসে যাবে।

‎​ছবি আপলোড করে প্রশ্ন করা (Base64 Image + Gemini Vision): ব্যবহারকারী ক্যামেরা বা গ্যালারি থেকে কোনো ছবি (যেমন: অংকের সমাধান, কোনো পণ্যের ছবি বা নোটের ছবি) সিলেক্ট করলে সেটি Base64 ফরম্যাটে রূপান্তর হয়ে জেমিনি এপিআই-এর কাছে যাবে এবং এআই ছবিটি বিশ্লেষণ করে উত্তর দেবে।

‎​২. আপগ্রেডেড পূর্ণাঙ্গ প্রজেক্ট কোড (Pro Version Source Code)

‎​নিচের কোডটি কপি করে আপনার index.html ফাইলে আগের কোডের বদলে পেস্ট করুন এবং YOUR\_API\_KEY\_HERE জায়গায় আপনার API Key-টি বসিয়ে দিন।

<!DOCTYPE html> <htm

‎<!DOCTYPE html>

‎<html lang="bn">

‎<head>

‎ <meta charset="UTF-8">

‎ <meta name="viewport" content="width=device-width, initial-scale=1.0">

‎ <title>AI Smart Studio Pro</title>

‎ <style>

‎ \* {‎ box-sizing: border-box;

‎ margin: 0;

‎ padding: 0;

‎ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

‎}

‎

‎ body {‎ background-color: #0b1120;

‎ color: #f8fafc;

‎ display: flex;

‎ flex-direction: column;

‎ height: 100vh;

‎}

‎

‎ header {‎ background-color: #1e293b;

‎ padding: 14px 20px;

‎ display: flex;

‎ justify-content: space-between;

‎ align-items: center;

‎ border-bottom: 1px solid #334155;

‎ box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4);

‎}

‎

‎ header h1 {‎ font-size: 1.2rem;

‎ color: #38bdf8;

‎}

‎

‎ #clear-btn {‎ background-color: #ef4444;

‎ color: white;

‎ border: none;

‎ padding: 6px 12px;

‎ border-radius: 6px;

‎ font-size: 0.8rem;

‎ cursor: pointer;

‎}

‎

‎ #chat-container {‎ flex: 1;

‎ overflow-y: auto;

‎ padding: 18px;

‎ display: flex;

‎ flex-direction: column;

‎ gap: 14px;

‎}

‎

‎.message-wrapper {‎ display: flex;

‎ flex-direction: column;

‎ max-width: 85%;

‎}

‎

‎.user-wrapper {‎ align-self: flex-end;

‎}

‎

‎.ai-wrapper {‎ align-self: flex-start;

‎}

‎

‎.message {‎ padding: 12px 16px;

‎ border-radius: 14px;

‎ line-height: 1.5;

‎ font-size: 0.95rem;

‎ word-wrap: break-word;

‎ white-space: pre-wrap;

‎}

‎

‎.user-message {‎ background-color: #2563eb;

‎ color: #ffffff;

‎ border-bottom-right-radius: 4px;

‎}

‎

‎.ai-message {‎ background-color: #1e293b;

‎ color: #e2e8f0;

‎ border: 1px solid #334155;

‎ border-bottom-left-radius: 4px;

‎}

‎

‎.chat-img-preview {‎ max-width: 200px;

‎ border-radius: 8px;

‎ margin-bottom: 8px;

‎ border: 1px solid #475569;

‎}

‎

‎.copy-btn {‎ align-self: flex-start;

‎ background: transparent;

‎ color: #94a3b8;

‎ border: 1px solid #334155;

‎ padding: 3px 8px;

‎ border-radius: 4px;

‎ font-size: 0.75rem;

‎ margin-top: 5px;

‎ cursor: pointer;

‎}

‎

‎.copy-btn:hover {‎ color: #38bdf8;

‎ border-color: #38bdf8;

‎}

‎

‎ #image-preview-bar {‎ display: none;

‎ background-color: #1e293b;

‎ padding: 8px 15px;

‎ border-top: 1px solid #334155;

‎ align-items: center;

‎ gap: 10px;

‎}

‎

‎ #image-preview-bar img {‎ height: 45px;

‎ border-radius: 6px;

‎}

‎

‎ #remove-img-btn {‎ background: #ef4444;

‎ color: white;

‎ border: none;

‎ border-radius: 50%;

‎ width: 22px;

‎ height: 22px;

‎ cursor: pointer;

‎ font-size: 0.8rem;

‎}

‎

‎ #input-area {‎ background-color: #1e293b;

‎ padding: 10px 12px;

‎ display: flex;

‎ align-items: center;

‎ gap: 8px;

‎ border-top: 1px solid #334155;

‎}

‎

‎.icon-btn {‎ background-color: #334155;

‎ color: #f8fafc;

‎ border: none;

‎ width: 40px;

‎ height: 40px;

‎ border-radius: 50%;

‎ font-size: 1.1rem;

‎ cursor: pointer;

‎ display: flex;

‎ align-items: center;

‎ justify-content: center;

‎}

‎

‎.icon-btn.recording {‎ background-color: #ef4444;

‎ animation: pulse 1s infinite;

‎}

‎

‎ @keyframes pulse {‎ 0% {transform: scale(1);}

‎ 50% {transform: scale(1.08);}

‎ 100% {transform: scale(1);}

‎}

‎

‎ #user-input {‎ flex: 1;

‎ background-color: #0f172a;

‎ border: 1px solid #475569;

‎ color: #f8fafc;

‎ padding: 10px 15px;

‎ border-radius: 22px;

‎ font-size: 0.95rem;

‎ outline: none;

‎}

‎

‎ #send-btn {‎ background-color: #38bdf8;

‎ color: #0f172a;

‎ border: none;

‎ padding: 10px 18px;

‎ border-radius: 22px;

‎ font-weight: bold;

‎ cursor: pointer;

‎}

‎

‎.loading {‎ font-style: italic;

‎ color: #38bdf8;

‎ font-size: 0.85rem;

‎}

‎ </style>

‎</head>

‎<body>

‎

‎ <header>

‎ <h1>AI Smart Studio Pro</h1>

‎ <button id="clear-btn">চ্যাট মুছুন</button>

‎ </header>

‎

‎ <div id="chat-container"></div>

‎

‎ <!- নির্বাচিত ছবির প্রিভিউ বার ->

‎ <div id="image-preview-bar">

‎ <img id="preview-thumb" src="" alt="Preview">

‎ <span style="font-size: 0.85rem; color: #cbd5e1;">ছবি সংযুক্ত করা হয়েছে</span>

‎ <button id="remove-img-btn">X</button>

‎ </div>

‎

‎ <div id="input-area">

‎ <!- ছবি আপলোড বাটন ->

‎ <input type="file" id="image-input" accept="image/\*" style="display: none;">

‎ <button class="icon-btn" id="upload-btn" title="ছবি যোগ করুন">📷</button>

‎

‎ <!- ভয়েস ইনপুট বাটন ->

‎ <button class="icon-btn" id="mic-btn" title="মুখে বলুন">🎤</button>

‎

‎ <input type="text" id="user-input" placeholder="প্রশ্ন লিখুন বা ছবি দিন." autocomplete="off">

‎ <button id="send-btn">পাঠান</button>

‎ </div>

‎

‎ <script>

‎ const API\_KEY = "YOUR\_API\_KEY\_HERE";

‎ const API\_URL = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${API\_KEY}`;

‎

‎ const chatContainer = document.getElementById('chat-container');

‎ const userInput = document.getElementById('user-input');

‎ const sendBtn = document.getElementById('send-btn');

‎ const clearBtn = document.getElementById('clear-btn');

‎ const uploadBtn = document.getElementById('upload-btn');

‎ const imageInput = document.getElementById('image-input');

‎ const imagePreviewBar = document.getElementById('image-preview-bar');

‎ const previewThumb = document.getElementById('preview-thumb');

‎ const removeImgBtn = document.getElementById('remove-img-btn');

‎ const micBtn = document.getElementById('mic-btn');

‎

‎ let selectedImageBase64 = null;

‎ let selectedImageMimeType = null;

‎

‎ // লোকাল স্টোরেজ থেকে আগের চ্যাট লোড করা

‎ let chatHistory = JSON.parse(localStorage.getItem('gemini\_chat\_history')) | [‎ {role: 'ai', text: 'স্বাগতম! আমি আপনার Pro এআই অ্যাসিস্ট্যান্ট। আপনি লিখে, মুখে বলে কিংবা যেকোনো ছবি আপলোড করে আমাকে প্রশ্ন করতে পারেন। '}

‎];

‎

‎ function renderChat() {‎ chatContainer.innerHTML = '';

‎ chatHistory.forEach(item => {‎ createMessageElement(item.text, item.role, item.image);

‎});

‎ chatContainer.scrollTop = chatContainer.scrollHeight;

‎}

‎

‎ function createMessageElement(text, role, imageDataUrl = null) {‎ const wrapper = document.createElement('div');

‎ wrapper.classList.add('message-wrapper', role = 'user'? 'user-wrapper' : 'ai-wrapper');

‎

‎ const msgDiv = document.createElement('div');

‎ msgDiv.classList.add('message', role = 'user'? 'user-message' : 'ai-message');

‎

‎ if (imageDataUrl) {‎ const img = document.createElement('img');

‎ img.src = imageDataUrl;

‎ img.classList.add('chat-img-preview');

‎ msgDiv.appendChild(img);

‎}

‎

‎ const textNode = document.createElement('div');

‎ textNode.textContent = text;

‎ msgDiv.appendChild(textNode);

‎ wrapper.appendChild(msgDiv);

‎

‎ // এআই মেসেজের জন্য কপি বাটন যোগ করা

‎ if (role = 'ai') {‎ const copyBtn = document.createElement('button');

‎ copyBtn.classList.add('copy-btn');

‎ copyBtn.textContent = '📋 কপি করুন';

‎ copyBtn.onclick = () => {‎ navigator.clipboard.writeText(text);

‎ copyBtn.textContent = '✅ কপি হয়েছে!';

‎ setTimeout() => copyBtn.textContent = '📋 কপি করুন', 2000);

‎};

‎ wrapper.appendChild(copyBtn);

‎}

‎

‎ chatContainer.appendChild(wrapper);

‎}

‎

‎ function saveHistory() {‎ localStorage.setItem('gemini\_chat\_history', JSON.stringify(chatHistory));

‎}

‎

‎ // ছবি নির্বাচনের লজিক

‎ uploadBtn.addEventListener('click', () => imageInput.click());

‎

‎ imageInput.addEventListener('change', (e) => {‎ const file = e.target.files[0];

‎ if (!file) return;

‎

‎ selectedImageMimeType = file.type;

‎ const reader = new FileReader();

‎ reader.onload = function(event) {‎ const fullDataUrl = event.target.result;

‎ previewThumb.src = fullDataUrl;

‎ imagePreviewBar.style.display = 'flex';

‎ // Base64 অংশটুকু আলাদা করা

‎ selectedImageBase64 = fullDataUrl.split(', ')[1];

‎};

‎ reader.readAsDataURL(file);

‎});

‎

‎ removeImgBtn.addEventListener('click', () => {‎ selectedImageBase64 = null;

‎ selectedImageMimeType = null;

‎ imageInput.value = '';

‎ imagePreviewBar.style.display = 'none';

‎});

‎

‎ // ভয়েস ইনপুট (Speech-to-Text) লজিক

‎ const SpeechRecognition = window.SpeechRecognition | window.webkitSpeechRecognition;

‎ if (SpeechRecognition) {‎ const recognition = new SpeechRecognition();

‎ recognition.lang = 'bn-BD'; // বাংলা ভাষা সেট করা

‎

‎ micBtn.addEventListener('click', () => {‎ recognition.start();

‎ micBtn.classList.add('recording');

‎});

‎

‎ recognition.onresult = (event) => {‎ const transcript = event.results[0][0].transcript;

‎ userInput.value += (userInput.value? ' ' : '') + transcript;

‎ micBtn.classList.remove('recording');

‎};

‎

‎ recognition.onerror = () => {‎ micBtn.classList.remove('recording');

‎ alert('ভয়েস ইনপুট কাজ করছে না। মাইক্রোফোন পারমিশন চেক করুন। ');

‎};

‎

‎ recognition.onend = () => {‎ micBtn.classList.remove('recording');

‎};

‎} else {‎ micBtn.style.display = 'none';

‎}

‎

‎ // মেসেজ পাঠানোর মূল ফাংশন

‎ async function sendMessage() {‎ const promptText = userInput.value.trim();

‎ if (!promptText &&!selectedImageBase64) return;

‎

‎ const currentImagePreview = selectedImageBase64? previewThumb.src : null;

‎ const userPromptDisplay = promptText | "এই ছবিটি সম্পর্কে বিস্তারিত বলো। ";

‎

‎ // ইউজারের মেসেজ সেভ ও প্রদর্শন

‎ chatHistory.push({role: 'user', text: userPromptDisplay, image: currentImagePreview});

‎ saveHistory();

‎ renderChat();

‎

‎ // রিকোয়েস্ট পেলোড তৈরি

‎ const parts = [{text: userPromptDisplay}];

‎ if (selectedImageBase64) {‎ parts.push({‎ inline\_data: {‎ mime\_type: selectedImageMimeType,

‎ data: selectedImageBase64

‎}

‎});

‎}

‎

‎ // ইনপুট রিসেট

‎ userInput.value = '';

‎ const tempBase64 = selectedImageBase64;

‎ removeImgBtn.click();

‎ sendBtn.disabled = true;

‎

‎ const loadingDiv = document.createElement('div');

‎ loadingDiv.classList.add('loading');

‎ loadingDiv.textContent = 'এআই বিশ্লেষণ করছে.';

‎ chatContainer.appendChild(loadingDiv);

‎ chatContainer.scrollTop = chatContainer.scrollHeight;

‎

‎ try {‎ const response = await fetch(API\_URL, {‎ method: 'POST',

‎ headers: {'Content-Type': 'application/json'},

‎ body: JSON.stringify({‎ system\_instruction: {‎ parts: [{text: "তুমি একজন প্রফেশনাল বাংলা এআই অ্যাসিস্ট্যান্ট। সবসময় নির্ভুল, স্পষ্ট ও তথ্যবহুল বাংলায় উত্তর দেবে। "}]

‎},

‎ contents: [{parts: parts}]

‎})

‎});

‎

‎ const data = await response.json();

‎ chatContainer.removeChild(loadingDiv);

‎

‎ if (data.candidates && data.candidates[0].content) {‎ const aiReply = data.candidates[0].content.parts[0].text;

‎ chatHistory.push({role: 'ai', text: aiReply});

‎} else {‎ chatHistory.push({role: 'ai', text: 'দুঃখিত, উত্তর তৈরি করতে সমস্যা হয়েছে। '});

‎}

‎} catch (error) {‎ chatContainer.removeChild(loadingDiv);

‎ chatHistory.push({role: 'ai', text: 'নেটওয়ার্ক ত্রুটি! ইন্টারনেট সংযোগ পরীক্ষা করুন। '});

‎} finally {‎ saveHistory();

‎ renderChat();

‎ sendBtn.disabled = false;

‎}

‎}

‎

‎ clearBtn.addEventListener('click', () => {‎ if (confirm('আপনি কি সব চ্যাট হিস্ট্রি মুছে ফেলতে চান?')) {‎ localStorage.removeItem('gemini\_chat\_history');

‎ chatHistory = [{role: 'ai', text: 'চ্যাট মুছে ফেলা হয়েছে। নতুন প্রশ্ন করুন!'}];

‎ renderChat();

‎}

‎});

‎

‎ sendBtn.addEventListener('click', sendMessage);

‎ userInput.addEventListener('keypress', (e) => {‎ if (e.key = 'Enter') sendMessage();

‎});

‎

‎ // শুরুতে চ্যাট লোড করা

‎ renderChat();

‎ </script>

‎</body>

‎</html>

‎

1. ‎ই কোডের গুরুত্বপূর্ণ কারিগরি দিকগুলো

‎​১. মাল্টিমোডাল পেলোড (inline\_data): জেমিনি এপিআই-এর সবচেয়ে বড় শক্তি হলো এটি একই সাথে টেক্সট এবং Base64 এনকোডেড ছবি গ্রহণ করতে পারে। কোডে FileReader ব্যবহার করে ব্যবহারকারীর ফোনের ছবিটিকে সরাসরি ডেটাতে রূপান্তর করে এপিআই-তে পাঠানো হয়েছে।

1. ‎বাংলা ভয়েস রিকগনিশন (recognition.lang = 'bn-BD'): ব্রাউজারের বিল্ট-ইন স্পিচ ইঞ্জিন ব্যবহার করা হয়েছে, যা বাংলাদেশি বাংলা উচ্চারণ খুব নির্ভুলভাবে টেক্সটে রূপান্তর করতে পারে।

2. ‎ডেটা পারসিসটেন্স (localStorage): ব্যবহারকারী অ্যাপ কেটে দিলেও তার চ্যাট এবং আপলোড করা ছবির হিস্ট্রি ফোনের স্টোরেজে জমা থাকবে।

‎

‎র্ব ৪: এপিআই সিকিউরিটি (API Key লুকিয়ে রাখা), ব্যাকএন্ড প্রক্সি সার্ভার এবং অ্যাপ থেকে আয় করার (Monetization) কৌশল

‎​আগের পর্বগুলোতে আমরা একটি পূর্ণাঙ্গ এআই অ্যাপ তৈরি করেছি। কিন্তু অ্যাপটি যখন আপনি প্লে-স্টোর বা অনলাইনে সবার জন্য উন্মুক্ত করবেন, তখন সরাসরি ফ্রন্টএন্ড কোডের (index.html) ভেতরে আপনার Gemini API Key রেখে দিলে একটি বড় ঝুঁকি তৈরি হয়। যেকেউ অ্যাপের সোর্স কোড বা নেটওয়ার্ক রিকোয়েস্ট চেক করে আপনার API Key-টি চুরি করে ফেলতে পারে।

‎​এই পর্বে আমরা শিখব কীভাবে ব্যাকএন্ড প্রক্সি সার্ভার ব্যবহার করে API Key সম্পূর্ণ সুরক্ষিত রাখা যায় এবং কীভাবে অ্যাপ থেকে অর্থ উপার্জন (Monetization) করা যায়।

‎​১. API Key সুরক্ষিত রাখার উপায়: ব্যাকএন্ড প্রক্সি (Cloudflare Workers)

‎​সরাসরি অ্যাপ থেকে গুগলের সার্ভারে রিকোয়েস্ট না পাঠিয়ে মাঝখানে একটি ফ্রি সার্ভার বা Cloudflare Worker ব্যবহার করা সবচেয়ে নিরাপদ এবং পেশাদার পদ্ধতি। এতে আপনার আসল API Key সার্ভারে লুকানো থাকবে, অ্যাপের কোডে কিছুই থাকবে না।

‎​ধাপসমূহ:

1. ‎Cloudflare অ্যাকাউন্ট: Cloudflare.com-এ গিয়ে একটি ফ্রি অ্যাকাউন্ট তৈরি করুন।

2. ‎Worker তৈরি: ড্যাশবোর্ডের বাম পাশ থেকে Workers & Pages > Create > Create Worker-এ ক্লিক করুন। এর একটি নাম দিন (যেমন: my-ai-proxy) এবং Deploy করুন।

3. ‎এনভায়রনমেন্ট ভেরিয়েবল (Secret Key) সেট করা: Worker-এর Settings > Variables and Secrets-এ গিয়ে Add ক্লিক করুন।

‎​Type: Secret সিলেক্ট করুন।

‎​Variable name: GEMINI\_API\_KEY লিখুন।

‎​Value: আপনার আসল Google AI Studio API Key-টি পেস্ট করে Save করুন।

‎​৪. Worker কোড বসানো: এবার Edit Code-এ ক্লিক করে নিচের ব্যাকএন্ড কোডটি পেস্ট করে Deploy করুন:

‎

‎export default {‎  async fetch(request, env) {‎ // CORS হেডার যাতে যেকোনো অ্যাপ বা ওয়েবসাইট থেকে রিকোয়েস্ট গ্রহণ করা যায়

‎ const corsHeaders = {‎ "Access-Control-Allow-Origin": "\*",

‎ "Access-Control-Allow-Methods": "POST, OPTIONS",

‎ "Access-Control-Allow-Headers": "Content-Type",

‎};

‎

‎ if (request.method = "OPTIONS") {‎ return new Response(null, {headers: corsHeaders});

‎}

‎

‎ if (request.method!= "POST") {‎ return new Response("Only POST requests allowed", {status: 405, headers: corsHeaders});

‎}

‎

‎ try {‎ const requestBody = await request.json();

‎ const apiKey = env.GEMINI\_API\_KEY; // সিক্রেট ভেরিয়েবল থেকে API Key নেওয়া হচ্ছে

‎ const geminiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${apiKey}`;

‎

‎ const geminiResponse = await fetch(geminiUrl, {‎ method: "POST",

‎ headers: {"Content-Type": "application/json"},

‎ body: JSON.stringify(requestBody),

‎});

‎

‎ const data = await geminiResponse.json();

‎ return new Response(JSON.stringify(data), {‎ headers: {.corsHeaders, "Content-Type": "application/json"},

‎});

‎

‎} catch (error) {‎ return new Response(JSON.stringify({error: "Server Error"}), {‎ status: 500,

‎ headers: {.corsHeaders, "Content-Type": "application/json"},

‎});

‎}

‎},

‎};

‎

‎৫. অ্যাপের কোডে পরিবর্তন: এবার আপনার আগের index.html ফাইলে API\_KEY লাইনটি মুছে ফেলুন এবং API\_URL-এর জায়গায় আপনার Cloudflare Worker-এর লিংকটি বসিয়ে দিন:

‎

‎// এখন আর কোনো API Key অ্যাপের কোডে রাখার প্রয়োজন নেই!

‎const API\_URL = "https://my-ai-proxy.your-subdomain.workers.dev";

‎

‎২. অ্যাপ থেকে আয় করার (Monetization) ৪টি সেরা উপায়

‎​অ্যাপটি তৈরি ও সুরক্ষিত করার পর এবার এটি থেকে আয় করার পালা। নিচের ৪টি পদ্ধতির যেকোনো একটি বা একাধিক পদ্ধতি ব্যবহার করে আপনি নিয়মিত আয় করতে পারেন:

‎​ক. গুগল অ্যাডমব (Google AdMob) দিয়ে আয়

‎​আপনি যদি অ্যাপটিকে অ্যান্ড্রয়েড APK বানিয়ে গুগল প্লে-স্টোর বা অন্য অ্যাপ স্টোরে প্রকাশ করেন, তবে এতে Google AdMob-এর বিজ্ঞাপণ বসাতে পারেন।

‎​ব্যানার অ্যাড (Banner Ads): অ্যাপের একদম নিচে বা ওপরে ছোট একটি বিজ্ঞাপণ দেখাবে।

‎​রিওয়ার্ডেড অ্যাড (Rewarded Video Ads): এটি এআই অ্যাপের জন্য সবচেয়ে লাভজনক। যেমন: ব্যবহারকারী দিনে ৫টি ফ্রি মেসেজ পাঠাতে পারবেন। এরপর আরও মেসেজ পাঠাতে চাইলে তাকে ১৫-৩০ সেকেন্ডের একটি ভিডিও অ্যাড দেখতে হবে। প্রতিবার অ্যাড দেখলে আপনার অ্যাকাউন্টে ডলার জমা হবে।

‎​খ. ডেইলি লিমিট ও সাবস্ক্রিপশন মডেল (Freemium Model)

‎​অ্যাপে একটি ক্রেডিট বা কয়েন সিস্টেম চালু করতে পারেন:

‎​নতুন ইউজার অ্যাকাউন্ট খুললে ১০টি ফ্রি ক্রেডিট পাবেন।

‎​ক্রেডিট শেষ হয়ে গেলে বিকাশ, নগদ বা গুগল পে-এর মাধ্যমে মাসিক সাবস্ক্রিপশন (যেমন: মাসে ৯৯ টাকা বা ২ ডলার) কিনে আনলিমিটেড ব্যবহার করার সুবিধা দিতে পারেন।

‎​গ. মার্কেটপ্লেসে সোর্স কোড বিক্রি (CodeCanyon / SellMyApp)

‎​আপনি যদি নিজে মার্কেটিং বা অ্যাড ম্যানেজ করতে না চান, তবে আপনার তৈরি করা এই প্রফেশনাল অ্যাপের সোর্স কোড এবং ডকুমেন্টেশন জিপ (ZIP) ফাইল করে Envato Market (CodeCanyon), Codester বা SellMyApp-এ বিক্রির জন্য আপলোড করতে পারেন।

‎​একটি ভালো মানের এআই চ্যাটবট বা কন্টেন্ট জেনারেটর অ্যাপের সোর্স কোড ১৫ থেকে ৪৯ ডলার পর্যন্ত বিক্রি হয়। একজন ক্রেতা কিনলে সেই একই কোড আপনি শত শত মানুষের কাছে বিক্রি করতে পারবেন।

‎​ঘ. ওয়েব অ্যাপে অ্যাড নেটওয়ার্ক (Adsterra / Google AdSense)

‎​অ্যাপটি যদি ওয়েবসাইট আকারে হোস্ট করেন, তবে ওয়েবসাইটের দুই পাশে বা নিচে Google AdSense অথবা Adsterra-এর ব্যানার অ্যাড বসিয়ে ভিজিটরদের ক্লিকের মাধ্যমে প্রতিদিন আয় করতে পারেন।

‎​৩. ক্রেডিট লিমিট লজিক (অ্যাপে ফ্রি মেসেজ লিমিট বসানোর কোড)

‎​আপনি যদি চান ব্যবহারকারী দিনে সর্বোচ্চ ৫টি প্রশ্ন ফ্রি করতে পারবেন, তবে আপনার জাভাস্ক্রিপ্ট কোডের শুরুতে নিচের ছোট লজিকটি যোগ করে দিতে পারেন:

‎

‎// দৈনিক মেসেজ লিমিট চেক করার ফাংশন

‎function checkDailyLimit() {‎ const today = new Date().toDateString();

‎ let usageData = JSON.parse(localStorage.getItem('ai\_usage\_limit')) | {date: today, count: 0};

‎

‎ // নতুন দিন শুরু হলে কাউন্ট রিসেট হবে

‎ if (usageData.date!= today) {‎ usageData = {date: today, count: 0};

‎}

‎

‎ if (usageData.count >= 5) {‎ alert("আজকের জন্য আপনার ৫টি ফ্রি মেসেজের লিমিট শেষ! আনলিমিটেড ব্যবহার করতে প্রো ভার্সন নিন। ");

‎ return false;

‎}

‎

‎ usageData.count += 1;

‎ localStorage.setItem('ai\_usage\_limit', JSON.stringify(usageData));

‎ return true;

‎}

‎

‎(মেসেজ পাঠানোর sendMessage() ফাংশনের একদম শুরুতে if (!checkDailyLimit()) return; বসিয়ে দিলেই এই লিমিট সিস্টেম চালু হয়ে যাবে। )

‎

‎র্ব ৫: ওয়েব অ্যাপটিকে অ্যান্ড্রয়েড APK-তে রূপান্তর, মার্কেটপ্লেসে (CodeCanyon) আপলোড এবং প্রজেক্ট প্যাকেজিং

‎​আমাদের এই মেগা গাইডের এটি হলো শেষ ও চূড়ান্ত পর্ব। আগের পর্বগুলোতে আমরা এআই অ্যাপের ডিজাইন, কোডিং, অ্যাডভান্সড ফিচার এবং সিকিউরিটি নিয়ে কাজ করেছি। আজকের পর্বে আমরা দেখব কীভাবে এই ওয়েব অ্যাপটিকে একটি পূর্ণাঙ্গ অ্যান্ড্রয়েড মোবাইল অ্যাপ (APK) এ রূপান্তর করতে হয় এবং এটিকে Envato Market (CodeCanyon) বা অন্যান্য প্ল্যাটফর্মে বিক্রির জন্য কীভাবে প্যাকেজ বা প্রস্তুত করতে হয়।

‎​১. ওয়েব অ্যাপকে অ্যান্ড্রয়েড APK-তে রূপান্তর করার উপায়

‎​আপনার তৈরি করা index.html ফাইলটি একটি লাইভ সার্ভারে (যেমন: Cloudflare Pages, Netlify বা GitHub Pages) হোস্ট করার পর সেটিকে মোবাইল অ্যাপে রূপান্তর করা অত্যন্ত সহজ। নিচে সবচেয়ে সহজ দুটি পদ্ধতি দেওয়া হলো:

‎​পদ্ধতি ক: PWABuilder ব্যবহার করে (সবচেয়ে সহজ ও ফ্রি)

‎​১. আপনার প্রজেক্টের লাইভ ওয়েব লিংকটি (যেমন: <https://your-app.pages.dev>) কপি করুন।

1. ‎ব্রাউজারে গিয়ে PWABuilder.com ওয়েবসাইটে প্রবেশ করুন।

2. ‎লিংকের ঘরে আপনার সাইটের ইউআরএল বসিয়ে Start বাটনে ক্লিক করুন।

3. ‎সাইটটি আপনার অ্যাপ অ্যানালাইসিস করার পর "Generate" অপশনে ক্লিক করুন।

4. ‎সেখান থেকে অ্যান্ড্রয়েড প্যাকেজ সিলেক্ট করে সরাসরি সাইন করা APK বা AAB ফাইল ডাউনলোড করে নিন। এটি সরাসরি অ্যান্ড্রয়েড ফোনে ইন্সটল করা যায়।

‎​পদ্ধতি খ: Android Studio WebView দিয়ে (প্রফেশনাল পদ্ধতি)

‎​আপনি যদি কোডক্যানিয়নে সোর্স কোড বিক্রি করতে চান, তবে অ্যান্ড্রয়েড স্টুডিওর একটি সহজ WebView Template তৈরি করা সবচেয়ে ভালো:

1. ‎অ্যান্ড্রয়েড স্টুডিও ওপেন করে একটি নতুন Empty Views Activity প্রজেক্ট তৈরি করুন।

2. ‎activity\_main.xml ফাইলে একটি WebView কম্পোনেন্ট যুক্ত করুন:

‎<WebView

‎ android:id="@+id/webview"

‎ android:layout\_width="match\_parent"

‎ android:layout\_height="match\_parent" />

‎

‎৩. MainActivity.java বা MainActivity.kt ফাইলে নিচের কোডটি দিয়ে আপনার ক্লাউডফ্লাওয়ার প্রক্সি বা হোস্টেড লিংকটি লোড করে দিন:

‎

‎WebView myWebView = findViewById(id.webview);

‎myWebView.getSettings().setJavaScriptEnabled(true);

‎myWebView.loadUrl("https://your-app-link.com");

‎

‎৪. প্রজেক্টটি বিল্ড করে APK তৈরি করে নিন।

‎​২. CodeCanyon বা মার্কেটপ্লেসে বিক্রির জন্য সোর্স কোড প্যাকেজিং

‎​আপনার তৈরি করা এই এআই অ্যাপটি যদি আপনি CodeCanyon বা অন্য কোনো ডিজিটাল মার্কেটপ্লেসে বিক্রি করতে চান, তবে প্রজেক্ট ফোল্ডারটি একটি নির্দিষ্ট কাঠামোর অধীনে সাজাতে হবে। ক্রেতারা যেন সহজে বুঝতে পারেন, সেজন্য একটি প্রফেশনাল ZIP ফাইল তৈরি করতে হবে।

‎

‎ফোল্ডার স্ট্রাকচার যেমন হবে:

‎AI-Smart-Assistant-Source-Code/

‎│

‎├── 📁 source-code/

‎│ ├── index.html (মূল ফ্রন্টএন্ড কোড)

‎│ └── worker.js (ক্লাউডফ্লাওয়ার প্রক্সি ব্যাকএন্ড কোড)

‎│

‎├── 📁 screenshots/

‎│ ├── preview-1.png (অ্যাপের আকর্ষণীয় স্ক্রিনশট)

‎│ └── preview-2.png (ফিচারের স্ক্রিনশট)

‎│

‎├── 📄 documentation.html (ব্যবহারবিধি বা সেটআপ গাইড)

‎└── 📄 README.txt (স্বাগতম ও ধন্যবাদ বার্তা)

‎

1. ‎কর্ষণীয় ডকুমেন্টেশন (Documentation) তৈরি করা

‎​মার্কেটপ্লেসে অ্যাপ বিক্রির সফলতার বড় একটি অংশ নির্ভর করে আপনার ডকুমেন্টেশনের ওপর। ক্রেতারা যেন কোনো ঝামেলা ছাড়াই অ্যাপটি সেটআপ করতে পারেন, সেজন্য ডকুমেন্টেশনে স্পষ্টভাবে নিচের বিষয়গুলো লিখে রাখবেন:

‎​Features List: অ্যাপে কী কী ফিচার আছে (যেমন: ডার্ক মোড, ভয়েস ইনপুট, ইমেজ ভিশন, লোকাল স্টোরেজ)।

‎​How to Setup API Key: ক্লাউডফ্লাওয়ার ওয়ার্কার বা গুগল এআই স্টুডিও থেকে কীভাবে এপিআই কি নিতে হবে, তার ধাপসমূহ স্ক্রিনশটসহ বর্ণনা।

‎​How to Run: লোকাল কম্পিউটারে বা হোস্টিংয়ে ফাইলটি কীভাবে রান করতে হবে তার নির্দেশনা।

‎​৪. মার্কেটপ্লেসে আপলোড ও সফল মার্কেটিংয়ের টিপস

‎​১. থাম্বনেইল ও প্রিভিউ: Canva ব্যবহার করে একটি প্রিমিয়াম ও আইওক্যাচি (Eye-catching) থাম্বনেইল তৈরি করুন, যেখানে বড় অক্ষরে লেখা থাকবে "AI Gemini Chatbot App - HTML/JS & Android Ready"।

1. ‎সঠিক দাম নির্ধারণ: নতুন বিক্রেতা হিসেবে প্রাথমিক পর্যায়ে অ্যাপের দাম ১৫ থেকে ২৫ ডলারের মধ্যে রাখা ভালো। পরবর্তীতে রিভিউ বাড়লে দাম বৃদ্ধি করতে পারেন।

2. ‎টেকটিউনস বা ব্লগে প্রচার: আপনি যে টেকটিউনস অ্যাকাউন্ট তৈরি করেছেন, সেখানে আপনার এই অ্যাপ তৈরির পুরো জার্নি নিয়ে একটি চমৎকার টিউন বা আর্টিকেল লিখে নিচে আপনার সোর্স কোডের ডেমো লিংক বা ডাউনলোডের তথ্য শেয়ার করতে পারেন। এতে আপনার লেখার মাধ্যমেও আয় হবে এবং প্রজেক্টের প্রচারও বাড়বে!

‎​আপনার এআই অ্যাপ প্রজেক্টের সমাপ্তি!

- ‎

‎

‎
