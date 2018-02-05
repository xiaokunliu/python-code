#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import logging
from functools import wraps

u"""
定义修饰类对象方法和函数的装饰器
"""


class Logged(object):
    u"""
    封装日志并使用装饰器应用在类对象方法和函数
    """

    def __init__(self, func, level=logging.ERROR):
        self._func = func
        self._logged = logging.getLogger(func.__name__)
        self._level = level

    def __call__(self, *args, **kwargs):
        try:
            self._logged.log(self._level,
                             "start call fn=%s", self._func.__name__)
            return self._func(*args, **kwargs)
        except Exception as e:
            self._logged.error('call fn=%s fail,the error=%s',
                               self._func.__name__,
                               e.message)
        finally:
            # close resources ..
            self._logged.log(self._level,
                             "end call fn=%s", self._func.__name__)


def tracker(func, level=logging.DEBUG):
    logger = logging.getLogger(func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logger.log(level, "start call fn=%s", func.__name__)
            return func(*args, **kwargs)
        except Exception as e:
            logger.error("call fn=%s caught error=%s",
                         func.__name__,
                         e.message)
        finally:
            logger.log(level, "end call fn=%s,", func.__name__)
    return wrapper