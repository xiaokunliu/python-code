#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class SliceObject:
	def __init__(self):
		print("call slice object init ...")
		self.__data = [1,2,3,4,5,6]

	def __getitem__(self, index):           # index为索引值或者分片对象
		if isinstance(index, int):
			print('indexing', index)
		else:
			# 分片对象有start stop 以及step属性
			print('slicing', index.start, index.stop, index.step)
		return self.__data[index]

	def __setitem__(self, index, value):    # index恒为索引下标,value为值
		print("call setitem ...")
		print("key[%s]--value[%s]" % (index,value))
		self.__data.insert(index,value)


class Slicer:
	"""
	py2.x 分片
	"""
	def __getitem__(self, index):
		print("call __getitem__ for index:%s" % str(index))

	def __getslice__(self, i, j):
		print("call __getslice__ for start[%d] to end[%d]" % (i,j))

	def __setslice__(self, i, j, seq):
		print("call __setslice__ for start[%d] to end[%d] with seq[%d]" % (i,j,seq))


def test_slice():
	# 设置值
	X = SliceObject()
	# X[0] = 1
	# X[1] = 2
	# X[2] = 3

	# 分片取值
	print(X[0:2])
	print(X[:-1])
	print(X[1:])

	# for item in X:
	# 	print(item, end = ",")


def test_slicer():
	Slicer()[1]
	Slicer()[1:9]
	Slicer()[1:9:2]


if __name__ == '__main__':
	# test_slice()
	test_slicer()