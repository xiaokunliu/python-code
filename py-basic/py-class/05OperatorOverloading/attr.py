#!/usr/bin/env python
# -*- coding: UTF-8 -*-


"""
属性访问:属性访问，__getattr__ & __setattr__
"""

# 属性引用（访问）


class AttrObject:
	def __getattr__(self, attr_name):
		print("Attr Object get attr method ....")
		if attr_name == 'age':
			return 40
		else:
			raise AttributeError("could not access the attr[%s]" % attr_name)

# 属性添加和删除

class AcessControl:
	def __init__(self):
		self.hobby = "basketball"   # 会调用下面的__setattr__方法

	def __setattr__(self, key, value):
		"""
			self.attrname 以及 instance.attrname 将会调用类的内置方法__setattr__方法
		:param key:
		:param value:
		:return:
		"""
		# self.name = "xxxx"        # 不能在__setattr__上使用self.attr,会导致递归应用循环
		print("access control set attr key[%s] for value[%s]..." % (key,value))
		if key == 'age':
			self.__dict__[key] = value + 10
		else:
			self.__dict__[key] = value
		# else:
		# 	raise AttributeError("the key[%s] is not allowed to be assigned" % key)

	def __delattr__(self, item):
		print("del item[%s]" % item)

	def __getattr__(self, item):
		print("get item[%s]" % item)

# 属性管理工具
"""
管理属性访问的一些注意点：
1. The__getattribute__ method intercepts all attribute fetches,not just those that are undefined, but when using it you must be more cautious than with __get attr__ to avoid loops
2.The property built-in function allows us to associate methods with fetch and set operations on a specific class attribute
3.Descriptors provide a protocol for associating __get__ and __set__ methods of a class with accesses to a specific class attribute.
4.Slots attributes are declared in classes but create implicit storage in each instance
"""


class AttrManager:
	pass
	# def __getattr__(self, item):
	# 	print("call __getattr__ method ...")
	#
	# def __getattribute__(self, item):
	# 	"""
	# 	注意点：
	# 	1. 这个方法将会拦截所有获取的属性的操作，包括未定义的属性
	# 	2. 属性内置函数允许我们将方法与特定类属性的获取和集合操作相关联
	# 	3. 属性描述符为特定的类的属性提供了一组__get__和__set__方法访问协议
	# 	4. 实例属性在类中声明但是在每一个类的对象实例中隐式存储
	# 	:param item:
	# 	:return:
	# 	这个要比__getattr__更加小心，避免产生递归循环引用
	# 	"""
	# 	print("call  __getattribute__ for item[%s] " % item)


# Emulating Privacy for Instance Attributes,属性私有的，--- 在exception中体现

class PrivacyException(Exception):pass


class PrivacyClass:
	def __setattr__(self, attr_name, value):        # On self.attr_name = value
		if attr_name in self.privates:
			raise PrivacyException(attr_name, self) # Make, raise user-define except
		else:
			self.__dict__[attr_name] = value        # Avoid loops by using dict key


class FirstPrivancy(PrivacyClass):
	privates = ['age']


class SecondPrivancy(PrivacyClass):
	privates = ['name', 'pay']

	def __init__(self):
		self.__dict__['name'] = 'Tom'


# for test
def test_empty():
	e = AttrObject()
	print(e.age)        # 调用__getattr__方法,访问age的属性
	print(e.hobby)      # AttributeError: could not access the attr[hobby]


def test_access_control():
	ac = AcessControl()
	ac.age = 10         # 调用__setattr__
	print(ac.age)       # 直接输入值，没有调用__getattr__
	print(ac.hobby)       # 当属性有值时，也就是非None是不会调用__getattr__方法的，如果没有值，即None就会调用__getattr__方法
	del ac.age          # 调用__delattr__
	print(ac.name)      # 调用__getattr__,调用未定义的属性时候就会回调这个函数并且返回None


def test_attr_manager():
	manager = AttrManager()
	manager.name = "attr manager name"
	print(manager.name)
	print(manager.age)


def test_privancy():
	a1 = FirstPrivancy()
	a2 = SecondPrivancy()
	a1.name = "success"
	# a2.name = "fail"
	print(a1.name)
	# print(a2.name)

	# a1.age = 10     # fail
	a2.age = 23     # success
	# print(a1.age)
	print(a2.age)


if __name__ == '__main__':
    # test_empty()
    # test_access_control()
    test_attr_manager()
    # test_privancy()