---
layout: post
title: UVa12219 Common Subexpression Elimination
date: 2014-10-06 00:20:18.000000000 +08:00
categories: 编程
tags:
- UVa
- 信息学竞赛
---
<blockquote>
<p>链接：<a href="http://uva.onlinejudge.org/index.php?option=com_onlinejudge&amp;Itemid=8&amp;page=show_problem&amp;problem=3371">Link</a> 状态：<strong>Runtime Error</strong></p>
</blockquote>
<h2>前言</h2>
<p>这题做的可真够久的，整整三个小时。但即便如此，还是只过了一部分的点，另一部分报运行时错误——估计是哈希表设计的不太好。但这确实是一道好题，因此，在睡觉前决定记录一下。</p>
<h2>分析</h2>
<p>很容易便想到：用一个三元组$(x,y,z)$表示节点，表示内容为x的节点下跟着标号为y和z的左右子树。这样一来，一类相同的子树便可以唯一确定了，而不必每构造一棵子树就把整棵树遍历一遍。<br />
对于三元组的储存，刚开始图方便，用了数组。查找也是用了$O(n)$的线性查找。磕磕碰碰写了两个多小时然后兴冲冲地提交，结果TLE了…………没办法，只好又花了半个小时写了一个哈希表，然后就是上文说过的情况了：<strong>Runtime Error204</strong>。可能是哈希数组过大的原因，日后再微调一下，今天实在是没有脑子了。</p>
<h2>Code</h2>
<pre><code>const
  maxn = 20000;
type
  NodeRec = record
    Value: string;
    l, r, index: longint;
  end;
  Node = record
     left, right: longint;   //Index of left and right child in the `tree` array, -1 for none.
     Rec: NodeRec;
     index: longint;
  end;
  //以下为哈希表的定义
  _PNode = ^_Node;
  _Node = record
    n: Node;
    next: _PNode;
  end;

  HashTable = object
    arr: array [0..maxn] of _PNode;
    function hash(n: NodeRec): longint;
    procedure add(n: Node);
    procedure clear;
    function find(n: NodeRec): longint;
  end;

procedure HashTable.clear;
var
  i: longint;
  p, q: _PNode;
begin
  for i := 0 to maxn do
  begin
    p := arr[i];
    while p&lt;&gt;nil do
    begin
      q := p^.next;
      dispose(p);
      p := q;
    end;
  end;
  fillchar(arr, sizeof(arr),0);
end;

function cmp(r1, r2: NodeRec): Boolean;
begin
  cmp := (r1.l = r2.l) and (r1.r = r2.r) and (r1.Value = r2.Value);
end;

function HashTable.hash(n: NodeRec): longint;
var
  i: longint;
begin
  hash := 0;
  for i := 1 to length(n.Value) do
    hash := (hash*5 + ord(n.Value[i]) - ord('a')) mod maxn;
  hash := (hash + n.l * 10 + n.r * 5) mod maxn;
end;

procedure HashTable.add(n: Node);
var
  h: longint;
  p, q: _PNode;
begin
  h := hash(n.rec);
  new(q);
  fillchar(q^, sizeof(_Node), 0);
  q^.next := arr[h];
  q^.n := n;
  arr[h] := q;
end;

function HashTable.find(n: NodeRec): longint;
var
  p: _PNode;
begin
  find := -1;
  p := arr[hash(n)];
  while (p&lt;&gt;nil) and not cmp(n, p^.n.rec) do p := p^.next;
  if p &lt;&gt; nil then
    find := p^.n.index;
end;
//哈系表定义结束
var
  inputs: Ansistring;
  _: longint;
  tree: array [1..50001] of Node;
  cur: longint;              //The current pointer of the input string.
  num: longint;              //The current number of the `tree` array.
  ls: longint;
  t: longint;
  tot: longint;
  ht: HashTable;

function build: longint; //建树
label lb;
var
  rec: NodeRec;
  i,j,l,r: longint;
begin
  l := 0;
  r := 0;
  fillchar(rec, sizeof(rec), 0);
  inc(tot);
  rec.index := tot;
  while (cur&lt;=ls) and (inputs[cur] in ['a'..'z']) do
  begin
    rec.Value := rec.Value+inputs[cur];
    inc(cur);
  end;
  if cur&gt;ls then goto lb;    //。。。这里被迫跳转控制流，由于实在不想多谢，就用了臭名昭著的label
  if inputs[cur] = '(' then
  begin
    inc(cur);
    l := build();
    rec.l := tree[l].rec.index;
    inc(cur);
    r := build();
    rec.r := tree[r].rec.index;
    inc(cur);
  end;
  j := ht.find(rec);
  if j&gt;0 then
  begin
    dec(tot);
    exit(j);
  end
  else
  begin
lb:
    inc(num);
    tree[num].left := l;
    tree[num].right := r;
    tree[num].rec := rec;
    tree[num].index := num;
    ht.add(tree[num]);
    exit(num);
  end;
end;

procedure print(n: longint);
begin
  if tree[n].rec.index &gt; t then
  begin
    write(tree[n].rec.Value);
    t := tree[n].rec.index;
  end
  else
  begin
    write(tree[n].rec.index);
    exit;
  end;
  if tree[n].right = 0 then
    exit;
  write('(');
  print(tree[n].left);
  write(',');
  print(tree[n].right);
  write(')');
end;
begin
  assign(input, 'main.in'); reset(input);
  assign(output, 'main.out'); rewrite(output);
  readln(_);
  fillchar(ht.arr, sizeof(ht.arr),0);
  while _&gt;0 do
  begin
    dec(_);
    readln(inputs);
    fillchar(tree, sizeof(tree), 0);
    ht.clear;
    ls := length(inputs);
    cur := 1;  num := 0; tot := 0;
    build;
    t := 0;
    print(num);
    writeln;
  end;
  close(input); close(output);
end.
</code></pre>
