#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
类的高级专题
1.内置类型扩展
2.新式类
2.1新式类模型
2.2新式类变化
2.3新式类扩展
3.静态方法和类方法
4.装饰器和元类
5.super call
6.类的其他问题
"""

# 内置类型扩展


""""
新式类的特性：
1.Attribute fetch for built-ins: instance skipped
2.Classes and types merged: type testing
3.Automatic object root class: defaults
4.Inheritance search order: MRO and diamonds
5.Inheritance algorithm
6.New advanced tools: code impacts
"""

# 1. Attribute fetch for built-ins: instance skipped


class Classic:
	def __init__(self):
		self.__name = "classic name"

	"""
	python2.x默认类为经典类
	由于__getatt__ 与 __getattribute__功能效果一样，这里只用__getattr__演示
	"""
	def __getattr__(self, method_name):
		print("call Classic __getattr__,it would call built-in[%s] method " % method_name)
		return getattr(self.__name,method_name)


class NewStyleClass(object):
	def __init__(self):
		self.__name = "newstyle name"
	"""
	python2.x需要指明为新式类，python3.x默认为新式类
	"""
	def __getattr__(self, item):
		print("call NewStyle __getattr__,it would call built-in[%s] method " %item)
		return getattr(self.__name,item)


class D:pass


class NClass(object):pass


def test_dir():
    C = Classic()
    N = NewStyleClass()
    print(dir(C))       # 经典类内置方法有__getattr__
    print(dir(N))       # 新式类的内置方法继承object对象,拥有object对象的属性信息


def test_classis():
	C = Classic()
	print("python2.x classic instance built-in attributes:")
	# print(str(C))   # 调用str()会执行内置函数__str__
	# print(C.__str__())

	# 为C添加可以加减赋值的操作
	C.__add__ = lambda x:x+2
	print(C+2)


def test_new():
	N = NewStyleClass()
	print("python3.x classic instance built-in attributes:")
	# print(str(N))   # 调用str()会执行内置函数__str__
	# print(type(N).__str__(N))

	# 为C添加可以加减赋值的操作, # unsupported operand type(s) for +: 'NewStyleClass' and 'int'
	N.__add__ = lambda x: x + 2
	print(N + 2)


# 2. Type Model Change,经典类中list和str除外
# classes are types
# types are classes

def test_model_change():
	C = Classic()
	print(type(C))
	print(C.__class__)

	N = NewStyleClass()
	print(type(N))
	print(N.__class__)


def test_model_change2():
	C1 = Classic()
	C2 = D()
	print("the type(C1) == type(C2) is %s" % (type(C1) == type(C2)))     # 经典类中的所有实例都拥有相同的type

	N1 = NewStyleClass()
	N2 = NClass()
	print("type(N1) == type(N2) is %s" % (type(N1) == type(N2)))     # 新式类:type is class,class is type


#3. All Classes Derive from “object”
# type > class > instance
def test_class():
	print("str instance type is %s" % type("str class"))
	print("str type is %s" % type(str))
	print("type type is %s" % type(type))


# 所有class都是继承object
def test_inherit():
	print(Classic.__bases__)
	print(dir(Classic))
	print(NewStyleClass.__bases__)
	print(dir(object))
	print(dir(NewStyleClass))


# 4.Diamond Inheritance Change
# For classic classes (the default in 2.X): DFLR,即深度优先，然后从左到右开始遍历
# For new-style classes (optional in 2.X and automatic in 3.X): MRO,即广度优先查询

# class A1(object):
# 	# pass
# 	attr = 2
#
#
# class A2(object):
# 	attr = 4

class A1(object):
	attr = 1


class A2(object):
	attr = 2


class B(A1):
	pass


class C(A2):
	attr = 4


class T(A2):pass


class D2(B,T,C):
	pass


def test_search():
	d = D2()    #
	print(d.attr)       # 经典类搜索：深度优先，即 D -- B --- A1 --- C --- A2，新式类：即D --- B --- C  --- A1 --- A2
	print(D2.__mro__)    # 列出D的遍历搜索方式,只有在新式类中生效并且只有属于同一个类下的才会走广度优先


if __name__ == '__main__':
	# test_dir()
	# test_classis()
	# test_new()
	# test_model_change()
	# test_model_change2()
	# test_class()
	# test_inherit()
    test_search()












