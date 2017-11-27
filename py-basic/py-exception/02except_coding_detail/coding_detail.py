#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
异常编写细节
1. try/except/else 语句
语法：
try:
	statements
except name1:
	statements
except (name2, name3):
	statements
except name4 as var:
	statements
except:     # try all exceptions
	statements
else:
	statements

工作流程：
1.当在try语句块中发生异常时，异常类型将会匹配except对应的name,然后根据对应的name分配对应的异常类对象，执行statement中的语句
2.当在try语句块中发生异常但没有在except中匹配到对应的name,python将会查询其他的异常直至进程最高级别的异常并退出程序，打印出默认的异常信息
3.如果try语句正常执行，那么最后也将会执行else语句
It inspects the except clauses from top to bottom and left to right, and runs the statements under the first one that matches.'


抓住任意和所有异常：
1.except clauses that list no exception name (except:) catch all exceptions not previously listed in the try statement
2.except clauses that list a set of exceptions in parentheses (except (e1, e2, e3):) catch any of the listed exceptions.

# py3.x 使用Exception，但Exception不包括系统异常
try:
	action()
except:
	...

# 同上
try:
	action()
except Exception:
	...


2. try/finally 语句

1)If an exception does not occur while the try block is running,
Python continues on to run the finally block, and then continues execution past the try statement.

2)If an exception does occur during the try block’s run,Python still comes back and runs the finally block,
but it then propagates the exception up to a previously entered try or the top-level default handler;
the program does not resume execution below the finally clause’s try statement.
That is, the finally block is run even if an exception is raised, but unlike an except,
the finally does not terminate the exception—it continues being raised after the finally block runs.


3. try/except/finally

4. raise 语句
5. assert 语句
6. with/as 上下文管理器
"""


