#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from .classtools import AttrDisplay


class Person(AttrDisplay):
	"""
	python函数中在默认第一个有参数之后的任何参数都必须拥有默认值
	"""
	def __init__(self, name, job = None, pay = 0):
		self.name = name
		self.job = job
		self.pay = pay

	def giveRaise(self, percent):
		self.pay = self.pay * (1 + percent)


class Manager(Person):
	"""
	构造带有职位名称为manager的Person，即定制化的Person
	"""
	def __init__(self,name,pay):
		Person.__init__(self,name,job = "manager",pay = pay)

	def giveRaise(self, percent,bouns=.10):
		Person.giveRaise(self,percent = percent+bouns)
