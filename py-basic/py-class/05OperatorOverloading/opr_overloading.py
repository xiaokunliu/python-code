#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
运算符重载
1.基础
2.索引和切片操作，__getitem__ & __setitem__
3.索引迭代器，__getitem__
4.迭代器对象，__iter__ & __next__
5.成员关系，__contains__ , __iter__ & __getitem__
6.属性访问，__getattr__ & __setattr__
7.对象输出字符串，__repr__ & __str__
8.right-side(进行+,-,%,...)以及in-place(+=,-=,...)计算:__radd__ & __iadd__
9.调用将回调内置方法__call__,如aClass()创建对象实例的时候将会回调__call__方法
10.比较操作,__lt__,__gt__,__cmp__
11.boolean操作,__bool__ & __len__
12.对象销毁方法操作,析构函数,__del__
"""

# 基础
# Operator overloading lets classes intercept normal Python operations.
# Classes can overload all Python expression operators.
# Classes can also overload built-in operations such as printing,function calls,attribute access, etc.
# Overloading makes class instances act more like built-in types.
# Overloading is implemented by providing specially named methods in a class


# 索引和切片操作，__getitem__ & __setitem__
# 1.__getitem__

# 索引操作
# indexer.py  - 索引

# 切片操作
# slice.py
# 迭代器操作

# 2. __setitem__ 索引赋值操作

# 3. 迭代器对象__iter__ & __next__

# 自定义迭代器对象iterator.py  __iter__ & __next__

# 4. 成员关系 membership.py   __contains__ , __iter__ & __getitem__

# 5. 属性访问 attr.py  __getattr__ & __setattr__

# 7.对象输出字符串，__repr__ & __str__

# 8.right-side(进行+,-,%,...)以及in-place(+=,-=,...)计算:__radd__ & __iadd__

# 9.调用将回调内置方法__call__,如aClass()创建对象实例的时候将会回调__call__方法

# 10.比较操作,__lt__,__gt__,__cmp__

# 11.boolean操作,__bool__ & __len__

# 12.对象销毁方法操作,析构函数,__del__