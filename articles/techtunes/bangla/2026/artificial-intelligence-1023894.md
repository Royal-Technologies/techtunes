---
archive_id: techtunes-1023894
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 1023894
title: Harness² – Google Research এর AI Agent বিপ্লব! যেখানে রয়েছে 2 Levels of Recursion,
  8 Editable Harness Components এবং Gemini 3.5 Flash এর জন্য 11.5 Points Gain, যা
  টেক ওয়ার্ল্ডে প্রতিদ্বন্দ্বীদের নিশ্চিহ্ন করে দিবে!
slug: artificial-intelligence-1023894
language: bn
status: publish
published_at: '2026-11-06T09:09:00+00:00'
modified_at: '2026-11-06T09:12:00+00:00'
original_url: https://www.techtunes.io/artificial-intelligence/tune-id/1023894
author: মো আতিকুর ইসলাম
author_url: https://www.techtunes.io/tuner/atikurofficial
categories:
- আর্টিফিশিয়াল ইন্টেলিজেন্স (এআই)
tags:
- আর্টিফিশিয়াল ইন্টেলিজেন্স
- এআই
content_hash: 580f0174352c2733faa5a16e5a153a1741912900420de09dce3acb663ad7dec8
archived_at: '2026-11-12T11:34:21.874377+00:00'
---

আজকের Artificial Intelligence এবং Software Engineering-এর দ্রুত পরিবর্তনশীল বিশ্বে আমরা এক রোমাঞ্চকার সন্ধিক্ষণে দাঁড়িয়ে আছি। আমরা প্রতিনিয়ত দেখছি কীভাবে সাধারণ Text Generation বা Chatbot-এর ধারণা অতিক্রম করে AI Models Recursive Agents হিসেবে আত্মপ্রকাশ করছে। কিন্তু প্রশ্ন হলো, একটি Model-কে কোনো জটিল বাস্তবমুখী কাজ বা Task সমাধান করতে দিলে সে ঠিক কীভাবে সেই পরিবেশের সাথে খাপ খাইয়ে নেয়?

কেবলমাত্র একটি শক্তিশালী Model থাকলেই কি একটি স্বায়ত্তশাসিত Agent সঠিকভাবে তার দায়িত্ব পালন করতে পারে? মোটেও না! একটি Model-কে বাস্তব জগতের কোনো Task-এ সফলভাবে পরিচালনা করতে তার চারপাশে একটি শক্তপোক্ত পরিবেশ বা System প্রয়োজন হয়। প্রযুক্তিবিদরা এই পুরো পরিপার্শ্বকে বলেন Harness।

আর ঠিক এই জায়গাতেই Google Research নিয়ে এসেছে এক বিপ্লবী উদ্ভাবন—Harness²! আজকের এই বিশাল ও বিস্তারিত টিউনে আমরা Google Research-এর উন্মোচিত Harness² Framework-এর প্রতিটি দিক গভীরভাবে বিশ্লেষণ করব। আপনি যদি AI, Software Architecture, বা স্বায়ত্তশাসিত Agents নিয়ে কাজ করে থাকেন বা জানতে আগ্রহী হন, তবে এই নির্দেশিকাটি আপনাকে Recursive Agent Harnessing-এর আদ্যোপান্ত বুঝতে সাহায্য করবে।

## Harness এবং Harnessing কী? গভীর থেকে সহজ ব্যাখ্যা

![Harness এবং Harnessing কী](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_8c3aa766bb9ab47cc74363313aac873a.png)

চলুন প্রথমেই কোনো জটিল পরিভাষায় না গিয়ে একদম বাস্তব জীবনের একটি সুন্দর উদাহরণের মাধ্যমে বিষয়টি বুঝে নিই।

