#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
this test_db.py is mainly for testing db opr(add /update/remove/search)
"""
import logging
import os
import time
import unittest

from dictionary.models import LabelType
from invitor.models import InvitorTask
from tool import encrypt, util
from users.models import Users, UsersAdditional, BASE_URL
from questions.models import Question
from task.models import AppTask
from sys_app.models import AppFeedback


logging.basicConfig(level=logging.INFO)


class DBTest(unittest.TestCase):
    def test_user(self):
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
            _ua.photo_url = os.path.join(BASE_URL,_user.user_id+"/"+encrypt.md5_1(_user.user_id)+".jpg")
            _ua.domain_desc = "SSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjk"
            _ua.work_desc = "SSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjkSSSSdehiudiewqugefgiegdfiueudeheudhidwdjk"
            _ua.save()
            count += 1
        #self.assertEqual(count,101)
        print "test_user done"

    def test_dictionary(self):
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
        
        print "test_dictionary done"
        
    def test_invitor(self):
        for i in range(100):
            _invitor_task = InvitorTask(project_publisher=i+1,
                                        project_invitors="1,45,89,20",
                                        project_context="publisher the invitor task",
                                        project_time = time.time()
                                        )
            _invitor_task.save()
        print "test_invitor done"   
    
    def test_questions(self):
        for i in range(100):
            _status_code = "0"
            if i%3 == 1:
                _status_code="1"
            elif i%3 == 2:
                _status_code="2"
                
            _q = Question(qt_title="question title %d" % i,
                          qt_desc="question desc %d " % i,
                          qt_status=_status_code,
                          qt_begin_time=time.time(),
                          qt_end_time=util.afterOneDay(),
                          qt_type_codes="10009,10003,20005",
                          qt_ask_user=i+1,
                          qt_answer_user=i%30,
                          groom_degree=(i%5)+"",
                          server_degree=(i%5)+"",
                          ability_degree=(i%5)+"",
                          qt_answer_remarked="very professional",
                          )
            _q.save()
        print "test_questions done"
    
    def test_sysapp(self):
        for i in range(100):
            _email = "kxl_90_%d@192.com" % i
            _f = AppFeedback(feed_email=_email,
                        feed_context="this app is too rubbished to use,dam,dam,dam")
            _f.save()
            
        print "test_sysapp done"
        
    def test_task(self):
        for i in range(100):
            _status_code = "0"
            if i%3 == 1:
                _status_code="1"
            elif i%3 == 2:
                _status_code="2"
            _task = AppTask(task_title="task title %d " % i,
                            task_deploy_time = util.getCurrentTime(),
                            task_deploy_user = i%40,
                            task_price = i * 5,
                            task_type_codes = "10005,20002",
                            task_desc="task desc %d " % i,
                            task_status = _status_code
                            )
            _task.save()
        
        print "test_sysapp done"
    
if __name__ == '__main__':
    unittest.main()