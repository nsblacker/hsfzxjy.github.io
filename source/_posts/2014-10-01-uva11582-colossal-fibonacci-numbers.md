---
layout: post
title: UVa11582 Colossal Fibonacci Numbers! && 大数操作
permalink: /uva11582-colossal-fibonacci-numbers/
date: 2014-10-01 19:12:27.000000000 +08:00
categories:
- UVa
- 信息学竞赛
- 编程
---
<blockquote>
<p>链接：<a href="http://uva.onlinejudge.org/index.php?option=com_onlinejudge&amp;Itemid=8&amp;page=show_problem&amp;category=27&amp;problem=2629&amp;mosmsg=Submission%20received%20with%20ID%2014290914">Link</a> 耗时：0.139s</p>
</blockquote>
<h2>前言</h2>
<p>这道题的主要思路就是打表，看看Fibonacci数列模n几个一循环。但由于这题给的数太大了，从而在细节上耗了很久。在此记录一下：</p>
<pre><code>var
    x: qword;
    y: longint;
begin
    x := 1&lt;&lt;64-1;
    y := 100;
    x := x mod y; //报错201
    x := x mod qword(y); //正确
end.
</code></pre>
<h2>Code</h2>
<pre><code>var
    a,b: qword;
    _, n, i, k, cnt: longint;
    f: array [1..1000000] of longint;

function superMod(a, b: qword; m: longint): longint;
var
    x: qword;
begin
    if b = 0 then
        exit(1);
    x := superMod(a, b shr 1, m);
    superMod := x * x mod m;
    if odd(b) then
        superMod := superMod * a mod m;
end;

begin
    assign(input, 'main.in'); reset(input);
    assign(output, 'main.out'); rewrite(output);
    readln(_);
    while _ &gt; 0 do
    begin
        dec(_);
        readln(a, b, n);
        if a = 0 then
        begin
            writeln(0);
            continue;
        end;
        if n = 1 then
        begin
            writeln(0);
            continue;
        end;
        f[1] := 1;
        f[2] := 1;
        cnt := 2;
        while not ((f[cnt-1] = 1) and (f[cnt] = 0)) do
        begin
            inc(cnt);
            f[cnt] := (f[cnt-1] + f[cnt-2]) mod n;
        end;
        //while x &gt; int64(1 &lt;&lt;60) do
        //    x := x - int64((cnt &lt;&lt; 59));
        a := a mod qword(cnt);
        k := superMod(a, b, cnt);
        writeln(f[k]);
    end;
    close(output); close(input);
end.
</code></pre>