ভেবে দেখুন, আপনার কাছে অত্যন্ত শক্তিশালী এবং অত্যাধুনিক একটি গাড়ি চালনার ইঞ্জিন বা Engine রয়েছে। এখন এই Engine-টি নিজে নিজে চলতে পারে না। এটিকে একটি পূর্ণাঙ্গ গাড়ি হিসেবে রাস্তায় চালাতে হলে আপনার প্রয়োজন হবে একটি স্টিয়ারিং, আধুনিক গিয়ার সিস্টেম, ব্রেক, ড্যাশবোর্ড, ফুয়েল ইনজেক্টর এবং নানা ধরনের সেন্সর। AI Agent-এর ক্ষেত্রেও ঠিক একই ব্যাপার ঘটে!

- **Harness**: এটি হলো একটি **Model**-এর চারপাশের সম্পূর্ণ **System**, যা তাকে কেবল টেক্সট জেনারেট করার মধ্যে সীমাবদ্ধ না রেখে বাস্তব বিশ্বে একটি কার্যকর **Agent** হিসেবে আচরণ ও কাজ করার সুযোগ তৈরি করে দেয়। এই **Harness**-এর ভেতরে অন্তর্ভুক্ত থাকে **Prompts**, **Tools**, **Memory**, **Skills**, **Orchestration**, **Guardrails**, **Scripts**, এবং **Plugins**।
- **Harnessing**: এটি হলো সেই পরিবেশ বা **Harness System**-টিকে পর্যবেক্ষণ করে প্রতিনিয়ত **Optimize** বা সর্বোত্তম অবস্থায় নিয়ে আসার একটি ধারাবাহিক প্রক্রিয়া।

### Open World-এর জন্য Harness² Framework

বাস্তব বিশ্ব বা Open World অত্যন্ত অনিশ্চিত। এখানে এমন বহু কাজ বা Tasks সামনে আসে, যেগুলো এজেন্ট তৈরির সময় বা Harness Design-এর সময় ডিজাইনারদের কল্পনাতেও ছিল না! এমন অনাকাঙ্ক্ষিত পরিস্থিতিতে কোনো এজেন্টের পারফরম্যান্স ধরে রাখা সবচেয়ে বড় চ্যালেঞ্জ।

Harness² হলো এমন একটি Plug-And-Play Framework, যা Open World-এ Recursive Agent Harnessing পরিচালনা করে। এর সবচেয়ে চমকপ্রদ দিক হলো, এটি মূল Model Weights সম্পূর্ণ স্থির বা Fixed রেখে এবং কোনো প্রকার নতুন Training বা Fine-Tuning ছাড়াই দুটি স্তরে Recursion ঘটিয়ে Harness-কে নতুন কাজের উপযোগী করে তোলে!

```
+-+ | Harness² | +-+ | +-+-+ | | [Task-Level Recursion] [Harnessing-Level Recursion]</p>

<ul>
<li>Propose–Probe–Compose Step - Updates Persistent Improvement Harness</li>
<li>Refines Execution Harness - Retains Adopted Harnesses &amp; Lessons</li>
<li>Works without Ground-Truth Feedback - Guides Future Refinements across Tasks
```

### দুটি শক্তিশালী Recursion Level

Harness² দুটি ভিন্ন স্তরের Recursion-কে চমৎকারভাবে যুক্ত করে:

1. **Task-Level Recursion**: এটি নির্দিষ্ট কোনো বর্তমান **Task** দক্ষতার সাথে সম্পন্ন করার জন্য **Execution Harness**-কে ক্ষুরধার ও নিখুঁত করে তোলে। এই পুরো প্রক্রিয়াটি সম্পন্ন হয় একটি বৈপরীত্যমূলক বা contrastive **Propose–Probe–Compose Step**-এর মাধ্যমে:
   - **Propose**: প্রথমে বর্তমান কাজের প্রয়োজনীয়তা বুঝে **Harness**-এর জন্য কিছু নতুন পরিবর্তন বা **Edits Propose** করা হয়।
   - **Probe**: এরপর সেই **Edits** একই **Task**-এ প্রয়োগ করে তাদের প্রভাব বা **Effects Probe** করে পরীক্ষা করে দেখা হয়।
   - **Compose**: কোনো প্রকার সরাসরি সঠিক উত্তর বা **Ground-Truth Feedback** ছাড়াই বিভিন্ন **Executions**-এর আচরণের পার্থক্য বা **Behavioral Contrasts** পর্যবেক্ষণ করে একটি চূড়ান্ত ও শক্তিশালী **Refined Harness Compose** করা হয়।
