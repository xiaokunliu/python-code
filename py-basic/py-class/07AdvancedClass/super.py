#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class SuperClass(object):
	def act(self):
		print("Super Class act method ...")


class SubClass(SuperClass):
	def act(self):
		SuperClass.act(self)
		# super().act()
		# super(SubClass,self).act()
		print("SubClass act method ...")

	# def display(self):
	# 	proxy = super()
	# 	print(proxy)


def test_super():
	sub = SubClass()
	sub.act()
	# sub.display()


class A(object):
	def act(self):
		print("call A act method ....")


class B(object):
	def act(self):
		print("call B act method ....")


class C(B,A):
	def act(self):
		super().act()


def test_mutil_inherict():
	c = C()
	c.act()


class E(object):
	def __getitem__(self, item):
		print("call E __getitem__ method ...")


class F(E):
	def __getitem__(self, item):
		print('call F __getitem__ method ..')
		E.__getitem__(self, item)
		super().__getitem__(item)
		super()[item]       # 不支持运算符操作，'super' object is not subscriptable


def test_opr():
	f = F()
	f[2]


class X:
	def m1(self):
		print("call X method")


class Y:
	def m1(self):
		print("call Y method")


class Z(X):
	def m1(self):
		super().m1()


def test_z():
	z = Z()
	z.m1()
	print("change Z class base for Y ....")
	Z.__bases__=(Y,)
	z.m1()


class IA(object):
	def __init__(self):
		print("call IA init ...")


class IB(IA):
	def __init__(self):
		print("call IB init ....")
		super().__init__()


class IC(IA):
	def __init__(self):
		print("call IC init ....")
		# super().__init__()


class ID(IC,IB):
	def __init__(self):
		print("call ID init ...")
		super().__init__()


def test_ID():
	d = ID()
	print(ID.mro())


class P1(object):
	def __init__(self):
		print("call P1 init ...")
		super().__init__()


class P2(object):
	def __init__(self):
		print("call P2 init ...")
		# super().__init__()


class T2(P2):
	def __init__(self):
		print("call T2 init ...")


class T1(P1):
	def __init__(self):
		print("call T1 init ...")


class S(T2, T1):
	def __init__(self):
		print("call S init ...")


def test_s():
	s = S()
	S.mro()


class MixSuperA(object):
	def m1(self):
		print("call mix super class A m1 method ...")


class MixSuperB(object):
	def m2(self):
		print("call mix super class B m2 method ...")


class SubClassA(MixSuperA):
	def m2(self):
		print("call sub class A m2 method ...")


class SubClassD(MixSuperA,MixSuperB):
	def m1(self):
		print("call sub class D m1 method ...")
		super().m2()
		super().m1()


class Person(object):
	def __init__(self,name,age):
		print("call person init ...")
		self.__name = name
		self.__age = age


class Student(Person):
	pass
	# def __init__(self,name,age):
	# 	print("call Student init ...")
	# 	super().__init__("keithl",age)


class Son(Person):
	def __init__(self,name,age):
		print("call son init ...")
		super().__init__("keithl",age)


class Me(Student,Son):
	pass

if __name__ == '__main__':
    # test_super()
    test_mutil_inherict()
    # test_opr()
    # test_z()
    # test_ID()
    # test_s()
    # d = SubClassD()
    # d.m1()
    # d.m2()
    # Me(27)
    # Me("keithl",27)