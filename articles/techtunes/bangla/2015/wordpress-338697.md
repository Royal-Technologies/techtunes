---
archive_id: techtunes-338697
source: techtunes
source_name: টেকটিউনস (Techtunes)
wordpress_id: 338697
title: 'ওয়ার্ডপ্রেস ওস্তাদ [পর্ব-১২] :: ওয়ার্ডপ্রেস থিম ফ্রেমওয়ার্ক ডেভলপমেন্ট (পর্ব-৬)'
slug: wordpress-338697
language: bn
status: publish
published_at: '2015-03-13T18:33:00+00:00'
modified_at: '2015-03-13T18:57:00+00:00'
original_url: https://www.techtunes.io/wordpress/tune-id/338697
author: অসীম কুমার পাল
author_url: https://www.techtunes.io/tuner/ashim
categories:
- ওয়ার্ডপ্রেস
tags:
- Ashim Kumar
- এডভান্স ওয়ার্ডপ্রেস
- ওয়ার্ডপ্রস
- ওয়েব ডেভলপমেন্ট
content_hash: a4a10855188fea87a81f478471e9fc9b7555e89b273daa653c09b6f1247fc11e
archived_at: '2026-11-12T12:57:29.598973+00:00'
---

সবাইকে আন্তরিক শুভেচ্ছা এবং স্বাগতম জানাচ্ছি “ওয়ার্ডপ্রেস ওস্তাদ” এডভান্স ওয়ার্ডপ্রেস ডেভলপমেন্টের উপর একটা পূর্ণাঙ্গ ফ্রি চেইন কোর্সে। টেকটিউনস বিশ্বের সবচেয়ে বড় বাংলা সোশ্যাল নেটওয়ার্ক । এরকম একটা বড় প্লাটফর্মে “ওয়ার্ডপ্রেস ওস্তাদ” কোর্সটি টেকটিউনস কতৃপক্ষের প্রত্যক্ষ সহযোগিতায় শুরু করতে পেরে ভালো লাগছে।

