#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
web driver api
http://selenium-python-zh.readthedocs.io/en/latest/getting-started.html
"""
from selenium.webdriver.phantomjs import webdriver

phantom_path = r"/Users/wind/mygithub/github/python-code/crawler/phantomjs/bin/phantomjs"
headers = {
			'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			# 'Accept-Encoding': "gzip, deflate, sdch, br",
			# 'Accept-Language': "zh-CN,zh;q=0.8,en;q=0.6",
			# 'Cache-Control': "no-cache",
			# 'Connection': "keep-alive",
			# 'Host': "www.baidu.com",
			# 'Pragma': "no-cache",
			# 'Upgrade-Insecure-Requests': "1",
			'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
}

# # 设置请求头
for key in headers:
	webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = headers[key]
driver = webdriver.WebDriver(executable_path = phantom_path)
driver.get("https://www.baidu.com")

# file_handler = open("baidu.html","wb")
# file_handler.write(driver.page_source.encode("utf-8"))
# file_handler.close()


# api 方法
# 根据html的id查询
driver.find_element_by_id()

# 根据name属性查询，比如input元素的name
driver.find_element_by_name()   # 查询一个
driver.find_elements_by_name()  # 查询多个

# 根据class定位
driver.find_element_by_class_name()     # 查询一个
driver.find_elements_by_class_name()    # 查询多个

# 根据标签元素查询
driver.find_element_by_tag_name()
driver.find_elements_by_tag_name()

# 根据link定位
# <a href="xxxx">text</a>
driver.find_element_by_link_text("a_text")  # 根据链接的文本信息查询
driver.find_element_by_partial_link_text("a_part_text")   ## 根据链接的部分文本查询





