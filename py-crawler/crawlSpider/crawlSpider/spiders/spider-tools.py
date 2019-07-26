#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import urllib2
from io import BytesIO
from urlparse import urlparse

import requests
from PIL import Image

_headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Host":"img1.mm131.m",
            "Referer":"http://www.mm131.com/xinggan/3035_27.html"}

class Tools(object):

	@staticmethod
	def get_domain(url):
		parts = urlparse(url)
		return parts.hostname

	@staticmethod
	def get_filename_from_url(url):
		parts = urlparse(url)
		path = parts.path
		index = path.rindex("/")
		return path[index+1:]

	@staticmethod
	def get_file_suffix(file_name):
		arr = file_name.split(".")
		return arr[1]

	@staticmethod
	def store_image(src,dist):
		file_name = Tools.get_filename_from_url(src)
		response = requests.get(src)
		try:
			image_file = Image.open(BytesIO(response.content))
			file_path = dist + file_name
			image_file.save(file_path)
		except IOError as e:
			print e

if __name__ == '__main__':
    Tools.store_image("http://mat1.gtimg.com/www/images/qq2012/qqlogo_1x.png","/Users/wind/projects/images/")


