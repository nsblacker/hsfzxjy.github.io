---
layout: post
title: LCA树上倍增
permalink: /lca-tree-multiplier/
date: 2014-11-02 16:23:13.000000000 +08:00
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
<pre><code>var
    a: array [1..100, 1..100] of boolean;
    depth: array [1..100] of longint;
    father: array [1..100, 0..16] of longint;
    n, m, i, x, y: longint;
    root: longint;

procedure dfs(x: longint);
var
    i: longint;
    j: longint;
begin
    depth[x] := depth[father[x][0]]+1;
    j := 1;
    while 1&lt;&lt;j&lt;=depth[x]-1 do
    begin
        father[x][j] := father[father[x][j-1]][j-1];
        inc(j);
    end;
    for i := 1 to n do
    begin
        if not a[x][i] or (father[x][0] = i) then continue;
        father[i][0] := x;
        dfs(i);
    end;
end;

procedure swap(var x, y: longint);
var
    t: longint;
begin
    t := x;
    x := y;
    y := t;
end;

function lca(x, y: longint): longint;
var
    t, j: longint;
begin
    if depth[x] &lt; depth[y] then
        swap(x, y);

    t := depth[x] - depth[y];
    for j := 0 to 15 do
        if t and (1&lt;&lt;j) &lt;&gt; 0 then
            x := father[x][j];
    if x = y then
        exit(x);
    for j := 15 downto 0 do
        if father[x][j] &lt;&gt; father[y][j] then
        begin
            x := father[x][j];
            y := father[y][j];
        end;
    lca := father[x][0];
end;

begin
    assign(input, 'main.in'); reset(input);
    assign(output, 'main.out'); rewrite(output);

    read(n, m);
    for i := 1 to m do
    begin
        read(x, y);
        a[x, y] := true;
        a[y, x] := true;
    end;
    read(root);
    father[root][0] := root;
    dfs(root);
    while not eof do
    begin
        read(x, y);
        writeln(lca(x, y));
    end;


    close(input); close(output);
end.
</code></pre>
