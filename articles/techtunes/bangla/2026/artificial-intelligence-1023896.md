---
archive_id: techtunes-1023896
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 1023896
title: AI-Job-Search – যেভাবে AI Framework Job Search পুরোপুরি বদলে দিল! Claude Code
  দিয়ে নিজের Machine-এ Job Hunting-এর কমপ্লিট গাইড
slug: artificial-intelligence-1023896
language: bn
status: publish
published_at: '2026-11-06T15:13:00+00:00'
modified_at: '2026-11-06T15:13:00+00:00'
original_url: https://www.techtunes.io/artificial-intelligence/tune-id/1023896
author: মো আতিকুর ইসলাম
author_url: https://www.techtunes.io/tuner/atikurofficial
categories:
- আর্টিফিশিয়াল ইন্টেলিজেন্স (এআই)
tags:
- অনলাইন জব
- আর্টিফিশিয়াল ইন্টেলিজেন্স
- এআই
content_hash: 3c56d7075fd805d0ade9e817668847f191a52d7d16f0a3aa74e4b6252166ed77
archived_at: '2026-11-12T11:34:22.073518+00:00'
---

কীভাবে একটি AI Framework আমার Job Search পুরোপুরি বদলে দিল: Claude Code দিয়ে নিজের Machine-এ Job Hunting-এর কমপ্লিট গাইড

আজকের এই দ্রুত পরিবর্তনশীল পৃথিবীর Technology ও Corporate জগতে Job Search করা প্রতিটি Developer, Engineer, Specialist এবং Professional-এর জন্যই এক অত্যন্ত মানসিক ও শারীরিক ক্লান্তিকর অভিজ্ঞতা। প্রতিদিন সকালে উঠে ঘণ্টার পর ঘণ্টা ধরে বিভিন্ন Job Board স্ক্রোল করা, একের পর এক জটিল ও দীর্ঘ Job Posting পড়া, প্রতিটি কোম্পানির পছন্দ অনুযায়ী আলাদা করে CV ও Cover Letter তৈরি করা, এবং দিনশেষে কোনো প্রকার Response না পেয়ে কেবল রিজেকশন বা নীরবতার মুখোমুখি হওয়া — এই হতাশাজনক চিত্র আমাদের সবারই জানা। কিন্তু কেমন হতো যদি এই পুরো ধকলপূর্ণ প্রসেসটি আপনার নিজের Personal Computer-এ একা হাতে সামলে নিত একটি বুদ্ধিমান AI Agent?

আজকে আমরা এমন একটি অসাধারণ, পাওয়ারফুল এবং সম্পূর্ণ ওপেন সোর্স প্রজেক্ট নিয়ে অত্যন্ত In-Depth আলোচনা করব, যার নাম ai-job-search। এটি তৈরি করেছেন Mads Lorentzen। বাজারে থাকা সাধারণ কোনো SaaS Platform বা যেকোনো অনলাইন সার্ভিস যেমন আপনার ডেটা তাদের সার্ভারে নিয়ে কাজ করে, এটি কিন্তু মোটেই সেরকম নয়। এটি এমন একটি Local Framework যা সরাসরি আপনার নিজের Machine-এ রান করে। এই বিস্তারিত ব্লগে আমরা এই প্রজেক্টের সৃষ্টি, এর কাজ করার অভ্যন্তরীণ মেকানিজম, ইনস্টলেশন নির্দেশিকা, প্রতিটি কমান্ডের ব্যবচ্ছেদ এবং কীভাবে এটি আপনার Job Hunting-এর অভিজ্ঞতায় এক নতুন যুগের সূচনা করতে পারে তা একদম পুঙ্খানুপুঙ্খভাবে আলোচনা করব।

## একটি লাইভ সাকসেস স্টোরি: Geophysicist থেকে AI Engineer হওয়ার পেছনের গল্প

![](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_f33e120bb1e9982bb0b16acf92bf72ad.png)

যেকোনো নতুন সল্যুশন বা Framework ব্যবহারের আগে আমাদের মনে প্রশ্ন জাগাটা স্বাভাবিক — *"এটি কি আসলেই বাস্তবে কাজ করে?"* এই টুলের পেছনের সৃষ্টিগাথাটি কোনো কাল্পনিক গল্প নয়, বরং এটি তৈরি হয়েছিল একজন মানুষের নিজের অস্তিত্ব রক্ষার Real-Life Success Story থেকে।

এই প্রজেক্টটির স্রষ্টা Mads Lorentzen শিক্ষাগত দিক থেকে একজন Geophysicist ছিলেন। ২০২৫ সালের শেষের দিকে যখন অনাকাঙ্ক্ষিত পরিস্থিতি ও কোম্পানি ডাউনসাইজিংয়ের কারণে তাঁর Position কেটে দেওয়া হয়, তখন তিনি ক্যারিয়ারের এক বিশাল অনিশ্চয়তার মুখোমুখি হন। তবে তিনি ভেঙে না পড়ে তাঁর টেকনিক্যাল জ্ঞানকে কাজে লাগিয়ে নিজের Machine-এ একটি Local AI-Powered Job Search Framework তৈরি করতে শুরু করেন।

তিনি তাঁর এই তৈরি করা সিসটেমের বিভিন্ন কমান্ড যেমন — `/scrape`, `/apply`, এবং `/interview` Workflow গুলো সপ্তাহে নিয়মিত ব্যবহার করে নিজের Career-এর জন্য Job Search পরিচালনা করতে থাকেন। সবচেয়ে চমৎকার ব্যাপার হলো, তিনি প্রতিটি Employer এবং Interviewer-এর সাথে কথা বলার সময় অত্যন্ত সত্যতার সাথে প্রকাশ করেছেন যে তিনি তাঁর এই Application Process-এর প্রস্তুতিতে একটি AI Framework ব্যবহার করছেন। অবাক করা বিষয় হলো, কোনো Employer এটাকে অলসতা বা নেতিবাচক হিসেবে দেখেননি; বরং এটি প্রতিটি ইন্টারভিউ টেবিলেই একটি চমৎকার এবং জেনুইন Technical Conversation-এর জন্ম দিয়েছিল!

চলুন এক নজরে তাঁর অর্জিত অবিশ্বাস্য Data Points এবং Application Funnel-এর ওপর চোখ বুলিয়ে নেওয়া যাক:

