#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
this users moudle is used for dn users table,the one module is just only one auto key
"""

from django.db import models, connection
from tool.webapp import AppError
# from django.core.management.sql import sql_all
# from tools.logs import getAppLog

# _log = getAppLog()

class UserManager(models.Manager): 
    def auth_count(self,auth_string):
        return self.filter(user_auth=auth_string).count()
    
    def getUsersExceptSelf(self,auth_string):
        cursor = connection.cursor()
        cursor.execute("""
        SELECT u.user_id FROM ss_user u WHERE u.user_auth!='%s' LIMIT 100
           """ % auth_string)
        
        _result = []
        
        for row in cursor.fetchall():
            _result.append(row[0])
        
        return _result
    
    def getId(self,auth_string):    
        cursor = connection.cursor()
        cursor.execute("""
        SELECT u.user_id FROM ss_user u WHERE u.user_auth!='%s'
           """ % auth_string)
        
        _id = 0
        try:
            _id = [0][0]
        except IndexError,e:
#             _log.error(e)
            print "UserManager-->token_expires-->",e
        finally:
            return _id
        
    
    def token_expires(self,auth_string):
        cursor = connection.cursor()
        cursor.execute("""
        SELECT u.user_token_expires FROM ss_user u WHERE u.user_auth='%s'
           """ % auth_string)
        _token_expires = 0
        try:
            _token_expires = [0][0]
        except IndexError,e:
#             _log.error(e)
            print "UserManager-->token_expires-->",e
        finally:
            return _token_expires
        
        
    def userId_count(self,user_id):
        cursor = connection.cursor()
        cursor.execute("""
        SELECT COUNT(0) FROM ss_user u WHERE u.user_id=%d
           """ % user_id)
        
        _nums = 0
        try:
            _nums = cursor.fetchall()[0][0]
        except IndexError,e:
#             _log.error(e)
            print "UserManager-->token_expires-->",e
        finally:
            return _nums  
         
    # for task 
    def getUserIdByLabelType(self,labelType,user_latitude,user_longitude):
        _label_list = labelType.split(",")
        
        if len(_label_list)==1:
            raise AppError("it must be use ',' to combinate label code ")
        
        toUserIds = []
        sql = """ SELECT u.user_id FROM ss_user u WHERE u.user_longitude=%d AND u.user_latitude=%d """ % (user_longitude,user_latitude)
        for label_code in _label_list:
            sql = sql + "u.user_label_type LIKE %"+label_code+"% ORDER BY u.user_type DESC LIMIT 1"
            print sql
            cursor = connection.cursor()
            cursor.execute(sql)
            toUserIds.append(cursor.fetchall()[0][0])
            
        return toUserIds 
     

class Users(models.Model):
    ## attention,this set blank = True but there is not applied at the db mysql
    user_id = models.PositiveIntegerField(auto_created=True,primary_key=True)
    user_email = models.EmailField(max_length=50,unique=True)
    user_phone = models.CharField(max_length=11,unique=True)
    user_pwd = models.CharField(max_length=32)
    user_really_name = models.CharField(max_length=50,blank=True,null=True)
    user_alias_name = models.CharField(max_length=50,blank=True,null=True)
    user_sex = models.SmallIntegerField(choices=((0, 'Male'), (1, 'Female')),default=1)
    user_auth = models.CharField(max_length=40,unique=True)
    user_token = models.CharField(max_length=40,unique=True)
    user_token_expires = models.FloatField()
    user_longitude =models.DecimalField(max_digits=10, decimal_places=6,blank=True,null=True)
    user_latitude =models.DecimalField(max_digits=10, decimal_places=6,blank=True,null=True)
    user_ip = models.PositiveIntegerField(blank=True,null=True)
    user_label_type = models.CharField(max_length=50,blank=True,null=True)
    user_type = models.SmallIntegerField(choices=((0, 'asker'), (1, 'helper')),default=0)
    
    def __unicode__(self):
        return u"%d %s %s %s" % (self.user_id,self.user_email,self.user_really_name,self.user_alias_name)
    
    auth_manager = UserManager()
    objects = models.Manager()
    
    class Meta:
        db_table = "ss_user"
        
        
BASE_URL = "/images/"    
REAL_PATH = "/home/public/images" 

class UsersAdditional(models.Model):
    ua_id = models.PositiveIntegerField(auto_created=True,primary_key=True)
    user_id = models.PositiveIntegerField(unique=True)  # references on table users_Uers user_id
    photo_url = models.URLField(max_length=200,null=True,blank=True)
    domain_desc = models.TextField(null=True,blank=True)
    work_desc = models.TextField(null=True,blank=True)
    

    def __unicode__(self):
        return u"%s %s" % (self.ua_id,self.user_id)
     
    class Meta:
        db_table = "ss_user_additional"
    
    objects = models.Manager()




## it would be have more user then use it
# class UserLabel(models.Model):
#     ul_id = models.PositiveIntegerField(auto_created=True,primary_key=True)
#     user_id = models.PositiveIntegerField(null=False,blank=False)
#     label_code = models.CharField(max_length=20,null=False,blank=False)
#     
#     objects = models.Manager()
#     
#     class Meta:
#         db_table = "ss_user_label"
        
        
        
        
        
