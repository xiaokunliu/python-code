#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Created on 2015年12月28日
@author: Keith
"""
from dictionary.models import LabelType
from tool import encrypt, util
from users.models import Users, UsersAdditional


def test_insert():
    count = 0
    while count<=100:
        _email = "kxl602_%s_XXX@163.com" % count
        _name = "keithl_%s" % count
        _u = Users(user_email=_email,
                   user_pwd=encrypt.md5_1("123456789"),
                   user_alias_name=_name,
                   user_auth=encrypt.build_auth(_name, "123456789"),
                   user_token=encrypt.build_token(),
                   user_token_expires=util.getTokenExpires()
                   )
        _u.save()
        _user = Users.objects.get(user_auth=_u.user_auth)
        _ua = UsersAdditional(user_id=_user.user_id)
        _ua.save()
        count += 1
    
    

def test_count(auth_string):
    count = Users.auth_manager.auth_count(auth_string)
    print count


def test_token_expires(auth_string):
    return Users.auth_manager.token_expires(auth_string)


def test_insert_label():
    _list_label = [
                   {"code":"10000","desc":"Develop language","parent_code":0},
                   {"code":"10001","desc":"Java","parent_code":"10000"},
                   {"code":"10002","desc":"IOS","parent_code":"10000"},
                   {"code":"10003","desc":"Android","parent_code":"10000"},
                   {"code":"10004","desc":"C","parent_code":"10000"},
                   {"code":"10005","desc":"C++","parent_code":"10000"},
                   {"code":"10006","desc":"JavaScript","parent_code":"10000"},
                   {"code":"10007","desc":"Python","parent_code":"10000"},
                   {"code":"10008","desc":"Perl","parent_code":"10000"},
                   {"code":"10009","desc":"HTML5","parent_code":"10000"},
                   {"code":"10010","desc":"PHP","parent_code":"10000"},
                   {"code":"10011","desc":"Node.js","parent_code":"10000"},
                   {"code":"20000","desc":"Develop Type","parent_code":"0"},
                   {"code":"20001","desc":"Web前端开发","parent_code":"20000"},
                   {"code":"20002","desc":"后台开发","parent_code":"20000"},
                   {"code":"20004","desc":"linux运维","parent_code":"20000"},
                   {"code":"20005","desc":"第三方接入开发","parent_code":"20000"},
                   {"code":"30000","desc":"Other","parent_code":"0"},
                   {"code":"30001","desc":"产品","parent_code":"30000"},
                   {"code":"30002","desc":"UI设计","parent_code":"30000"}
                   ]
    for label in _list_label:
        _t = LabelType(type_code=label['code'],type_desc=label['desc'],parent_code=label['parent_code'])
        _t.save()
    

def test_label_parent():
    _parent =  LabelType.objects.get_parent()
    for p in _parent:
        print p.type_code,p.type_desc,p.parent_code
    
    print LabelType.objects.get_sub()

def test_search_type():
    _obj_list = []
    _parent_list = LabelType.objects.get_parent()
    for p in _parent_list:
        _t = dict(code=p.type_code,desc=p.type_desc,sub_list=[])
        _obj_list.append(_t)
        
    
    _sub_list = LabelType.objects.get_sub()
    for pa in _obj_list:
        for sub in _sub_list:
            if pa['code'] == sub['parent']:
                pa['sub_list'].append(sub)
                
    print _obj_list
    

if __name__ == '__main__':
#     test_insert()
#     test_count("EC5ECB78CA288126EAF5DD56A96CED53DDE227D4")
# 84ED128091A8148A35F19FF602F1294AAB3C8BED
#     print test_token_expires("EC5ECB78CA288126EAF5DD56A96CED53DDE227D4")
    test_insert_label();
#     test_label_parent()
#     test_search_type()
    print "done"
