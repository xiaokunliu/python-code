#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import http.cookiejar
import urllib.request
from bs4 import BeautifulSoup

login_url = "https://login.taobao.com/member/login.jhtml?style=mini&newMini2=true&css_style=alimama&from=alimama&redirectURL=http%3A%2F%2Fwww.alimama.com&full_redirect=true&disableQuickLogin=true"
req = urllib.request.Request(login_url)
req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
data = urllib.request.urlopen(req).read()
bs4 = BeautifulSoup(data,"lxml")
inputList = bs4.find("form",{"id":"J_Form"}).findAll("input")
post_data = {}
for line in inputList:
	name = line.get("name")
	value = line.get("value","").strip()
	if name:
		if name == "TPL_username":
			post_data[name] = "zkkxl114"
		elif name == "TPL_password":
			post_data[name] = "Ilikemaths602"
		else:
			post_data[name] = value
post_data = urllib.parse.urlencode(post_data)

# 伪装浏览器
chrome_headers = [
	("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"),
	("Accept-Language","zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4"),
	("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"),
]

cjar=http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
