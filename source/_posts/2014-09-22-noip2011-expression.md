---
layout: post
title: NOIP2011 表达式计算
date: 2014-09-22T13:57:50.000Z
categories: [编程]
tags: [信息学竞赛, 编程]
status: publish
type: post
published: true
---

> 记得11年的时候，觉得这道题爆难，根本无从下手。三年后再次回顾，终于AC了，就当是对表达式求值和动态规划的复习吧。

# 题目：[Link](http://codevs.cn/problem/1133/)

```cpp
// Accepted.
#include &lt;iostream&gt;
#define Mod 10007;
using namespace std;

typedef struct {
    long long v0;  //当前值为0的个数
    long long v1;  //当前值为1的个数
    char ch;  //当前字符
} vertex;

vertex f[100000];

void merge_sum(int p) {
    int w0 = f[p-1].v0 * f[p].v0;
    int w1 = f[p-1].v0*f[p].v1+f[p-1].v1*f[p].v0+f[p-1].v1*f[p].v1;
    f[p-1].v0 = w0 % Mod;
    f[p-1].v1 = w1 % Mod;
}

inline void merge_product(int p)  //处理当前的值和前一个值取'*'的操作
{
       int w0=f[p-1].v0*f[p].v0+f[p-1].v0*f[p].v1+f[p-1].v1*f[p].v0;
       int w1=f[p-1].v1*f[p].v1;
       f[p-1].v0=w0%Mod;
       f[p-1].v1=w1%Mod;
}

int main()
{
    int n;
    cin>>n;
    f[0].v0=f[0].v1=1;
    while (n--)
    {
          now++;   //新建一个空位读入新符号
          cin>>f[now].ch;
          f[now].v0=f[now].v1=1;  //初始化当前符号的前面的值(虽然')'除外,但也不影响)
          if (f[now].ch=='+')
          {
             if (f[now-1].ch=='*') //处理'*'
             {
                now--;
                merge_product(now);
                f[now]=f[now+1];
             }
             if (f[now-1].ch=='+') //处理'+'
             {
                now--;
                merge_sum(now);
                f[now]=f[now+1];
             }
          }
          if (f[now].ch=='*')
           if (f[now-1].ch=='*') //处理'*'
           {
              now--;
              merge_product(now);
              f[now]=f[now+1];
           }
          if (f[now].ch==')') //处理')'(比较麻烦)
          {
             now--;
             if (f[now].ch=='*')
             {
                merge_product(now);
                now--;
             }
             if (f[now].ch=='+')
             {
                merge_sum(now);
                now--;
             }
             now--;
             f[now].v0=f[now+1].v0;
             f[now].v1=f[now+1].v1;
             if (f[now].ch=='*')
             {
                merge_product(now);
                now--;
             }
          }
    }
    if (f[now].ch=='*')  //处理完了以后,可能还有残留的'*'和'+'
    {
       merge_product(now);
       now--;
    }
    if (f[now].ch=='+')
    {
       merge_sum(now);
       now--;
    }
    cout<<f[0].v0;
    return 0;
}
```
