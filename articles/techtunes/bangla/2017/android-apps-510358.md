---
archive_id: techtunes-510358
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 510358
title: '[root] Amplify দিয়ে ব্যাটারির ড্রেইন কমান [xposed]'
slug: android-apps-510358
language: bn
status: publish
published_at: '2017-08-20T16:16:00+00:00'
modified_at: '2017-08-21T05:50:00+00:00'
original_url: https://www.techtunes.io/android-apps/tune-id/510358
author: আয়মান শিহাব
author_url: https://www.techtunes.io/tuner/us71r1i
categories:
- অ্যান্ড্রয়েড Apps
tags:
- Android
- Root
- xposed
content_hash: f2140e9e29cc8bae01dcf585af06b94a922ac4ec2f7afc537bf147bcdf0b9061
archived_at: '2026-11-12T12:41:06.524813+00:00'
---

এন্ড্রয়েডে ব্যাটারি যেন জাতীয় সমস্যা,যেন লেগেই থাকে। অনেকেই বলেন,দামী ফোন কিনেও শান্তি নাই-ব্যাটারি আগের মত ব্যাকাপ দেয় না। এজন্য বার বার ফোন ফ্ল্যাশ ও দিয়ে থাকেন ! Well,সমস্যা টা গুরুতর হলেও এর সমাধান অসম্ভব নয়। এজন্য দরকার ছোট একটু ট্রিক্স।

## ব্যাটারি ড্রেইনিং কি?

সোজা কথায়,ব্যাটারির চার্জ খুব দ্রুত হারে কমা।মানে আপনি হটাত মোবাইল টা নিলেন,আর দেখলেন যে ৫ মিনিটের মাথায় ৩% শেষ! তখন মেজাজ কি আর ঠিক থাকে? আসলে ড্রেইনিং প্রায় সব মোবাইল এই হয়। তবে তা লিমিটের মধ্যে থাকে বলে বোঝা যায় না। আর আমাদের দেশি walton,symphony তে এগুলা হারে হারে টের পাওয়া যায়  😆

## ড্রেইনিং এর মুল কারণ

ড্রেইনিং এর মুল কারণ হল background এ এপস চালু থাকা। মানে? বুঝি নাই

