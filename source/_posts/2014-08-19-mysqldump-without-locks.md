---
layout: post
title: MySQLDump导出时不加锁
date: 2014-08-19T09:50:37.000Z
permalink: /mysqldump-without-lock/
categories: 编程
tags: mysql
status: publish
type: post
published: true
---

在SAE上进行应用开发时，常常需要导入数据库，这时候就需要用MySQLDump工具进行本地数据库导出。

首先MySQLDump最基本的语法是这样的 `mysqldump <database_name>`，执行之后可以在控制台上看到SQL源码。但我第一次尝试将导出的源码上传至SAE时SAE却报错，原因是SAE的数据库管理不支持LOCK和UNLOCK语句。曾有一段时间，我是手动一行行删除LOCK语句。。30多张表那叫一个蛋疼。。后来，我翻阅了mysqlDump的help文档，发现可以添加这么一个参数`--ADD-LOCKS=FALSE`。几经尝试后发现果然没有LOCK语句了。 在此记录下整句命令：

```sh
mysqldump --add-locks=FALSE -uroot -p <database_name> > example.sql
```
