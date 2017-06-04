#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
this moudle is to connect with 3rd api

"""
from rongyun.config import RONGYU_DEV
from rongyun.rong import ApiClient


_RongyunApi = None       #private static

def getRongyun():
    global _RongyunApi
    if _RongyunApi is None:
        _RongyunApi = ApiClient(RONGYU_DEV['key'],RONGYU_DEV['sec'])
    return _RongyunApi







