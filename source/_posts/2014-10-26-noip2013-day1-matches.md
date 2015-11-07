---
layout: post
title: NOIP2013 Day1 火柴排队：快速求逆序对
permalink: /noip2013-day1-matches/
date: 2014-10-26 11:42:23.000000000 +08:00
categories:
- 编程
tags:
- 归并排序
- 逆序对
- 信息学竞赛
---
<h2><strong>题目</strong></h2>
<blockquote>
<p>涵涵有两盒火柴，每盒装有 n 根火柴，每根火柴都有一个高度。现在将每盒中的火柴各自排成一列，同一列火柴的高度互不相同，两列火柴之间的距离定义为：$\sum_{i=1}^{n}{(a_i-b_i)^2}$<br />
  ，其中 ai表示第一列火柴中第 i 个火柴的高度，bi表示第二列火柴中第 i 个火柴的高度。<br />
  每列火柴中相邻两根火柴的位置都可以交换，请你通过交换使得两列火柴之间的距离最小。请问得到这个最小的距离，最少需要交换多少次？如果这个数字太大，请输出这个最小交换次数对 99,999,997 取模的结果。</p>
</blockquote>
<h2><strong>分析</strong></h2>
<p>这真是一道好题——断断续续想了几天才完全AC。<br />
事实上，由排序不等式可知：</p>
<blockquote>
<p><strong>当$a_i, b_i$从小到大排序时，距离最小。</strong></p>
</blockquote>
<p>这是一个重要的信息。因此，我们只需把$a_i,b_i$进行排序，并把对应项“捆绑”成一项，再按$a_i$原有的顺序进行复原，此时，可以得到由%b_i$原先的下标组成的一个序列。也就是说，我们要求$1,2,\ldots,n$至少经过多少步才能变为该序列。这可以用逆序对来解决。<br />
只可惜，传统的逆序对算法时间复杂度为$O(n^2)$，这里n可达20,0000，一定会超时（<strong>事实上，只过了70%的点</strong>）。因此我们需寻求更好的算法。</p>
<h2><strong>用归并排序求逆序对</strong></h2>
<p>在归并排序的过程中，有一个步骤称为合并。在这个步骤中，需要轮流判断左右区间的第一个数的大小关系。注意到：<strong>左右区间已经有序，从而若左区间的第一个数大于右区间的第一个数，则左区间之后的所有数都大于右区间的第一个数</strong>，从而我们可以在合并时做一些修改：</p>
<pre><code>procedure nx(l, r: longint);
var
    mid, i, j, k: longint;
begin
    if l = r then
    begin
        tmp[l] := a[l];
        exit;
    end;
    mid := (l + r) shr 1;
    nx(l, mid);
    nx(mid+1, r);
    i := l;
    j := mid+1;
    k := l;
    while k &lt;= r do 
    begin
        if (j&gt;r) or (i&lt;=mid) and (a[i]&lt;=a[j]) then //注意这里为等号
        begin
            tmp[k] := a[i];
            inc(i);
        end
        else
        begin
            cnt := cnt + mid - i + 1; //加上逆序数
            tmp[k] := a[j];
            inc(j);
        end;
        inc(k);
    end;
    for i := l to r do 
        a[i] := tmp[i];
end;
</code></pre>
<p>这个算法复杂度为$O(nlogn)$，是一种比较理想的算法，实现起来也简单。但他有个缺点：<strong>会打乱原数组顺序</strong>。</p>
<h2><strong>原题代码</strong></h2>
<pre><code>//AC
const
    MODN = 99999997;
type
    rec = record value, index: longint; end;
    TArr = array [1..100000] of rec;
var
    n: longint;
    a, b, c, tmp: TArr;
    ok: Boolean;
    l, r, i, j: longint;
    cnt: int64;

procedure sort(var arr: TArr; l, r: longint);
var
    i, j: longint;
    m, t: rec;
begin
    i := l;
    j := r;
    m := arr[(i+j) shr 1];
    repeat
        while arr[i].value &lt; m.value do inc(i);
        while arr[j].value &gt; m.value do dec(j);
        if i &lt;= j then
        begin
            t := arr[i];
            arr[i] := arr[j];
            arr[j] := t;
            inc(i);
            dec(j);
        end;
    until i &gt;j;
    if i &lt; r then sort(arr, i, r);
    if l &lt; j then sort(arr, l, j);
end;

procedure nx(l, r: longint);
var
    mid, i, j, k: longint;
begin
    if l = r then
    begin
        tmp[l] := c[l];
        exit;
    end;
    mid := (l + r) shr 1;
    nx(l, mid);
    nx(mid+1, r);
    i := l;
    j := mid+1;
    k := l;
    while k &lt;= r do 
    begin
        if (j&gt;r) or (i&lt;=mid) and (c[i].index&lt;=c[j].index) then
        begin
            tmp[k] := c[i];
            inc(i);
        end
        else
        begin
            cnt := cnt + mid - i + 1;
            cnt := cnt mod MODN;
            tmp[k] := c[j];
            inc(j);
        end;
        inc(k);
    end;
    for i := l to r do 
        c[i] := tmp[i];
end;

begin
    assign(input, 'main.in'); reset(input);
    assign(output, 'main.out'); rewrite(output);

    readln(n);
    for i := 1 to n do
    begin
        read(a[i].value);
        a[i].index := i;
    end;
    for i := 1 to n do
    begin
        read(b[i].value);
        b[i].index := i;
    end;
    sort(a, 1, n);
    sort(b, 1, n);

    for i := 1 to n do
        c[a[i].index] := b[i];

    cnt := 0;
    nx(1, n);
    writeln(cnt);

    close(input); close(output);
end.
</code></pre>
