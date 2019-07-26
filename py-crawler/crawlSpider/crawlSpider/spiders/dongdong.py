#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import logging
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor



class DongSpider(CrawlSpider):
	name = u"dongdong"
	allowed_domains = ['ivsky.com']
	start_urls = ['http://www.ivsky.com']
	target = ""

	rules = (
		Rule(link_extractor = LinkExtractor(allow = ("/tupian/\s{1,}/"))),
	)

	def parse_start_url(self, response):
		self.log(message = "parsing start url to item",level = logging.WARNING)
		print response.url
		img_list = response.xpath("//div[@class='syl_pic']/a/img")
		for img in img_list:
			paths = img.xpath("@src").extract()
			download_img(paths)

	def download_img(self,paths):
		if paths and type(paths) == "list":
			for path in paths:
				tools.store_image(path,self.target)
