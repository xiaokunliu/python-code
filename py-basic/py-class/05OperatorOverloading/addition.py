#!/usr/bin/env python
# -*- coding: UTF-8 -*-


"""
__radd__ and __iadd__
"""

# __radd__ ：right side addition

class Counter:
	def __init__(self, value = 0):
		self.data = value

	def __radd__(self, other):
		if isinstance(other,Counter):
			print("counter data[%s] radd [%d]..." % (self.data,other.data))
		elif isinstance(other,int):
			print("counter data[%s] radd [%d]..." % (self.data, other))
		return self.data + other

	def __add__(self, other):
		if isinstance(other,Counter):
			print("counter data[%s] add [%d]..." % (self.data,other.data))
		elif isinstance(other,int):
			print("counter data[%s] add [%d]..." % (self.data, other))
		return self.data + other


class Counter1:
	def __init__(self, value = 0):
		self.__data = value

	# def __add__(self, other):
	# 	print("[%s] add ..." % self.__data)
	# 	return self.__data + other
	#
	# def __radd__(self, other):
	# 	print("[%s] radd ..." % self.__data)
	# 	return self.__add__(other)  # 等价于 self + other

	def __iadd__(self, other):
		print("call iadd method...")
		self.__data += other
		return self

	def get_value(self):
		return self.__data


class Counter2:
	def __init__(self, value = 0):
		self.data = value

	def __add__(self, other):
		print("[%s] add ..." % self.data)
		# return self + other
		return self.__add__(other)  # 等价于 self + other

	__radd__ = __add__


class NumberCounter:
	def __init__(self,value = 0):
		self.value = value

	def __iadd__(self, other):
		self.value += other     # self.value 是具体值
		return self             # Usually returns self


# def test_radd():
# 	# r = Counter()
# 	# # q = r + 1024       # call add, instance +
# 	# # print("q is %d" % q)
# 	# p = 1024 + r       # call radd, + instance
# 	# print("the p is %d" % p)
# 	a = Counter(2)
# 	b = Counter(4)
# 	sum = a + b         # a + b ==> (2 + other)2 + b ==> (4 + other)4 + 2
# 	print(sum)


# def test_number():
# 	num = NumberCounter()
# 	num += 2
# 	print(num.value)


def test_radd2():
	c = Counter1(3)
	# c1 = c + 2
	# print(c1)
	# c2 = 4 + c
	# print(c2)
	c+=8
	print(c.get_value())

if __name__ == '__main__':
    # test_radd()
	# test_number()
	test_radd2()