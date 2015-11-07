---
layout: post
title: UVa10285 Longest Run on a Snowboard
date: 2014-09-29 22:00:35.000000000 +08:00
categories:
- UVa
- 信息学竞赛
- 编程
---
<blockquote>
<p>链接：<a href="http://uva.onlinejudge.org/index.php?option=com_onlinejudge&amp;Itemid=8&amp;page=show_problem&amp;category=14&amp;problem=1226&amp;mosmsg=Submission%20received%20with%20ID%2014282250">Link</a> 耗时：0.028s</p>
</blockquote>
<p>一道简单的动态规划，主要思路就是：</p>
<blockquote>
<p><strong>用f[i,j]表示到达(i,j)的最长路径的长度。</strong>找到每个最高点，从其开始向四周的低处搜索。如果该点已搜过并且f值大于当前长度则退出回溯。直到达到某个最低点为止。</p>
</blockquote>
<p>不多说了，直接上代码：</p>
<pre><code>const
    delta :array [1..4, 1..2] of integer = ((-1, 0), (1, 0), (0, 1), (0, -1)); //四个方向向量
var
    _: Integer;
    name: string;
    n, m, i, j, x: Integer;
    ans: longint;
    map: array [0..101, 0..101] of integer;
    f: array [1..100, 1..100] of longint;

function max(x, y: longint): longint; inline;
begin
    if x&gt;y then exit(x) else exit(y);
end;

function can(x, y: integer): Boolean; inline; //判断是否是最高点
var
    i: Integer;
    tx, ty: integer;
begin
    can := true;
    for i := 1 to 4 do
    begin
        tx := x + delta[i, 1];
        ty := y + delta[i, 2];
        can := can and (map[x, y] &gt;= map[tx, ty]);
        if not can then break;
    end;
end;

procedure dp(x, y: integer; len: longint); //回溯进行动态规划
var
    i: Integer;
    tx, ty: integer;
begin
    inc(len);
    if f[x, y] &gt; len then exit;
    f[x, y] := len;
    ans := max(ans, len);
    for i := 1 to 4 do
    begin
        tx := delta[i, 1] + x;
        ty := delta[i, 2] + y;
        if (tx = 0) or (tx &gt; n) or (ty = 0) or (ty &gt; m) then continue;
        if map[x, y] &lt;= map[tx, ty] then continue;
        dp(tx, ty, len);
    end;
end;

procedure ReadAndProcessName; //处理那行该死的名字！！
var
    s: string;
    i: integer;
begin
    readln(s);
    i := 1;
    name := '';
    n := 0;
    m := 0;
    while s[i] &lt;&gt; ' ' do
    begin
        name := name + s[i];
        inc(i);
    end;
    inc(i);
    while s[i] &lt;&gt; ' ' do
    begin
        n := n * 10 + ord(s[i]) - ord('0');
        inc(i);
    end;
    inc(i);
    while i &lt;= length(s) do
    begin
        m := m * 10 + ord(s[i]) - ord('0');
        inc(i);
    end;
end;

begin
    assign(input, 'main.in');reset(input);
    assign(output, 'main.out');rewrite(output);
    readln(_);
    while _&gt;0 do
    begin
        dec(_);
        fillchar(map, sizeof(map), 0);
        ReadAndProcessName;

        for i := 1 to n do
            for j := 1 to m do
            begin
                read(x);
                map[i, j] := x+1;
            end;
        readln;

        fillchar(f, sizeof(f), 0);
        ans := 0;
        for i := 1 to n do
            for j := 1 to m do
                if can(i, j) then
                    dp(i, j, 0);
        writeln(name, ': ', ans);
    end;
    close(input);close(output);
end.
</code></pre>
