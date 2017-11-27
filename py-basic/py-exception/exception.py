#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys


def catch_index():
	str="keithl"
	try:
		print(str[10])
		# print(str[2])
	except IndexError as e:
		print(e)
	else:
		print("try正常执行，没有异常发生...")


def raise_index():
	str = "keithl"
	try:
		print(str[10])
	except IndexError as e:
		raise e


class MyException(Exception):
	def __str__(self):
		return "my exception object"


def define_exception():
	try:
		raise MyException
	except MyException as e:
		print("get my exception error[%s]" % str(e))
	finally:
		print("try statement to close resource ...")


def raise_index_finally():
	str = "keithl"
	try:
		print(str[10])
	except IndexError:
		print("except index error")
	finally:
		print("try statement to close resource ...")


def test_exception():
	try:
		for i in range(10):
			print(i)
			if i == 5:
				sys.exit(-1)
	except Exception:
		print("直接使用空的异常来捕获")


def raise_exception():
	raise MyException()


def test_try_finally():
	try:
		raise_exception()
	finally:
		print("execute test_try_finally statement ...")


def test_try_except():
	try:
		1 / 0
	except Exception as e:
		print("test_try_except caught exception ...")


if __name__ == '__main__':
    # catch_index()
    # raise_index()
    # define_exception()
    raise_index_finally()
    # test_exception()
    # test_try_finally()