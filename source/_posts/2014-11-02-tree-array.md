---
layout: post
title: 树状数组
permalink: /tree-array/
date: 2014-11-02 00:31:54.000000000 +08:00
categories:
- 编程
tags:
- 树状数组
- 信息学竞赛
---
<h2><strong>介绍</strong></h2>
<p>所谓树状数组，就是将线性的数组预处理成树状的结构以降低时间复杂度。先来看一幅经典的图： <img src="/assets/TArry1.jpg" alt="enter image description here" /><br />
其中的a数组为原生数组，c数组为辅助数组，计算方式为： $$c_1=a_1——{(1)}&#95;{10}={(1)}&#95;2$$ $$c_2=a_2+c_1——{(2)}&#95;{10}={(10)}&#95;2$$ $$\ldots$$              不难发现，c[k]存储的实际上是从k开始向前数k的二进制表示中右边第一个1所代表的数字个元素的和。这样写的好处便是可以利用位运算轻松计算sum。上代码。</p>
<h2><strong>Code</strong></h2>
<pre><code>var
    n, i: longint;
    a, c: array [1..10000] of longint;

//计算x最右边的1所代表的数字。
//如：lowbit(0b1100)=0b100
function lowbit(x: longint): longint; 
begin
    lowbit := x and (-x);
end;

//给a[index]加上x
procedure add(index, x: longint);
begin
    inc(a[index], x);
    while index&lt;=n do 
    begin
        inc(c[index], x);
        inc(index, lowbit(index));
    end;
end;

//求a[1~index]的和
function sum(index: longint): longint;
begin
    sum := 0;
    while index&gt;0 do
    begin
        inc(sum, c[index]);
        dec(index, lowbit(index));
    end;
end;

var
    s: longint;
    op: longint;
    x,y: longint;

begin
    assign(input, 'main.in'); reset(input);
    assign(output, 'main.out'); rewrite(output);

    readln(n);
    for i := 1 to n do
    begin
        read(a[i]);
        add(i, a[i]);
    end;

    while not eof do
    begin
        read(op);
        if op = 1 then //添加操作
        begin
           read(x, y);
           Add(x, y); 
        end
        else           //求和操作
        begin
            read(s);
            writeln(sum(s));
        end;
    end;

    close(input); close(output);
end.
</code></pre>
