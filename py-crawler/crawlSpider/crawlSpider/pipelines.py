# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

_mongodb_uri = "mongodb://keithl:keithl123@127.0.0.1:27017/dongdong"
_mongodb_db = "dongdong"
_client = MongoClient(_mongodb_uri)
_db = _client[_mongodb_db]


class DBModel(object):
    def __init__(self,collection_name):
        self._collection = _db[collection_name]

    def insert_one(self,document):
        _rs = self._collection.insert_one(document)
        return _rs.inserted_id

    def insert_many(self,documents_list):
        _rs = self._collection.insert_many(documents_list)
        return _rs.inserted_ids

    def query_one(self,condition):
        return self._collection.find_one(condition)

    def query_conditions(self,conditions):
        return self._collection.find(conditions)

    def total(self):
        return self._collection.count()

    def query_limit(self,index = 0,size = 20):
        return self._collection.find().skip(index).limit(size)

    def remove_one(self,condition):
        _rs = self._collection.delete_one(condition)
        return _rs.deleted_count

    def remove_all(self):
        _rs = self._collection.delete_many({})
        return _rs.deleted_count

    def update_many(self,condition,post):
        self._collection.update_many(condition,post)

    def update_one(self, condition, post):
        self._collection.update_one(condition, post)

    def is_exist(self,condition):
        return self.query_conditions(condition).count() > 0


class CrawlItemPipeline(object):
    def __init__(self):
        self._mongodb = DBModel('it')

    def process_item(self, item, spider):
        # _is_exist = self._mongodb.is_exist({"title":item['title']})
        # if _is_exist is False:
        #     print "insert to mongodb ...."
        #     self._mongodb.insert_one(dict(item))
        # else:
        #     _post_data = copy.deepcopy(item)
        #     _post_data.pop('title')
        #     print "update to mongodb ...."
        #     self._mongodb.update_one({'title':item['title']},{'$set':dict(_post_data)})
        return item
