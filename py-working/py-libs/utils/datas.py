#!/usr/bin/env python
# -*- coding: UTF-8 -*-

u"""
常用的文件处理
"""
from xml.etree.ElementTree import fromstring, Element, tostring, parse


class CSVUtils(object):
    
    @staticmethod
    def dict_to_xml(params, root="xml"):
        if not isinstance(params, dict):
            raise Exception("the params should be dict instance")
        root_ele = Element(root)
        if params:
            for key, value in params.items():
                child = Element(key)
                child.text = str(value)
                root_ele.append(child)
        return tostring(root_ele)

    @staticmethod
    def parse_xml_string(xml_string):
        if not xml_string:
            raise Exception("the xml string should not be empty ")
        root = fromstring(xml_string)
        return root
    
    @staticmethod
    def parse_xml_file(xml_file):
        import os
        if not os.path.exists(xml_file):
            raise Exception("the xml file[%s] is not exist" % xml_file)
        doc = parse(xml_file)
        return doc      # 返回文档对象
    
