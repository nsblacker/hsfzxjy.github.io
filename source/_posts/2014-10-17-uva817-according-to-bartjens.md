---
layout: post
title: UVa817 According to Bartjens
date: 2014-10-17 20:05:06.000000000 +08:00
categories:
- UVa
- 信息学竞赛
- 编程
tags:
- 搜索
---
<blockquote>
<p>链接：<a href="http://uva.onlinejudge.org/index.php?option=com_onlinejudge&amp;Itemid=8&amp;page=show_problem&amp;category=10&amp;problem=758&amp;mosmsg=Submission%20received%20with%20ID%2014367065">Link</a> 状态：<strong>WA</strong></p>
</blockquote>
<h2><strong>分析</strong></h2>
<p>做了两个小时，很可惜最终还是WA了。非常奇怪——和网上的C++代码运行结果完全一样，但却WA了。不过，在这里我还是记录一下解题的过程。<br />
这道题数据量很小，直接爆搜每个空位，用*, +, -, #0来代表符号或不填。</p>
<h2><strong>Code</strong></h2>
<pre><code>const
    operators: array [1..4] of char = ('*', '+', '-', #0); //符号
var
    s: string;
    _, n: integer;
    op: array [0..10] of char;
    yes: Boolean;

function toValue(ch: char): integer;
begin
    exit(ord(ch) - ord('0'));
end;

procedure calcAndPrint; 
var
    numtop, opstop: Integer;  //数字栈，符号栈
    num: array [1..10] of longint;
    ops: array [1..10] of char;
    i: integer;
begin
    i := 1;
    numtop := 1;
    num[numtop] := toValue(s[1]);
    opstop := 0;
    while i &lt;= n do
    begin
        while (i &lt; n) and (op[i] = #0) do
        begin
            inc(i);
            num[numtop] := num[numtop] * 10 + toValue(s[i]);
        end;
        if (op[i] in ['+', '-']) or (i &gt;= n) then
        begin
            while (opstop &gt; 0) and (ops[opstop] = '*') do
            begin
                dec(opstop);
                num[numtop - 1] := num[numtop] * num[numtop -1];
                dec(numtop);
            end;
        end;
        if i &gt;= n then break;
        inc(opstop);
        ops[opstop] := op[i];
        inc(i);
        inc(numtop);
        num[numtop] := toValue(s[i]);
    end;
    i := 1;
    while i &lt; numtop do
    begin
        if ops[i] = '+' then
            num[i+1] := num[i] + num[i+1]
        else
            num[i+1] := num[i] - num[i+1];
        inc(i);
    end;
    if (num[numtop] = 2000) and (opstop &gt; 0) then
    begin
        yes := True;
        write('  ');
        for i := 1 to n do
        begin
            write(s[i]);
            if op[i] &lt;&gt; #0  then
                write(op[i]);
        end;
        writeln('=');
    end;
end;

procedure dfs(t: integer); //搜索第t个位置
var
    i: Integer;
    ch: char;
begin
    if t = n then
    begin
        calcAndPrint;
        exit;
    end;
    for i := 1 to 4 do
    begin
        ch := operators[i];
        if (ch = #0) and (s[t] = '0') and ((t = 1) or (t &gt; 1) and (op[t-1] &lt;&gt; #0)) then continue;
        op[t] := ch;
        dfs(t+1);
    end;
end;

var
    i: Integer;

begin
    assign(input, 'main.in'); reset(input);
    assign(output, 'main.out'); rewrite(output);

    readln(s);
    _ := 0;
    while not eof and (s[1] &lt;&gt; '=') do
    begin
        i := 1;
        while not (s[i] in ['0'..'9', '=']) do
        begin
            inc(i);
        end;
        delete(s, 1, i-1);
        n := pos('=', s) - 1;
        inc(_);
        writeln('Problem ', _);
        yes := False;
        fillchar(op, sizeof(op), 0);
        dfs(1);
        if not yes then
            writeln('  IMPOSSIBLE');
        readln(s);
    end;

    close(input); close(output);
end.
</code></pre>
