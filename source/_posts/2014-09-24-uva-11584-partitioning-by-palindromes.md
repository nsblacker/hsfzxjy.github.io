---
layout: post
title: UVa11584 Partitioning by Palindromes
date: 2014-09-24 22:00:14.000000000 +08:00
categories:
- UVa
- 信息学竞赛
- 编程
---
<blockquote>
<p>这是一道区间型DP，转移方程很简单，但在实现的过程中却遇见了很多坑，在此记录一下。 链接：<a href="http://uva.onlinejudge.org/index.php?option=com_onlinejudge&amp;Itemid=8&amp;page=show_problem&amp;category=27&amp;problem=2631&amp;mosmsg=Submission%20received%20with%20ID%2014256745">Link</a> 耗时：0.368s</p>
</blockquote>
<p>容易想到，前i个数的划分情况可以由1,2,3...,i-1的划分情况来决定。因此很容易得到状态转移方程：</p>
<blockquote>
<p>d[i] = min(d[i], d[j]+1) //j = 0, 1, 2...n-1 并且 s[j+1, i]为回文串，初始条件：d[i] = i。</p>
</blockquote>
<p>d[i]表示前i项的最小划分。这样一来状态转移的复杂度就为O($n^2$)。<br />
但状态转移的判断呢？“回文串”是一个复杂的条件，判断一个串是否为回文串需要将该串至少遍历一遍。这样一来时间复杂度就上升为O($n^3$)了。而事实上在这种算法中有许多无谓的计算，因此我们可以先对字符串进行预处理：用huiwen[i,j]表示s[i,j]是否为回文串（奇怪的名字。。。）。如此一来，时间复杂度就降为O($n^2$)了。</p>
<p>Code：</p>
<pre><code>var
    s: AnsiString;
    n, _, i, j, l: integer;
    huiwen: array [1..1000, 1..1000] of boolean; //s[i,j]是否为回文串
    dp: array [0..1000] of integer; //一定从0开始，否则当整串为回文串时就考虑不到了。

function min(x,y: integer): integer;
begin
    if x&lt;y then exit(x) else exit(y);
end;

procedure process(i,j: integer); //对回文串进行预处理
var
    mid: Integer;
    x,y: integer;
begin
    if j = i then
    begin
        huiwen[i,j] := true;
        exit;
    end;
    mid := i + (j-i+1) shr 1;
    x := i;
    y := j;
    while (x &lt;= mid) and (s[x] = s[y]) do
    begin
        inc(x);
        dec(y);
    end;
    huiwen[i, j] := x &gt; mid;
end;

begin
    //assign(input, 'main.in'); reset(input);
    //assign(output, 'main.out'); rewrite(output);
    readln(n);
    for _ := 1 to n do
    begin
        readln(s);
        l := length(s);
        //Pre-process
        fillchar(huiwen, sizeof(huiwen), 0);
        for i := 1 to l do
            for j := i to l do //一定是从i开始，这个错卡了我很久。
                process(i, j);
        //DP
        for i := 1 to l do
        begin
            dp[i] := i;
            for j := 0 to i-1 do
                if huiwen[j+1, i] then
                    dp[i] := min(dp[i], dp[j]+1);
        end;
        write(dp[l]);
        {if _ &lt;&gt;n then }writeln; //吐槽一下：一开始我还谨慎地加上这句以避免行末回车，没想到UVa居然报错了。。看来UVa的比较算法还有待改进啊。
    end;

    //close(input);close(output);
end.
</code></pre>
