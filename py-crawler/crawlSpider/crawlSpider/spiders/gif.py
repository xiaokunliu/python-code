#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import scrapy
from scrapy import Request
from crawlSpider.items import CrawlItem

"""
Spider是用户编写用于从单个网站(或者一些网站)爬取数据的类
通过命令行传递参数
scrapy crawl gif -a url=http://gifdx.net/
"""


class GifSpider(scrapy.Spider):
	"""
	抓取动态图片数据
	执行带参数的url
	scrapy crawl gif -a url=http://gifdx.net/
	name:用于区别Spider。 该名字必须是唯一的，您不可以为不同的Spider设定相同的名字
	start_urls: 包含了Spider在启动时进行爬取的url列表。 因此，第一个被获取到的页面将是其中之一。 后续的URL则从初始的URL获取到的数据中提取
	"""
	name = r"gif"
	# url_list = ['http://gifdx.net/','http://www.gifcc.com/forum-38-1.html']

	def __init__(self,url = None):
		super(GifSpider,self).__init__()
		self.start_urls = [url]

	"""
	以初始的URL初始化Request，并设置回调函数。
	当该request下载完毕并返回时，将生成response，并作为参数传给该回调函数。
	spider中初始的request是通过调用 start_requests() 来获取的。
	start_requests() 读取 start_urls 中的URL， 并以 parse 为回调函数生成 Request
	该方法的默认实现是使用 start_urls 的url生成Request
	当指定了URL时，make_requests_from_url() 将被调用来创建Request对象
	该方法仅仅会被Scrapy调用一次，因此您可以将其实现为生成器
	"""
	def start_requests(self):
		for url in self.start_urls:
			yield scrapy.Request(url = url, callback = self.parse)

	"""
	parse() 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。
	该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象
	"""
	def parse(self, response):
		from .tools import Tools
		domain = Tools.get_domain(response.url)
		if domain == r'gifdx.net':
			return self.parse_gifdx(response)
		elif domain == r'www.gifcc.com':
			return self.parse_gifcc(response)

	def parse_gifdx(self,response):
		req_list = self.parse_gifdx_item(response)
		next_a_link = None
		try:
			next_a_link = response.xpath("//div[@class='pagination']/a[@class='next']/@href").extract()[0]
		except Exception as e:
			print e
		print next_a_link
		if next_a_link:
			req = Request(next_a_link,callback = self.parse_gifdx)
			req_list.append(req)
		return req_list

	def parse_gifdx_item(self,response):
		req_list = []
		alink_list = response.xpath("//ul[@id='post_container']/li/div[@class='thumbnail']/a")
		if alink_list:
			for alink in alink_list:
				link = alink.xpath("@href").extract()[0]
				print link
				req = Request(link,callback = self.parse_gifdx_item_context)
				req_list.append(req)
		return req_list

	def parse_gifdx_item_context(self,response):
		item = CrawlItem()
		item['image_category'] = 'gif'
		item['image_no'] = 1
		item['image_list'] = []
		img_list = response.xpath("//div[@id='post_content']/p/img")
		if img_list:
			for img in img_list:
				url = img.xpath('@src').extract()[0]
				self.download_image(url, category = 'gif')
				item['image_list'].append(url)
		print item

	def parse_gifcc(self,response):
		pass

	def download_image(self,url,category):
		"""
		下载图片
		去除水印
		设计图片存储
		程序要设计定时来执行job
		:param url:
		:param category:
		:return:
		"""
		pass