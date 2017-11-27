#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
异常基础
1. 异常的作用

2. 异常如何定义

异常语句类型
try/except
Catch and recover from exceptions raised by Python, or by you.
try/finally
Perform cleanup actions, whether exceptions occur or not.
raise
Trigger an exception manually in your code.
assert
Conditionally trigger an exception in your code.
with/as
Implement context managers in Python 2.6, 3.0, and later (optional in 2.5).

异常扮演的角色
Error handling:错误处理机制，在代码使用try的语句块抓住并响应异常错误信息
Event notification:事件通知，即当我们应用程序在传入数据并进行数据处理过程中，针对不合法的事件我们是采取抛出异常而不是返回一个表示不合法的数据结果
Special-case handling：在异常处理器处理程序个别极端情况，可以通过assert来检查条件是否如我们的预期值一样
Termination actions:即保证程序中的资源能够在异常发生之后正常关闭
Unusual control flows:不正常的控制流，使用raise抛出异常信息
"""
