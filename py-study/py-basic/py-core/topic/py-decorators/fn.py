#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# def decorator_fn(call_fn):
#     print("auth checking ...")
#     if False:
#         # have not been auth then not done
#         return callable(None)
#     return call_fn
#
#
# @decorator_fn
# def call_fn():
#     print("call fn ...")


# call_fn = decorator_fn(call_fn)
# if __name__ == '__main__':
#     callable(call_fn)


# def decorator(fn):
#     def proxy(*args, **kwargs):
#         u"""
#         作为代理函数来调用原有的函数，并对原来的函数进行auth的校验
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         print("auth checking")
#         fn(*args, **kwargs)
#     return proxy
#
#
# @decorator
# def fn(a=9, b=10):
#     print(a+b)

# if __name__ == '__main__':
#     fn(2,4)

def decorator(cache_time, strategy):
    print("fake decorator ...")

    def actual_decorator(fn):
        print("using cache_time[%s] and strategy[%s] do the first job" % (cache_time, strategy))

        def proxy(*args, **kwargs):
            print("before call must be do the second job..")
            fn(*args, **kwargs)
        return proxy
    return actual_decorator


# @decorator(cache_time=10, strategy="")
# def call_fn(a, b=10):
#     if a < b:
#         print("a < b")
#     elif a > b:
#         print("a > b")
#     else:
#         print("a = b")


class Person(object):

    @decorator(cache_time=10, strategy="nio")
    def cal(self,a, b=10):
        if a < b:
            print("a < b")
        elif a > b:
            print("a > b")
        else:
            print("a = b")

# def fn(a, b=10):
#     if a < b:
#         print("a < b")
#     elif a > b:
#         print("a > b")
#     else:
#         print("a = b")
#
# if __name__ == '__main__':
#     n_fn = decorator(cache_time=10,strategy="aio")(fn)
#     n_fn(5,6)

# if __name__ == '__main__':
#     p = Person()
#     p.cal(9)