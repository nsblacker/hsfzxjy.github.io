---
layout: post
title: UVa1647 Computer Transformation
date: 2014-10-24 18:50:30.000000000 +08:00
categories:
- UVa
- 信息学竞赛
- 数学
- 数论
- 编程
tags:
- 数列
- 高精度
status: publish
type: post
published: true
meta:
  _edit_last: '1'
author:
  login: hsfzxjy
  email: 956357208@qq.com
  display_name: hsfzxjy
  first_name: ''
  last_name: ''
excerpt: !ruby/object:Hpricot::Doc
  options: {}
---
<blockquote>
<p>链接：<a href="http://uva.onlinejudge.org/index.php?option=com_onlinejudge&amp;Itemid=8&amp;category=825&amp;page=show_problem&amp;problem=4522">Link</a> 耗时：0.679s</p>
</blockquote>
<h2><strong>分析</strong></h2>
<p>本质上，这是一道求数列通项的题目。我们列出前几个字符串：<br />
$$01,$$<br />
$$1001,$$<br />
$$01101001,$$<br />
$$1001011001101001,$$<br />
$$\ldots$$<br />
如果用$S_i$表示第i个字符串中“00”的个数，则有：<br />
$$S_1=0,\ S_2=1,\ S_3=1,\ S_4=3,\ S_5=5,\ S_6=11,\ldots$$<br />
经过观察可以发现有如下规律：<br />
$$S_n=2\times S_{n-1}+{(-1)}^n$$<br />
求通项就简单了，换个元即可：<br />
$$S_n=\frac{1}{3}[{(-1)}^n+2^{n-1}]$$<br />
程序采用高精度实现。</p>
<h2><strong>Code</strong></h2>
<pre><code>const
    JINDU = 100000;
var
    n: Integer;
//在数字前补0
procedure PrintANumber(x: longint);
var
    t: longint;
begin
    if x = 0 then
        write('00000')
    else
    begin
        t := JINDU;
        while t &gt; x * 10 do 
        begin
            write(0);
            t := t div 10;
        end;
        write(x);
    end;
end;

var
    ans: array [1..300] of longint;
    len, i: integer;
//计算2^(n-1)
procedure calc2;
var
    i, x, t, mul: longint;
begin
    len := 1;
    ans[1] := 1;
    t := n-1;
    while t &gt; 0 do
    begin
        if t &lt; 6 then 
            mul := 1 &lt;&lt; t
        else 
            mul := 64;
        x := 0;
        for i := 1 to len do
        begin
            ans[i] := ans[i] * mul + x;
            x := ans[i] div JINDU;
            ans[i] := ans[i] mod JINDU;
        end;
        if x &gt; 0 then
        begin
            inc(len);
            ans[len] := x;
        end;
        dec(t, 6);
    end; 
end;
//除以3
procedure div3;
var
    i, x, t: longint;
begin
    i := len;
    x := 0;
    while i &gt; 0 do
    begin
        t := (x * JINDU + ans[i]);
        ans[i] := t div 3;
        x := t mod 3;
        dec(i);
    end;
    while ans[len] = 0 do dec(len);
end;

begin
    assign(input, 'main.in'); reset(input);
    assign(output, 'main.out'); rewrite(output);

    while not eof do
    begin
        readln(n);
        if n=1 then   //特殊情况处理
        begin
            writeln(0);
            continue;
        end;
        fillchar(ans, sizeof(ans), 0);
        calc2;
        if odd(n) then
            dec(ans[1])
        else
            inc(ans[1]);
        div3;
        write(ans[len]);
        for i := len-1 downto 1 do 
            PrintANumber(ans[i]);
        writeln;
    end;

    close(input); close(output);
end.
</code></pre>
