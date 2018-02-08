#!/usr/bin/env python
# -*- coding: UTF-8 -*-

u"""
属性管理
1. 属性管理的作用
2. 属性
3. 描述符
4. __getattr__ and __getattribute__
5. 属性校验
"""

u"""
__getattr__ and  __setattr__:
routing undefined attribute fetchesand all attribute assignments to generic handler methods.

__getattribute__:
routing all attribute fetches to a generic handler method

property:
routing specific attribute access to get and set handler functions
1.attribute = property(fget, fset, fdel, doc)
2.使用装饰器@property

descriptor protocol:
routing specific attribute accesses to instances of classes with arbitrary get
and set handler methods, and the basis for other tools such as properties and slots
"""


"""
property 设置
"""


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        # name = property(name)
        print('fetch...')
        return self._name
    
    @name.setter
    def name(self, value): # name = name.setter(name)
        print('change...')
        self._name = value

    @name.deleter
    def name(self): # name = name.deleter(name)
        print('remove...')
        del self._name


"""
属性描述池：Descriptors

Using State Information in Descriptors
1. Descriptor state is used to manage either data internal to the workings of the
descriptor, or data that spans all instances. It can vary per attribute appearance(often per client class).

2.Instance state records information related to and possibly created by the client class.
It can vary per client class instance (that is, per application object)

in short:descriptor state is per-descriptor data and instance state is per-client-instance data

# 属性使用__slots__

"""


class Descriptor(object):
    
    def __get__(self, instance, owner):
        u"""
        self is the  Name class instance
        instance is the  Person class instance
        owner is the  Person class
        :return:
        """
        print(self, instance, owner, sep="\n")
        return instance._name
        
    def __set__(self, instance, value):
        print(self, instance, value, sep="\n")
        instance._name = value
    
    def __delete__(self, instance):
        print(self, instance, sep="\n")
        del instance._name
    
    
class Person(object):
    u"""
    定义在__slots__的属性与使用Descriptor修饰的属性名称不能重复定义
    """
    __slots__ = ['name', 'age']
    
    # name = Descriptor()
    # age = Descriptor()
    

# if __name__ == '__main__':
#     p = Person()
#     p.name = "xiaokun1"
#     print(p.name)       # p.name == Descriptor.__get__(Person.name, p, Person)
#
#     p.xxx = "xxx"
#     p1 = Person()
#     p1.name = "xiaokun2"
#     print(p1.name)


"""
python属性重载运算符
__getattr__：__getattr__ is run for undefined attributes,because it is run only for attributes
not stored on an instance or inherited from one of its classes,its use is straightforward

__getattribute__：is run for every attribute,you must be cautious when using this
method to avoid recursive loops by passing attribute accesses to a superclass.
"""


class Student(object):
    def __getattribute__(self, attr):  # On [obj.any]
        print('get: ' + attr)
        if attr == 'name':  # Intercept all names
            attr = '_name'  # Map to internal name
        # return self._name # 会再次触发__getattribute__导致引用死循环
        return object.__getattribute__(self, attr)  # Avoid looping here


"""
self.value=start inside the constructor triggers  __setattr__
self.value inside  __getattribute__ triggers  __getattribute__ again
"""





