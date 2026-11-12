---
archive_id: techtunes-969171
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 969171
title: ChatGPT ও Bard এর মত AI তৈরি করার ৮ টি ওপেনসোর্স Framework
slug: artificial-intelligence-969171
language: bn
status: publish
published_at: '2024-05-27T07:19:00+00:00'
modified_at: '2024-04-30T15:23:00+00:00'
original_url: https://www.techtunes.io/artificial-intelligence/tune-id/969171
author: সোহানুর রহমান
author_url: https://www.techtunes.io/tuner/sohanur-raihan
categories:
- আর্টিফিশিয়াল ইন্টেলিজেন্স (এআই)
tags:
- Open Source. ওপেন সোর্স
- Tips টিপস
- আর্টিফিসিয়াল ইন্টিলিজেন্স
content_hash: ef46fdbdb465e654b7a04ce881df9249186e78f72416025e9d226d406b69e483
archived_at: '2026-11-12T12:04:53.658640+00:00'
---

আসসালামু আলাইকুম, কেমন আছেন টেকটিউনস কমিউনিটি? আশা করছি সবাই ভাল আছেন। আজকে আবার হাজির হলাম নতুন টিউন নিয়ে।

ChatGPT একটি LLM এবং Framework এর উপর তৈরি করা এটি আমরা সবাই জানি। আজকের এই টিউনে আমরা আটটি ওপেন সোর্স Framework এবং মডেল আপনাদের সাথে পরিচয় করিয়ে দেব যেগুলো ব্যবহার করে আপনি নিজের চ্যাটবট বা AI প্রোডাক্ট তৈরি করতে পারবেন।

## ১. LLaMA

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_d20c2cff224c71b6640f8edeaf9473e5.png)

LLaMA প্রজেক্ট ফান্ডামেন্টাল ল্যাংগুয়েজ মডেলের উপর ভিত্তি করে তৈরি করা। যার রয়েছে ৭ বিলিয়ন থেকে ৬৫ বিলিয়ন প্যারামিটার। এই মডেল গুলোকে মিলিয়ন এর মত টোকেন এবং পাবলিক এভেইলেবল ডেটাসেটের উপর ট্রেনিং করানো হয়েছে। ফলাফল সরূপ, LLaMA-13B, GPT-3 (175B) কে ছাড়িয়ে গেছে এবং LLaMA-65B, Chinchilla-70B এবং PaLM-540B এর মত মডেল গুলোর মত পারফরম্যান্স দেখাতে পারে।

