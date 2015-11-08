---
layout: post
title: UVa1647 Computer Transformation
date: 2014-10-24 18:50:30.000000000 +08:00
categories:
- 编程
tags:
- 数列
- 高精度
- UVa
- 信息学竞赛
- 数学
- 数论
---
> 链接：[Link](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=825&page=show_problem&problem=4522) 耗时：0.679s

## **分析**

本质上，这是一道求数列通项的题目。我们列出前几个字符串：  
$$01,$$  
$$1001,$$  
$$01101001,$$  
$$1001011001101001,$$  
$$\ldots$$  
如果用$S_i$表示第i个字符串中“00”的个数，则有：  
$$S_1=0,\ S_2=1,\ S_3=1,\ S_4=3,\ S_5=5,\ S_6=11,\ldots$$  
经过观察可以发现有如下规律：  
$$S_n=2\times S_{n-1}+{(-1)}^n$$  
求通项就简单了，换个元即可：  
$$S_n=\frac{1}{3}[{(-1)}^n+2^{n-1}]$$  
程序采用高精度实现。

## **Code**

    const
        JINDU = 100000;
    var
        n: Integer;
    //在数字前补0
    procedure PrintANumber(x: longint);
    var
        t: longint;
    begin
        if x = 0 then
            write('00000')
        else
        begin
            t := JINDU;
            while t > x * 10 do 
            begin
                write(0);
                t := t div 10;
            end;
            write(x);
        end;
    end;

    var
        ans: array [1..300] of longint;
        len, i: integer;
    //计算2^(n-1)
    procedure calc2;
    var
        i, x, t, mul: longint;
    begin
        len := 1;
        ans[1] := 1;
        t := n-1;
        while t > 0 do
        begin
            if t < 6 then 
                mul := 1 << t
            else 
                mul := 64;
            x := 0;
            for i := 1 to len do
            begin
                ans[i] := ans[i] * mul + x;
                x := ans[i] div JINDU;
                ans[i] := ans[i] mod JINDU;
            end;
            if x > 0 then
            begin
                inc(len);
                ans[len] := x;
            end;
            dec(t, 6);
        end; 
    end;
    //除以3
    procedure div3;
    var
        i, x, t: longint;
    begin
        i := len;
        x := 0;
        while i > 0 do
        begin
            t := (x * JINDU + ans[i]);
            ans[i] := t div 3;
            x := t mod 3;
            dec(i);
        end;
        while ans[len] = 0 do dec(len);
    end;

    begin
        assign(input, 'main.in'); reset(input);
        assign(output, 'main.out'); rewrite(output);

        while not eof do
        begin
            readln(n);
            if n=1 then   //特殊情况处理
            begin
                writeln(0);
                continue;
            end;
            fillchar(ans, sizeof(ans), 0);
            calc2;
            if odd(n) then
                dec(ans[1])
            else
                inc(ans[1]);
            div3;
            write(ans[len]);
            for i := len-1 downto 1 do 
                PrintANumber(ans[i]);
            writeln;
        end;

        close(input); close(output);
    end.