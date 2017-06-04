#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import os

from users.models import REAL_PATH


def testjson(jsonstring):
    _map = json.loads(jsonstring)
    print _map['user_name'],_map['user_email'],_map['user_pwd']



if __name__ == '__main__':
    """ this is for test json """
#     jsonstring = '{"user_name":"keithl","user_email":"kxl602@163.com","user_pwd":"123456"}'
#     testjson(jsonstring)
    
    """ this is  test for base64 """
#     base64_pwd = encrypt.encode_base64("123456")
#     print "encode base64 %s" % base64_pwd
#      
#     pwd = encrypt.decode_base64(base64_pwd)
#     print "decode base64 %s" % pwd
#     
#     print encrypt.build_auth("keithl", "123456")


    """  this is for jsonstring test  """
#     jsonstring = '{"data":{"user_alias_name":"xiaoxiao","user_pwd":"MTIzNDU2","user_email":"454878","user_auth":"341B7F704D6CB19D1C404932D90FA0FBFD856579"}}';
#     _obj = json.loads(jsonstring)
#     print _obj
#     _data = _obj['data']
#     print _data
#     print _data['user_alias_name'],_data['user_pwd'],_data['user_email'],_data['user_auth']

#     print time.time()

    """ for ip test """
#     ip =  inet_aton("192.168.235.10")
#     print type(ip)
#     print type(inet_ntoa(ip))
# 
#     """  test catch exception """
#     try:
#         _p = 9/0
#     except BaseException,e:
#         print e
#     finally:
#         print "done"
    
#     _str = "12,90,89"
#     if not isinstance(_str,list):
#         _str = [_str]
#     
#     for name in _str:
#         print name
    
    
    """  for string split test """
    _my_str = "2004,2330,3002"
    _my_str_list = _my_str.split("|,|")
    
    print len(_my_str_list)
#     for _str in _my_str_list:
#         print _str
    print os.path.join("2","7.jpng")








    