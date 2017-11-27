#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
字符串：__str__ & __repr__
"""

#  __str__ 与 __repr__区别
# 1.  __str__ is tried first for the print operation and the str built-in function
# It generally should return a user-friendly display.

# 2. __repr__is used in all other contexts:
# for interactive echoes,the repr function,and nested appearances,
# as well as by print and str if no __str__ is present.
# It should generally return an as-code string that could be used to re-create the object,
# or a detailed display for developers

# __repr__
"""
If defined, __repr__ (or its close relative, __str__) is called automatically
when class instances are printed or converted to strings.
These methods allow you to define a better display format for your objects than the default instance display
"""


class DisplayClass:
	"""
	__repr__ is used everywhere, except by print and str when a __str__ is defined.
	__str__ to support print and str exclusively.
	"""
	def __repr__(self):
		return "display __repr__ class"

	def __str__(self):
		return "display __str__ class"


def test_repr():
	d = DisplayClass()
	print(d)    # if __str__ is defined,then use __str__ method,__str__ > __repr__ 方法 > 对象地址（> 这里表示优先）
# 	显示调用repr
	print(repr(d))
# 	显示调用str
	print(str(d))
# 	使用命令行
	"""
	>>> d                   repr
	>>> print(d)            str
	>>> print(repr(d))      repr
	>>> print(str(d))       str
	"""




if __name__ == '__main__':
    test_repr()





