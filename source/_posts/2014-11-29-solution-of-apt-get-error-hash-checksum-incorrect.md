---
layout: post
title: Ubuntu下解决apt-get “Hash校验和不符的方案”
permalink: /solution-of-apt-get-error-hash-checksum-incorrect/
date: 2014-11-29 18:26:18.000000000 +08:00
categories:
- Ubuntu
---
<p>各种坑爹，我也不知道为什么：</p>
<pre><code>sudo gedit etc/apt/apt.conf.d/00aptitude
</code></pre>
<p>最后加一行：<code>Acquire::CompressionTypes::Order "gz";</code></p>