- **৬৯টি** অত্যন্ত সুনির্দিষ্ট ও Tailored Applications
- **২০টি** First Interviews-এর জন্য সরাসরি কল
- **১টি** ফাইনাল Signed Contract

এবং এই চমৎকার প্রসেসের চূড়ান্ত ফলাফল হিসেবে ২০২৬ সালের June মাসে তিনি আনুষ্ঠানিকভাবে একজন AI Engineer হিসেবে তাঁর নতুন প্রযুক্তিভিত্তিক ক্যারিয়ার যাত্রা শুরু করেন! মানুষের ক্রমাগত কৌতুহল এবং চাহিদার কারণে তিনি সিদ্ধান্ত নেন তাঁর তৈরি এই পরীক্ষিত সিসটেমটি সবার ব্যবহারের জন্য Open-Source করে দেওয়ার।

> জরুরি ডিসক্লেইমার, সিকিউরিটি ওয়ার্নিং ও ডিসক্লোজার:  
>  এই প্রজেক্টটি একটি সম্পূর্ণ স্বাধীন Open-Source Project (যা MIT License-এর অধীনে প্রকাশিত) এবং এটি Anthropic-এর সাথে কোনোভাবেই Affiliated, Endorsed, Sponsored বা Maintained নয়। Anthropic এবং Claude Code-এর নাম শুধুমাত্র এই Workflow-টিতে ব্যবহৃত Toolchain বর্ণনা করার উদ্দেশ্যে ব্যবহার করা হয়েছে।
>
> প্রজেক্টটির স্রষ্টা স্পষ্টভাবে জানিয়ে দিয়েছেন যে এই Project-এর সাথে সম্পর্কিত কোনো Cryptocurrency, Token বা Paid Sponsorship Program নেই। কেউ যদি এমন কোনো দাবী করে, তবে সেটি সম্পূর্ণ Unauthorized এবং স্ক্যাম বা প্রতারণা হিসেবে গণ্য হবে। প্রজেক্টটিকে Support করার একমাত্র অনুমোদিত উপায় হলো তাঁর Ko-fi লিংক এবং GitHub-এ কন্ট্রিবিউট করা। তাঁর এই সফলতার দীর্ঘ গল্প এবং সম্পূর্ণ Application Funnel আপনি পাবেন তাঁর LinkedIn প্রোফাইলে। এছাড়া August ২০২৬-এ ধারণকৃত The Next New Thing-এর একটি চমৎকার Hands-On Walkthrough Video রয়েছে (যদিও সময়ের সাথে সাথে কিছু Command হয়তো কিছুটা Evolve করতে পারে)।
>
> *“Did This Save You a Sunday of Cover-Letter Writing? Consider a Coffee. Did It Land You the Job? Maybe Two. ☕”*

### AI Job Search