আরে,ধরুন আপনি আপনার এক বন্ধু কে বললেন যে বাইরে রাস্তা থেকে কালো বিড়াল ধরে আনতে,আপনার বন্ধু ঘন্টার পর ঘন্টা দারিয়ে থেকে বিড়াল ধরে আনল  ![:mrgreen:](https://dnc.techtunes.io/wp-includes/images/smilies/mrgreen.png) এটায় যে পরিশ্রম হয়েছে তা বলার অপেক্ষা রাখে না। তো আপনার ফোন কি করে? সেও আপনাকে নোটিফিকেশন দেওয়ার জন্য ঘন্টার পর ঘন্টা ব্যাকগ্রাউন্ড এ এক্টিভ থাকে।এতে, চার্জ কার খরচ করে ? আমার না আপনার?

## **কেন Amplify?**

গুগোল প্লেস্টোরে এই background সমস্যার মানে ব্যাটারি সমস্যার জন্য অনেক বেশি এপস আছে। সত্য কথা বলতে গেলে,এগুলার মধ্যে ৯৯ ভাগ ই আপনাকে সত্যিকার অর্থে আগের মত ব্যাটারি দিতে পারবে না। কারণ এরা নিজেরাই ব্যাকগ্রাউন্ড এ এপস থামাতে থামাতে নিজেরাই ব্যাকগ্রাউন্ড এ থাকে  😛 মানে আপনি ওজন কমানোর জন্য ১ ঘন্টা হেটে,পিপাসায় কাতর হয়ে ১ লিটার পেপসি খেলেন  ![:mrgreen:](https://dnc.techtunes.io/wp-includes/images/smilies/mrgreen.png)

amplify এপ টা মুলত এই কাজটাই করে,তবে একটু ভিন্ন ভাবে। এটি এপের যে ব্যাকগ্রাউন্ড এর এলেমেন্টস গুলা কে টাইম অনুযায়ী সেট করে দেয়,মানে আগে অটোমেটিক এত সময় পর এপ ব্যাকগ্রাউন্ড এ এক্টিভ থাকত,এখন তার চায়ে অনেক পরে থাকবে। আর এর সবচেয়ে বড় সুবিধা হল,কয়েক ঘন্টা মোবাইল কে ফেলে রাখলেও প্রায় অনেক সময় ব্যাটারি চার্জ খরচ করে না,প্রায় সেম ই থাকে।

![](https://dnc.techtunes.io/tDrive/tuner/us71r1i/510358/1.png)

এখানে,মোবাইল টা প্রায় সাড়ে ৬ ঘন্টার মত পরে ছিল, ওয়াইফাই এবং বাকি এপস ও চালু ছিল। কিন্তু বিন্দু মাত্র চার্জ খরচ হয় নাই বললেই চলে।

## **Amplify Install**

প্রথমেই বলে নেই, এই এপস টা একটা xposed module. তাই আপনাকে রুট করতেই হবে। রুট করতে না চাইলে পরের অংশ আপনার জন্য না।সরি ! আর রুট user হইলে আসেন,সিস্টাম টা শিখায়া দেই

প্রথমে xposed install করতে হবে। 4.0-4.4 পর্যন্ত user হলে [এখানে](http://dl-xda.xposed.info/modules/de.robv.android.xposed.installer_v33_36570c.apk) ক্লিক করে install করুন।

5.0-6.0 পর্যন্ত হলে [এখানে](https://forum.xda-developers.com/attachment.php?attachmentid=3383776&d=1435601440) আর [এখানে](https://forum.xda-developers.com/attachment.php?attachmentid=3921508&d=1477916609) ডাউনলোড দিয়ে ইনস্টল দিন। 5.0-6.0 এর জিপ ফাইল টা রেকোভারি দিয়ে ফ্ল্যাশ করুন এরপর [এখান থেকে](https://userscloud.com/6777lrmew0w2) amplify এর pro এপস টা ডাউনলোড দিয়ে,ইনস্টল দিন। এরপর xposed এর modules এ গিয়ে amplify এ টিক দিয়ে মোবাইল টা একবার রিবুট দিন। রিবুট এর পর amplify তে ঢুকুন। আর এখন শুরু হবে মেইন কাজ !  ![:mrgreen:](https://dnc.techtunes.io/wp-includes/images/smilies/mrgreen.png)

নিচের লেখা গুলো থেকে alarms,wakelocks আর services অনুযায়ী cataegory তে গিয়ে,লেখা গুলা serch দিন। যেমন,wakelock এ গিয়ে \*net\_scheduler\* লিখে সার্চ দিন (সম্পূর্ণ লেখা লাগবে না,শুধু net লেখলেই এসে পরবে) সেখানে ভিতরে গিয়ে অফ কে অন করে 10800 বসিয়ে দিন (একেক টার একেক রকম সময় হয়) আর services এর ক্ষেত্রে এরকম সার্চ দিয়ে ডেনি দিলেই হবে।

**বিঃদ্রঃ যদি কোনটা ফাইল সার্চ দেওয়ার পর ও না পাওয়া যায়,তখন সেটা বাদ দিলেও চলে।**

তাহলে, শুরু করা যাক

Alarms

**Alarms(Allow every 600 seconds)**

- com.android.internal.telephony.data-stall

**Alarms(Allow every 1800 seconds)**

- com.oasisfeng.greenify.CLEAN\_NOW

**Alarms(Allow every 3600 seconds)**

- android.appwidget.action.APPWIDGET\_UPDATE

**Alarms(Allow every 7200 seconds)**

- android.content.syncmanager.SYNC\_ALARM(delays sync)

**Alarms(Allow every 10800 seconds)**

- android.net.ConnectivityService.action.PKT\_CNT\_SAM PLE\_INTERVAL\_ELAPSED
- com.facebook.common.executors.WakingExecutorServic e.ACTION.ALARM.com.facebook.katana
- com.google.android.apps.hangouts.CLEANUP\_DB
- com.pushbullet.android/.gcm.GcmFixReceiver
- com.android.server.action.NETWORK\_STATS\_POLL
- com.diune.pictures.intent.action.MEDIA\_CHECK
- LocationManagerService

**Alarms[LOCATION](Allow every 41400 seconds)**

- ALARM\_WAKEUP\_LOCATOR(com.google.android.gms.nlp.AL ARM\_WAKEUP\_LOCATOR)
- ALARM\_WAKEUP\_CACHE\_UPDATER
- ALARM\_WAKEUP\_BURST\_COLLECTOR(com.google.android.gm s.nlp.ALARM\_WAKEUP\_BURST\_COLLECTOR)
- com.google.android.gms.location.fused.GPS\_ALARM\_BA LANCED\_ACCURACY
- ALARM\_WAKEUP\_ACTIVE\_COLLECTOR
- ALARM\_WAKEUP\_PASSIVE\_COLLECTOR
- ALARM\_WAKEUP\_BURST\_COLLECTION\_TRIGGER
- com.google.android.intent.action.SEND\_IDLE
- ALARM\_WAKEUP\_ACTIVITY\_DETECTION
- com.google.android.location.reporting.ACTION\_UPDAT E\_WORLD

**Alarms(Allow every 93600 seconds)**

- android.app.backup.intent.RUN
- com.google.android.gms/.checkin.EventLogService$Receiver
- com.google.android.gms/.checkinCheckinService%Receiver

**Wakelocks**

**Wakelocks(Allow every 800 seconds)**

- WakefulIntentService[GCoreUlr-LocationReportingService]
- RILJ
- NetworkStats

**Wakelocks(Allow every 3600 seconds)**

- WeatherUpdateService

**Wakelocks(Allow every 10800 seconds)**

- SyncLoopWakeLock(delays sync)
- \*net\_scheduler\*
- GCoreFlp
- Icing
- Wakeful StateMachine: GeofencerStateMachine
- NfcService:mRoutingWakeLock
- wake:com.pushbullet.android/.gcm.GcmService
- SyncService(Package: Push Bullet)
- ai(Package: Push Bullet)
- ae(Package: Push Bullet)
- AsyncService

**Wakelocks(Allow every 41400 seconds)**

- NlpWakeLock
- NlpCollectorWakeLock
- LocationManagerService
- Config Service Fetch

**Wakelocks(Allow every 9999999 seconds)**

- \*job\*/com.facebook.katana/com.facebook.analytics2.logger.LollipopUploadServi ce
- JobSchedulerHack-com.facebook.analytics2.logger.LollipopUploadServi ce
- UploadServiceLogic-com.facebook.analytics2.logger.LollipopUploadServi ce
- \*job\*/com.facebook.orca/com.facebook.bugreporter.scheduler.LollipopService (com.facebook.orca.Messenger)
- \*job\*/com.facebook.katana/com.facebook.bugreporter.scheduler.LollipopService (com.facebook.katana.Facebook)

**Services**

**Services(Block/Deny)**

- com.google.android.gms.analytics.AnalyticsService
- com.google.android.gms/com.google.android.location.internal.GoogleLocatio nManagerService**(Location Service)**
- com.android.gms.Feedback.FeedbackService**(Breaks Play Games)**
- com.android.gms.ads.AdRequestBrokerService
- com.google.android.gms/com.google.android.location.network.NetworkLocatio nService**(Location Service)**
- com.google.android.location.geofencer.service.Geof encerProviderService**(GPS Service)**
- com.google.android.gms/com.google.android.location.copresence.service.Pro ximitySettingInjectorService **(location service)**
- com.facebook.katana/com.facebook.analytics.service.AnalyticsService
- com.facebook.orca/com.facebook.analytics.service.AnalyticsService
- com.android.cellbroadcastreceiver/.CellBroadcastAlertService
- com.android.cellbroadcastreceiver/.CellBroadcastConfigService

**আমি লোকেশন ব্যবহার করি না,তাই এগুলায় যেগুলা ব্যবহার করলে যা সমস্যা হবে,তা উল্লেখ করে দিলাম।লোকেশন ব্যবহার করতে চাইলে এগুলার ব্লক না করলেও হবে**

**Alarms(REGEX Blocking)**

- ALARM\_WAKEUPxxxxx
- CONTEXT\_MANAGER\_ALARM\_WAKEUP\_xxxxx

**Procedure**

- - Open Amplify.
  - Select Alarms from the menu.
  - Tap the list icon on the top right corner
  - Tap + button on top.
  - Add the following code to 'Enter Regex to match'

    Code:

    ```
    ALARM_WAKEUP[0-9]+
    ```

- **Set the interval to 9999999 seconds**

ব্যাস,এতটুকুই। এরপর সেট টাকে একবার রিস্টার্ট মারেন এবং স্বাভাবিক হারে চালাতে থাকেন।কিছু দিন পর আপনি নিজেই টের পাবেন যে ব্যাটারি কত উন্নতি হয়েছে আগের চেয়ে। চাইলে power nap ও use করতে পারেন এর পাশাপাশি। তখন এই এপস কে whitelist এ রাখলেই হবে।কোন সমস্যা হলে ফেসবুকে আমাকে জানাতে পারেন

[ফেসবুকে আমি](https://www.facebook.com/aymaan.shihab)
