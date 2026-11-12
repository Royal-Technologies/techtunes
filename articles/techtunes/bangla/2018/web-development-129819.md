---
archive_id: techtunes-129819
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 129819
title: ১৫টি ওয়ার্ডপ্রেস ফিচার প্লাগিনমুক্তঅবশ্যই নতুনদের কাজে লাগবে
slug: web-development-129819
language: bn
status: publish
published_at: '2018-11-03T10:52:00+00:00'
modified_at: '2018-11-03T10:52:00+00:00'
original_url: https://www.techtunes.io/web-development/tune-id/129819
author: সিএক্স রানা
author_url: https://www.techtunes.io/tuner/ranapatwary
categories:
- ওয়েব ডেভেলপমেন্ট
tags:
- ওয়ার্ডপ্রেস
- ওয়ার্ডপ্রেস সর্ট ফিচার
- টিটি
content_hash: 848104729e2cdd4d185bb23ee3c500b7286d3565b59b28afb7c9573d3cc46383
archived_at: '2026-11-12T12:58:46.319220+00:00'
---

[নিচের যেকোন ফিচার আপনার সাইটে যুক্ত করতে চাইলে আগে সাইটের থীমস এর ব্যাকআপ ফাইল রাখুন]

*ওয়ার্ডপ্রেস সর্ট ফিচার*

