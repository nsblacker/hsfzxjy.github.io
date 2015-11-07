---
layout: post
title: UVa10285 Cake Slicing
date: 2014-10-01 12:20:18.000000000 +08:00
categories: 编程
tags:
- UVa
- 信息学竞赛
---
<blockquote>
<p>链接：<a href="http://uva.onlinejudge.org/index.php?option=com_onlinejudge&amp;Itemid=8&amp;category=825&amp;page=show_problem&amp;problem=4504">Link</a>  耗时：1.825s</p>
</blockquote>
<p>这道题做的可真够久的：前前后后加起来将近有两个小时，因此当AC的那一刻，自己心中还是挺自豪的。<br />
事实上，这是一道复杂一点的区间型动态规划，之所以说“复杂”，是因为它的状态转移是<strong>二维</strong>的：切蛋糕既可以横切，也可以纵切。由此我想到了分治算法：</p>
<blockquote>
<p>假设一个矩形它所需要切的刀数是f，则f可以由组成该矩形的小矩形的f值决定。</p>
</blockquote>
<p>因此，这个问题具有最优子结构。由于每个状态为一个矩形，因此需要4个维度来记录状态（及左上、右下两个顶点）。下面是横切时的状态转移方程，纵切时同理可得：</p>
<blockquote>
<p>f(up, down, left, right) = min{f(up, i, left, right) + f(i, down, left, right) + right - left} (i = up + 1 .. down -1)</p>
</blockquote>
<p>Code:</p>
<pre><code>{$R-}
const INF = maxint div 5; //正无穷
var
    f: array [0..20, 0..20, 0..20, 0..20] of integer;
    cherries: array [1..500, 1..2] of integer;
    map: array [0..20, 0..20] of boolean;
    n, m, i, k: integer;

function min(x, y: integer): integer; inline;
begin
    if x&lt;y then exit(x) else exit(y);
end;

function cherryin(u, d, l, r: integer): integer; inline; //判断矩形内有没有樱桃
var
    i, j: integer;
begin
    cherryin := 0;
    for i := u+1 to d do
        for j := l+1 to r do
            if map[i, j] then
            begin
                inc(cherryin);
                if cherryin = 2 then exit;
            end;
end;

function dp(u, d, l, r: integer): integer;
var
    b: integer;
    i: integer;
begin
    if f[u, d, l, r] &lt;&gt; -1 then
        exit(f[u,d , l, r]);
    b := cherryin(u, d, l, r);
    if b = 1 then
    begin
        f[u, d, l, r] := 0;
        exit(0);
    end;
    if b = 0 then
    begin
        f[u, d, l, r] := INF;
        exit(INF);
    end;
    dp := INF;
    for i := u+1 to d-1 do
        dp := min(dp, dp(u, i, l, r)+dp(i, d, l, r)+r-l);
    for i := l+1 to r-1 do
        dp := min(dp, dp(u, d, l, i)+dp(u, d, i, r)+d-u);
    f[u, d, l, r] := dp;
end;

var
    _: integer;

begin
    assign(input, 'main.in');reset(input);
    assign(output, 'main.out');rewrite(output);
    _ := 0;
    readln(n, m, k);
    while n&gt;0 do
    begin
        inc(_);
        fillchar(map, sizeof(map), 0);
        fillchar(f, sizeof(f), -1);
        for i := 1 to k do
        begin
            readln(cherries[i, 1], cherries[i, 2]);
            map[cherries[i, 1], cherries[i, 2]] := true;
        end;
        writeln('Case ',_,': ', dp(0,n,0,m));
        readln(n, m, k);
    end;
    close(input);close(output);
end.
</code></pre>
