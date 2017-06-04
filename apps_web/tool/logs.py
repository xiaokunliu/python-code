#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
this logs.py is used for record the logging data
"""
import logging.config



_log = None

class _applog(object):
    def __init__(self):
        # for web ./config/logging.conf
        # for project ../config/logging.conf
        logging.config.fileConfig("./config/logging.conf")
        self._log = logging.getLogger("applog")
     
    def getLog(self):
        return self._log

def getAppLog():
    global _log
    if _log is None:
        _log = _applog().getLog()
    return _log

# test code
if __name__ == '__main__':
    getAppLog().info("msg")


    