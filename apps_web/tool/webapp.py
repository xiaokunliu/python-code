#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""this webapp.py is mainly to increse the method of the request and the response 
   to define the app error to deal with the logic error 
"""   

import json

class AppError(Exception):
    pass

class json_object(object):
    def __init__(self,rs_data,code=200,desc="success"):
        self.code = code
        self.desc = desc
        if rs_data is None:
            raise AppError("pass the rs_data is required,not none..")
        self.result = rs_data
        
    
def jsonToObject(jsonstring):
    return json.loads(jsonstring)
    


# for test code    
    
# if __name__ == '__main__':
#     _testUser = Users(user_id=11,user_email="keithl@163.com",user_pwd=encrypt.md5_1("123456"))
#     _mydic = dict(user_id=_testUser.user_id,user_email=_testUser.user_email,user_pwd=_testUser.user_pwd) 
#     _json = json_object(_mydic)
#     print json.dumps(_json,default=lambda _json:_json.__dict__)  
#     jsonstring = '{"code": 200, "result": {"user_id": 11, "user_pwd": "E10ADC3949BA59ABBE56E057F20F883E", "user_email": "keithl@163.com"}, "desc": "success"}';
#     _obj = jsonToObject(jsonstring)
#     print _obj['code'],_obj['result'],_obj['desc']
#     _user_info = dict(_obj['result'])
#     print _user_info['user_id']
#     _u = Users(_user_info)
#     print _u
    

    
        