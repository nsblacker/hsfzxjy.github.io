---
layout: post
title: Sublime configuration for Pascal
date: 2014-10-23 21:22:54.000000000 +08:00
categories:
- Sublime
tags:
- Pascal
- Sublime
---

> 鉴于U盘中Sublime的配置常常莫名其妙地消失，在此将其记录一下。

## **Code**

    {
        "cmd": ["fpc", "-S2", "${file}", "-o${file_path}/${file_base_name}.exe"],
        "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
        "working_dir": "${file_path}",
        "selector": "source.pascal",

        "variants": [
            {
                "name": "Run",
                "cmd": ["cmd", "/c", "fpc", "-S2", "${file}", "-o${file_path}/${file_base_name}.exe", 
     "&&", "${file_path}/${file_base_name}.exe"]
            }
        ],

        "osx":
        {
            "path": "/usr/local/bin:/usr/bin:/bin:${path}"
        }
    }