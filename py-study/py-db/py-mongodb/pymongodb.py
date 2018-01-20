#!/usr/bin/env python
# -*- coding: UTF-8 -*-

u"""
封装pymongodb 的操作
https://docs.mongodb.com/manual/tutorial/query-documents/
"""
from pymongo import MongoClient
import settings


class PyMongoClient(object):
    u"""
    pymongo client
    """
    _client = MongoClient(settings.MONGO_URI)
    
    def __init__(self, collections):
        self._collection = self._client[collections]
        
    def find_all_collections(self):
        u"""
        查看mongodb该db下的所有collection
        :return:
        """
        return self._collection.collection_names(
            include_system_collections=False)
        
    def add(self, document_map):
        u"""
        添加一个文档操作
        :param document_map:
        :return:
        """
        return self._collection.insert_one(document_map).inserted_id
    
    def batch_add(self, document_list):
        u"""
        批量添加
        :param document_list:
        :return:
        """
        if not isinstance(document_list, list):
            raise Exception("document_list should be list type")
        return self._collection.insert_many(document_list).inserted_ids
    
    def query_by_id(self, _id, keys=[]):
        u"""
        根据mongodb的查询指定的keys数据
        :param _id:
        :param keys:
        :return:
        """
        if keys:
            _search_keys = {}
            for key in keys:
                _search_keys[key] = 1
            return self._collection.find_one({"_id": _id},
                                             _search_keys)
        return self._collection.find_one({"_id": _id})
    
    def query_one(self, filed, value):
        u"""
        根据指定的field查询mongodb中一条数据
        :param filed:
        :param value:
        :return:
        """
        return self._collection.find_one({filed: value})
    
