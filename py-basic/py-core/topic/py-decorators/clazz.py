#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# instances = {}
#
#
# def singleton(aClass):
#     u"""
#     使用装饰器修饰类
#     - 单例类
#     """
#     def wrapper(*args, **kwargs):
#         if aClass not in instances:
#             instances[aClass] = aClass(*args, **kwargs)
#         return instances[aClass]
#     return wrapper
#
#
# @singleton
# class SingletonClass(object):
#     pass
#
#
# def tracker(aClass):
#     u"""
#     跟踪类对象接口
#     """
#     class Wrapper(object):
#
#         def __init__(self,*args, **kwargs):
#             self.fetches = 0
#             self.wrapped = aClass(*args, **kwargs)
#
#         def __getattr__(self, item):
#             print("Trace:" + item)
#             self.fetches += 1
#             return getattr(self.wrapped, item)
#     return Wrapper
#
#
# @tracker
# class MyList(list):pass

#
# # 直接管理函数和类
# registry = {}
#
#
# def register(obj):
#     u"""
#     注册对象并将其添加到字典中
#     :param obj:
#     :return:
#     """
#     registry[obj.__name__] = obj
#     return obj

# def inter1(fn):
#     print("inter1 before ...")
#     fn()
#     print("inter1 after ...")
#
#
# def inter2(fn):
#     print("inter2 before ...")
#     fn()
#     print("inter2 after ...")

#
# def decorator(aClass):
#     try:
#         print("before init1 ....")
#         return aClass()
#     except Exception as e:
#         print("exception intercept ..")
#     finally:
#         print("close ...")
#
#
# @decorator
# class Person(object):
#
#     def __call__(self, *args, **kwargs):
#         print("call person")


# if __name__ == '__main__':
    # p = Person()
    # print(id(p))
    #
    # p2 = Person()
    # print(id(p2))
    #
    # p3 = Person()
    # print(id(p3))
    # MyList()
    # pass

# def decorator(aClass):

