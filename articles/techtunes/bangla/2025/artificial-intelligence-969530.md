---
archive_id: techtunes-969530
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 969530
title: GPT-Engineer – আপনার আর্টিফিশিয়াল ইন্টেলিজেন্স ভিত্তিক কোডিং পার্টনার
slug: artificial-intelligence-969530
language: bn
status: publish
published_at: '2025-02-24T03:45:00+00:00'
modified_at: '2025-02-23T03:47:00+00:00'
original_url: https://www.techtunes.io/artificial-intelligence/tune-id/969530
author: সোহানুর রহমান
author_url: https://www.techtunes.io/tuner/sohanur-raihan
categories:
- আর্টিফিশিয়াল ইন্টেলিজেন্স (এআই)
tags:
- Tips টিপস
- ওয়েব প্রোগ্রামিং
- কোডিং
content_hash: 84ce94a2304a8badc8748c25a50c13bbf00c8bee5f607e201a2852155a3aea44
archived_at: '2026-11-12T12:04:53.295052+00:00'
---

আসসালামু আলাইকুম, কেমন আছেন টেকটিউনস কমিউনিটি? আশা করছি সবাই ভাল আছেন। আজকে আবার হাজির হলাম নতুন টিউন নিয়ে।

## GPT-Engineer কী?

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_f89615bf9406ca614c866f8f67cf796f.png)

কেমন হবে যদি আপনার একটি কোডিং পার্টনার থাকে যে কখনো ক্লান্ত হবে না, ঘণ্টার পর ঘণ্টা কাজ করবে একটি সিঙ্গেল প্রেজেক্ট ডেসক্রিপশনে একটি পুরো কোডবেস জেনারেট করে দেবে? নিঃসন্দেহে চমৎকার হবে। আর আর অভিপ্রায়ে তৈরি করা হয়েছে নতুন আর্টিফিশিয়াল ইন্টেলিজেন্স প্রজেক্ট GPT-Engineer। এটি উদীয়মান AI পাওয়ারড কোডার গুলোর মধ্যে একটি। এটি GPT ব্যবহার করে এপ্লিকেশন বিল্ড করবে। Anton Osika, দ্বারা ডেভেলপ করা GPT-Engineer হতে পারে AI এসিস্ট্যান্ট ডেভেলপমেন্টের গেম চেঞ্জার।

GPT-Engineer এটি শুধু মাত্র একটি AI টুলই নয় বরং এটি আপনার কোডিং এসিস্ট্যান্ট। হোক সিম্পল কোন অ্যাপ অথবা কমপ্লেক্স কোন গেম, GPT-Engineer আপনাকে সাহায্য করতে পারে। এটি আপনার পাশে একজন জুনিয়র ইঞ্জিনিয়ার হিসেবে থাকবে, পুরো প্রজেক্ট রিকুয়ারমেন্ট বুঝার জন্য বিভিন্ন প্রশ্ন করবে।

### GPT-Engineer

গিটহাব রিপু @ [GPT-Engineer](https://github.com/AntonOsika/gpt-engineer)

## GPT-Engineer কীভাবে ব্যবহার করবেন?

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_29c2b33b469d10934fad87f4430d5408.jpeg)

