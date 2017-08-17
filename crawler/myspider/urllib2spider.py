#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import urllib.request
import urllib.parse

# file = urllib.request.urlopen("http://www.baidu.com")
# data = file.read()  ## 读取文件的全部内容，read会把读取的内容赋给一个字符串变量
# print(data)

# dataline = file.readline() ## 读取文件的一行内容
# print(dataline)
#
# list = file.readlines() ## 读完文件的全部内容，readlines会把读取到的内容赋给一个列表变量
# print(list)
#
# ### 保存到文件中
# file_handler = open("files/baidu.html","wb")
# file_handler.write(data)
# file_handler.close()

### 上面的步骤可以简化为下面一句话
# urllib.request.urlretrieve("http://www.baidu.com",filename = "files/baidu.html")

# 清除缓存
# urllib.request.urlcleanup()
#
# # 查看返回的信息
# print(file.info())
#
# # 获取当前状态码
# print(file.getcode())
#
# # 获取当前url
# print(file.geturl())
#
# # 进行编码
# encoding_url = urllib.request.quote("http://www.baidu.com")
# print(encoding_url)

# 进行解码
# decoding_url = urllib.request.unquote("http%3A//www.baidu.com")
# print(decoding_url)

# 模拟浏览器 -- headers属性
# 方法一
# 构造user-agent
# headers = ("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")
# # 构建opener
# opener = urllib.request.build_opener()
# opener.addheaders = [headers]
#
# url = "http://blog.csdn.net/"
# data = opener.open(url,timeout = 30).read()
# print(data)
#
# file_handler = open("files/csdn.html","wb")
# file_handler.write(data)
# file_handler.close()

# 方法二
# 使用add_header()添加报头
# url = "http://www.csdn.net/"
# req = urllib.request.Request(url)
# req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
# data = urllib.request.urlopen(req).read()
# print(data)

# GET的方式
# 目前只能使用http而不能使用https
# keywd = "java"
# url = "http://www.baidu.com/s?wd="+urllib.request.quote(keywd)
# req = urllib.request.Request(url)
# data = urllib.request.urlopen(req).read()
# file_handler = open("files/java.html","wb")
# file_handler.write(data)
# file_handler.close()

# POST 方式
# url = "http://www.iqianyue.com/mypost/"
# post_data = urllib.parse.urlencode({
# 	"name":"ceo@iqianyue.com",
# 	"pass":"aA123456"
# }).encode('utf-8')
# req = urllib.request.Request(url,post_data)
# req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
# data = urllib.request.urlopen(req).read()
# file_handler = open("files/post.html","wb")
# file_handler.write(data)
# file_handler.close()

# 代理服务器的设置
from urllib.error import URLError


def use_proxy(proxy_address,url):
	proxy = urllib.request.ProxyHandler({'http':proxy_address})
	opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler(debuglevel = 1))
	urllib.request.install_opener(opener)  ## 创建全局默认的opener对象
	try:
		return urllib.request.urlopen(url).read().decode('utf-8')
	except URLError as e:
		if hasattr(e,"code"):
			print(e.code)
		if hasattr(e,"reason"):
			print(e.reason)
	return None


# http://www.xicidaili.com/  代理服务器：121.61.18.218:8118
proxy_addr = "121.61.18.218:8118"
data = use_proxy(proxy_addr,"http://www.baidu.com")
print(data)






