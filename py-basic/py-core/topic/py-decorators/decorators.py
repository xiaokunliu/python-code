#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
装饰器
1. 装饰器的作用：为函数和类指定管理或增强代码的一种方式
1)作为代理
    代理函数调用，其实就是在原有的函数方法进行功能的增强
    代理接口类的调用，包装类对象，增强原有的类对对象行为或者特征
2）管理函数和类
    函数管理：其函数的装饰器能够被用于管理函数对象和函数调用
    类的管理：直接管理定义对象的类本身和类的实例对象，通过元类来定义

2. 装饰器基础
1）函数装饰器：是一种在运行时对函数的声明，即函数实际被调用的时候会直接返回一个由装饰器包装好的函数对象进行回调
def decorator_fn(call_fn, *args, **kwargs):
    try:
       # call fn
       return call_fn()
    finally:
       # close resources

@decorator_fn
def call_fn():
    pass

2）类的装饰器
def decorator_cls(cls, *args, **kwargs):
    try:
        cls(args, kwargs)
    finally:
        # close resource


@decorator_cls
class CallClass(object):
    pass


3) 装饰器的嵌套
@d1
@d2
@d3
def f(..):
    pass


4)带参数的装饰器
@decorate(A,B)
def fn(*args, **kwargs):
   pass


5)定义带参数的装饰器
def decorate(A,B):
   def actual_decorator(call_fn):
       return callable
   return actual_decorator


6)装饰器管理函数对象和类

def decorator(0):
   return 0

@decorator
def Fn():pass       # Fn = decorator(Fn)


@decorator
def Clazz():pass       # Clazz = decorator(Clazz)

3. 编写函数装饰器

1)装饰器状态将会被保留
    1.1定义类来定义装饰器，可以保留到相应的类实例信息
    1.2闭包作用域
        global
        nolocal
        函数对象的属性

2)装饰类的实例对象方法
    1. 使用嵌套的函数去修饰方法
    2. 使用描述符来修饰方法
    装饰器修饰函数仅会调用它的__call__方法，而不会调用它的__get__方法
    装饰器修饰类对象的方法会先调用__get__方法，并且通过__get__方法来获取它的实例对象再调用它的__call__方法

3）定时调用


4）添加装饰器参数
def decorate_fn(label="", ...)


4. 编写类装饰器
1)单例类

2)跟踪对象接口
    1.用类的装饰器跟踪接口
    2.使用类的内置类型类的装饰器,如list,string

3)保留多实例对象

=====
使用装饰器产生的影响
1）类型的变更
2）对原有的类或者方法的功能增强

5. 可以直接管理函数和类


6. "private" & "public" 属性


7. 验证函数参数
"""


class Tracker(object):
    u"""
    定义类来实现跟踪函数的调用，使用类作为装饰器
    """
    def __init__(self,func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("call %s to %s " % (self.calls,self.func.__name__))


@Tracker
def fn(a, b, c):
    print(a+b+c)


calls = 0


def tracker(func):
    u"""
    python3.x and python2.x
    使用函数闭包来实现装饰器功能
    global
    """
    def warpper(*args, **kwargs):
        global calls
        calls += 1
        print("call %s to %s" % (calls, func.__name__))
        return func(*args,**kwargs)
    return warpper


def tracker(func):
    u"""
    python3.x
    使用函数闭包来实现装饰器功能
    global
    """
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print("call %s to %s" % (calls, func.__name__))
        return func(*args,**kwargs)
    return wrapper


def tracker(func):
    u"""
    python3.x
    使用函数闭包来实现装饰器功能，并使用函数的属性
    global
    """
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print("call %s to %s" % (calls, func.__name__))
        return func(*args,**kwargs)
    wrapper.calls = 0
    return wrapper


# 使用函数的嵌套类来实现装饰器
# def tracker_fn(func):
#     calls = 0
#     def onCall(*args, **kwargs):
#         nolocal calls
#         calls += 0
#         print("call %s to %s" % (calls,func.__name__))
#         return func(*args,**kwargs)
#     return onCall


# 使用描述符来装饰方法
class DescriptorObject(object):

    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("call %s to %s" % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            return self(instance,*args, **kwargs)
        # return Wrapper(self, instance)
        return wrapper


class Wrapper(object):
    def __init__(self, desc, object):
        self.desc = desc
        self.object = object

    def __call__(self, *args, **kwargs):
        return self.desc(self.object, *args, **kwargs)

if __name__ == '__main__':
    fn(1, 3, 4)
    fn(1, 3, 4)
    fn(1, 3, 4)