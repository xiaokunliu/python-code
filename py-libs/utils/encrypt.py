#!/usr/bin/env python
# -*- coding: UTF-8 -*-


u"""
处理加密的共用方法
"""
import hashlib
import base64
import uuid

from wrapper.class_wraps import Singleton


@Singleton
class EncryptClass(object):
    u"""
    处理加密的工具类
    """
    def __init__(self):
        u"""
        初始化加密工具类
        """
        self._md5 = hashlib.md5()
        self._sha1 = hashlib.sha1()

    def md5_text(self, text):
        u"""
        注意进行加密的时候需要将文本转换为字符串，使用Unicode会报错
        :param text:
        :return:
        """
        if isinstance(text, unicode):
            text = text.encode("UTF-8")
        self._md5.update(text)
        return self._m5.hexdigest()

    def sha1(self, text):
        if isinstance(text, unicode):
            text = text.encode("UTF-8")
        self._sha1.update(text)
        return self._sha1.hexdigest()
    
    @staticmethod
    def base64_encode(text):
        return base64.b64encode(text)

    @staticmethod
    def base64_decode(text):
        return base64.b64decode(text)
    
    @staticmethod
    def uuid_3(namespace, name):
        return uuid.uuid3(namespace, name)

    @staticmethod
    def uuid_5(namespace, name):
        return uuid.uuid5(namespace, name)

    @staticmethod
    def uuid_1():
        _str = uuid.uuid1().__str__()
        return _str.replace("-", "").upper()