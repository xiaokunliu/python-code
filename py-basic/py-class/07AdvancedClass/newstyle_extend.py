#!/usr/bin/env python
# -*- coding: UTF-8 -*-


"""
新式类的扩展
1. 槽:__slots__
定义：assigning a sequence of string attribute names,用一个序列存储字符串属性名称
作用：
1)避免随意添加类的实例属性，只能通过槽指定的属性来做设置和访问
2)可以优化内存的使用和加快程序执行的速度
声明：
1)通过内置属性 __slots__变量来定义
2)必须定义在类顶部的语句中
注意点：
必须为槽定义的属性名称进行分配值，如果没有分配而进行访问将会报错，即AttributeError

使用规则：
1.如果父类没有槽，在子类中使用槽是没有意义的,因为类的实例对象创建的时候会创建字典属性__dict__
2.同样地，如果子类中没有定义槽，槽在父类中使用也没有存在的意义，在创建类的实例对象的时候会创建字典属性__dict__
3.父类和子类定义相同的槽是没有意义的
4.
5.Slots and __dict__:slots会排除实例字典属性，除非字典属性会显式地定义在槽中
"""


class MyObject(object):
	"""
	定义属性槽，类实例只能使用下面的属性来进设置和访问，试图设置或者访问不在槽定义的会报错
	"""
	__slots__ = ['age','name','job']
	# __slots__ = ['age','name','job','__dict__']


def test_slots():
	obj = MyObject()
	# print(obj.age)      # 未分配但尝试访问报错
	obj.age = 10
	print(obj.age)

	obj.hobby = u"不存在槽中的属性将报错"
	# obj.hobby = u"不存在槽中的dic属性将存储在命名空间字典中"
	# print(obj.__dict__)

"""
槽与命名空间字典
一旦我们需要定义槽以外的属性存储在命名空间字典的时候，需要在槽里面添加一个属性,即__dict__
"""


"""
在继承树中使用槽,子类将继承父类的槽属性取并集操作
"""

class P(object):
	__slots__ = ['a','b']


class E(object):
	__slots__ = ['c', 'd']


class M(E):
	__slots__ = ['xx','a']


def test_inherhit_class():
	m = M()
	print(dir(m))


if __name__ == '__main__':
    test_slots()
	# test_inherhit_class()
