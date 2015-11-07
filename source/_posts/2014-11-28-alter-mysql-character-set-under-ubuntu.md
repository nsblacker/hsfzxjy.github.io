---
layout: post
title: 在Ubuntu下更改MYSQL的字符集
permalink: /alter-mysql-character-set-under-ubuntu/
date: 2014-11-28 21:49:30.000000000 +08:00
categories:
- MySql
- Ubuntu
- 编程
---
<p>修改<code>/etc/mysql/my.cnf</code>：</p>
<pre><code>[client]
default-character-set=utf8

[mysqld]
character_set_server=utf8

[mysql]
default-character-set=utf8
</code></pre>
<p>然后：<code>sudo service mysql restart</code></p>
