---
layout: post
title: Extended和Double的奇怪问题
date: 2014-08-20T05:37:46.000Z
permalink: /strange-extended-and-double-problem/
categories: 编程
tags: [Delphi, 浮点数]
status: publish
type: post
published: true
---

最近在做一个项目，其中有一段判断一个Extended浮点数是否为整数的代码。我用如下方式实现：

```pascal
function IsInt(F: Extended): Boolean;
begin
  result := Trunc(F)-F = 0; //整数部分等于自身
end;
```

测试了许多样例都过了，唯独这个没过：

```pascal
IsInt(4.000000002*1000000000); //False
```

调试时发现： Trunc(F)居然等于4000000001！开始以为是精度的问题，找了许多资料也没能解决。后来将Extended换成了Double，就通过了。百思不得其解中。
