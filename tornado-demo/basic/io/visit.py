#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
同步与异步IO
'''
from tornado.httpclient import HTTPClient, AsyncHTTPClient


def sync_visit():
    _client = HTTPClient()
    _response = _client.fetch("https://www.baidu.com")
    print _response.body


def handle_response(response):
    print response.body


def async_visit():
    _client = AsyncHTTPClient()
    _client.fetch("https://www.baidu.com",callback=handle_response)

async_visit()