GitHub: [facebookresearch/llama](https://github.com/facebookresearch/llama)

Demo: [Baize Lora 7B](https://huggingface.co/spaces/project-baize/baize-lora-7B)

## ২. Alpaca

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_5352b7cdc8ca89c04e2e85e1b89113f2.png)

Stanford Alpaca দাবী করে তারা ChatGPT এর সাথে প্রতিদ্বন্দ্বিতা করতে পারে এবং যেকেউ চাইলে ৬০০ ডলারেরও কমে নিজস্ব ChatGPT তৈরি করে ফেলতে পারবে। Alpaca 7B কে ৫২ হাজার ইন্সট্রাকশনের ভিত্তিতে LLaMA 7B মডেল থেকে ফাইনটিউন করা হয়েছে।

GitHub: [tatsu-lab/stanford\_alpaca](https://github.com/tatsu-lab/stanford_alpaca)

Demo: [Alpaca-LoRA](https://huggingface.co/spaces/tloen/alpaca-lora)

## ৩. Vicuna

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_dd5eebad1231f722ae67c67f25d7cbe2.png)

Vicuna কে ShareGPT থেকে কালেক্ট করা ইউজার শেয়ারড কনভারসেশনের ভিত্তিতে, LLaMA মডেল থেকে ফাইনটিউনড করা হয়েছে। Vicuna-13B ইতিমধ্যে OpenAI এর ChatGPT এবং Google Bard থেকে ৯০% কোয়ালিটি দক্ষতা অর্জন করেছে। এটি প্রায় ৯০% ক্ষেত্রে LLaMA এবং Stanford Alpaca মডেলকে ছাড়িয়ে গেছে। Vicuna কে ট্রেনিং করাতে খরচ হয়েছে প্রায় ৩০০ ডলারের মত।

GitHub: [lm-sys/FastChat](https://github.com/lm-sys/FastChat#fine-tuning)

Demo: [FastChat (lmsys.org)](https://chat.lmsys.org/)

## ৪. OpenChatKit

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_47c8b7373045dad808de906da9273fd1.png)

OpenChatKit একটি ওপেনসোর্স ChatGPT অলটারনেটিভ কমপ্লিট টুলকিট যা দিয়ে আপনি নিজের চ্যাটবট তৈরি করে ফেলতে পারবেন। এটি আপনার মডেলকে ট্রেইন করা এবং ফাইন টিউন করার ইন্সট্রাকশন দেবে। সর্বোপরি চ্যাটবট তৈরিতে সাহায্য করবে OpenChatKit। GPT-NeoXT-Chat-Base-20B মডেল ইতিমধ্যে মধ্যে প্রশ্ন-উত্তরের দিক থেকে GPT-NoeX কেও ছাড়িয়ে গেছে।

GitHub: [togethercomputer/OpenChatKit](https://github.com/togethercomputer/OpenChatKit)

Demo: [OpenChatKit](https://huggingface.co/spaces/togethercomputer/OpenChatKit)

Model card: [togethercomputer/GPT-NeoXT-Chat-Base-20B](https://huggingface.co/togethercomputer/GPT-NeoXT-Chat-Base-20B)

## ৫. GPT4ALL

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_5d3a5967cfc47b17d3ab86f182ace26d.png)

GPT4ALL একটি কমিউনিটি ড্রাইভেন প্রজেক্ট যাকে ম্যাসিভ ডেটা যেমন কোড, এসিস্ট্যান্ট ইন্টারেকশন, স্টোরি ইত্যাদির উপর ট্রেইন করা হয়েছে। এই মডেলটির টিম তাদের ডেটাসেট, মডেলের পরিমাণ, ডেটা কিউরেশন প্রসেস, ট্রেনিং কোড সব কিছু ওপেন সোর্সে দিয়েছে। তারা এই মডেলের একটি ৪ বিট ভার্সনও রিলিজ করেছে যা আপনি ল্যাপটপে রান করতে পারবেন। আপনি চাইলে Python ক্লাইন্টেও এই মডেল রান করতে পারবেন।

GitHub: [nomic-ai/gpt4al](https://github.com/nomic-ai/gpt4all)

Demo: [GPT4All](https://huggingface.co/spaces/rishiraj/GPT4All)

Model card: [nomic-ai/gpt4all-lora · Hugging Face](https://huggingface.co/nomic-ai/gpt4all-lora)

## ৬. Raven RWKV

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_2e7b6e01f2585f292f7b187aa24a21c4.png)

RWKV ল্যাংগুয়েজ মডেল দ্বারা তৈরি Raven RWKV 7B একটি ওপেন সোর্স চ্যাটবট যা ChatGPT এর মত রেজাল্ট দিতে পারে। এই মডেলটি RNN ইউজ করে যা কোয়ালিটি এবং স্ক্যালিং এর দিক থেকে Transformer গুলোর এর সাথে ম্যাচ করে এবং এতে প্রচুর VRAM সেভ হয়। Raven, কে Stanford Alpaca, code-alpaca, সহ আরও অনেক ডেটাসেট থেকে ফাইনটিউন করা হয়েছে।

GitHub: [BlinkDL/ChatRWKV](https://github.com/BlinkDL/ChatRWKV)

Demo: [Raven RWKV 7B](https://huggingface.co/spaces/BlinkDL/Raven-RWKV-7B)

Model card: [BlinkDL/rwkv-4-raven](https://huggingface.co/BlinkDL/rwkv-4-raven)

## ৭. OPT

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_f2927f7d651a1177add4c990fd7a26df.png)

OPT বা Open Pre-trained Transformer ল্যাংগুয়েজ মডেল ChatGPT থেকে সেরা এমনটি বলা যাবে না তবে Stereotypical Bias এনালাইসিসের ক্ষেত্রে এটি দারুণ পারফরম্যান্স দেখিয়েছে। আরও সেরা ফলাফল পেতে আপনি এটার সাথে Alpa, Colossal-AI, CTranslate2, এবং FasterTransformer ইন্টেগ্রেট করতে পারেন।

এটি এই লিস্টে কারণ টেক্সট জেনারেশন ক্যাটাগরিতে এর মাসিক ডাউনলোড ৬২৪৭১০ এর মত।

GitHub: [facebookresearch/metaseq](https://github.com/facebookresearch/metaseq)

Demo: [A Watermark for LLMs](https://huggingface.co/spaces/tomg-group-umd/lm-watermarking)

Model card: [facebook/opt-1.3b](https://huggingface.co/facebook/opt-1.3b)

## ৮. Flan-T5-XXL

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_468e6e69050be35da65a77eabd328d44.png)

Flan-T5-XXL একটি ফাইনটিউন T5 মডেল। এখানে এক ধরনের ইন্সট্রাকশন ভিত্তিক ফাইন টিউন করা হয়েছে। এই ধরনের ইন্সট্রাকশন ফাইন টিউনিং PaLM, T5, এবং U-PaLM এর মত বিভিন্ন মডেলের পারফরম্যান্স নাটকীয় ভাবে বৃদ্ধি করেছে। এছাড়াও Flan-T5-XXL মডেলকে আরও ১০০০ টিরও বেশি অতিরিক্ত টাস্কে ফাইন টিউন করা হয়েছে যা এর কার্যক্ষমতা আরও বাড়িয়েছে।

GitHub: [google-research/t5x](https://github.com/google-research/t5x)

Demo: [Chat Llm Streaming](https://huggingface.co/spaces/olivierdehaene/chat-llm-streaming)

Model card: [google/flan-t5-xxl](https://huggingface.co/google/flan-t5-xxl?text=Q%3A+%28+False+or+not+False+or+False+%29+is%3F+A%3A+Let%27s+think+step+by+step)

## শেষ কথা

ইন্টারনেটে এমন অনেক ওপেন সোর্স অপশন এভেইলেবল রয়েছে আমি সেরা কয়েকটা তুলে ধরার চেষ্টা করলাম। এই ওপেনসোর্স চ্যাটবট বা মডেল গুলো আগামী কয়েক মাসের মধ্যে আরও দুর্দান্ত হয়ে উঠবে তখন হয়তো এটি পারফরম্যান্স এর দিক থেকে ChatGPT কেও পেছনে ফেলে দিতে পারে।

তো আজকে এই পর্যন্তই পরবর্তী টিউন পর্যন্ত ভাল থাকুন আল্লাহ হাফেজ।