অফিসিয়াল ওয়েবসাইট @ [AI Job Search](https://github.com/ai-job-search-dev/ai-job-search)

## AI Job Search কী এবং কীভাবে কাজ করে?

![AI Job Search কী এবং কীভাবে কাজ করে?](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_de9f0f175ef87129a7310373967a1857.jpg)

খুব সহজ ভাষায় বলতে গেলে, `ai-job-search` হলো একটি অত্যন্ত সুনির্দিষ্ট ও Structured Workflow যা Anthropic-এর Claude Code (CLI Tool)-কে আপনার নিজের সম্পূর্ণ নিজস্ব একটি Full-Stack Job Application Assistant-এ পরিণত করে।

### এই সিসটেমের বিশেষ মূলনীতি ও স্থাপত্য (Architecture):

1. **Local & Privacy-First Architecture:** এটি বাইরের কোনো অজানা Cloud Server-এ কাজ করে না; আপনার যাবতীয় ব্যক্তিগত কন্টাক্ট, ক্যারিয়ার হিস্ট্রি, Diplomas, Credentials এবং চাকরির অতীত ফাইলস আপনার নিজের Local Machine-েই অত্যন্ত নিরাপদ ও গোপন থাকে।
2. **Language- and Country-Agnostic Core Engine:** এই Framework-এর Core Logic বা ইঞ্জিন (যেমন: Self-Profiling, Fit Evaluation এবং Drafter-Reviewer Application Pipeline) সম্পূর্ণভাবে আন্তর্জাতিকভাবে যেকোনো ভাষার জন্য ব্যবহারযোগ্য। অর্থাৎ, আপনি যে দেশেই থাকুন না কেন বা যে ভাষাতেই আবেদন করতে চান না কেন, এর মূল নীতি একই থাকে।
3. **Market-Specific Job Search Tools:** বাই-ডিফল্ট এই প্রজেক্টটিতে ডেনিশ মার্কেটের প্রধান Job Portals (যেমন: Jobindex, Jobnet, Akademikernes Jobbank, Jobdanmark) এর জন্য পোর্টাল সার্চ টুল দেওয়া থাকলেও, এটি এমনভাবে ডিজাইন করা হয়েছে যাতে আপনি পৃথিবীর যেকোনো প্রান্তের আপনার স্থানীয় Job Boards-এর সাথে একে Swap করে নিতে পারেন।
4. **Career Guidance Best Practices:** এই সিসটেমের কোডের গভীরে অভিজ্ঞ Career Advisors-দের সেরা সেরা গাইডলাইন গেঁথে দেওয়া হয়েছে। যার মধ্যে রয়েছে Structured Evaluation Criteria, Forward-Looking Cover Letter Framing এবং প্রয়োজনে অপশনাল Salary Benchmarking।

### জব সার্চের দুটি ভিন্ন মোড (Two Modes of Job Searching):

এই Framework মূলত দুটি ভিন্ন দৃষ্টিকোণ থেকে আপনাকে নতুন চাকরির সন্ধান দেয়:

- **Explicit Targeting Mode:** যদি আপনার সুনির্দিষ্ট লক্ষ্য থাকে যে আপনি ঠিক কোন Role, Technology Stack বা কোন Sector-এ কাজ করতে চান, তবে এটি আপনার স্কিল বিশ্লেষণ করে সেই নির্দিষ্ট ধরনের সার্কুলারগুলো Filter ও Prioritize করতে সাহায্য করে।
- **Latent Opportunity Discovery Mode:** অনেক সময় আমরা নিজেরাই বুঝতে পারি না আমাদের অর্জিত স্কিল অন্য কোনো ভিন্ন ইন্ডাস্ট্রিতে কতটা মূল্যবান হতে পারে। এই সিসটেমটি আপনার কাজের সম্পূর্ণ ইতিহাস বিশ্লেষণ করে এমন কিছু Career Paths এবং Transferable Skills বের করে আনে যা আপনি হয়তো কখনো ভেবেই দেখেননি! আপনার অতীতের কাজের কোন অংশ আপনাকে Energized করেছে আর কোনটা Drained করেছে — তা বুঝে নিয়ে এটি নতুন নতুন সম্ভাবনা উন্মোচন করে।

```
/setup /scrape /apply &amp;lt;url&amp;gt; | | | v v v
Fill in Search job Evaluate fit
your profile portals Score &amp;amp;amp; recommend | | | v v v
Profile Present matches Draft CV + Cover Letter
files ready with fit ratings (LaTeX, tailored) | | v v Pick a match Reviewer agent critiques -&amp;gt; /apply -&amp;gt; Revise -&amp;gt; Final output
```

## এই Framework রান করার জন্য কী কী Prerequisites লাগবে?

![এই Framework রান করার জন্য কী কী Prerequisites লাগবে?](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_709c5f9b730819315153b814e03dd7a2.jpg)

আপনার Machine-এ এই অত্যাধুনিক AI-Powered Workflow সফলভাবে পরিচালনা করার জন্য আগে থেকেই কিছু Tooling এবং Environment প্রস্তুত রাখতে হবে। নিচে বিস্তারিত তালিকা দেওয়া হলো:

1. **Claude Code (CLI):** Anthropic-এর অফিশিয়াল Terminal Tool। মনে রাখবেন, Claude Code-এর কোনো Free Tier নেই। এটি ব্যবহার করার জন্য আপনার একটি Claude Pro, Claude Max, বা Claude Team Subscription অথবা Anthropic API Credits থাকতে হবে। যদি আপনি অল্প ব্যবহারের জন্য কাজ করেন, তবে API Credits (Pay-Per-Token) ব্যবহার করা তুলনামূলকভাবে অনেক সাশ্রয়ী। আপনি যদি Claude-এর বদলে অন্য কোনো Agent Tool (যেমন: Codex, Antigravity, বা Gemini CLI) ব্যবহার করতে চান, তবে `AGENTS.md` ফাইল থেকে শুরু করতে পারেন; সেখানকার ডিরেকশন অনুযায়ী Community Forks ব্যবহার করে পুরো সিসটেম চালানো সম্ভব।
2. **Python 3.10+:** ব্যাকএন্ডের বিভিন্ন স্ক্রিপ্ট ও হেল্পার ফাইল রান করার জন্য Python ইনস্টল থাকা আবশ্যক।
3. **Bun:** এটি একটি অত্যন্ত দ্রুতগতির JavaScript Runtime, যা Job Search CLI Tools চালানোর জন্য ব্যাকএন্ডে ব্যবহৃত হয়।
4. **LaTeX Distribution (`lualatex` ও `xelatex` সহ):** সুন্দর ও নিখুঁত ডকুমেন্টস তৈরির জন্য সিসটেমে TeX Live, MacTeX, TinyTeX, অথবা MiKTeX ইনস্টল থাকতে হবে।
   - **মনে রাখবেন:** আপনার CV ফাইল কম্পাইল করার জন্য `lualatex` ব্যবহৃত হয় (কারণ আধুনিক MiKTeX ইনস্টলে `fontawesome5` ফন্টের কারণে `pdflatex` প্রায়ই ব্যর্থ হয়)।
   - অন্যদিকে Cover Letter কম্পাইল করতে ব্যবহৃত হয় `xelatex` (কারণ এর কাস্টম `cover.cls` ফাইলের জন্য `fontspec` অত্যন্ত জরুরি)।
   - আপনি যদি TinyTeX বা BasicTeX-এর মতো Minimal TeX Install ব্যবহার করেন, তবে `SETUP.md`-এ উল্লেখিত Extra Packages অবশ্যই আলাদাভাবে ইনস্টল করে নিতে হবে।
5. **Optional ATS Tools:** আপনি যদি `/apply` কমান্ডের সাহায্যে জেনারেট হওয়া সিভির ATS Parseability Check করতে চান, তবে `pip install pypdf` (BSD License) কমান্ড চালিয়ে নিতে পারেন। এতে Poppler-এর প্রয়োজন হয় না। এছাড়া বিকল্প হিসেবে Poppler-এর `pdftotext` টুলটিও Fallback হিসেবে ব্যবহার করা যায় (macOS-এ: `brew install poppler`, Debian/Ubuntu-তে: `apt install poppler-utils`, Windows-এ: `choco install poppler`)। যদি দুটি টুলই অনুপস্থিত থাকে, তবে ATS প্রসেসটি সাধারণ Visual Keyword Review-তে অবনমিত হবে।

## স্টেপ-বাই-স্টেপ সেটআপ এবং ইনস্টলেশন গাইড

![স্টেপ-বাই-স্টেপ সেটআপ এবং ইনস্টলেশন গাইড](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_923d9c37bdacda9dba61b83468f7dcf6.jpg)

এখন আমরা দেখব কীভাবে শুরু থেকে এই চমৎকার প্রজেক্টটি আপনার কম্পিউটারে রান করবেন।

### ১. Fork এবং Clone করা

প্রথমে Repository-টি আপনার সিস্টেমে ক্লোন করে নিন:

```
gh repo fork MadsLorentzen/ai-job-search -clone
cd ai-job-search
```

> অত্যন্ত গুরুত্বপূর্ণ নিরাপত্তা সতর্কবার্তা:  
>  মনে রাখবেন, GitHub-এর নিয়ম অনুযায়ী Public Repository-র যেকোনো Fork সর্বদাই Public থাকে। আর এই প্রজেক্টের `/setup` কমান্ড রান করলে আপনার সংবেদনশীল Data (Name, Contact Details, Employment History, Salary Expectations) এমন কিছু ফাইলে লেখা হবে যা Git দ্বারা Track করা হয়।  
>  তাই আপনার উদ্দেশ্য যদি প্রজেক্টে কোড Contribute করা না হয়ে স্রেফ নিজের কাজের জন্য ব্যবহার করা হয়ে থাকে, তবে মূল Repo-কে `upstream` হিসেবে কানেক্ট করে একটি Private Repository ব্যবহার করুন! এর ২ মিনিটের সহজ রেসিপি `SETUP.md`-এর Section 8-এ বিস্তারিত দেওয়া আছে। শুধুমাত্র Contribution-এর জন্যই কেবল Public Fork ব্যবহার করুন।

### ২. Job Search Tools ইনস্টল করা

এরপর আপনার প্রয়োজনীয় পোর্টাল টুলগুলো ইনস্টল করতে নিচের স্ক্রিপ্টটি চালান:

```
python3 tools/install&amp;lt;em&amp;gt;portal&amp;lt;/em&amp;gt;clis.py # Windows-এ: python tools\install&amp;lt;em&amp;gt;portal&amp;lt;/em&amp;gt;clis.py
```

এই স্ক্রিপ্টটি অটোমেটিকভাবে সার্ভিস অটো-ডিসকভার করে `.agents/skills/*/cli/` ফোল্ডারের অধীনে থাকা প্রতিটি Job Portal CLI-তে `bun install` রান করবে। কোনো CLI-এর `package.json`-এ যদি নিরাপত্তার জন্য ঝুঁকিপূর্ণ কোনো Lifecycle Script (যেমন: `postinstall`) থাকে, তবে এটি নিজে থেকেই তা Skip করবে এবং Report তৈরি করবে। আপনি চাইলে `-dry-run` কমান্ড চালিয়ে আগে থেকেই পরীক্ষা করতে পারেন সিসটেমটি কী ইনস্টল করতে যাচ্ছে।

উল্লেখ্য, `linkedin-search` এবং `freehire-search`-এর জন্য এই ইনস্টলেশন একদম Optional; কারণ এদের কোনো Runtime Dependency নেই এবং তারা প্লেইন `bun` দিয়েই একদম স্মুথলি কাজ করে।

### ৩. Profile প্রস্তুত করা

এখন Terminal-এ ক্লড ইন্টারফেস চালু করুন এবং অনবোর্ডিং প্রসেস শুরু করুন:

```
claude&amp;lt;/wp-p&amp;gt;

&amp;lt;h1&amp;gt;Then inside Claude Code:&amp;lt;/h1&amp;gt;

&amp;lt;wp-p&amp;gt;/setup
```

`/setup` কমান্ড চালু হওয়ার পর সিসটেম আপনাকে ৩টি অনবোর্ডিং প্যাথের অপশন দেবে:

- **Path A (Documents Folder Mode):** আপনার কম্পিউটারের `documents/` ফোল্ডারে আপনার প্রয়োজনীয় কাগজপত্র (যেমন: CV PDF, LinkedIn Export, Diplomas, Reference Letters, Past Applications) রেখে দিলে সিসটেম নিজে থেকে তা রিড করবে। এটি একটি Idempotent প্রসেস, যা পরবর্তীতে নতুন ফাইল যোগ করার পরও নিশ্চিন্তে আবার রান করা যায়। বিস্তারিত জানতে `documents/README.md` দেখুন।
- **Path B (CV Paste Mode):** সরাসরি চ্যাট উইন্ডোতে আপনার বিদ্যমান কোনো সিঙ্গেল CV পেস্ট করে Import করার সুবিধা।
- **Path C (Interactive Interview Mode):** ক্লড নিজে আপনাকে একের পর এক প্রশ্ন জিজ্ঞেস করবে এবং একটি বিস্তারিত Interview-এর মাধ্যমে আপনার সম্পূর্ণ ক্যারিয়ার ফাইল তৈরি করবে।

### ৪. Job খুঁজে বের করা (Scrape)

```
/scrape
```

এই কমান্ডটি আপনার সেটআপ করা Profile-এর সাথে ম্যাচ করে এমন সমস্ত ওপেন সার্কুলার বিভিন্ন Portals থেকে খুঁজে বের করে নিয়ে আসবে, একই সার্কুলারের একাধিক কপি থাকলে তা Deduplicate করবে এবং Fit Rating অনুযায়ী ক্রমানুসারে সাজিয়ে আপনার সামনে উপস্থাপন করবে। আপনি সরাসরি সেখান থেকে বেছে নিয়ে `/apply` রান করতে পারেন, অথবা কাজের সুবিধার্থে `/rank` কমান্ড দিয়ে একসাথে অনেকগুলোকে Batch-Score করে একটি চমৎকার Shortlist বানিয়ে নিতে পারেন।

### ৫. কোনো জব-এ Apply করা

```
/apply https://jobindex.dk/job/1234567
```

যদি কোনো সাইট তাদের সিকিউরিটির জন্য Automated Web Scraping ব্লক করে রাখে, তবে আপনি বিকল্প হিসেবে পুরো Job Description টি কপি করে এভাবেও কমান্ড দিতে পারেন:

```
/apply &amp;lt;paste the full job description here&amp;gt;
```

এই একটি মাত্র কমান্ড পুরো পাওয়ারফুল পাইপলাইন চালু করে দেবে: জব মূল্যায়ন, CV ও Cover Letter ড্রাফট তৈরি, অন্য একটি Reviewer Agent দিয়ে প্রুফ-রিড করানো, ফাইল সংশোধন করা এবং চূড়ান্ত Output উপস্থাপন করা।

> নিরাপত্তা টিপস: সার্কুলার থেকে আসা ডেটাকে সিসটেম সবসময় Untrusted Input হিসেবে দেখে। তাই কোনো ক্ষতিকর টেক্সট দিয়ে যদি কমান্ড বাইপাস করার চেষ্টা করা হয়, তবুও সিসটেম কোনো বডি লিংক ভিজিট করবে না বা হিডেন ইন্সট্রাকশন ফলো করবে না। নিরাপত্তা সম্পর্কে গভীর ধারণা পেতে `SECURITY.md` পড়ে দেখতে পারেন।

## /apply কমান্ডের ম্যাজিক: Drafter-Reviewer Workflow এবং PDF Verification

![Drafter-Reviewer Workflow এবং PDF Verification](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_bdc46d13c6b65e5fdcd9bfc2e2b4f3c5.jpg)

যখনই আপনি সিসটেমকে `/apply` কমান্ড দেন, তখন স্ক্রিনের পেছনে মোট ৮টি সুনির্দিষ্ট এবং নিখুঁত ধাপ সম্পন্ন হয়:

1. **Parse:** জব সার্কুলারের আসল তথ্য, রিকোয়ারমেন্ট এবং দায়িত্বসমূহ বিশ্লেষণ করা।
2. **Evaluate Fit:** ক্যান্ডিডেটের মূল Profile-এর সাথে সেই পদের মিল ও অমিলগুলো (Skills, Experience, Culture, Location, Career Alignment) পরিমাপ করা।
3. **Draft:** LaTeX ফাইল এনভায়রনমেন্টের মধ্যে কাস্টমাইজড CV এবং একটি আধুনিক Cover Letter ড্রাফট করা।
4. **Spawn Reviewer Agent:** একদম নতুন ও তাজা Context নিয়ে সম্পূর্ণ আলাদা একটি দ্বিতীয় Claude Agent তৈরি করা, যা সেই নির্দিষ্ট কোম্পানির ইতিহাস নিয়ে গবেষণা করবে এবং প্রথম এজেন্টের লেখা ড্রাফটের নিরপেক্ষ সমালোচনা (Critique) করবে।
5. **Revise:** Reviewer Agent-এর সুনির্দিষ্ট পরামর্শ ও ফিডব্যাকের ওপর ভিত্তি করে কন্টেন্ট রিভাইজ ও ফাইনাল ফ্রেমিং তৈরি করা।
6. **Compile and Inspect PDF:** ফাইনাল LaTeX কোডকে PDF-এ রূপান্তর করতে CV-র জন্য `lualatex` এবং Cover Letter-এর জন্য `xelatex` চালানো হয়। এরপর ক্লড নিজেই তৈরি হওয়া PDF পেজ ভিজ্যুয়ালি ইনস্পেক্ট করে চেক করে। সিসটেমে কিছু স্পেশাল ফিক্স বা কাস্টম ট্রিকস যুক্ত করা আছে (যেমন: `\needspace`, `\enlargethispage` এবং নির্দিষ্ট তালিকা বা লিস্টের জন্য Font-Matching Wrappers), যা নিশ্চিত করে যে CV-টি ঠিক ২ পেজ এবং Cover Letter-টি নির্দিষ্ট ফন্টে ঠিক ১ পেজে নিখুঁতভাবে শেষ হয়েছে।
7. **ATS Check on Text Layer:** সাধারণ মানুষ যেভাবে রেজুমে দেখে, ATS কিন্তু সেভাবে দেখে না! ATS পড়ে ডকুমেন্টের ভেতরের টেক্সট লেয়ার। এই পাইপলাইনটি `pdftotext` ব্যবহার করে পিডিএফের আসল টেক্সট লেয়ার বের করে আনে। কোনো টেক্সট বা আইকন যেন নষ্ট না হয়ে যায় (গ্যার্বল্ড গ্লিফ) তা যাচাই করে এবং জবের প্রয়োজনীয় Keyword কাভারেজ হিসাব করে। এখানে কঠোর **Honesty Rule** মানা হয় — যদি কোনো স্কিল ক্যান্ডিডেটের না থাকে তবে সেটি কখনোই জোর করে টাইপ করা হয় না; বরং জেনুইন স্কিল গ্যাপ হিসেবে রিপোর্টে দেখানো হয়।
8. **Present Output:** সমস্ত কাজ শেষ হলে একটি সম্পূর্ণ Verification Checklist সহ ফাইলগুলো ব্যবহারকারীর সামনে উপস্থাপন করা হয়।

### এই পাইপলাইনের অনন্য উদ্ভাবনসমূহ:

- **PDF Verification Loop:** যেকোনো সাধারণ রেজুমে টেমপ্লেটে দেখা যায় কাঁচা `.tex` ফাইলে দেখতে ভালো লাগলেও PDF করলে পেজের নিচে শিরোনাম একা পড়ে থাকে (Orphan Title) কিংবা কভার লেটার ভুল করে দুই পেজে ছড়িয়ে পড়ে। কিন্তু এই সিস্টেমে ক্লড প্রতিবার ফাইল রেন্ডার করে নিজের চোখে দেখে নিশ্চিত হওয়ার পরেই ইউজারকে প্রদান করে।
- **Relevance-Weighted CV Cutting:** যখন সিভি দুই পেজের লিমিট ছাড়িয়ে যায়, তখন সিসটেম স্রেফ শেষের বা পুরোনো কাজ মুছে দেয় না! প্রতিটি লাইনের Relevance (জবের সাথে মিল), Uniqueness (অন্য লাইনের সাথে পুনরাবৃত্তি) এবং Cover Letter-এর সাথে সম্পর্কের ওপর ভিত্তি করে নম্বর দেওয়া হয়। যে লাইনের স্কোর সবচেয়ে কম ওঠে, ফাইল ছোট করতে কেবল সেই লাইনটিই ডিলিট করা হয়!
- **Drafter-Reviewer Separation:** একজন লিখবে এবং আরেকজন নিরপেক্ষভাবে ভুল ধরবে — মানুষের এই লেখার কৌশলকে AI Agents-এর মধ্যে রূপদান করা হয়েছে।
- **Token-Efficient Reviewer Dispatch:** ক্ষতিকারক টোকেন অপচয় রোধ করতে সিসটেম ড্রাফটগুলো রিভিউয়ারের কাছে সরাসরি পাঠায় এবং ভেরিফিকেশন চেকটি একদম শেষে একবার রান করে।
- **Language Gate Handling:** `04-job-evaluation.md` ফাইলের মাধ্যমে একটি বিশেষ নিরাপত্তা তৈরি করা রয়েছে। যদি কোনো জবে এমন ভাষার কথা বলা হয় যা আপনি একেবারেই জানেন না, সিসটেম তাৎক্ষণিকভাবে সেই জবটিকে Rejected ঘোষণা করবে। তবে যদি আপনার কোনো ভাষায় B1/B2 লেভেলের জ্ঞান থাকে কিন্তু সার্কুলারে "Fluent" চাওয়া হয়, তবে সিসটেম নিজে সিদ্ধান্ত না নিয়ে ব্যবহারকারীর বিচারবুদ্ধির জন্য বিষয়টি ফ্ল্যাগ করে রাখবে।

## এই Framework-এর পাওয়ারফুল কমান্ডস এবং এক্সটেনশন মডেল

![এই Framework-এর পাওয়ারফুল কমান্ডস এবং এক্সটেনশন মডেল](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_25ca1567452abb79f8181454d23c9367.jpg)

কোর কাজের বাইরের পুরো Job Search প্রক্রিয়া সহজ করতে এই ফ্রেমওয়ার্কে আরও ১০টি অত্যাধুনিক কমান্ড যুক্ত রয়েছে:

- **`/rank`:** স্ক্র্যাপ করা শত শত জবের তালিকার ওপর সমান্তরাল Agents চালু করে একযোগে ৫টি মূল্যায়ন ক্ষেত্রে নম্বর দেয় এবং একটি নিরপেক্ষ Shortlist প্রদান করে। এতে Deal-Breakers স্বয়ংক্রিয়ভাবে বাদ পড়ে যায়, Deadlines এর জন্য উরজেন্সি ফ্ল্যাগ আসে এবং বন্ধ হয়ে যাওয়া জবগুলোকে Expired হিসেবে চিহ্নিত করা হয়।
- **`/interview`:** কোনো নির্দিষ্ট জবের ইন্টারভিউ কনফার্ম হলে এটি সেই জবের যাবতীয় আর্কাইভ (বিজ্ঞপ্তি, আপনি যে সিভি বা কভার লেটার জমা দিয়েছিলেন এবং পূর্ববর্তী রাউন্ডের ফিডব্যাক) পড়ে প্যাক তৈরি করে। ইন্টারভিউয়ারদের রিচার্জ করে `07-interview-prep.md`-এর নিয়ম মেনে একটি বাস্তবসম্মত Mock Interview নেয় এবং প্রতিটি প্রশ্নের জন্য আপনাকে STAR Framework অনুযায়ী উত্তর তৈরি করতে সাহায্য করে।
- **`/outcome`:** জবের প্রতিটি আপডেট (যেমন: Interview Stages, Offers, Rejections, Silence) রেকর্ড করে এবং ফাইলগুলোকে সুন্দরভাবে `documents/applications/<company>_<role>/` এ সেভ করে পরিচ্ছন্ন `outcome.md` বজায় রাখে।
  - **`/outcome followup`:** যেসব আবেদনে ১০ দিন ধরে কোনো সাড়া পাওয়া যায়নি, সেগুলোর জন্য আপনার নিজস্ব রাইটিং স্টাইল বজায় রেখে ভদ্র ও সুন্দর একটি ফলো-আপ মেসেজ ড্রাফট করে দেয়।
- **`/notion-sync`:** অফিশিয়াল Notion MCP Server (OAuth) ব্যবহার করে আপনার পুরো পাইপলাইনের একটি একমুখী (Read-Only) ড্যাশবোর্ড আপনার নোশন ডাটাবেসে তৈরি করে দেয়। এর মাধ্যমে ফোন বা ব্রাউজার থেকেই যেকোনো স্থান থেকে এক নজরে অ্যাপ্লিকেশনের স্ট্যাটাস দেখা যায়।
- **`/gmail-sync`:** আপনার Gmail (via Gmail Connector) কানেক্ট করে নতুন ইন্টারভিউ ইনভাইট, অ্যাসেসমেন্ট লিংক, রিজেকশন বা অফার সম্পর্কিত ইমেইল পড়ে পরিবর্তনগুলো একসাথে প্রস্তাব করে। ইউজার কনফার্ম করলে ফাইল আপডেট হয়ে যায়।
- **`/expand`:** প্রোফাইলে লিংক করা GitHub Repos, Portfolio, Kaggle, Google Scholar ইত্যাদি স্ক্যান করে এবং আপনার সার্টিফিকেশন ও কোর্সের নাম দেখে আপনার অঘোষিত স্কিলগুলো খুঁজে বের করে প্রোফাইলে যুক্ত করে।
- **`/upskill`:** বাজার চাহিদার সাথে আপনার বর্তমান স্কিলের তুলনামূলক গ্যাপ বিশ্লেষণ করে একটি Heatmap এবং পড়ালেখার জন্য Time Estimate ও Web-Searched পড়াশোনার লিংক সহ একটি সম্পূর্ণ Learning Plan বানিয়ে দেয়।
- **`/html-report`:** অফলাইনে আপনার পিসিতে ব্রাউজারে খোলার জন্য `job_search_tracker.csv` থেকে একটি দৃষ্টিনন্দন HTML Dashboard তৈরি করে। যেখানে Stat Cards, Inline SVG Charts (Status, Sector, Channel, Funnel) এবং Filterable Table থাকে।
- **`/add-template`:** স্টক টেমপ্লেটের পরিবর্তে আপনার নিজস্ব যেকোনো LaTeX, Typst বা অন্য কমান্ড-লাইন ভিত্তিক ডকুমেন্টস ইঞ্জিনের টেমপ্লেট ইনস্টল করতে ব্যবহৃত হয়। Commands: `/add-template -list`, `/add-template -use <name>`, `/add-template -use default`
- **`/add-portal`:** সম্পূর্ণ নতুন কোনো Job Portal থেকে ডেটা স্ক্র্যাপ করার জন্য নতুন একটি CLI Skill জেনারেট করে দেয়।
- **`/reset`:** আপনার প্রোফাইল তথ্য বা ফাইল রিসেট করতে ব্যবহৃত হয়। অপশনগুলো হলো `/reset profile`, `/reset documents` এবং `/reset all` (নিরাপত্তার স্বার্থে ব্র্যাকেটে নিশ্চিত করতে `RESET` কথাটি হাতে লিখতে হয়)।
- **`/setup -section search`:** মূল ক্যান্ডিডেট প্রোফাইল না মুছে কেবল সার্চের জন্য টার্গেট করা পদ, এলাকা বা স্কিল দ্রুত পরিবর্তন করার সুযোগ দেয়।

## গ্লোবাল সার্চ পোর্টাল এবং স্যালারি বেঞ্চমার্কিং

![গ্লোবাল সার্চ পোর্টাল এবং স্যালারি বেঞ্চমার্কিং](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_5fa87485f8ab442b7256746b36c332aa.jpg)

আপনি যদি ডেনমার্কের বাইরে বা আন্তর্জাতিক মার্কেটে জব খুঁজতে চান, তবে রেপোতে দুটি বিল্ট-ইন সার্বজনীন সার্চ স্কিল রয়েছে:

1. **`linkedin-search`:** এটি লিঙ্কডইনের পাবলিক, Unauthenticated `jobs-guest` এন্ডপয়েন্টের ওপর তৈরি। এর কোনো অতিরিক্ত Runtime Dependency নেই এবং শুধুমাত্র `bun` দিয়েই চলে। যেকোনো দেশের নির্দিষ্ট জায়গার নাম দিয়ে জব খুঁজতে এটি ব্যবহার করতে পারেন (যেমন: `-l "Berlin, Germany"`, `-l "Mumbai, Maharashtra, India"`, `-l "Remote"`)\।
2. **`freehire-search`:** এটি `freehire.me` এগ্রিগেটরের পাবলিক REST API (JSON, কোনো API Key লাগে না) ব্যবহার করে সার্চ করে। এটি মূল টেক জবের জন্য ভীষণ উপযোগী এবং `-region`, `-country`, `-remote` ফ্ল্যাগ দিয়ে ফিল্টার করা যায়। ব্যাকএন্ড সম্পূর্ণ MIT-Licensed ও Self-Hostable (`FREEHIRE_API_URL`)\।

### অন্য Fork থেকে স্কিল ধার করার নিয়ম:

আপনি যদি Community Portal Index (Discussion #78) থেকে অন্য কোনো ইউজার বা ডেভেলপারের তৈরি করা পোর্টাল স্কিল নিয়ে আপনার প্রজেক্টের `.agents/skills/` ফোল্ডারে যুক্ত করতে চান, তবে অবশ্যই নিরাপত্তার স্বার্থে নিচের পদক্ষেপগুলো মেনে চলবেন:

- স্কিল ফোল্ডারের কোড ভালো করে নিজে পড়ে বুঝে নিন।
- দেখুন উক্ত কোডটি নির্দিষ্ট জব সাইট ছাড়া অন্য কোথাও অনাকাঙ্ক্ষিত Network Call করছে কিনা।
- `package.json` ফাইলে কোনো অশুভ Dependency বা Lifecycle Script আছে কিনা খেয়াল করুন।
- ইন্টারনেটের সাথে কানেকশন বন্ধ রেখে আপনার টার্মিনালে অফলাইনে টেস্ট রান করে নিন (যেমন: `bun test` চালানো)।

### স্যালারি বেঞ্চমার্কিং

যদি আপনার কাছে নির্দিষ্ট সেক্টর বা ইউনিয়নের বেঞ্চমার্ক স্যালারি ডেটা থাকে (যেমন: Excel ফাইল), তবে `convert_salary_excel.py` দিয়ে সেটিকে JSON বানিয়ে `salary_lookup.py` টুলের সাথে কানেক্ট করতে পারেন। বিস্তারিত দিকনির্দেশনা রয়েছে `tools/README_SALARY_TOOL.md`-এ। ডেটা না থাকলে এই ধাপটি নিছক Skipped হবে।

## প্রোফাইল ডেপথ এবং সিস্টেম মেইনটেন্যান্স গাইড

![প্রোফাইল ডেপথ এবং সিস্টেম মেইনটেন্যান্স গাইড](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_3e7fe75e799cf3200bc2e45b0c86f8c6.jpg)

আপনি আপনার প্রোফাইলে যত নিখুঁত ও গভীর বিবরণ দেবেন, ক্লডের তৈরি আউটপুট তত বেশি ধারালো ও রিয়েলিস্টিক হবে!

- **Role Descriptions:** পদবি লেখার পাশাপাশি সেই পদে আপনার দৈনন্দিন দায়িত্ব, মেজারেবল অর্জন, ব্যবহৃত প্রযুক্তি ও প্রজেক্টগুলোর স্পষ্ট বিবরণ লিখুন।
- **Skills in Context:** কেবল "Python" বা "Project Management" না লিখে এভাবে উপস্থাপন করুন: *"Built ML Pipelines for Customer Churn Prediction in Python using scikit-learn"* — এতে AI অনেক বেশি প্রাসঙ্গিক তথ্য খুঁজে পায়।
- **ম্যানুয়ালি এডিট করার জন্য জরুরি ফাইলসমূহ:**

| File | What to change |
| --- | --- |
| `CLAUDE.md` | ক্যান্ডিডেটের সম্পূর্ণ প্রোফাইল (Name, Education, Experience, Skills, Goals) |
| `01-candidate-profile.md` | সিভি ডেটার কাস্টমাইজড স্ট্রাকচার্ড রূপ |
| `02-behavioral-profile.md` | ব্যক্তিত্ব ও আচরণগত মূল্যায়নের ডেটা (PI/DISC) |
| `04-job-evaluation.md` | জব বাছাই ও স্কিল ফিল্টারিংয়ের কাস্টম রুলস |
| `05-cv-templates.md` | সিভির বিভিন্ন Profile Statements-এর ছাঁচ |
| `07-interview-prep.md` | ক্যান্ডিডেটের বাস্তব জীবনের ঘটনার ওপর ভিত্তি করে তৈরি করা STAR Examples |
| `search-queries.md` | নির্দিষ্ট স্কিল বা লোকেশন অনুযায়ী Job Search Queries |

### আপস্ট্রিম আপডেট ট্র্যাকিং

এই ওপেন সোর্স প্রজেক্টটি খুব দ্রুত উন্নত হচ্ছে। প্রতিদিন সরাসরি `master` Branch থেকে Pull করার চেয়ে নির্দিষ্ট Tagged Release ব্যবহার করা নিরাপদ।

আপডেট করার আগে আপনার কাস্টমাইজড ফাইলগুলোতে কী প্রভাব পড়বে তা দেখতে রান করুন: `python3 tools/check_upstream_updates.py` এবং আপস্ট্রিমের হাজারো কমটের মধ্যে কোনগুলো আপনার দেখা উচিত তা সাজিয়ে নিতে ব্যবহার করুন: `python3 tools/upstream_triage.py`!

## প্রজেক্টের সম্পূর্ণ ফাইল ডিরেক্টরি পরিচিতি

![প্রজেক্টের সম্পূর্ণ ফাইল ডিরেক্টরি পরিচিতি](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_82e9bce6966c79c0110e97fbda56a941.jpg)

```
ai-job-search/
├── CLAUDE.md # Main candidate profile + workflow rules
├──.claude/
│ ├── commands/
│ │ ├── apply.md # /apply workflow (drafter-reviewer)
│ │ ├── setup.md # /setup onboarding (documents folder, CV import, or interview)
│ │ ├── expand.md # /expand competency enrichment from documents and online presence
│ │ ├── add-template.md # /add-template register custom templates (LaTeX, Typst, .)
│ │ ├── add-portal.md # /add-portal generate a job-portal search skill for your market
│ │ ├── rank.md # /rank triage scraped jobs into a ranked shortlist
│ │ ├── outcome.md # /outcome record application results, archive materials
│ │ ├── gmail-sync.md # /gmail-sync auto-detect application status from Gmail
│ │ ├── interview.md # /interview stage-specific prep pack + mock interview
│ │ ├── html-report.md # /html-report generate application tracker dashboard
│ │ ├── notion-sync.md # /notion-sync one-way pipeline view in a Notion database
│ │ └── reset.md # /reset wipe profile data or documents folder
│ ├── skills/
│ │ ├── job-application-assistant/ # Core application skill
│ │ │ ├── SKILL.md # Skill definition
│ │ │ ├── 01-candidate-profile.md # Your education, experience, skills
│ │ │ ├── 02-behavioral-profile.md# PI/DISC/personality assessment
│ │ │ ├── 03-writing-style.md # Tone, structure, do's and don'ts
│ │ │ ├── 04-job-evaluation.md # Scoring framework for job fit
│ │ │ ├── 05-cv-templates.md # LaTeX CV structure + tailoring rules
│ │ │ ├── 06-cover-letter-templates.md # LaTeX cover letter templates
│ │ │ └── 07-interview-prep.md # STAR examples + interview framework
│ │ ├── job-scraper/ # Job search orchestration
│ │ └── upskill/ # /upskill skill gap analysis and learning plan
│ └── settings.json # Claude Code permissions (shared, scoped)
├──.agents/skills/ # Job portal CLI tools
│ ├── jobbank-search/ # Akademikernes Jobbank (Denmark)
│ ├── jobdanmark-search/ # Jobdanmark.dk (Denmark)
│ ├── jobindex-search/ # Jobindex.dk (Denmark)
│ ├── jobnet-search/ # Jobnet.dk (Denmark, government portal)
│ ├── linkedin-search/ # LinkedIn public job listings (country-agnostic)
│ └── freehire-search/ # freehire.me tech job aggregator (multi-market, REST API)
├── cv/
│ └── main&amp;lt;em&amp;gt;example.tex # moderncv LaTeX template
├── cover&amp;lt;/em&amp;gt;letters/
│ ├── cover.cls # Custom cover letter LaTeX class
│ ├── cover&amp;lt;em&amp;gt;example.tex # Example cover letter (structural reference + CI smoke test)
│ └── OpenFonts/ # Lato + Raleway fonts
├── templates/ # Custom templates registered via /add-template
│ └── README.md # Folder layout instructions
├── documents/ # Career source materials for /setup Path A and /expand
│ ├── README.md # Folder layout instructions
│ ├── cv/ # Master CV (PDF or.tex)
│ ├── linkedin/ # LinkedIn profile export (PDF)
│ ├── diplomas/ # Degree certificates and transcripts
│ ├── references/ # Reference letters
│ └── applications/ # Past application records (&amp;lt;company&amp;gt;&amp;lt;/company&amp;gt;&amp;lt;/em&amp;gt;&amp;lt;role&amp;gt;/)
├──.github/workflows/ci.yml # CI: LaTeX smoke compiles, skill lint, CLI typechecks
├── salary&amp;lt;em&amp;gt;lookup.py # Salary benchmarking tool (BYO data)
├── tools/
│ ├── check&amp;lt;/em&amp;gt;framework&amp;lt;em&amp;gt;version.py # CI check: framework&amp;lt;/em&amp;gt;version bumped when skill files change
│ ├── check&amp;lt;em&amp;gt;upstream&amp;lt;/em&amp;gt;updates.py # Preview which personalized files an upstream update touches
│ ├── convert&amp;lt;em&amp;gt;salary&amp;lt;/em&amp;gt;excel.py # Convert salary Excel to JSON
│ ├── install&amp;lt;em&amp;gt;portal&amp;lt;/em&amp;gt;clis.py # Install every discovered portal CLI (bun install)
│ ├── lint&amp;lt;em&amp;gt;skills.py # CI lint for skills, commands, settings.json
│ ├── robots&amp;lt;/em&amp;gt;check.py # Gate the browser-header retry against robots.txt
│ ├── security&amp;lt;em&amp;gt;guards.py # CI guards: permission allowlist, gitignore rules, manifests
│ ├── upstream&amp;lt;/em&amp;gt;triage.py # Sort upstream commits into worth-reviewing vs probably-skip
│ ├── verify&amp;lt;em&amp;gt;layout.py # Measure a compiled PDF's page layout (holes, orphans, footer collisions)
│ ├── verify&amp;lt;/em&amp;gt;pdf.py # Verify a compiled PDF's page count and extractable text
│ └── README&amp;lt;em&amp;gt;SALARY&amp;lt;/em&amp;gt;TOOL.md # Salary tool setup instructions
├── job&amp;lt;em&amp;gt;scraper/ # Scraper state (seen jobs, results)
├── gmail&amp;lt;/em&amp;gt;sync/ # /gmail-sync state (processed message IDs, last sync date)
├── upskill/ # /upskill report output (markdown reports per run)
├── job&amp;lt;em&amp;gt;search&amp;lt;/em&amp;gt;tracker.csv # Application tracking spreadsheet
└── SETUP.md # Detailed setup guide
```

## সমাপনী

![সমাপনী, কৃতজ্ঞতা প্রকাশ ও লাইসেন্স](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_7e827d10299cf42ed00984c1c49ea66e.jpg)

প্রজেক্টের বিভিন্ন হেল্পার টুলস এবং অটোমেশনের জন্য বিশেষ ধন্যবাদ জানাতে হয় Mikkel Krogholm-কে (তাঁর `skills repo`-র জন্য)। প্রজেক্টের পুরো সিসটেম পরিচালিত হয় Anthropic-এর Claude Code দ্বারা। আপনি যদি প্রজেক্টে কোনো নতুন পরিবর্তন নিয়ে Pull Request (PR) পাঠাতে চান, তবে প্রথমে তাদের গাইডলাইন ফাইল `CONTRIBUTING.md` ভালোভাবে পড়ে নেওয়ার অনুরোধ রইল। প্রজেক্টটির যাবতীয় কোড MIT License-এর আওতায় সম্পূর্ণ উন্মুক্ত।

আশাকরি এই ইন-ডেপথ টিউনটি আপনার নিজের কম্পিউটারে এক চমৎকার ও স্মার্ট Job Search Infrastructure গড়ে তুলতে সাহায্য করবে। ম্যানুয়াল পরিশ্রম কমিয়ে প্রযুক্তিকে কাজে লাগিয়ে নিজের স্বপ্নের ক্যারিয়ার গড়ে তুলুন! হ্যাপি জব হান্টিং!
