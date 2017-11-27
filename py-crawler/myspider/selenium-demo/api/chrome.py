#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium.webdriver.chrome import webdriver

chrome_path = r"/Users/wind/mygithub/github/python-code/crawler/tools/chromedriver"
chrome = webdriver.WebDriver(executable_path = chrome_path)
url = "http://www.baidu.com/"
chrome.get(url)




