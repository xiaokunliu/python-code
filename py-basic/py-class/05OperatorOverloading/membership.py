#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import print_function

"""
py成员关系
__contains__,__iter__,__getitem__
"""


class Iters:
	def __init__(self, value):
		self.data = value

	def __getitem__(self, i):    # Fallback for iteration,index,slice
		print('get[%s]:' % i, end='')
		return self.data[i]

	def __iter__(self):          # Preferred for iteration
		print('iter=> ', end='')
		self.ix = 0
		return self

	def __next__(self):
		print('next:', end='')
		if self.ix == len(self.data):raise StopIteration
		item = self.data[self.ix]
		self.ix += 1
		return item

	def __contains__(self, x):      # Preferred for 'in'
		print('contains: ', end='')
		return x in self.data

	next = __next__


class Iters2:
	def __init__(self, value):
		self.data = value

	def __getitem__(self, i):    # Fallback for iteration,index,slice
		print('get[%s]:' % i, end='')
		return self.data[i]

	def __iter__(self):          # Preferred for iteration
		print('iter=> next:', end='')
		for x in self.data:
			yield x
			print('next:',end = '')

	def __contains__(self, x):      # Preferred for 'in'
		print('contains: ', end='')
		return x in self.data



if __name__ == '__main__':
	X = Iters([1, 2, 3, 4, 5])
	print(3 in X)   # contains: True
	# call __iter__, __next__,
	for i in X:
		print(i, end=' | ')

	# print()
	# print(X[2])     # 调用__getitem__如果有定义则可以使用索引、分片等操作，否则抛出异常：TypeError: 'Iters' object does not support indexing
	# print([i ** 2 for i in X])
	# print(list(map(bin, X)))    # 转成二进制
	# I = iter(X)
	# while True:
	# 	try:
	# 		print(next(I), end=' @ ')
	# 	except StopIteration: break
	#
	# print()
	# X1 = Iters2([1, 2, 3, 4, 5])
	# print([i ** 2 for i in X1])     # 返回数据并保存在列表中

