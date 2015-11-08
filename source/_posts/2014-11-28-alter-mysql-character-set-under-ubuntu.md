---
layout: post
title: 在Ubuntu下更改MYSQL的字符集
date: 2014-11-28 21:49:30.000000000 +08:00
categories:
- 编程
tags:
- MySql
- Ubuntu
---

修改`/etc/mysql/my.cnf`：

    [client]
    default-character-set=utf8

    [mysqld]
    character_set_server=utf8

    [mysql]
    default-character-set=utf8

然后：`sudo service mysql restart`