2. **Harnessing-Level Recursion**: এটি সময়ের সাথে সাথে এজেন্টের অভিজ্ঞতা সঞ্চয় করার ক্ষমতা গড়ে তোলে। প্রতিটি **Task** সফলভাবে শেষ হওয়ার পর এই স্তরটি সফলভাবে গৃহীত **Adopted Harnesses** এবং প্রমাণ ভিত্তিক শিক্ষা বা **Evidence-Supported Lessons** সংরক্ষণ করে। এরপর এটি একটি স্থায়ী **Improvement Harness Update** করে রেখে দেয়, যা ভবিষ্যতে নতুন কোনো কাজের মুখোমুখি হলে সঠিক দিকনির্দেশনা বা **Refinement Guide** হিসেবে সহায়তা জোগায়।

### প্রফেশনাল Benchmark-এ অর্জিত চমকপ্রদ পারফরম্যান্স

গবেষণায় দেখা গেছে, তিনটি পেশাদার Benchmarks এবং চারটি পৃথক Model–Harness Configurations জুড়ে কেবল একটি মাত্র Harness² Step প্রয়োগ করেই GLM-5 এবং Gemini 3.5 Flash তাদের স্বাভাবিক Base Harnesses-এর তুলনায় বিশাল অগ্রগতি প্রদর্শন করেছে:

- **WorkBuddy-Bench**: সর্বোচ্চ **11.5 Points Gain** অর্জন করেছে।
- **JobBench**: সর্বমোট **4.5 Points Gain** পাওয়া গেছে।
- **LAB Benchmark**: **Partial Pass Rate**-এর ক্ষেত্রে **11.8 Percentage Points** অভূতপূর্ব বৃদ্ধি দেখা গেছে।

সবচেয়ে দারুণ ব্যাপার হলো, আপনি যদি এজেন্টের Task-Level Recursion Budget বৃদ্ধি করেন, তবে এই সাফল্যের হার ও Gains আরও অনেক গুণ বেড়ে যায়! বর্তমানে উন্মুক্ত এই রিলিজটিতে Parallel And Sequential Recursion, OpenCode And Codex Executors, এবং প্রফেশনাল JobBench, LAB, And WorkBuddy-Bench পূর্ণাঙ্গভাবে সমর্থিত।

### Harness

