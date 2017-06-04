#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
the module is referenced on db data 
"""

from django.db import models, connection
from tool.webapp import AppError
from tool.logs import getAppLog

_log = getAppLog()

class QueManager(models.Manager):
    def getLastestQtId(self,user_id):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT q.qt_id FROM ss_question q WHERE q.qt_ask_user=%d ORDER BY q.qt_begin_time DESC LIMIT 1
                       """ % user_id)
        _id = 0
        try:
            _id = cursor.fetchall()[0][0]
        except IndexError,e:
            print "QueManager-->getLastestQt-->",e
        finally:
            return _id
    
    
    def getQtByAsker(self,user_id,conditions,order_by,optional_fields,index,size):
        if user_id is None:
            raise AppError("it must be pass the asker id")
        
        if not optional_fields:
            sql = "SELECT qt.* FROM ss_question qt WHERE 1=1 "
        else:
            sql = "SELECT "
            for feild in optional_fields:
                sql = sql+"qt."+feild+","
            
            sql = sql[:-1]
            sql = sql + " FROM ss_question qt WHERE qt.qt_ask_user = %d " % user_id
        
        ## list the table which to search by field,it just use key=?
        if conditions:
            for key in conditions.keys():
                if key == "qt_begin_time":
                    sql = sql +" AND qt.qt_begin_time >= %d " % conditions[key]
                else: ## qt_status,groom_degree,server_degree,ability_degree
                    sql = sql +" AND qt.qt_status = '%s' " % conditions[key]
                
        if order_by:
            sql = sql +"ORDER BY "
            for key in order_by.keys():
                if order_by[key]:
                    # 1 asc
                    sql = sql + "qt."+key+"ASC,"
                else:
                    sql = sql + "qt."+key+"DESC,"
            
            sql = sql[:-1]
        
        if index >0 and size > 0:
            sql = sql + "LIMIT %d %d " % (index,size)
        
        _log.info("getQtByAsker-->sql:"+sql)
        
        cursor = connection.cursor()
        cursor.execute(sql)
        
        _result = []
        for row in cursor.fetchall():
            _rs = dict(row)
            _result.append(_rs)
    
        return _result

    
    def getQuestionRemark(self,user_id,conditions,order_by,index,size):
        if user_id is None:
            raise AppError("it must be pass the asker id")
        
        sql = "SELECT qt.qt_answer_remarked FROM ss_question qt WHERE 1=1 AND qt.qt_answer_user = %d " % user_id
        
        ## list the table which to search by field,it just use key=?
        if conditions:
            for key in conditions.keys():
                if key == "qt_begin_time":
                    sql = sql +" AND qt.qt_begin_time >= %d " % conditions[key]
                else: ## qt_status,groom_degree,server_degree,ability_degree
                    sql = sql +" AND qt."+key+" = '%s' " % conditions[key]
                
        if order_by:
            sql = sql +"ORDER BY "
            for key in order_by.keys():
                if order_by[key]:
                    # 1 asc
                    sql = sql + "qt."+key+" ASC,"
                else:
                    sql = sql + "qt."+key+" DESC,"
            
            sql = sql[:-1]
        
        if index >0 and size > 0:
            sql = sql + "LIMIT %d %d " % (index,size)
        
        _log.info("getQuestionRemark-->sql:"+sql)
        
        cursor = connection.cursor()
        cursor.execute(sql)
        
        _result = []
        for row in cursor.fetchall():
            _result.append(row[0])
            
        return _result


# Create your models here.
class Question(models.Model):
    qt_id = models.PositiveIntegerField(auto_created=True,primary_key=True)
    qt_title = models.CharField(max_length=60,blank=True,null=True) 
    qt_desc = models.TextField(blank=True,null=True)
    qt_status = models.CharField(default="0",max_length=1)
    qt_begin_time = models.FloatField(default=0.00)
    qt_end_time = models.FloatField(default=0.00)
    qt_type_codes = models.CharField(max_length=50)
    qt_ask_user = models.PositiveIntegerField()
    qt_answer_user = models.PositiveIntegerField()
    groom_degree = models.CharField(max_length=1,default="0")
    server_degree = models.CharField(max_length=1,default="0")
    ability_degree = models.CharField(max_length=1,default="0")
    qt_answer_remarked = models.TextField(blank=True,null=True)
    
    objects = models.Manager()
    
    qt_manager = QueManager()
    
    class Meta:
        db_table = "ss_question"
    
    
    