কোডিং এর মধ্যে GPT-Engineer কে ব্যবহার করতে প্রথমে আপনাকে এটি ইন্সটল করে নিতে হবে। এটা করতে প্রথমে GPT-Engineer রিপুটি গিটগাব পেজ থেকে ক্লোন করে নিন। এর পর Python রিসেন্ট ভার্সন দিয়ে নতুন একটি এনভায়রনমেন্ট ক্রিয়েট করুন এবং প্রয়োজনীয় মডিউল ইন্সটল করুন। বিস্তারিত জানতে এই [পেজটি](https://github.com/AntonOsika/gpt-engineer) ভিজিট করতে পারেন।

### Design Documentation Prompts এর জন্য GPT-4 ব্যবহার করা

GPT-Engineer কে দিয়ে কাজ করাতে প্রথমে আমাদের Design Documentation তৈরি করে নিতে হবে। চলুন GPT-4 দিয়েই Design Documentation তৈরি করে নিই।

প্রথমে ডিজাইন ডকুমেন্টেশন তৈরি করে নেয়ার সুবিধা হচ্ছে, GPT-Engineer অ্যাপ তৈরি করার সব ইনফরমেশন পেয়ে যাবে। অ্যাপটি কেমন হবে সেটার সম্পর্কে পরিষ্কার ধারণা পাবে।

চলুন প্রথমে GPT-4 দিয়ে একটি ডিজাইন ডকুমেন্টেশনে তৈরি করি, এর জন্য নিচের মত prompt দিব।

I want to implement a game of snake in Python, using the game's classic rules and gameplay. It can use external libraries to accomplish this. Generate a design document for this project.

Prompt টি দেবার পর GPT-4 নিচের মত একটি আউটপুট আমাদের দেবে যা আমরা GPT-Engineer এ ব্যবহার করব। চলুন কিছু অংশ দেখে নিই,

Introduction  
 The purpose of this design document is to outline the implementation details for creating a classic Snake game in Python. The game will adhere to the traditional rules and gameplay, where the player controls a snake that grows in length by eating food while avoiding collisions with itself and the game boundaries. The game will be developed using external libraries to facilitate graphics and user input.

Game Components  
 The Snake game will consist of the following components:  
 a) Snake: A movable object that grows in length when it eats food and loses the game if it collides with itself or the game boundaries.  
 b) Food: A randomly placed object that the snake can eat to increase its length and score.

তো আমাদের এখন একটি ডিজাইন ডকুমেন্টস রয়েছে যা আমরা GPT-Engineer এ ব্যবহার করতে পারব।

### ChatGPT দিয়ে Design Document তৈরি

GPT-Engineer সেরা হল এর বহুমুখিতার জন্য। আপনি এটি দিয়ে সিম্পল একটি স্নেক গেম ও তৈরি করতে পারেন অথবা শুধুমাত্র Python এর স্ট্যান্ডার্ড লাইব্রেরী মডিউল ব্যবহার করে, সিম্পল কী ভ্যালু ডাটাবেস এর মত অসংখ্য অ্যাপ তৈরি করতে পারবেন। শুধুমাত্র main.prompt ফাইলে আপনার ডেসক্রিপশনটি দিন, GPT-Engineer যা যা প্রয়োজন সব কিছু আপনার জিজ্ঞেস করবে। সব ডিটেল দেয়ার পর শান্ত হয়ে বসুন GPT-Engineer আপনার কোডবেস জেনারেট করে দেবে।

প্রথমে আমরা ChatGPT-4 দিয়ে একটি ডিজাইন ডকুমেন্ট তৈরি করে নেব। এটা তৈরি করতে সব সময় ChatGPT ই ব্যবহার করতে হবে এমন নয়। আপনার কাছে অ্যাপটি নিয়ে বিস্তারিত ডেসক্রিপশন থাকলেও চলবে। সাজানো গুছানো ডেসক্রিপশন তৈরি করতে ChatGPT-4 ব্যবহার করাই ভাল।

ChatGPT-4 দিয়ে ডিজাইন ডকুমেন্ট তৈরি করার Prompt হতে পারে,

Generate a high quality design document that can be used by our project team to design the software described below. It should be complete and usable as the sole design documentation to get our team to complete our project.

-  
 Simple key-value database engine written in Python using only standard library modules (except those mentioned below).

The basic interaction with the database engine when it is running should be via imported Python module with a clear and concise library API.

There should also be a separate console that can be run to act as a command line REPL for interacting with the database engine and databases.

Additional methods of interaction should include an API created with Fast API (external library).

Design specifications:

A key-value database is a type of NoSQL database that stores data as a collection of key-value pairs. Unlike traditional relational databases, key-value databases do not enforce a rigid schema, providing flexibility and scalability for certain use cases. Designing a key-value database involves considering several important specifications.

Commands that should be accessible:  
 - connect to database  
 - delete database  
 - get key  
 - insert data  
 - update data  
 - delete data  
 - search for existence of both keys and values

Data Model: Each record consists of a unique key and an associated value. The value can be a simple scalar value or a complex data structure (such as JSON or XML).

Key Structure: The key serves as the primary identifier for each data entry and must be unique within the database. Keys can be alphanumeric strings, integers, or even composite keys (multiple values combined to form a single key).

