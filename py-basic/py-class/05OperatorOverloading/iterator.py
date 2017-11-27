#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 迭代器对象__iter__ & __next__

# =======================================自定义迭代器===================================
from __future__ import print_function   ## 兼容py3.x

class Squares:
	# 类的生成器
	def __init__(self, start, stop):
		self.value = start - 1
		self.stop = stop

	def __iter__(self):
		print("call iter ...")
		return self

	def __next__(self):
		if self.value == self.stop:
			raise StopIteration
		print("call next for value:", end='')
		# print("call next for value..")
		self.value += 1
		return self.value ** 2


def test():
	X = Squares(1, 5)
	S = iter(X)
	# 迭代器不支持使用索引
	X[1]    # TypeError: 'Squares' object does not support indexing


def test_for():
	# 循环使用迭代器
	for item in Squares(2, 9):  # 调用Squares.__iter__,
		print(item)             # 调用Squares.__next__


def test_single():
	# 逐个调用迭代器
	X = Squares(2, 9)
	# 显示将X转换为迭代器对象，条件是该对象有实现__iter__，只需调用一次
	I = iter(X)             # Squares.__iter__
	print(next(I))          # 调用Squares.__next__
	print(next(I))          # 调用Squares.__next__


def single_scan():
	print("start single scan ....")
	X = Squares(1, 2)
	# 首次会执行__iter__对迭代器进行初始化，
	# 并且每次执行将调用__next__将数据返回并保存当前迭代器的状态，
	list1 = [n for n in X]
	print(list1)
	# 迭代器已经记录自己的状态，即当前是不可继续往下迭代的状态，因此list是一个空的列表
	list2 = [n for n in X]       # now list2 is empty
	print(list2)
	print("end single scan ....")


def mutil_scan():
	print("start mutil scan ... ")
	# 方式一：每次都是重新创建新的迭代器来进行迭代
	list1 = [n for n in Squares(1,2)]
	print(list1)
	list2 = [n for n in Squares(1, 2)]
	print(list2)

	# 方式二 转换为列表并用列表解析器来转换
	list_iter = list(Squares(1,2))
	list3 = [n for n in list_iter]
	print(list3)
	list4 = [n for n in list_iter]
	print(list4)
	print("end mutil scan ...")


def fn_generator(start,end):
	# 函数的生成器，与类的迭代器比较，函数生成器创建的时候，明确指出迭代的状态以及符合协议的迭代方法
	for index in range(start,end):
		yield index**2      # 每次调用一次就保持状态并挂起等待继续下一次的调用，类似于类迭代器中的__next__方法


def test_fn_gen():
	for item in fn_generator(1,5):
		print(item)


def test_express_gen():
	# 生成器表达式
	tuple1 = (n ** 2 for n in range(1,5))
	print(tuple1)

# =======================================一个对象多个迭代器
# 对象单个迭代器对象,即不能作为类似于上述的操作,python有map、zip、函数生成器以及生成器表达式
# 对象多个迭代器对象,即可以来操作上述的动作，python有list、string、range
# 使用类的迭代器，我们可以自定义迭代器是单例还是多例


class SingleIterator:
	def __iter__(self):
		return self


class MutilIterator:
	def __init__(self, wrapper):
		self.__wrapper = wrapper

	def __iter__(self):
		print("call iter method ...")
		return DefineIterator(self.__wrapper)


class DefineIterator:
	def __init__(self, wrapped):
		self.wrapped = wrapped
		self.offset = 0

	def __next__(self):
		if self.offset >= len(self.wrapped):
			raise StopIteration
		else:
			item = self.wrapped[self.offset]
		self.offset += 1
		return item

# 	py2.x 没有next方法,python2.x 和 python3.x 都可用
	next = __next__


def test_mutil_object_iter():
	"""
	之前说的迭代器对象都会保持状态，为什么这里使用同一个对象的迭代器却没有保存状态,原因是在新的循环中创建了新的迭代器对象
	:return:
	"""
	S = "abcd"
	# 索引遍历操作
	M = MutilIterator(S)
	for x in M:
		print("recreate iterator for y loop by creating M iterator ...")
		for y in M:
			print(x+y,end = ",")
		print("")

# 小结：迭代器是一个很强大的工具，能够让我们创建自定义迭代器对象来完成自己的业务需求，
# 比如支持大型数据库在多个游标中进行数据查询时获取迭代

# __iter__ 与 yield的使用


class MixIterator:
	def __init__(self,start,stop):
		self.__start = start
		self.__stop = stop

	def __iter__(self):
		for index in range(self.__start,self.__stop+1):
			yield index**2      # 返回一个生成器对象，通过调用next()来显示值


def test_mix_iterator():
	iterator = MixIterator(1,5)
	list1 = [index for index in iterator]
	list2 = [index for index in iterator]
	print(list1)
	print(list2)
	# for item in list1:
	# 	print(item)


def test_gen():
	g = fn_generator(1,3)
	print(g.__iter__() == g)    ## True


# 对于上述要实现多个迭代器对象可以进行以下改进

class MutilIterator2:
	def __init__(self,wrapper):
		self.__wrapper = wrapper

	def __iter__(self):
		print("call iter ... ")
		offset = 0
		while offset < len(self.__wrapper):
			item = self.__wrapper[offset]
			offset+=1
			yield item


def test_mutil2_iterator():
	S = "abcd"
	M = MutilIterator2(S)
	for x in M:                        # 执行__iter__方法
		print("recall iter method ..")
		for y in M:                    # 执行__iter__方法，进入方法的时候offset又变为初始化
			print(x+y,end = ",")
		print()


if __name__ == '__main__':
	# test()
	# test_for()
	# test_single()
	# single_scan()
	# mutil_scan()
	# test_fn_gen()
	# test_mutil_object_iter()
	# test_mix_iterator()
    # test_gen()
    test_mutil2_iterator()

