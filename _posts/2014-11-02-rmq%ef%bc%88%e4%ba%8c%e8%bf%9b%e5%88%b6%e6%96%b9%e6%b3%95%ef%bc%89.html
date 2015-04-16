---
layout: post
title: RMQ（二进制方法）
permalink: /RMQ-binary/
date: 2014-11-02 15:07:05.000000000 +08:00
categories:
- 信息学竞赛
- 编程
tags: []
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
<p>问题描述：已知数组a以及若干个查询(x, y)，求a[x~y]之间的最小值。</p>
</blockquote>
<h2><strong>分析</strong></h2>
<p>不难发现：若取t使得$2^t\leq y-x+1$且$2^{t+1}>y-x+1$，则有：<br />
$$[x, x+t]\bigcup[y-t+1,y]=[x,y]$$<br />
运用二进制的思想，我们只需预处理出$i~i+2^k-1$之间的最小值，即可快速完成查询。设dp[i][j]为$i~i+2^j-1$之间的最小值，则有：<br />
$$dp[i][j]=min(dp[i][j-1],dp[i+2^{j-1}][j-1])$$。</p>
<h2><strong>Code</strong></h2>
<pre><code>var
    a: array [1..100000] of longint;
    dp: array [1..100000, 0..20] of longint;
    n, i: longint;

function min(x, y: longint): longint;
begin
    if x &lt; y then exit(x) else exit(y);
end;

procedure init;
var
    i, j: longint;
begin
    for i := 1 to n do dp[i, 0] := a[i];
    j := 1;
    while 1&lt;&lt;j-1&lt;=n do
    begin
        for i := 1 to n-1&lt;&lt;(j-1) do
            dp[i, j] := min(dp[i, j-1], dp[i+1&lt;&lt;(j-1), j-1]);
        inc(j);
    end;
end;

function query(x, y: longint): longint;
var
    t: longint;
begin
    t := 0;
    while (1&lt;&lt;(t+1)&lt;=y-x+1) do inc(t);
    query := min(dp[x][t], dp[y-(1&lt;&lt;t)+1][t]);
end;

var
    x, y: longint;

begin
    assign(input, 'main.in'); reset(input);
    assign(output, 'main.out'); rewrite(output);

    readln(n);
    for i := 1 to n do read(a[i]);
    init;
    while not eof do
    begin
        read(x, y);
        writeln(query(X, y));
    end;

    close(input); close(output);
end.
</code></pre>