Value Structure: The value associated with each key can be of any data type. It can range from basic data types (strings, numbers, booleans) to more complex structures like nested objects or arrays.

Performance and Caching: In-memory caching techniques should be employed to speed up read operations and reduce latency.

![](https://dnc.techtunes.io/tDrive/tuner/2023/07/techtunes_cdf71977f3af48d1317d56adbd1d0e21.png)

ChatGPT-4 এর তৈরি ডিজাইন ডকুমেন্ট

# Overview  
 The main goal of this project is to design and develop a lightweight key-value database engine written in Python, using only standard library modules, and FastAPI for the HTTP interface. The application will provide the essential features of a key-value database, including connecting to the database, data insertion, update, deletion, and retrieval, along with search functionality for keys and values.

The database will be interfaced via three methods:  
 1. A Python module that can be imported by other Python programs.  
 2. A command line REPL console for manual interaction.  
 3. An API created with FastAPI for remote interactions.

# Components  
 The database engine will have the following main components:

1. \*Data Store\*: The actual storage for the key-value pairs. As a simple Python implementation, this could be a dictionary where keys are unique identifiers and values can be of any datatype. The data store should have efficient methods for accessing, adding, updating, and deleting data.  
 2. \*Database Engine\*: The engine that provides the methods to interact with the data store. This will include methods to connect to a database, insert, update, and delete data, as well as fetch a value by key. It should also include a method to check the existence of a particular key or value in the data store.  
 3. \*In-Memory Cache\*: A cache layer that holds frequently accessed data to improve read speed and reduce latency. This can be implemented using Python's `functools.lru\_cache` decorator or a custom caching solution.  
 4. \*CLI\*: A command-line interface for manual interaction with the database engine. This would use the `cmd` or `argparse` module from the Python standard library to create a REPL interface.  
 5. \*HTTP API\*: A FastAPI application that exposes the database engine methods as a HTTP API. This will allow remote interaction with the database.

# Data Model  
 The database engine will follow a simple key-value data model. Each record in the database will consist of a unique key and an associated value.

# Key Structure  
 Keys can be alphanumeric strings, integers, or composite keys. They must be unique within the database and will serve as the primary identifier for each data entry.

# Value Structure  
 The value associated with each key can be of any Python data type. It can range from basic data types (strings, numbers, booleans) to more complex structures like nested objects or arrays.

# API Design  
 The Python library API, CLI, and FastAPI should provide the following functions:  
 - `connect(database\_name: str)`: Connect to a database. Creates the database if it does not exist.  
 - `delete\_database(database\_name: str)`: Deletes a database.  
 - `insert(key: str, value: Any)`: Inserts a new key-value pair into the database.  
 - `update(key: str, value: Any)`: Updates the value of an existing key.  
 - `delete(key: str)`: Deletes a key-value pair from the database.  
 - `get(key: str)`: Fetches the value of a key from the database.  
 - `exists\_key(key: str)`: Checks if a key exists in the database.  
 - `exists\_value(value: Any)`: Checks if a value exists in the database.

# Performance and Caching  
 In-memory caching techniques will be employed to speed up read operations and reduce latency. The `functools.lru\_cache` decorator or a custom caching solution could be used for this purpose. The cache should have a maximum size to prevent excessive memory usage.

# Conclusion  
 This document provides a high-level design for a simple key-value database engine using Python and FastAPI. By adhering to this design, we can ensure that the database will be flexible and scalable, meeting the needs of various applications.

এখন GPT-Engineer রান করুন এবং প্রয়োজনীয় দিক নির্দেশনা দিন।

## শেষ কথা

বলাই যায় GPT-Engineer শুধুমাত্র একটি টুল নয়, এটি AI, LLM এর ক্ষমতার শক্তিশালী প্রমাণ হতে পারে অথবা হতে পারে কোডিং ভবিষ্যতের একটি আভাস। আপনি জেনারেট করা কোডে কোন ইস্যু পেলে সেটা ফিক্স করতে ChatGPT Code Generator প্লাগ-ইন ব্যবহার করতে পারেন।

তো আজকে এই পর্যন্তই পরবর্তী টিউন পর্যন্ত ভাল থাকুন আল্লাহ হাফেজ।