[“ওয়ার্ডপ্রেস ওস্তাদ ” কোর্সের ঘোষণা](https://www.techtunes.io/wordpress/tune-id/289721)  টেকটিউন্সে প্রকাশ করার পর আপনাদের মধ্যে যে আগ্রহ দেখেছি, তা এই কোর্সটিকে সুন্দর করে পরিচালনা করতে সাহায্য করবে। সকলের সক্রিয় অংশগ্রহণ কামনা করছি।

![](https://dnc.techtunes.io/tDrive/tuner/ashim/289721/1111.png)

## ওয়ার্ডপ্রেস থিম ফ্রেমওয়ার্ক ডেভলপমেন্ট (পর্ব-৬)

গতপর্বে আমরা যে content.php ফাইল তৈরি করেছিলাম , সেখানে author meta, date meta, category,tags,comments ইত্যাদি কিভাবে যুক্ত করতে হয় দেখবো।

গতপর্বে functions.php ফাইলে আমরা নিচের ফাংশনটি নিয়েছিলাম।

```
if ( ! function_exists( 'auamy_post_meta' ) ) {
	function auamy_post_meta() {
		echo '<ul class="list-inline entry-meta">';

		if ( get_post_type() === 'post' ) {

		}

		echo '</ul>';
	}
}
```

উপরের কোড এডিট করে

```
if ( get_post_type() === 'post' ) {

		}
```

এর মধ্যে নিচের কোডটুকু যুক্ত করুন।

```
			// If the post is sticky, mark it.
			if ( is_sticky() ) {
				echo '<li class="meta-featured-post"><i class="fa fa-thumb-tack"></i> ' . __( 'Sticky', 'auamy' ) . ' </li>';
			}

			// Get the post author.
			printf(
				'<li class="meta-author"><a href="%1$s" rel="author">%2$s</a></li>',
				esc_url( get_author_posts_url( get_the_author_meta( 'ID' ) ) ),
				get_the_author()
			);

			// Get the date.
			echo '<li class="meta-date"> ' . get_the_date() . ' </li>';

			// The categories.
			$category_list = get_the_category_list( ', ' );
			if ( $category_list ) {
				echo '<li class="meta-categories"> ' . $category_list . ' </li>';
			}

			// The tags.
			$tag_list = get_the_tag_list( '', ', ' );
			if ( $tag_list ) {
				echo '<li class="meta-tags"> ' . $tag_list . ' </li>';
			}

			// Comments link.
			if ( comments_open() ) :
				echo '<li>';
				echo '<span class="meta-reply">';
				comments_popup_link( __( 'Leave a comment', 'auamy' ), __( 'One comment so far', 'auamy' ), __( 'View all % comments', 'auamy' ) );
				echo '</span>';
				echo '</li>';
			endif;

			// Edit link.
			if ( is_user_logged_in() ) {
				echo '<li>';
				edit_post_link( __( 'Edit', 'auamy' ), '<span class="meta-edit">', '</span>' );
				echo '</li>';
			}
```

## কোড পর্যালোচনা

```
if ( get_post_type() === 'post' ) {

		}
```

কনটেন্টের post type যদি post হয় তাহলে এই if কন্ডিশনাল স্টেটমেন্টের কন্ডিশন সত্য হবে এবং {} ব্রাকেটের মধ্যেকার ইন্সট্রাকশন সমূহ কাজ করবে।

```
if ( is_sticky() ) {
				echo '<li class="meta-featured-post"><i class="fa fa-thumb-tack"></i> ' . __( 'Sticky', 'auamy' ) . ' </li>';
			}
```

এখাসে is\_sticky() এর মাধ্যমে চেক করবে পোস্টটি স্টিকি কিনা।যদি স্টিকি হয় তাহলে fortawesome এর fa-thumb-tack আইকনটি যুক্ত করবে। এবং Sticky লেখাটি দেখাবে।\_\_( 'Sticky', 'auamy' ) ব্যবহৃত হচ্ছে Sticky লেখাটি প্রদর্শনের জন্য। এবং সাইটটি যদি অন্য কোন ভাষায় হয়ে থাকে তাহলে তা ট্রান্সলেট করে ঐ ভাষায় দেখাবে।

```
// Get the post author.
			printf(
				'<li class="meta-author"><a href="%1$s" rel="author">%2$s</a></li>',
				esc_url( get_author_posts_url( get_the_author_meta( 'ID' ) ) ),
				get_the_author()
			);
```

এর মাধ্যমে লেখকের নাম প্রদর্শন করবে এবং author পেজের সাথে লিংক তৈরি করবে। এখানে

```
<li class="meta-author"><a href="%1$s" rel="author">%2$s</a></li>
```

এর %1$s এর মাধ্যমে esc\_url( get\_author\_posts\_url( get\_the\_author\_meta( 'ID' ) ) ) এর ভ্যালুকে রিপ্রেজেন্ট করে এবং পরবর্তী %2$s প্রকৃতপক্ষে get\_the\_author() এর এর ভ্যালুকে রিপ্রেজেন্ট করে।

```
// Get the date.
			echo '<li class="meta-date"> ' . get_the_date() . ' </li>';
```

এর মাধ্যমে তারিখ প্রদর্শিত হবে।

```
// The categories.
			$category_list = get_the_category_list( ', ' );
			if ( $category_list ) {
				echo '<li class="meta-categories"> ' . $category_list . ' </li>';
			}
```

এর মাধ্যমে পোস্টের ক্যাটাগরি লিস্ট প্রদর্শন করবে। এখানে $category\_list = get\_the\_category\_list( ', ' ); এর মাধ্যমে প্রথমে ক্যাটেগরী সমূহ $category\_list ভেরিয়েবলের আন্ডারে একটা এরেতে জমা হবে।  
 if ( $category\_list ) {} এর মাধ্যমে চেক করা হচ্ছে কোন ক্যাটেগরী আছে কিনা, যদি থাকে তাহলে

```
echo '<li class="meta-categories"> ' . $category_list . ' </li>';
```

এর মাধ্যমে লিস্ট আইটেম হিসেবে প্রদর্শন করবে।যদিও css ব্যবহার করে পরবর্তীতে একই লাইনে ক্যাটেগরী সমূহকে প্রদর্শন করা যাবে।

```
// The tags.
			$tag_list = get_the_tag_list( '', ', ' );
			if ( $tag_list ) {
				echo '<li class="meta-tags"> ' . $tag_list . ' </li>';
			}
```

এর মাধ্যমে ট্যাগ সমূহ প্রদর্শন করা হয়।$tag\_list = get\_the\_tag\_list( '', ', ' ); এর মাধ্যমে ক্যাটেগরীর অনুরূপ প্রথমে ট্যাগ সমূহ $tag\_list ভেরিয়েবলের আন্ডারে একটা এরেতে জমা হবে।এর পর if ( $tag\_list ){} এর মাধ্যমে চেক করা হচ্ছে কোন ট্যাগ আছে কিনা, যদি থাকে তাহলে

```
echo '<li class="meta-tags"> ' . $tag_list . ' </li>';
```

এর মাধ্যমে লিস্ট আইটেম হিসেবে ট্যাগ সমূহকে প্রদর্শন করবে।

```
			// Comments link.
			if ( comments_open() ) :
				echo '<li>';
				echo '<span class="meta-reply">';
				comments_popup_link( __( 'Leave a comment', 'auamy' ), __( 'One comment so far', 'auamy' ), __( 'View all % comments', 'auamy' ) );
				echo '</span>';
				echo '</li>';
			endif;
```

এর মাধ্যমে পোস্টে কমেন্ট আছেকিনা, আর থাকলে কতগুলো কমেন্ট আছে তা প্রদর্শন করা হয়।if ( comments\_open() )এর মাধ্যমে চেক করা হচ্ছে পোস্টটিতে বা কমেন্ট এনাবল করা আছে কিনা।comments\_popup\_link( \_\_( 'Leave a comment', 'auamy' ), এর মাধ্যমে প্রদর্শিত হবে Leave a comment ম্যাসেজটি।অর্থাৎ পোস্টে কোন কমেন্ট নেই, কমেন্ট যুক্ত করুন।\_\_( 'One comment so far', 'auamy' ),এর মাধ্যমে বলা হচ্ছে একটা কমেন্ট আছে। আর \_\_( 'View all % comments', 'auamy' ) );এর মাধ্যমে বলা হচ্ছে নির্দিষ্ট সংখ্যক কমন্টে আছে।

```
// Edit link.
			if ( is_user_logged_in() ) {
				echo '<li>';
				edit_post_link( __( 'Edit', 'auamy' ), '<span class="meta-edit">', '</span>' );
				echo '</li>';
			}
```

এর মাধ্যমে পোস্ট কাস্টমাইজ করার জন্য edit বাটন যুক্ত করা হয়।if ( is\_user\_logged\_in() ) এর মাধ্যমে চেক করবে ইউজার লগইন আছে কিনা। যদি লগইন অবস্থায় থাকে তাহলে edit\_post\_link( \_\_( 'Edit', 'auamy' ), '', '' ); এর মাধ্যমে একটা edit লিংক যুক্ত হবে।

## সম্পূর্ণ কোড

```
/**
 * ----------------------------------------------------------------------------------------
 * 5.0 - Display meta information for a specific post.
 * ----------------------------------------------------------------------------------------
 */
if ( ! function_exists( 'auamy_post_meta' ) ) {
	function auamy_post_meta() {
		echo '<ul class="list-inline entry-meta">';

		if ( get_post_type() === 'post' ) {
			// If the post is sticky, mark it.
			if ( is_sticky() ) {
				echo '<li class="meta-featured-post"><i class="fa fa-thumb-tack"></i> ' . __( 'Sticky', 'auamy' ) . ' </li>';
			}

			// Get the post author.
			printf(
				'<li class="meta-author"><a href="%1$s" rel="author">%2$s</a></li>',
				esc_url( get_author_posts_url( get_the_author_meta( 'ID' ) ) ),
				get_the_author()
			);

			// Get the date.
			echo '<li class="meta-date"> ' . get_the_date() . ' </li>';

			// The categories.
			$category_list = get_the_category_list( ', ' );
			if ( $category_list ) {
				echo '<li class="meta-categories"> ' . $category_list . ' </li>';
			}

			// The tags.
			$tag_list = get_the_tag_list( '', ', ' );
			if ( $tag_list ) {
				echo '<li class="meta-tags"> ' . $tag_list . ' </li>';
			}

			// Comments link.
			if ( comments_open() ) :
				echo '<li>';
				echo '<span class="meta-reply">';
				comments_popup_link( __( 'Leave a comment', 'auamy' ), __( 'One comment so far', 'auamy' ), __( 'View all % comments', 'auamy' ) );
				echo '</span>';
				echo '</li>';
			endif;

			// Edit link.
			if ( is_user_logged_in() ) {
				echo '<li>';
				edit_post_link( __( 'Edit', 'auamy' ), '<span class="meta-edit">', '</span>' );
				echo '</li>';
			}
		}

		echo '</ul>';
	}
}
```

functions.php তে যে ফাংশন তৈরি করা হলো তা content.php তে auamy\_post\_meta(); এর অনুরূপ কল করতে হবে।যা গতপর্বে দেখানো হয়েছিলো।

```
<p class="entry-meta">
			<?php
				// Display the meta information
				auamy_post_meta();
			?>
		</p>
```

### সোর্স ফাইল ডাউনলোড

<http://www.mediafire.com/download/0ocyoqeh869bop8/6.WordPress_Theme_Framework_Development(Part-6)>.zip

![](https://dnc.techtunes.io/tDrive/tuner/ashim/293935/girl-beauty-consultant-indicate-icon.png)

আজ এ পর্যন্তই। সবাইকে ধন্যবাদ । শুভকামনা রইলো।
