#!/usr/bin/env python
# -*- coding: UTF-8 -*-

u"""
启动flask框架的应用
"""
from flask import Flask

app = Flask(__name__)

# 配置管理
app.config[r'DEBUG'] = True


# 配置加载的方式
def load_config1():
	u"""
	通过字符串的模块名字进行加载
	:return:
	"""
	app.config.from_object('setting')


def load_config2():
	u"""
	或者引用模块
	:return:
	"""
	import settings
	app.config.from_object(settings)


def load_config_by_filename():
	u"""
	通过文件名称加载,不限于.py后缀的文件名称
	使用slice=True的时候：当文件不存在的时候不会抛出异常，只是返回一个False,
	而设置slice=False会抛出异常
	:return:
	"""
	app.config.from_pyfile('settings.py',slice=True)


def load_config_by_env():
	u"""
	通过环境变量加载
	在环境变量配置
	export FLASK_SETTINGS = /path/settings.py
	:return:
	"""
	app.config.from_envvar("FLASK_SETTINGS")


@app.route("/")
def index():
	return u"index"


@app.route("/index/<uuid:id>")
def convert_url():
	u"""
	动态路由匹配规则<converter:var>
	converter有以下几种

	string:接受没有任何斜杆的"/"
	int:接受整数
	float:同int，但是接受浮点数
	path：和默认的相似，但也接受斜杆
	uuid：只接受uuid的字符串
	any：可以指定多种路径，但是需要传入参数
	:return:
	"""
    pass


@app.route("/any(a,b):page_name")
def any_url():
	pass


if __name__ == '__main__':
	u"""
	Flask默认监听的host是127.0.0.1，以及对应的端口是5000
	服务器启动之后会调用werkzeug.serving.run_simple进入轮询，默认是
	使用单进程单线程的werkzeug.serving.BaseWSGIServer处理请求，实际上还是使用BaseHttp
	Server.HTTPServer，通过select.select做0.5s的'while True'的事件轮询，这种启动方式
	仅适用于调试，生产环境要使用uwsgi或者是Gunicorn
	"""
	app.run(host=u"0.0.0.0", port=9000, debug=True)
