---
layout: post
title: UVa12186 Another Crisis && [Dynamic Arrays in Pascal]
date: 2014-09-27 16:26:32.000000000 +08:00
categories: 编程
tags:
- UVa
- 信息学竞赛
---
> 链接：[Link](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&amp;Itemid=8&amp;category=243&amp;page=show_problem&amp;problem=3338) 耗时：0.586s 

昨晚做的太急了，没时间写总结，正好下午有空，补上。

这是一道典型的树形动态规划，不是很难，但十分坑语言。思路大致如下：

对于第i个节点，用d(i)表示其上诉所需的最小工人数。若i为叶节点，则d(i)=1；否则，遍历求出i的子节点所对应的d值，并由小到大排序，取出最小的几个相加，即为d(i)。

很容易想到用递归来实现。但对于“子节点的d值的排序”实现起来却十分困难：因为事先不知道有多少个数。当然啦，如果是C++组，用vector可以轻松搞定，可至于P党，实现起来却难上加难。思来想去，决定试试Pascal的动态数组。磕磕碰碰调了近1个小时，终于AC了。

Code:

```pascal
//Accepted
var
    tree: array [0..100000] of array of int64;
    T: Integer;
    f: array [0..100000] of int64;
    i,l,n,x:longint;

function min(x,y: int64): int64;
begin
    if x&lt;y then exit(x) else exit(y);
end;

procedure sort(var arr: array of int64;l,r:longint); overload;
var
  i,j:longint;
  m,t: int64;
begin
  i := l;
  j := r;
  m := arr[(l+r) &gt;&gt; 1];
  repeat
    while arr[i]&lt;m do inc(i);
    while arr[j]&gt;m do dec(j);
    if i&lt;=j then
    begin
      t := arr[i];
      arr[i] := arr[j];
      arr[j] := t;
      inc(i);
      dec(j);
    end;
  until i&gt;j;
  if i&lt;r then sort(arr, i, r);
  if l&lt;j then sort(arr, l, j);
end;

procedure sort(var arr: array of int64); overload;
begin
  sort(arr, low(arr), high(arr));
end;
function dp(x: longint): int64;
var
  arr: array of int64;
  l,i, num: longint;
begin
    if f[x] &lt;&gt; 0 then
    begin
        dp := f[x];
        exit;
    end;
    if length(tree[x]) = 0 then
    begin
      dp := 1;
      f[x] := 1;
      exit;
    end;
    l := length(tree[x]);
    SetLength(arr, l);
    for i := Low(tree[x]) to High(Tree[x]) do
      arr[i] := dp(tree[x][i]);
    Sort(arr);
    num := (l*T-1) div 100+1;
    for i := Low(arr) to num-1 do
      f[x] := f[x] + arr[i];
    dp := f[x];
end;

begin
    assign(input, 'main.in');reset(input);
    assign(output,'main.out');rewrite(output);
    readln(n, T);
    while n&gt;0 do
    begin
        fillchar(f, sizeof(f), 0);
        fillchar(tree, sizeof(tree), 0);
        for i := 1 to n do
        begin
            read(x);
            SetLength(tree[x], length(tree[x])+1);
            tree[x][high(tree[x])] := i;
        end;
        readln;
        dp(0);
        writeln(f[0]);
        readln(n, T);
    end;
    close(input); close(output);
end.
```

## Dynamic Arrays

这里，再总结一下动态数组的用法。

 1. 定义：`a: array of [type];`
 2. 设置长度： `SetLength(a, 10);`
 3. 长度加一： `SetLength(a, Length(a)+1);`
 4. 取得最大、最小下标： `High(a)`, `Low(a)`

事实上，从[1.1](http://freepascal.org/docs-html/ref/refsu18.html#x42-480003.3.1)版本开始FPC就支持Dynamic Arrays了。所以在NOIP竞赛中我们大可放心使用。
