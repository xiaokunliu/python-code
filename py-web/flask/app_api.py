#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask import Flask, jsonify
from flask.views import MethodView

u"""
使用flask编写api接口 -- 面向对象的方式
"""

app = Flask(__name__)


class UserAPI(MethodView):
    u"""定义user对应的API接口"""
    
    def http_get(self):
        return jsonify({
            'username': 'fake',
            'uri': 'https://www.baidu.com'
        })
    
    
    def http_post(self):
        return "http post method"
    
app.add_url_rule('/user', view_func=UserAPI.as_view('userview'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)
