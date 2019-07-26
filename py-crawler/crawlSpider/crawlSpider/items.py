# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

"""
Item 是保存爬取到的数据的容器；其使用方法和python字典类似， 并且提供了额外保护机制来避免拼写错误导致的未定义字段错误
"""

import scrapy


class CrawlItem(scrapy.Item):
    image_list = scrapy.Field()
    image_category = scrapy.Field()
    image_no = scrapy.Field()






