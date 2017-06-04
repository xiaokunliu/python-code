#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from concurrent.futures import ThreadPoolExecutor
from tornado import gen
from tornado.httpclient import AsyncHTTPClient

'''
python2.7 ThreadPoolExecutor 属于第三方futures包
python3.2之后是自带的
'''
thread_pool = ThreadPoolExecutor(2)


def my_sleep(count):
    import time
    for i in range(count):
        time.sleep(i)

@gen.corountine
def call_blocking():
    print "start blocking call ....."
    yield thread_pool.submit(my_sleep,10)
    print "end blocking call ....."



'''
在协程中等待多个异步调用
'''
@gen.coroutine
def async_wait():
    http_client = AsyncHTTPClient()
    dict_result = yield {
        "duniang":http_client.fetch("www.baidu.com"),
        "sina":http_client.fetch("www.sina.com"),
    }

    for k,v in dict.items():
        print k,v