![](https://dnc.techtunes.io/tDrive/tuner/ranapatwary/129819/wordpress-snippets.jpg)

১। ভিজিটর কাউন্ট সিস্টেমস/ফিচার

সাধারনত আমরা অনেকেই আমারদের টিউন কতজন ভিজিটর পড়েছেন তা জানার জন্য Post-Views প্লাগিন ইউজ করি, ছোট খাট কিছু কাজ আছে যার জন্য প্লাগিন ব্যবহার না করাই উত্তম।

এ জন্য আজকে আমরা ওয়ার্ডপ্রেস ব্লগ/সাইটের টিউন ভিউ কাউন্ট করার সিস্টেম করবো কয়েক লাইন কোড লিখেই।

ধাপ সমূহ: প্রথমে আপনার wp-admin অপশন থেকে apperance মেনু থেকে editor অপশনে যান এবং টেমপ্লেট ফাইলগুলো থেকে `functions.php`

ফাইলটি সিলেক করুন।

এবার নিচের কোডটি লিখুন:

```
function getPostViews($postID){$count_key = 'post_views_count'; $count = get_post_meta($postID, $count_key, true); if($count=''){delete_post_meta($postID, $count_key); add_post_meta($postID, $count_key, '0'); return &quot;0 View&quot;} return $count.' Views';}
function setPostViews($postID) {$count_key = 'post_views_count'; $count = get_post_meta($postID, $count_key, true); if($count=''){$count = 0; delete_post_meta($postID, $count_key); add_post_meta($postID, $count_key, '0');}else{$count+; update_post_meta($postID, $count_key, $count);}
```

[মনে রাখবেন কোড লিখবেন অবশ্যই <?php এর পরে এবং?> এর আগে]

ধাপ ২: এবার টেমপ্লেট ফাইলের `single.php`ফাইল খুলুন এবং নিচের কোড লিখুন

```
&lt;?php setPostViews(get_the_ID());?&gt;
```

ধাপ৩: এবার আপনি কোন অবস্থানে টিউন ভিউ কাউন্টার প্রদর্শন করাতে চান সেথানে নিচের কোডটি লিখুন

```
&lt;?php echo getPostViews(get_the_ID());?&gt;
```

[সাধারনত অনেকেই টিউন টাইটেল, তারিখ এর পাশেই ইউজ করে, তাই আপনাকে অবশ্যই `single.php` তে বসাতে হবে]

২। আপনার ওয়ার্ডপ্রেস ব্লগের/সাইটের কন্ট্রিবিউটর দের ফটো আপলোড করার পারমিশন দিবেন যেভাবে

প্রথমে থীমসের `functions.php`ফাইলটি যে কোন এডিটরে ওপেন করুন যেমন: নোটফ্যাড/নোটপ্যাড+ অথবা ওয়ার্ডপ্রেস ড্যাশবোর্ড থেকে।  
 এবার নিচের কোড লিখুন

```
&lt;?php
//allow contributor to add photos
if (current_user_can('contributor') &amp;&amp;!current_user_can('upload_files')) {add_action('admin_init', 'allow_contributor_uploads'); function allow_contributor_uploads() {$contributor = get_role('contributor'); $contributor-&gt;add_cap('upload_files');}?&gt;
```

[এই কোড `functions.php`ফাইল এর একদম শুরুতেই বসালেও হবে, ]

৩। আপনার ব্লগের যেকোন স্থানে আপনার ফেইসবুক প্যানের সংক্ষা দেখাতে চাইলে নিচের কোডটি থীমসের যেকোন স্থানে লিখুন, যেমন : হেডার, ফুটার, কিংবা প্রতিটি টিউনের  
 সাথে, single.php তে

```
&lt;?php $page_id = &quot;YOUR PAGE-ID&quot; $xml = @simplexml_load_file(&quot;http://api.facebook.com/restserver.php?method=facebook.fql.query&amp;query=SELECT%20fan_count%20FROM%20page%20WHERE%20page_id=&quot;.$page_id.&quot;&quot;) or die (&quot;a lot&quot;); $fans = $xml-&gt;page-&gt;fan_count; echo $fans;?&gt;
```

৪। ডিসপ্লে গুগল সার্চ টার্মস  
 ![](http://youngblah.com/wp-content/uploads/2012/03/Google-logo.jpg)

```
 ধরুন কেউ একজন গুগলে কিছু লিখে সার্চ করার পর আপনার সাইটের লিংক পেয়ে আপনার সাইটে এসছে, আপনি চাইলে সেই ভিজিটরকে আবারো মনে করিয়ে দিতে পারবেন সে কি
লিখে সার্চ করলে আপনার সাইট সে গুগলে পেয়েছে, এতে ভিজিটর আপনার সাইটের কিওয়ার্ড মনে রাখতে পারবে সহজে।

নিচের কোড লিখুন যেখান আপনি সার্চ টার্মস মেসেজটি দেখাতে চান :

```
&lt;?php
$refer = $_SERVER[&quot;HTTP_REFERER&quot;];
if (strpos($refer, &quot;google&quot;)) {$refer_string = parse_url($refer, PHP_URL_QUERY); parse_str($refer_string, $vars); $search_terms = $vars['q']; echo 'Welcome Google visitor! You searched for the following terms to get here: '; echo $search_terms;};?&gt;
```

[আমার পরামর্শ আপনি সাইটের ফুটারে উক্ত মেসেজ দেখাতে পারেন]

৫। টিউনাদের অটোমেটিক ভাবে জানিয়ে দিন টিউন পারলিশ খবর  
 দরুন আপনার একটি ব্লগ আছে এবং সেই ব্লগে অনেকেই টিউন লিখে, আর সকল টিউন আপনার মডারেশনে আছে, তাই নিচের সিস্টেমটি করলে আপনি যখন তাদের  
 টিউন পাবলিশ করবেন তখন তারা ইমেইল খবরটি জানতে পারবে।  
 ধাপ: আগের মত থীমসের function.php ফাইলে নিচের কোড লিখুন

```
function wpr_authorNotification($post_id) {$post = get_post($post_id); $author = get_userdata($post-&gt;post_author); $message = &quot; Hi &quot;.$author-&gt;display_name.&quot;, Your post, &quot;.$post-&gt;post_title.&quot; has just been published. Well done! &quot; wp_mail($author-&gt;user_email, &quot;Your article is online&quot;, $message);}
add_action('publish_post', 'wpr_authorNotification');
```

[কোডটি অবশ্যই?> এর উপরে লিখুত হবে]

৬। লিমিট টিউন রিভিশন  
 আমরা যখন একটি টিউন কয়েকভার এডিট করি তখন প্রতিবার একটি টিউন রিভিশন হয়, যা ডাটাবেসের জন্য মোটেই ভালো নয়, তাই রিভিশন লিমিট করে দিন, যদিও এতে টিউনের কোন ক্ষতি হবে না।

নিচের কোড লিখুন wp-config.phpফাইলে

```
?php
# Maximum 5 revisions #
define('WP_POST_REVISIONS', 5);
# Disable revisions #
define('WP_POST_REVISIONS', false);?&gt;
```

[wp-config.php ফাইলটি আপনার ওয়ার্ডপ্রেস এর একটি কোর ফাইল, যা থীমসের কোন অংশ নয়]

৭। ওয়ার্ডপ্রেস ড্যাশবোর্ডে বিল্ট ইন ইউডজেট বানান  
 যখন আমরা কোন সাইটে লগিন করি তখন রিডাইরেক্ট হয়ে ড্যাশবোর্ড আসে, এবং সেখান রাইট নাও “Right Now” দেখায়  
 আপনি চাইলে তার নিচে আপনার ইচ্ছেমত মেসেজ সেট করতে পারবেন, যেমন আপনি চাইলে সাইটের/ব্লগের নীতিমালাটি ড্যাশবোর্ডে সেটিং করে পারবনে।  
 যেখানে html, php, text সাপোর্ট করবে।  
 নিচের কোডটি আগের মতই থীমসের functions.phpতে লিখুন

```
&lt;?php function your_dashboard_widget() {?&gt;
&lt;h3&gt;লগিন করার জন্য আপনাকে স্বাগতম&lt;/h3&gt;
&lt;p&gt;এখানে এডমিন কর্তৃক মেসেজ লিখুন, এখানে html, php সাপোর্ট করবে&lt;/p&gt;
&lt;?php};
function add_your_dashboard_widget() {wp_add_dashboard_widget('your_dashboard_widget', _('টাইটলে লিখুন এখানে'), 'your_dashboard_widget');}
add_action('wp_dashboard_setup', 'add_your_dashboard_widget');?&gt;
```

৮। ওয়ার্ডপ্রেস ড্যাশবোর্ড এর “Howdy” এডমিন লেখাটি পাল্টে দিন  
 থীমসের functions.php ফাইলে নিচের কোড লিখুন

```
&lt;?php
// replace WordPress Howdy in WordPress 3.3
function replace_howdy($wp_admin_bar) {$my_account=$wp_admin_bar-&gt;get_node('my-account'); $newtitle = str_replace('Howdy, ', 'লগিন করেছেন', $my_account-&gt;title); $wp_admin_bar-&gt;add_node(array('id' =&gt; 'my-account', 'title' =&gt; $newtitle, ));}
add_filter('admin_bar_menu', 'replace_howdy', 25);?&gt;
```

[এখানে লগিন করেছেন কথাটি হচ্ছে নতুন টাইটেল আপনি ইচ্ছে কররে তা পরিবর্তন করে নিন] ৯। ডাইনামিক কপিরাইট টেক্সট আমাদের অনেক সাইটে আমরা দীর্ঘদিন ধরেই লগিন করিনা, যখন নতুন বছর আসে তখন সাইটের ফুটারে কপিরাইট বছর অটোমেটিকভাবেই পাল্টে যাবে যদি ডাইনামিক কপিরাইট সিস্টেম করে রাখেন, তাহলে আপনাকে আর প্রত বছর বছর ফুটারে নিজের থেকে বছর/তারিখ চেন্জ করতে হবে না। নিচের কোড লিখুন থীমসের ফুটার.পিএইপি (footer.php)পাইলে

```
&lt;b&gt;(c) &lt;?php echo date('Y');?&gt;&lt;/b&gt;
| &lt;a href=&quot;&lt;?php bloginfo('url');?&gt;&quot;&gt;&lt;?php bloginfo('name');?&gt;&lt;/a&gt;
| &lt;?php bloginfo('description');?&gt;
```

১০। কাস্টম ফিড ফুটার যখন কেই আপনার সাইটের Feed এর মাধ্যমে লেখা পড়ে তখন আপনি চাইলে ফিডের ফুটারে নিজের ইচ্ছে মত কিছু মেসেজ সেট করতে পারবনে, নিচের কোড লিখুন থীমসের ফাংশন ডিট পিএইপি তে

```
&lt;?php
if (!function_exists('custom_feed_footer'))
{function custom_feed_footer($content) {if(is_feed()) $content.= 'আপনি যা লিখতে চান'; return $content;} add_filter('the_excerpt_rss', 'custom_feed_footer'); add_filter('the_content', 'custom_feed_footer');}?&gt;
```

১১। কিভাবে ভিজিটরকে ইমপ্রেস করবেন আর চমক দেখাবেন? আশাকরি, যদি সে ম্যাক ইউজ করে তবে তাকে বলবো ধন্যবাদ ম্যাক ইউজ করার জন্য আর যদি windows ইউজ করে তাকেও বলবো ধন্যবাদ। নিচের কোডটি থীমসের হেডার কিংবা ফুটারে লিখুন

```
&lt;?php
if (stristr($_SERVER['HTTP_USER_AGENT'], &quot;mac&quot;)) {echo 'Hello, Im a Mac User.';} else {echo 'Thank you for useing PC';}?&gt;
```

১২। (time ago) মিনিট আগে টিউন লেখা হয়েছে, টুইটার স্টাইলে নিচের কোডটি লিখুন থীমসের সিঙ্গেল ডট পিএইচপি(single.php) তে যেখানে দেখাতে চান সেখানে বসিয়ে দিবেন

```
&lt;?php
# For posts &amp; pages #
echo human_time_diff(get_the_time('U'), current_time('timestamp')). ' ago';
# কমেনটস অংশের জন্য #
echo human_time_diff(get_comment_time('U'), current_time('timestamp')). ' ago'; 

// Change to the date after a certain time
$time_difference = current_time('timestamp') - get_the_time('U');
if($time_difference &lt; 86400) {//here goes the code from one of the sample above} else {the_time();};?&gt;
```

১৩। টুইটার থেকে আপনার লিংক পেয়ে কেউ যদি আপনার ব্লগে টিউন পড়তে আসে, তবে তাকেও স্বাগতম জানান নিচের কোড টি থীমসের যেখানে ইচ্ছে লিখুন (header, footer, single.php)

```
&lt;?php
if (strpos($_SERVER[HTTP_REFERER], &quot;twitter.com&quot;) = true) {echo &quot;ধন্যবাদ টুইটার থেকে ভিজিট করার জন্য&quot;}?&gt;
```

১৪। ওয়ার্ডপ্রেস ড্যাশবোর্ড ফুটারে নিজের ইচ্ছেমত লিখুন সাধারনত নতুন ভার্সনে লেখা থাকে, Thank you for creating with WordPress আপিন চাইলে তা পরিবর্তন করে নিতে পারবেন খুব সহজে, আপনি নেচর কোডটি লিখুন থীমসের function.php ফাইলে

```
&lt;?php
function remove_footer_admin () {echo 'এখানে রিখুন. Thank you &lt;a href=&quot;http://wordpress.org&quot;&gt;Wordpress&lt;/a&gt; for giving me this filter.';}
add_filter('admin_footer_text', 'remove_footer_admin');?&gt;
```

১৫। হোম পেজ থকে যেকোন বিভাগের লেখা সরিয়ে রাখুন, ইচ্ছে অনুযায়ী থীমসের function.php তে নিচের কোড লিখুন

```
&lt;?php
function excludeCat($query) {if ($query-&gt;is_home) {$query-&gt;set('cat', '-3, -5, -23');} return $query;}
add_filter('pre_get_posts', 'excludeCat');?&gt;
```

যেই ID গুলোর আগে মাইনাস আছে তার টিউন প্রথম পেজে আসবে না, এখানে 3, 5, এবং 23 হচ্ছে ক্যাটাগরি আইডি [কেউ কোড কপি করে পেস্ট করবেন না, প্লিজ কোডগুলো দেখে দেখে নিজের হাতেই লিখুন] আজ আর দিতে পারলোম না, অন্য দিন সময় করে আরো কিছু ওয়ার্ডপ্রেস ফাংশনাল সর্টকার্ট সিস্টেম জানিয়ে দেব। আর যারা ইংরেজী বালো পড়তে পারেন, তারা নিয়মিত আমার ইংরেজী ব্লগে ভিজিট করে ওয়েব ডিজাইন এবং ডেভেলপমেন্ট রিলেটেড় আর্টিকেল পড়তে পারেন। Click
```
