#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
python获取属性
property方法：property(get,set,del,doc)
"""


class PropertyObject(object):
	@property
	def name(self):
		print("call get_name method...")
		return "keithl"

	@name.setter
	def name(self,value):
		print("call set_name method for value[%s]..." % value)
		self.__name = value

	# def __getattribute__(self, item):
	# 	print("intercept attribute method ...%s" % item)
	# 	print(self.__name)

	# def get_name(self):
	# 	print("call get_name method...")
	# 	return "keithl"
	#
	# def set_name(self, value):
	# 	print("call set_name method...")
	# 	self.__name = value
	#
	# name = property(fget = get_name,fset = set_name)


def test_property():
	po = PropertyObject()
	print(po.name)

	po.name = "xiaokun"


class NameDescriptor(object):
	def __get__(self, instance, owner):return "get_keithl"
	def __set__(self, instance, value):instance._name="set_"+value


class descriptors(object):
	name = NameDescriptor()


def test_name_desc():
	nd = descriptors()
	print(nd.name)
	nd.name = "keithl"
	print(nd.name)
	print(nd._name)


if __name__ == '__main__':
    # test_property()
    test_name_desc()


# 可以参考先前的python面向对象编程（1）中提到的属性继承搜索  图8