#!/usr/bin/env python
# -*- coding: UTF-8 -*-

u"""
操作日期工具
"""
import datetime


class TimeFormat(object):
    DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H:%M:%S"


def get_curr_str(format=TimeFormat.DATE_TIME_FORMAT):
    return datetime.datetime.now().strftime(format)


