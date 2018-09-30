#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def maxSubSum1(list=None):
	if list is None:
		print "the list is empty,could not cal max sub sum"
		return 0
	_max_sum = 0
	_count = len(list)
	for i in range(0,_count):
		for j in range(0,_count):
			_current_sum = 0
			for k in range(i,j+1):
				_current_sum+=list[k]
			if _current_sum > _max_sum:
				_max_sum = _current_sum
	return _max_sum


def maxSubSum2(list = None):
	if list is None:
		print "the list is empty,could not cal max sub sum"
		return 0
	_len = len(list)
	_max_sum = 0
	for i in range(0,_len):
		_current_sum = 0
		for j in range(i,_len):
			_current_sum += list[j]
			if _current_sum > _max_sum:
				_max_sum = _current_sum
	return _max_sum


if __name__ == '__main__':
	_list = [-29,2,8,3,-7,-19,2,5,8,-1]
	# _sum = maxSubSum1(_list)
	_sum = maxSubSum2(_list)
	print _sum





