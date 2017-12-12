#!/usr/bin/env python
# -*- coding: UTF-8 -*-

u"""
定义修饰类的装饰器
"""


class Singleton(object):
    u"""
    设置单例类提供共享数据和行为信息的复用
    """
    class_map = {}

    def __init__(self, aClass):
        self._aClass = aClass
        self._name = aClass.__name__

    def __call__(self, *args, **kwargs):
        if self._name not in self.class_map:
            self.class_map[self._name] = self._aClass(*args, **kwargs)
        return self.class_map[self._name]