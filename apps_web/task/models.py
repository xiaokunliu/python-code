#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
this moudle is reference on ss_task
"""

from django.db import models, connection

from tool.logs import getAppLog
from tool.webapp import AppError


_log = getAppLog()

class AppTaskManager(models.Manager):
    def getTaskByAsker(self,ask_id,index,size):
        if ask_id is None:
            raise AppError("it must be pass the asker id")
        
        sql = "SELECT t.* FROM ss_task t WHERE 1=1 FROM ss_task t WHERE t.task_deploy_user = %d ORDER BY t.task_deploy_time DESC " % ask_id
        
        ## list the table which to search by field,it just use key=?
        if index >0 and size > 0:
            sql = sql + "LIMIT %d %d " % (index,size)
        
        _log.info("getTaskByAsker-->sql:"+sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        
        _result = []
        for row in cursor.fetchall():
            _rs = dict(row)
            _result.append(_rs)
    
        return _result

# Create your models here.
class AppTask(models.Model):
    task_id = models.PositiveIntegerField(auto_created=True,primary_key=True)
    task_title = models.CharField(max_length=100)
    task_deploy_time = models.FloatField(default=0.00)
    task_deploy_user = models.PositiveIntegerField()
    task_price = models.FloatField(max_digits=10, decimal_places=2,default=0.00)
    task_type_codes = models.CharField(max_length=50)
    task_desc =  models.TextField(null=True,blank=True)
    task_status = models.CharField(max_length=1,default="0")
    
    objects = models.Manager()
    
    task_manager = AppTaskManager()
    
    class Meta:
        db_table = "ss_task"
        