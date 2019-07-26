#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import scrapy


class SexSpider(scrapy.Spider):
	"""
	抓取性感图片数据
	"""
	name = r"sex"

	def start_requests(self):
		urls = [
			'http://www.mm131.com/',
		]
		for url in urls:
			yield scrapy.Request(url = url, callback = self.parse)

	def parse(self, response):
		pass