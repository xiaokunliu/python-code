#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
this views is mainly for develop core logic code
"""

import json
import os

from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from tool import cons, encrypt, util
from tool.logs import getAppLog
from tool.webapp import json_object, AppError
from users.models import Users, UsersAdditional, REAL_PATH, BASE_URL


_userlog = getAppLog()

def test(request):
    return HttpResponse("<h3>test user</h3>")

@csrf_exempt
def register(request):
    resp_json = None
    try:
        if request.method!="POST":
            raise AppError(cons.respon_msg.POST_ERROR_METHOD)
         
        if not request.POST.get("strJson"):
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
         
        jsonstring = request.POST.get("strJson")
        _userlog.info("register,jsonstirng is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        _data = _map['data']
        _uname = _data['user_alias_name']
        _upass = encrypt.decode_base64(_data['user_pwd'])
        _auth = _data['user_auth']
        _auth_string = encrypt.build_auth(_uname, _upass)
        
        if _auth_string!=_auth:
            raise AppError(cons.user_error.INVALIDATE_AUTH)
        
        count = Users.auth_manager.auth_count(_auth_string)
        if count > 0:
            raise AppError(cons.user_error.REGISTER_FAIL)
        
        if util.validateEmail(_data["user_email"]):        
            _user = Users(user_email=_data["user_email"],
                          user_pwd=encrypt.md5_1(_data["user_pwd"]),
                          user_alias_name=_uname,
                          user_auth=_auth_string,
                          user_token=encrypt.build_token(),
                          user_token_expires=util.getTokenExpires()
                         )
            _user.save()
            
            #it would be error 
            _query_user = Users.objects.get(user_auth=_auth_string)
            
            _user_add = UsersAdditional(user_id=_query_user.user_id)
            _user_add.save()
        
            ## "user_alias_name":"keithl","user_email":"xxxx@163.com","user_pwd":base64("123456"),"user_auth":"encrpyt()","user_token":"tokenId","user_token_expires":7*60*60*24
            rs_data = dict(user_alias_name=_user.user_alias_name,
                           user_email=_user.user_email,
                           user_auth=_user.user_auth,
                           user_token=_user.user_token,
                           user_token_expires=util.formatTime(_user.user_token_expires)
                           )
            resp_json = json_object(rs_data,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
        else:
            rs_data = dict()
            resp_json = json_object(rs_data,cons.user_error.INVALIDATE_EMAIL["code"],cons.user_error.INVALIDATE_EMAIL["desc"])
    except AppError,e:
        _userlog.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _userlog.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG["code"],cons.respon_msg.ERROR_MSG["desc"])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False)
    

def login(request):
    resp_json = None
    try:
        if request.method!="GET":
            raise AppError(cons.respon_msg.GET_ERROR_METHOD)       
        
        if not request.GET.get("strJson"):
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
        
        jsonstring = request.GET.get("strJson")
        _userlog.info("login,jsonstring is %s " % jsonstring)
        
        _map = json.loads(jsonstring)
        _data = _map['data']
        _auth_string = _data['user_auth']
        _token = _data['user_token']
        
        nums = Users.auth_manager.auth_count(_auth_string)
        if nums==0:
            _userlog.error("the user is not exist")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        
        # build token and token expires 
        _u = Users.objects.get(user_auth=_auth_string)
        _u.user_token =encrypt.build_token()
        _u.user_token_expires = util.getTokenExpires()
        _u.save()
        rs_data = dict(user_auth=_auth_string,
                       user_token=_u.user_token,
                       user_token_expires= util.formatTime(_u.user_token_expires)
                       )
        resp_json = json_object(rs_data,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _userlog.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _userlog.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG['code'],cons.respon_msg.ERROR_MSG['desc'])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False)
    
    
@csrf_exempt
def detail(request):
    resp_json = None
    try:
        if request.method!="POST":
            raise AppError(cons.respon_msg.POST_ERROR_METHOD)
        
        if not request.POST.get("strJson"):
            raise AppError(cons.respon_msg.NOT_PASS_ARGS) 
        
        jsonstring = request.POST.get("strJson")
        _userlog.info("detail,the jsonstring is %s " % jsonstring)
        
        _map = json.loads(jsonstring)
        _data = _map['data']
        _auth_string = _map['user_auth']
        _token = _map['user_token']
        
        nums = Users.auth_manager.auth_count(_auth_string)
        if nums == 0:
            _userlog.error("the user is not exist")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        
        _u = Users.objects.get(user_auth=_auth_string)
        if _u.user_token_expires < util.getCurrentTime():
            _userlog.error("you have to login again,the token expires have been out of date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
        _user_additional = UsersAdditional.objects.get(user_id=_u.user_id)
        _user_additional.domain_desc = _data['user_domain_desc']
        _user_additional.work_desc = _data['user_work_desc']
        _user_additional.save()
        
        rs_data = dict(user_auth=_auth_string,
                       user_token=_u.user_token,
                       user_token_expires= util.formatTime(_u.user_token_expires)
                       )
        resp_json = json_object(rs_data,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _userlog.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _userlog.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG['code'],cons.respon_msg.ERROR_MSG['desc'])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False) 
    
    
@csrf_exempt
def addPosition(request):
    resp_json = None
    try:
        if request.method!="POST":
            raise AppError(cons.respon_msg.POST_ERROR_METHOD)
        
        if not request.POST.get("strJson"):
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
        
        jsonstring = request.POST.get("strJson")
        _userlog.info("addPosition,the jsonstring is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        
        _auth_string = _map['user_auth']
        _token = _map['user_token']
        _token_expires = Users.auth_manager.token_expires(_auth_string)
        
        _userlog.info("the _token_expires is %s" % _token_expires)
        
        if _token_expires == 0:
            _userlog.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _userlog.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
        _data = _map['data']
        _longitude = _data['user_longitude']
        _latitude = _data['user_latitude']
        
        _u = Users.objects.get(user_auth=_auth_string,user_token=_token)
        _u.user_longitude = _longitude
        _u.user_latitude = _latitude
         
        _u.save()
                
        rs_data = dict(user_auth=_auth_string,
                       user_token=_token,
                       user_token_expires= util.formatTime(_u.user_token_expires)
                       )
        resp_json = json_object(rs_data,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _userlog.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException,e:
        _userlog.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG['code'],cons.respon_msg.ERROR_MSG['desc'])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False) 


@csrf_exempt
def editName(request):
    resp_json = None
    try:
        if request.method !="POST":
            raise AppError(cons.respon_msg.POST_ERROR_METHOD)
        
        if not request.POST.get("strJson"):
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
        
        jsonstring = request.POST.get("strJson")
        _userlog.info("editName,the jsonstring is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        
        _auth_string = _map['user_auth']
        _token = _map['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
        
        _userlog.info("the _token_expires is %s" % _token_expires)
        
        if _token_expires == 0:
            _userlog.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _userlog.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
        _data = _map['data']
        _user = Users.objects.get(user_auth=_auth_string,user_token=_token)
        _user.user_alias_name = _data['user_alias_name']
        _user.save()
        
        rs_data = dict(user_auth=_auth_string,
                       user_token=_token,
                       user_token_expires= util.formatTime(_user.user_token_expires)
                       )
        resp_json = json_object(rs_data,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _userlog.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException,e:
        _userlog.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG['code'],cons.respon_msg.ERROR_MSG['desc'])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False) 

@csrf_exempt
def editLabel(request):
    resp_json = None
    try:
        if request.method !="POST":
            raise AppError(cons.respon_msg.POST_ERROR_METHOD)
        
        if not request.POST.get("strJson"):
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
        
        jsonstring = request.POST.get("strJson")
        _userlog.info("editName,the jsonstring is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        
        _auth_string = _map['user_auth']
        _token = _map['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
        
        _userlog.info("the _token_expires is %s" % _token_expires)
        
        if _token_expires == 0:
            _userlog.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _userlog.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
        _data = _map['data']
        _user = Users.objects.get(user_auth=_auth_string,user_token=_token)
        _user.user_label_type = _data['user_label_type']
        _user.save()
        
        rs_data = dict(user_auth=_auth_string,
                       user_token=_token,
                       user_token_expires= util.formatTime(_user.user_token_expires),
                       user_label_type = _user.user_label_type
                       )
        resp_json = json_object(rs_data,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _userlog.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException,e:
        _userlog.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG['code'],cons.respon_msg.ERROR_MSG['desc'])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False) 
    

def queryUser(request):
    resp_json = None
    try:
        if request.method!="GET":
            raise AppError(cons.respon_msg.GET_ERROR_METHOD)       
         
        if not request.GET.get("strJson"):
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
        
        jsonstring = request.GET.get("strJson")
        _userlog.info("queryUser,the jsonstring is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        _data = _map['data']
        _auth_string = _data['user_auth']
        _token = _data['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
        
        _userlog.info("the user_token_expires %s" % _token_expires)
        
        if _token_expires == 0:
            _userlog.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _userlog.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
        _u = Users.objects.get(user_auth=_auth_string,user_token=_token)
        
        # build token and token expires 
        rs_data = dict(user_auth=_auth_string,
                       user_token=_token,
                       user_token_expires= util.formatTime(_u.user_token_expires),
                       user_id=_u.user_id,
                       user_email = _u.user_email,
                       user_phone = _u.user_phone,
                       user_really_name = _u.user_really_name,
                       user_alias_name = _u.user_alias_name,
                       user_sex = _u.user_sex,
                       user_longitude = _u.user_longitude,
                       user_latitude = _u.user_latitude,
#                        user_ip = _u.user_ip,
                       user_label_type = _u.user_label_type)
        resp_json = json_object(rs_data,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _userlog.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException,e:
        _userlog.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG['code'],cons.respon_msg.ERROR_MSG['desc'])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False)


def queryForDetail(request):
    resp_json = None
    try:
        if request.method!="GET":
            raise AppError(cons.respon_msg.GET_ERROR_METHOD)       
         
        if not request.GET.get("strJson"):
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
        
        jsonstring = request.GET.get("strJson")
        _userlog.info("queryForDeatil,the jsonstring is %s " % jsonstring)
        
        _map = json.loads(jsonstring)
        _data = _map['data']
        _auth_string = _data['user_auth']
        _token = _data['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
        _userlog.info("the user token expires %s" % _token_expires)
        
        if _token_expires == 0:
            _userlog.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _userlog.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
            
                
        _u = Users.objects.get(user_auth=_auth_string,user_token=_token)
        _ua = UsersAdditional.objects.get(user_id=_u.user_id)
        
        rs_data = dict(user_auth=_u.user_auth,
                       user_token=_u.user_token,
                       user_token_expires=util.formatTime(_u.user_token_expires),
                       photo_url=_ua.photo_url,
                       domain_desc=_ua.domain_desc,
                       work_desc=_ua.work_desc
                       )
        resp_json = json_object(rs_data,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _userlog.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _userlog.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG['code'],cons.respon_msg.ERROR_MSG['desc'])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False)
        
@csrf_exempt
def offerHelp(request):       
    try:
        if request.method!="POST":
            _userlog.error("it must be use post method...")
            raise AppError(cons.respon_msg.POST_ERROR_METHOD)
        
        if not request.POST.get("strJson"):
            _userlog.error("have not pass any args...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)    
        
        jsonstring = request.POST.get("strJson")
        _userlog.info("offerHelp,the jsonstring is %s " % jsonstring)
    
        _map = json.loads(jsonstring)
        _auth_string = _map['user_auth']
        _token = _map['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
        _userlog.info("the user token expires %s" % _token_expires)
        
        if _token_expires == 0:
            _userlog.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _userlog.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
        _u = Users.objects.get(user_auth=_auth_string,user_token=_token)
        _u.user_type = 1
        _u.save()
        
        rs_data = dict(user_auth=_u.user_auth,
                       user_token=_u.user_token,
                       user_token_expires=util.formatTime(_u.user_token_expires)
                       )
        resp_json = json_object(rs_data,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _userlog.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _userlog.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG['code'],cons.respon_msg.ERROR_MSG['desc'])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False)
    
@csrf_exempt    
def getVerifyCode(request):
    try:
        if request.method!="POST":
                _userlog.error("it must be use post method...")
                raise AppError(cons.respon_msg.POST_ERROR_METHOD)
            
        if not request.POST.get("strJson"):
            _userlog.error("have not pass any args...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)  
              
        jsonstring = request.POST.get("strJson")
        _userlog.info("getVerifyCode,the jsonstring is %s " % jsonstring)
    
        _map = json.loads(jsonstring) 
        
        _email = _map["data"]["user_email"]
    
        if util.validateEmail(_email):
            ## get verify code
            _verify_code = util.getVerifyCode()
            request.session['verify_code'] = _verify_code
            util.sendEmail(_email, "请根据以下的验证码去修改密码<br/>,验证码：<a style='color:black'>%s</a>" % _verify_code, "验证码确认")
            resp_json = json_object(dict(),cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
        else:
            resp_json = json_object(dict(),cons.user_error.INVALIDATE_EMAIL["code"],cons.user_error.INVALIDATE_EMAIL["desc"])
        
    except AppError,e:
        _userlog.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _userlog.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG['code'],cons.respon_msg.ERROR_MSG['desc'])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False)

@csrf_exempt    
def updatePwd(request):
    try:
        if request.method!="POST":
                _userlog.error("it must be use post method...")
                raise AppError(cons.respon_msg.POST_ERROR_METHOD)
            
        if not request.POST.get("strJson"):
            _userlog.error("have not pass any args...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)  
              
        jsonstring = request.POST.get("strJson")
        _userlog.info("updatePwd,the jsonstring is %s " % jsonstring)
        
        _map = json.loads(jsonstring)
        _auth_string = _map['user_auth']
        _token = _map['user_token']
        
        _num = Users.auth_manager.auth_count(_auth_string)
        if _num < 0 :
            _userlog.error("the auth have been modified,invalidate operate")
            raise AppError(cons.user_error.INVALIDATE_AUTH)
        
        
        _data = _map['data']
        _pwd = _data['user_pwd']
        _encrypt_pwd = _data['encrypt_pwd']
        if encrypt.md5_1(_pwd)!=_encrypt_pwd:
            _userlog.error("the password have been changed,not modify the password")
            raise AppError(cons.user_error.UPDATE_PWD_FAIL)
#       "data":{"user_pwd":"","encrypt_pwd":"md5(pwd)","verify_code":""}//密码使用base64进行传输,加密的密码传输到时再具体商量用什么规则加密
        
        _verify_code = _data['verify_code']
        if request.session['verify_code']!=_verify_code:
            _userlog.error("the verify_code have been changed,not modify the password")
            raise AppError(cons.user_error.UPDATE_PWD_FAIL)
        
        
        _u = Users.objects.get(user_auth=_auth_string)
        _u.user_pwd =  encrypt.md5_1(_pwd)
        _u.user_auth =  encrypt.build_auth(_u.user_alias_name, _pwd)
        _u.save()
        
        ## return 
        rs_data = dict(user_auth=_u.user_auth)
        resp_json = json_object(rs_data,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
        
    except AppError,e:
        _userlog.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _userlog.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG['code'],cons.respon_msg.ERROR_MSG['desc'])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False)
  

#upload pictures,TODO have not been tested
@csrf_exempt
def uploadImg(request):
    resp_json = None
    try:
        if request.method!="POST":
                _userlog.error("it must be use post method...")
                raise AppError(cons.respon_msg.POST_ERROR_METHOD)
        
        if not request.POST.get("strJson"):
            _userlog.error("have not pass any args...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)  
              
        jsonstring = request.POST.get("strJson")
        _userlog.info("updatePwd,the jsonstring is %s " % jsonstring)
        
        _map = json.loads(jsonstring)
        _auth_string = _map['user_auth']
        _token = _map['user_token']
        
        _num = Users.auth_manager.auth_count(_auth_string)
        if _num < 0 :
            _userlog.error("the auth have been modified,invalidate operate")
            raise AppError(cons.user_error.INVALIDATE_AUTH)   
        
        
        _u = Users.objects.get(user_auth=_auth_string)
        _ua = UsersAdditional.objects.get(user_id=_u.user_id) 
        
        ##write file to server
        _user_floder = os.path.join(REAL_PATH,_u.user_id)
        if not os.path.exists(_user_floder):
            os.mkdir(_user_floder)
        
        _f = request.FILES['file']
        #get file external file
        _f_ext_name = str(_f.name).split(".")[-1]
        _f_name = encrypt.build_token()+"."+_f_ext_name
        _f_path = os.path.join(_user_floder,_f_name)
        util.handle_uploaded_file(_f, _f_path)
        
        _path = os.path.join(_u.user_id,_f_name)
        _ua.photo_url = os.path.join(BASE_URL,_path)
        
        _ua.save()
        resp_json = json_object(dict(),cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _userlog.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _userlog.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG['code'],cons.respon_msg.ERROR_MSG['desc'])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False)


#logout 







    
    