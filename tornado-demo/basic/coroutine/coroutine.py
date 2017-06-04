#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop

'''
协程函数
'''
@gen.coroutine
def coroutine_visit():
    http_client = AsyncHTTPClient()
    _response = yield http_client.fetch("https://www.baidu.com")
    print _response.body



'''
调用协程函数
1. 在本身是协程函数内通过yield关键字调用
2. 在IOLoop尚未启动时，通过IOLoop的run_sync()调用
3. 在IOLoop已经启动时，通过IOLoop的spawn_callback()调用
'''
@gen.coroutine
def outer_coroutine():
    print "start call coroutine ..."
    yield coroutine_visit()
    print "end call coroutine ..."

# start IOLoop --- 调用协程函数  --- end IOLoop
def func_normal():
    print "start func_normal call coroutine ..."
    IOLoop.current().run_sync(lambda:coroutine_visit())
    print "end func_normal call coroutine ..."

# IOLoop is running
def func_start_normal():
    print "start func_start_normal call coroutine ..."
    IOLoop.current().spawn_callback(coroutine_visit)
    print "end func_start_normal call coroutine ..."
