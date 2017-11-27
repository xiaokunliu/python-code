#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
python requests 库
pip install requests
"""

# 执行GET请求
# from imp import reload
import requests

# 设置当前的编码格式
# reload(sys)
# sys.setdefaultencoding('utf8')

"""
资料查阅
http://docs.python-requests.org/en/master/user/quickstart/
"""

url = "https://www.baidu.com/"
response = requests.get(url)                                    ## 执行url的get请求
print(response.status_code)                                     ## 显示返回状态码
print(response.text.encode("ISO-8859-1").decode("utf-8"))       ## 打印整个html页面信息
print(response.content)
print(response.cookies)
print(response.encoding)    ## 查看响应的编码格式



