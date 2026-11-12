---
archive_id: techtunes-649254
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 649254
title: জাভা কিভাবে কাজ করে এবং  জাভা Architecture এর বিভিন্ন কম্পোন্যনন্টসমূহ
slug: programming-649254
language: bn
status: publish
published_at: '2020-04-08T16:00:00+00:00'
modified_at: '2021-09-08T10:17:00+00:00'
original_url: https://www.techtunes.io/programming/tune-id/649254
author: মোহাম্মদ আক্তারুজ্জামান
author_url: https://www.techtunes.io/tuner/coderzaman
categories:
- প্রোগ্রামিং
tags:
- advance java
- Bangla Java tutorial
- জাভা
content_hash: 2f6ae0ec119e4526bf3c9203192cadd54e2511eaf595124fb102824827b17fd9
archived_at: '2026-11-12T12:25:37.244871+00:00'
---

![](https://dnc.techtunes.io/tDrive/tuner/2020/04/techtunes_e146a7e54f2a9a23366c4da1b433c5c0-640x360.png)

**জাভা কিভাবে কাজ করে?**

জাভা কোডকে কম্পাইল করলে সেটি একটি অন্তর্বর্তীকালীন ল্যাংগুয়েজ এ রূপান্তরিত হয়। সেটিকে বাইট কোড বলা হয়। এটি ঠিক হিউম্যান রিডএবল না আবার মেশিন রিডএবলও না। এই বাইটকোড শুধুমাত্র জাভা ভার্চুয়াল মেশিন(JVM) বুঝতে পারে। JVM বাইট কোডকে ইন্টারপ্রেট করে মেশিন ল্যাংগুয়েজ এ রূপান্তরিত করে। এর জন্যে JVM জাস্ট ইন টাইম(JIT) কম্পাইলার ব্যবহার করে।

![](https://dnc.techtunes.io/tDrive/tuner/2020/04/techtunes_f5b3b1ceb78be4d90dd803914dae6e47-640x360.png)

**জাভা Architecture এর বিভিন্ন কম্পোন্যান্টসমূহ:**

**1. JAVA DEVELOPMENT KIT(JDK):**  জাভা ডেভলপমেন্ট কীট(JDK) হচ্ছে এমন একটি সফটওয়্যার ডেভলপমেন্ট ইনভায়রমেন্ট যার সাহায্যে জাভা এবং **অ্যাপলেট অ্যাপলিকেশন** ডেভলপ করা হয়। যেখানে অন্তর্ভূক্ত থাকে **জাভা রান টাইম ইনভায়রমেন্ট(JRE)**, একটি ইন্টারপ্রেটার বা লোডার (যেটি হচ্ছে **জাভা ভার্চুয়াল মেশিন[JVM]**),  **জাভা কম্পাইলার(javac)**, একটি **জাভা আর্কাইভার(jar)**, একটি ডকুমেন্টেশন জেনারেটর**(Java doc)**, জাভা ডেভলেপমেন্ট জন্য প্রয়োজনীয় অন্যান্য টুলস।

**অ্যাপলেট অ্যাপলিকেশন:** অ্যাপলেট হচ্ছে একটি জাভা প্রোগ্রাম যা ওয়েব ব্রাউজারে রান করা হয়ে থাকে। একটি অ্যাপলেট একটি সম্পূর্ণ ফাংশনাল জাভা অ্যাপ্লিকেশন হতে পারে কারণ জাভা API(Application programming interface) সম্পূর্ণভাবে এটি নিয়ন্ত্রণ করে থাকে।

**2. জাভা রান টাইম ইনভায়রমেন্ট(JRE):** জাভা রান-টাইম এনভায়রনমেন্ট (জেআরই) জাভা ডেভলপমেন্ট কিটের (JDK) অংশ। এটি একটি ফ্রি সফ্টওয়্যার যার মধ্যে রয়েছে Java Class Library, specific tools এবং JVM। এটি জাভা সোর্স কোডকে জাভা বাইট কোডে রুপান্তর করে। আপনি যদি কোনও প্ল্যাটফর্মে এই বাইটোকডটি চালাতে চান তবে আপনার জেআরই দরকার। জেআরই ক্লাসগুলি লোড করে, মেমরিতে অ্যাক্সেস যাচাই করে এবং সিস্টেম রিসোর্সগুলো পুনরুদ্ধার করে। জেআরই অপারেটিং সিস্টেমের শীর্ষের একটি লেয়ার হিসেবে কাজ করে। এটি মূলত একটি জাভা প্রোগ্রামকে রান করার জন্য অন্ততপক্ষে যে সব কম্পোন্যান্টগুলো লাগে তার একটি প্যাকেজ।

**2.1: জেআরই এর মধ্যে যা রয়েছে:**

- **Deployment technologies:** such as deployment, Java plug-in, and Java Web Start.
- **User interface toolkits:** including Abstract Window Toolkit (AWT), Swing, Java 2D, Accessibility, Image I/O, Print Service, Sound, drag, and drop (DnD) and input methods.
- **Integration libraries:** including Interface Definition Language (IDL), Java Database Connectivity (JDBC), Java Naming and Directory Interface (JNDI), Remote Method Invocation (RMI), Remote Method Invocation Over Internet Inter-Orb Protocol (RMI-IIOP) and scripting.
- **Other base libraries:** including international support, input/output (I/O), extension mechanism, Beans, Java Management Extensions (JMX), Java Native Interface (JNI), Math, Networking, Override Mechanism, Security, Serialization and Java for XML Processing (XML JAXP).
- **Lang and util base libraries:** including lang and util, zip, Java Archive (JAR), instrument, reflection, Collections, Concurrency Utilities, management, versioning, Logging, Preferences API, Ref Objects and Regular Expressions.
- **Java Virtual Machine (JVM):** which comprise of Server Virtual Machine and Java HotSpot Client.

**2.2: জেআরই কীভাবে জেভিএমের সাথে কাজ করে?**

যখন আমরা কোন প্রোগ্রাম লিখি তখন.java এক্সটেনশন যুক্ত ফাইলে এটিকে সংরক্ষণ করে থাকি। প্রোগ্রামটি কম্পাইল করার পর সোর্স কোডগুলো বাইট কোডে পরিণত হয়, যা কিনা প্লাটফর্ম ইন্ডিফেন্ডেন্ট এবং এর সাথে নতুন একটি.class এক্সটেনশন যুক্ত ফাইল তৈরি হয় যেখানে বাইট কোডগুলো থাকে। বাইট কোডটি প্লাটফর্ম ইন্ডিফেন্ডেন্ট। জেআরই আছে এরকম যেকোন ডিভাইসে একে রান করা যাবে। এখানে জেআরই এর কাজ শুরু হয়। যেকোন জাভা প্রোগ্রাম রান করার জন্য অবশ্যই জেআরই প্রয়োজন। তারপর বাইটকোডটি রান হতে নিচের flow অবলম্বন করে:

![](https://dnc.techtunes.io/tDrive/tuner/2020/04/techtunes_55814ed40c536c6a8315bfdcfda94596-640x360.png)

*Class Loader:* এ ধাপে প্রোগ্রাম চালানোর জন্য ক্লাস লোডার যে ক্লাসগুলো প্রয়োজন হয় সে ক্লাসগুলো লোড করে। এরপর ক্লাস লোডার স্বয়ক্রিয়ভাবে জাভা ভার্চুয়াল মেশিনে ক্লাসগুলো লোড করে।

When the JVM is started, three class loaders are used:

- Bootstrap class loader
- Extensions class loader
- System class loader

*Byte code verifier:* বাইট কোড verifier কে দ্বাররক্ষী হিসাবে বিবেচনা করা যেতে পারে। এখানে বাইটকোড যাচাই করার কারণ হচ্ছে যাতে interpreter এ কোনও ধরনের বিঘ্ন সৃষ্টি না হয়। এটি তখনই ইন্টারপ্রেট করতে পারে যখন Byte code verifier এর সবগুলো ধাপ সফল ভাবে অতিক্রান্ত করতে পারে।

Interpreter: যখন কোডগুলো ভ্যারিফাই হয়ে যায় তখন এই বাইট কোডগুলোকে ইন্টাপ্রেটার এক্সিকিউট করে এবং মেশিন কোডে রুপান্তরিত করে।

**এইভাবে, প্রোগ্রামটি জেআরইতে চলে।**

**3.জাভা ভার্চুয়াল মেশিন[JVM]:** জেভিএম (জাভা ভার্চুয়াল মেশিন) একটি অ্যাবস্ট্রাক মেশিন। এটি একটি সবিস্তার বিবরণী যা রানটাইম এনভাযরমেন্ট সরবরাহ করে এবং এখানে জাভা বাইটকোড এক্সিকিউট করা যায়। জেভিএম অনেকগুলো অপারেটিং সিস্টেমের জন্য আলাদা আলাদাভাবে তৈরি করা হয়েছে। যেমন: উইন্ডোজ, ম্যাক ওএস, লিনাক্স, সোলারিস ইত্যাদি। আমাদের লেখা জাভা প্রোগ্রাম যেকোন অপারেটিং সিস্টেমে রান করা যাবে। এর কারণ জাভা কোড কোন মেশিনকে উদ্দেশ্য করে না লিখে জেভিএমকে উদ্দেশ্য করে লেখা হয়। যেহেতু প্রত্যেক অপারেটিং সিস্টেমের জন্য ভিন্ন ভিন্ন জেভিএম আছে তাই জাভা কোড সব অপারেটিং সিস্টেমে রান করা যায়। তাই এজন্য জাভাকে WORA(Write once, run anywhere) ল্যাংগুয়েজও বলা হয়।

*জেভিএম নিম্নলিখিত ক্রিয়াকলাপ সম্পাদন করে:*

- Loads code
- Verifies code
- Executes code
- Provides runtime environment

*জেভিএম যা সংজ্ঞায়িত করে:*

- Memory area
- Class file format
- Register set
- Garbage-collected heap
- Fatal error reporting etc.

*জেভিএম আর্কিটেকচার:* এবার জেভিএম এর অভ্যন্তরীন আর্কিটেকচার সম্পর্কে জানা যাক। এটিতে ক্লাসলোডার, মেমরি এরিয়া, এক্সিকিউশন ইঞ্জিন ইত্যাদি

রয়েছে।

![](https://dnc.techtunes.io/tDrive/tuner/2020/04/techtunes_a7866af7976c24a174c269c0626dbb71-640x360.jpg)

1.Classloader: ক্লাসলোডার জেভিএমের একটি সাবসিস্টেম যা ক্লাস ফাইল লোড করতে ব্যবহৃত হয়। যখনই আমরা জাভা প্রোগ্রামটি চালাই, এটি ক্লাসলোডার দ্বারা প্রথমে লোড করা হয়। জাভাতে তিনটি অন্তর্নির্মিত ক্লাসলোডার রয়েছে।

- Bootstrap ClassLoader: This is the first classloader which is the super class of Extension classloader. It loads the rt.jar file which contains all class files of Java Standard Edition like java.lang package classes, java.net package classes, java.util package classes, java.io package classes, java.sql package classes etc.
- Extension ClassLoader: This is the child classloader of Bootstrap and parent classloader of System classloader. It loads the jar files located inside $JAVA\_HOME/jre/lib/ext directory.
- System/Application ClassLoader: This is the child classloader of the Extension classloader. It loads the class files from classpath. By default, classpath is set to the current directory. You can change the classpath using "-cp" or "-classpath" switch. It is also known as the Application classloader.

এগুলি জাভা দ্বারা সরবরাহ করা অভ্যন্তরীণ ক্লাসলোডার। আপনি যদি নিজের(ইউজার ডিফাইন) ক্লাসলোডার তৈরি করতে চান তবে আপনাকে ক্লাসলোডার ক্লাসকে এক্সটেন্ড করতে হবে।

2.Class(Method) Area: Class(Method) Area প্রতি ক্লাসের স্ট্রাকচার স্টোর করে রাখে। যেমন: runtime constant pool, field and method data, মেথডের জন্য কোড।

3.Heap:  এটি রানটাইম ডেটা এরিয়া, যেখানে অবজেক্টগুলি allocated করা হয়।

4.Stack: জাভা স্ট্যাক ফ্রেম স্টোর করে। এটি লোকাল ভেরিয়েবল ধারণ করে থাকে। প্রতিটি থ্রেডের একটি প্রাইভেট জেভিএম স্ট্যাক থাকে, যা থ্রেড হিসাবে একই সময়ে তৈরি করা হয়। প্রত্যেকবার একটি মেথড কল করা হলে একটি নতুন ফ্রেম তৈরি করা হয়। কোনও ফ্রেম নষ্ট হয়ে যায় যখন এর মেথডের invocation সম্পূর্ণ হয়।

5.Program and Counter Register: পিসি (প্রোগ্রামের কাউন্টার) রেজিস্টারটিতে বর্তমানে executed হওয়া জাভা ভার্চুয়াল মেশিনের instruction address থাকে।

6. Native method stack: এতে অ্যাপ্লিকেশনটিতে ব্যবহৃত সমস্ত নেটিভ method রয়েছে।

7. Execution Engine: এতে রয়েছে

- A virtual processor
- Interpreter: বাইট কোড স্ট্রিম পড়ে এবং ইন্সট্রাকশনগুলো এক্সিকিউট করে।
- Just-In-Time(JIT) compiler:  বাইট কোডকে এক্সিকিউট করার জন্য জাভা ভার্চুয়াল মেশিন JIT Compiler ব্যবহার করে। JIT বাইট কোডকে সরাসরি ইন্টারপ্রেট করে এবং মেশিন কোডে রুপান্তর করে যা সিপিউ রান করে।

8. Java Native Interface: জাভা নেটিভ ইন্টারফেস (জেএনআই) এমন ইন্টারফেইস যা সি, সি +, এসেম্বলি ইত্যাদিতে লেখা অ্যাপলিকেশনগুলার সাথে কমিউনিকেট করতে সাহায্য করে। কনসোলে আউটপুট প্রেরণ করতে বা ওএস লাইব্রেরির সাথে ইন্টারেক্ট করতেও জাভা জেএনআই ইন্টারফেস ব্যবহার করা হয়।

**4. জাভা কম্পাইলার(javac):**  javac হ'ল ওরাকল কর্পোরেশন থেকে জাভা ডেভেলপমেন্ট কিট (জেডিকে) এর অন্তর্ভুক্ত জাভা কম্পাইলার। যা প্রথমে জাভা ভাষায় লিখিত প্রোগ্রামকে বাইট কোডে রুপান্তর করে। তারপর বাইটকোডের স্পেসিপিকেশন মেনে মেশিন কোড তৈরি করে। জাভাতে দুই ধরনের কম্পাইলার রয়েছে:

- Javac: জাভাক জাভা প্রোগ্রামে লিখা কোডকে মেশিন ইন্ডিফেন্ডেন্ট বাইট কোডে রুপান্তর করে।
- JIT Compiler জাভা RE ভিতরে চলে যা বাইট কোড সমূহকে মেশিন কোডে রুপান্তর করে।

**5.জাভা আর্কাইভার(jar):** JAR (Java Archive) হ'ল একটি প্যাকেজ ফাইল ফর্ম্যাট যা সাধারণত অনেক জাভা ক্লাস ফাইল, সম্পর্কিত মেটাডেটা এবং রিসোর্সসমূহকে(text, images, ইত্যাদিকে) ডিস্ট্রিবিউশনের জন্য একটি ফাইলে একত্রিত করতে ব্যবহৃত হয়।

**6. ডকুমেন্টেশন জেনারেটর(Java doc):** জাভাডক টুল হল জাভা প্রোগ্রামিং ল্যাংগুয়েজের একটি ডকোমেন্টেশন জেনারেটর টুল। যা এইচটিএমএল ফর্ম্যাটে স্ট্যান্ডার্ড ডকুমেন্টেশন তৈরি করে। এটি এপিআই(API) ডকুমেন্টেশন জেনারেট করে।

জাভাডক ব্যবাহারের আগে অবশ্যই জাভাডক টিউমেন্টে class, method এবং constructor ইত্যাদির বিবরণ দিতে হবে।  একটি ভাল এবং বোধগম্য ডকোমেন্ট API তৈরি করার জন্য প্রত্যেক জাভা ফাইলের টিউমেন্টে -এ class, method and constructor এর উপযুক্ত বিবরণ দিতে হবে।

![](https://dnc.techtunes.io/tDrive/tuner/2020/04/techtunes_ff74f6febc6bd19463f863e68e636030-640x360.png)

JavaDoc Tags

1. TAG: @author. PARAMETER: author\_name. DESCRIPTION: Describes an author

2.TAG: @param. PARAMETER: description DESCRIPTION: provide information about the method parameter or the input it takes.

3.TAG: @see. PARAMETER: reference. DESCRIPTION: generate a link to other elements of the document

4.TAG: @version. PARAMETER: version-name. DESCRIPTION: provide a version of the class, interface or enum.

5.TAG: @return. PARAMETER: description. DESCRIPTION: provide the return value
