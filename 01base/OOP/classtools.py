#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class AttrDisplay:
	""" 文档注释
	通过内置属性__dict__动态获取实例属性信息
	"""
	def __get_all_attrs(self):
		attrs = []
		for key,value in self.__dict__.items():
			attrs.append(("%s=%s" % (key,value)))
		return ",".join(attrs)

	def __str__(self):
		return "%s[%s]" % (self.__class__.__name__,self.__get_all_attrs())