অফিসিয়াল ওয়েবসাইট @ [Harness](https://arxiv.org/abs/2610.14224)

## Video Overview

[[https://www.techtunes.io/tDrive/tuner/2026/11/techtunes\_43e8d5556301779dcd1d1d06fbe3c716.mp4](https://dnc.techtunes.io/tDrive/tuner/2026/11/techtunes_43e8d5556301779dcd1d1d06fbe3c716.mp4)](https://dnc.techtunes.io/tDrive/tuner/2026/11/techtunes_43e8d5556301779dcd1d1d06fbe3c716.mp4?_=1)

প্রজেক্টটির পাইপলাইন, কাজ করার ধরন এবং সম্পূর্ণ মেকানিজমের ভিডিও ওভারভিউ টিউটোরিয়াল দেখতে পাবেন।

## Harness Components: ৮টি প্রদেয় Editable Components

![Harness Components: ৮টি প্রদেয় Editable Components](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_5e1a32850208424031ff72e902621341.jpg)

Harness² Framework-এ একটি Model-এর চারপাশের কার্যকারিতা নিখুঁতভাবে পরিচালনা করতে আটটি পরিবর্তনযোগ্য বা Editable Components উন্মুক্ত রাখা হয়েছে। প্রসেস চলার সময় এগুলোকে তাদের নির্দিষ্ট দায়িত্ব বা Runtime Role অনুসারে চারটি গ্রুপে ভাগ করা হয়:

```
+-+
| 8 Harness Components |
+-+
| 1. Context Construction | - System Prompt  - Guardrails  - Memory  - Skills |
| 2. Tool Interface | - Tool Guidance  - Scripts |
| 3. Orchestration | - Subagents |
| 4. Middleware | - Plugins |
+-+
```

### ১. Context Construction (কনটেক্সট গঠন)

- **System Prompt**: মডেলটির প্রাথমিক পরিচয়, ভূমিকা এবং মূল আচরণ নির্ধারণ করে।
- **Guardrails**: এজেন্ট যেন কাজের সময় নিরাপত্তার সীমানা বা নীতি লঙ্ঘন না করে তা নিশ্চিত করে।
- **Memory**: এজেন্টের পূর্বের ইন্টারঅ্যাকশন ও অর্জিত তথ্য সংরক্ষণ করে যা পরবর্তী সিদ্ধান্তে কাজে লাগে।
- **Skills**: সুনির্দিষ্ট কোনো জটিল কাজ সম্পন্ন করার জন্য প্রয়োজনীয় বিশদ গাইডলাইন ও দক্ষতা সরবরাহ করে।

### ২. Tool Interface (টুল ইন্টারফেস)

- **Tool Guidance**: এজেন্ট কীভাবে বিভিন্ন ফাইল, টার্মিনাল বা এপিআই টুল ব্যবহার করবে তার সঠিক নির্দেশনা।
- **Scripts**: স্বায়ত্তশাসিতভাবে বিভিন্ন প্রসেস চালানোর জন্য ছোট ছোট এক্সিকিউটেবল কোড বা স্ক্রিপ্ট।

### ৩. Orchestration (সমন্বয়সাধন)

- **Subagents**: যখন কোনো কাজ একা করা কঠিন হয়ে পড়ে, তখন কাজটি ছোট ছোট অংশে ভাগ করে অন্যান্য বিশেষায়িত সাব-এজেন্টদের কাছে অর্পণ বা **Delegation** করার মেকানিজম।

### ৪. Middleware (মিডলওয়্যার নিয়ন্ত্রণ)

- **Plugins**: এক্সটার্নাল সার্ভিস, এপিআই ইন্টারফেস এবং সিস্টেম রানটাইমের মধ্যে যোগাযোগের সংযোগকারী প্লাগইন।

এই আটটি উপাদান একত্রিত হয়ে Context Construction, Tool Interface, Delegation, এবং Tool Loop-এর ভেতরে এজেন্টের সার্বিক আচরণ নিয়ন্ত্রণ করে।

## Install: সিস্টেম প্রয়োজনীয়তা ও ইন্সটলেশন নির্দেশিকা

![সিস্টেম প্রয়োজনীয়তা ও ইন্সটলেশন নির্দেশিকা](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_65ba7c76d2f6ff099a6977637e945b42.jpg)

Harness² সঠিক উপায়ে ইনস্টল ও কনফিগার করার প্রক্রিয়া অত্যন্ত সহজ ও সোজা। চলুন প্রতিটি ধাপ বিস্তারিত জেনে নিই।

### সিস্টেমের পূর্বশর্ত (Prerequisites)

এই প্রজেক্টটি চালানোর জন্য আপনার পিসিতে Linux Operating System, Python 3.12, এবং দ্রুতগতির প্যাকেজ ম্যানেজার `uv` ইনস্টল থাকতে হবে।

### ১. স্থানীয় Demo Setup (কোনো API Credentials ছাড়া)

আপনার প্রোজেক্টের Repository Root থেকে টার্মিনাল খুলে নিচের কমাণ্ডগুলো ধারাবাহিকভাবে রান করুন:

```
uv venv -python 3.12.venv
source.venv/bin/activate
uv pip install -e '.[render]'
harness2-demo -output runs/demo -k 2
```

এই লোকাল Demo ভার্সনটি চালনা করতে কোনো প্রকার Model Credentials বা পেইড এপিআই-এর প্রয়োজন হয় না। এটি Deterministic Editors এবং আসল Python Executions ব্যবহার করে উভয় Recursion Modes সাফল্যের সাথে পরীক্ষা করে।

### ২. Model-Backed Benchmarks Setup

আপনি যদি আসল LLM Models দ্বারা পরিচালিত প্রফেশনাল Benchmarks টেস্ট করতে চান, তবে আপনার পিসিতে Node.js 20+, Google Cloud CLI, এবং নির্দিষ্ট বেন্চমার্কের ডিপেন্ডেন্সি থাকতে হবে:

- **LAB Benchmark**-এর ডকুমেন্ট প্রসেসিংয়ের জন্য প্রয়োজন **Pandoc** এবং **Poppler**।
- **WorkBuddy-Bench**-এর কনটেইনারাইজড এনভায়রনমেন্টের জন্য **Docker** ইনস্টল থাকা বাধ্যতামূলক।

এরপর আপনার মডেল কনফিগারেশন সেটআপ করুন:

```
cp.env.example.env</p>

<h1>.env ফাইলটি এডিট করে আপনার Vertex AI project এবং model IDs যুক্ত করুন। </h1>

<p>gcloud auth application-default login
```

অন্যান্য মডেল সেটিংস, বিকল্প অথেনটিকেশন মেথড এবং Codex Executor সংক্রান্ত বিস্তারিত গাইডলাইনের জন্য প্রজেক্টের `docs/SETUP.md` ফাইলটি দেখুন।

## Run A Benchmark: কীভাবে কমাণ্ড রান, বিচার এবং রিপোর্ট তৈরি করবেন

![Run A Benchmark: কীভাবে কমাণ্ড রান, বিচার এবং রিপোর্ট তৈরি করবেন](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_a74a6dacfcd1473ccc8ad263e7be39d6.jpg)

নিচে একটি বাস্তবিক উদাহরণ দিয়ে দেখানো হলো কীভাবে LAB Benchmark ইনস্টল করে একটিমাত্র Task Run করা যায়, এবং পরবর্তীতে তার ফলাফল Evaluate ও Report তৈরি করা যায়। মনে রাখবেন, Model-Backed Runs চালানোর ক্ষেত্রে এপিআই খরচ বা API Costs হয়; তাই শুরুতেই ছোট Task Selection নির্বাচন করা নিরাপদ।

```
harness2-setup lab
harness2-check -bench lab
harness2 -bench lab -k 1 -mode parallel \ -only-domains antitrust-competition -max-tasks 1
harness2-judge -bench lab -k 1 -mode parallel
harness2-report -bench lab -k 1 -mode parallel
```

### কমাণ্ড ব্যবহারের নিয়মাবলী:

- **Sequential Recursion**: একই কমাণ্ডগুলো যদি পরপর পর্যায়ক্রমিক ধাপে চালাতে চান, তবে কমাণ্ডের সাথে `-mode sequential` যোগ করুন।
- **Task-Level Recursion Budget**: কমাণ্ডের `-k` প্যারামিটারটি হলো রেকারশন বাজেট সেট করার অপশন।
- **Judging And Reporting Rules**: মূল্যায়নের সততা ধরে রাখতে **Judging** এবং **Reporting** করার সময় মূল **Refinement Run**-এ ব্যবহৃত একই **Benchmark**, **Executor**, **Subset**, `-k`, `-mode`, এবং **Seed** প্রয়োগ করতে হবে।
- **Dry-Run Feature**: কোনো প্রকার এপিআই খরচ বা **Model Calls** না করে কেবল কোড কোন টাস্কগুলো সিলেক্ট করছে তা প্রিভিউ দেখতে `harness2` কমাণ্ডের সাথে `-dry-run` যোগ করুন।

### সমর্থিত Benchmarks-এর বিবরণ

| Benchmark | Tasks | Install | Guide |
| --- | --- | --- | --- |
| JobBench | Professional Work | `harness2-setup jb` | JobBench Guide |
| LAB | Legal Work | `harness2-setup lab` | LAB Guide |
| WorkBuddy-Bench | Office, Web, And Code | `harness2-setup wb` | WorkBuddy Guide |

প্রতি কমাণ্ডে কেবল একটি Benchmark বেছে নিন। WorkBuddy প্রজেক্ট সেটআপ সম্পন্ন হওয়ার পর থেকে প্রতিটি কমাণ্ডে সাবসেট হিসেবে `-subset office`, `-subset web`, অথবা `-subset code` গ্রহণ করে। প্রতিটি বেন্চমার্কের ডেটা, ডোমেইন এবং গ্রেডিং মেকানিজম বুঝতে প্রজেক্টের Benchmark Guides নির্দেশিকা দেখুন।

## Experiments: Task-Level Recursion স্কেল করার বৈজ্ঞানিক পদ্ধতি

![Experiments: Task-Level Recursion স্কেল করার বৈজ্ঞানিক পদ্ধতি](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_b00334f2b0b59dc80f2d694b10afd69a.jpg)

Task-Level Recursion বাজেট স্কেল বা সম্প্রসারণ করার জন্য দুটি প্রধান টেকনিক রয়েছে:

1. **Parallel Recursion**: এটি একটি বিস্তৃত পদ্ধতি। এটি একসাথে একাধিক **Candidate Harnesses Explore** করে এবং তাদের সমস্ত **Execution Evidence** একত্রিত করে একটি শক্তিশালী **Refinements Compose** তৈরি করে।
2. **Sequential Recursion**: এটি একটি গভীর বিশ্লেষণাত্মক পদ্ধতি। এটি একটি **Refined Harness** এবং তার পূর্বে অর্জিত **Accumulated Evidence**-কে সাথে নিয়ে পরপর কয়েকটি **Propose–Probe–Compose Steps**-এর মাধ্যমে সিস্টেমকে নিখুঁত করে তোলে।

> *সহজ কথায় মনে রাখার নীতি: Parallel Recursion চারপাশে ব্যাপকভাবে খোঁজে (Explores Wider); আর Sequential Recursion সমাধানকে গভীরে নিয়ে নিখুঁত করে (Refines Deeper)।*

```
[Parallel Recursion] -> Probe (K General + K Domain Candidates) -> Produce K Compositions
[Sequential Recursion] -> Step 1 -> Step 2 ->. -> Step K (Deep Refinement)
```

### Experiments Option Table

| Option | Behavior |
| --- | --- |
| `-k 1` | একটিমাত্র Propose–Probe–Compose Step সম্পাদন করে। |
| `-k K -mode parallel` | $K$ সংখ্যক General এবং $K$ সংখ্যক Domain-Specific Candidates Probe করে এবং সর্বশেষে $K$ সংখ্যক Compositions উৎপাদন করে। |
| `-k K -mode sequential` | পরপর $K$ সংখ্যক ধারাবাহিক Successive Steps-এর মাধ্যমে Harness-কে উন্নত বা Refine করে। |
| `-substrate cx` | ডিফল্ট OpenCode Executor-এর পরিবর্তে Codex Executor ব্যবহার করে। |

প্রতিটি কাজ শেষ হওয়ার পরে, Harnessing-Level Recursion সফলভাবে গৃহীত Adopted Harness এবং প্রমাণ ভিত্তিক পাঠ বা Evidence-Supported Lessons সংরক্ষণ করে রাখে যা পরবর্তী নতুন কাজের ক্ষেত্রে নির্দেশিকা দেয়। টাস্ক সিলেক্ট করার নিয়ম, Concurrency, Reproducibility, এবং Baseline Comparisons জানতে প্রজেক্টের `docs/EXPERIMENTS.md` ডকুমেন্ট দেখুন।

## Web Access: নিরাপত্তা ও নেটওয়ার্ক নিয়ন্ত্রণ সতর্কতা

![Web Access: নিরাপত্তা ও নেটওয়ার্ক নিয়ন্ত্রণ সতর্কতা](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_51e167733be97df4d3e7ac4714b53d29.jpg)

Harness² Framework ব্যবহার করার সময় নিরাপত্তা এবং মূল্যায়নের নিরপেক্ষতা অত্যন্ত গুরুত্বের সাথে বিবেচনা করতে হবে:

- প্রসেস চলার সময় **Executor Network Access** সম্পূর্ণ অনিয়ন্ত্রিত বা **Unrestricted** থাকে।
- **Codex Substrate** রান করার সময় তার অভ্যন্তরীণ **Sandbox Disabled** অবস্থায় থাকে।
- অনলাইনে সোর্স কোড বা পাবলিক **Benchmark Rubrics** এজেন্টের নাগালের মধ্যে এসে যেতে পারে।
- **জরুরি সতর্কতা**: এজেন্টের পারফরম্যান্স নিরপেক্ষভাবে যাচাই করার জন্য মূল্যায়নের পূর্বে যথাযথ **Network Restrictions** কনফিগার করে নিন, যাতে এজেন্ট কোনোভাবেই অনলাইনের সরাসরি উত্তর বা **Benchmark Answers** এবং **Grading Criteria** এক্সেস না করতে পারে।

## Results And Resume: রেজাল্ট সংরক্ষণ ও রান রিজিউম করার নিয়ম

![Results And Resume](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_f1f1a413c4b0d03f3f465071aec0996a.jpg)

আপনার প্রতিটি রান সফলভাবে সম্পন্ন হওয়ার পর তার সমস্ত আউটপুট এবং ফলাফল `runs/` ডিরেক্টরির ভেতরে সুন্দরভাবে সংরক্ষিত হয় (বেন্চমার্ক এবং সাবসেট অনুযায়ী আলাদা ফোল্ডারে)।

ফলাফলের ফোল্ডারে যে সমস্ত গুরুত্বপূর্ণ ফাইল ও তথ্য অন্তর্ভুক্ত থাকে:

- **Task Summaries**: কাজের সংক্ষিপ্ত ফলাফল ও সারাংশ।
- **Deliverables**: এজেন্ট কর্তৃক তৈরিকৃত মূল ফাইল, কোড বা ডেলিভারেবল।
- **Adopted Harnesses**: সফলভাবে গৃহীত হার্নেসের কনফিগারেশন।
- **Reflection Notes**: এজেন্টের কাজের নিজস্ব বিশ্লেষণাত্মক নোট।
- **Evaluation Results**: মূল্যায়নের নম্বর এবং পারফরম্যান্স রিপোর্ট।

কোনো কারণে প্রসেস আটকে গেলে বা বন্ধ হয়ে গেলে পুনরায় শুরু করতে বা Resume করতে আগের কমাণ্ডটি হুবহু পুনরায় টাইপ করে রান করুন। তবে আপনি যদি ব্যবহৃত Models বা Task Selection পরিবর্তন করেন, তবে একটি নতুন `HARNESS2_RUNS_DIR` এনভায়রনমেন্ট ভ্যারিয়েবল ডিক্লেয়ার করুন। প্রতিটি কমাণ্ডের বিশদ ব্যবহারের জন্য শেষে `-help` যোগ করুন।

## Citation: প্রজেক্ট সাইটেশন তথ্য

![Citation: প্রজেক্ট সাইটেশন তথ্য](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_4864420d690664f424f9d2f26db11f58.jpg)

আপনি যদি একাডেমিক পেপার, সাইন্টিফিক রিসার্চ বা নিজস্ব প্রজেক্টে Harness² ব্যবহার করেন, তবে নিচের অফিশিয়াল BibTeX Citation ব্যবহার করে কৃতিত্ব প্রদান করার জন্য অনুরোধ করা হচ্ছে:

@article{xu2026harness2, title = {Harness$^2$: Recursive Agent Harnessing for an Open World}, author = {Xu, Ruiyao and Chen, Yanfei and CuiZhu, Zhongying and Dalvi Mishra, Bhavana and Ming, Yifei and Yu, Han and Han, Rujun and Lee, Chen-Yu and Pfister, Tomas}, journal = {arXiv preprint arXiv:2610.14224}, year = {2026}, url = {https://arxiv.org/abs/2610.14224}

এই গবেষণাপত্রটির সম্মানিত গবেষক ও লেখকবৃন্দ হলেন: Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu, Bhavana Dalvi Mishra, Yifei Ming, Han Yu, Rujun Han, Chen-Yu Lee, এবং Tomas Pfister। গবেষণা পত্রটি ২০২৬ সালে arXiv (arXiv:2610.14224)-এ সংরক্ষিত ও প্রকাশিত হয়।

## Contributing: প্রজেক্টে অবদানের নিয়মাবলী

![Contributing: প্রজেক্টে অবদানের নিয়মাবলী](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_d4442fa3ed74b557b0aa1e291225269a.jpg)

Harness² একটি ওপেন-সোর্স প্রজেক্ট। আপনি যদি এই প্রজেক্টের কোডবেসে অবদান রাখতে চান, নতুন কোনো ফিচার যুক্ত করতে চান বা বাগ রিপোর্ট করতে চান, তবে গিটহাবের `CONTRIBUTING.md` ফাইলে উল্লিখিত নির্দেশিকা মেনে চলুন।

## License: লাইসেন্স ও থার্ড-পার্টি অধিকার

![License: লাইসেন্স ও থার্ড-পার্টি অধিকার](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_3f9e002df41abec6d1bc62447d868ac9.jpg)

Harness² প্রজেক্টের মূল কোডবেস Apache License 2.0-এর অধীনে লাইসেন্সকৃত। তবে প্রজেক্টের `third_party/` ডিরেক্টরির অধীনে থাকা থার্ড-পার্টি কোড, ব্যবহৃত Datasets, এবং Benchmarks তাদের মূল সরবরাহকারীর লাইসেন্স বা Upstream Licenses মেনে চলে। বিস্তারিত জানার জন্য `dependencies/README.md` ফাইল থেকে থার্ড-পার্টি নোটিশসমূহ পড়ে নিন।

## Disclaimer: অফিশিয়াল ডিসক্লেইমার

![Disclaimer: অফিশিয়াল ডিসক্লেইমার](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_8f043647da89e136ed25e10392072a1c.jpg)

এটি Google-এর কোনো অফিশিয়ালি সমর্থিত প্রোডাক্ট বা Officially Supported Google Product নয়। এছাড়া এই প্রজেক্টটি Google Open Source Software Vulnerability Rewards Program-এর অধীনস্থ সুবিধা বা পুরষ্কারের জন্য গ্রহণযোগ্য বা Eligible নয়।

## AI Agent Harnessing-এর নতুন দিগন্ত

![AI Agent Harnessing-এর নতুন দিগন্ত](https://dnc.techtunes.io/tDrive/tuner/2026/10/techtunes_e80a6b57aa6de950f414ee04ce821e74.jpg)

Google Research-এর Harness² প্রমাণ করে দিয়েছে যে স্বায়ত্তশাসিত AI Agents তৈরি করতে হলে কেবল বিশাল মডেল তৈরি করাই শেষ কথা নয়; বরং মডেলের চারপাশের পরিবেশ বা Harness System-কে বুদ্ধিভিত্তিক উপায়ে Optimize করাটা কতটা বৈপ্লবিক পরিবর্তন আনতে পারে।

Recursive Agent Harnessing ভবিষ্যতে Open World-এর নানা জটিল চ্যালেঞ্জ মোকাবিলা করতে প্রযুক্তির দুনিয়াকে বহুদূর এগিয়ে নিয়ে যাবে। আপনি যদি একজন AI Developer বা গবেষক হন, তবে এখনই লোকাল ডেমো সেটআপ করে Harness²-এর দুর্দান্ত কার্যকারিতা পরীক্ষা করে দেখতে পারেন।

আশাকরি আজকের এই বিশাল ও বিস্তারিত গাইডটি থেকে আপনি Harness²-এর প্রতিটি অলিগলি সহজে বুঝতে পেরেছেন। এই প্রযুক্তি নিয়ে আপনার কোনো প্রশ্ন বা মতামত থাকলে অবশ্যই নিচে টিউমেন্ট করে জানান। ধন্যবাদ!
