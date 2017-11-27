#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 索引和切片操作，__getitem__ & __setitem__
# indexer.py  - 索引


class Indexer:
	def __init__(self):
		print("call init ...")
		self.__data = [1,2,3]

	def __getitem__(self, index):           # index为索引值
		print("call getitem index...",end = "")
		return self.__data[index]

	def __setitem__(self, index, value):    # index恒为索引下标,value为值
		print("call setitem ...")
		print("key[%s]--value[%s]" % (index,value))
		self.__data.insert(index,value)


class Indexing:
	"""
	this method returns an integer value for an instance when needed and is used by built-ins that convert to digit strings
	py3.x 新增的内置方法，但是该操作不是表示索引操作，而是为一个对象实例返回一个整型数值,并且用于转换为数值字符串的内置操作
	"""
	def __index__(self):
		return 200


def test_index():
	# 设置值
	X = Indexer()
	# X[0] = 1  # 等价于Indexer.__setitem__(X,0,1)
	# X[1] = 2
	# X[2] = 3

	# 取值
	for i in range(3):
		print(X[i])  # 等价于Indexer.__getitem__(X,i)


def test_iterator():
	X = Indexer()
	# X[0] = 1  # 等价于Indexer.__setitem__(X,0,1)
	# X[1] = 2
	# X[2] = 3
	for item in X:
		print(item)


def test_indexing():
	X = Indexing()
	print(hex(X))       # 将对象转换为数值字符串，这里执行两个内置方法,__index__ 和 __str__


if __name__ == '__main__':
	# test_index()
	test_iterator()
	# test_indexing()