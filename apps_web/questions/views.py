
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
this views is mainly for develop core logic code
"""

import json

from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rongyun import api
from tool import cons, util
from tool.logs import getAppLog
from tool.webapp import AppError, json_object
from users.models import Users
from questions.models import Question


_qt_log = getAppLog()

def test(request):
    return HttpResponse("<h3>test questions</h3>")

@csrf_exempt
def publishQuestion(request):
    resp_json = None
    try:
        if request.method!="POST":
            _qt_log.error("the request is not post method")
            raise AppError(cons.respon_msg.POST_ERROR_METHOD)
         
        if not request.POST.get("strJson"):
            _qt_log.error("have not pass any args ...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
        
        jsonstring = request.POST.get("strJson")
        _qt_log.info("publishQuestion,jsonstirng is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        _auth_string = _map['user_auth']
        _token = _map['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
        
        _qt_log.info("the _token_expires is %s" % _token_expires)
        
        if _token_expires == 0:
            _qt_log.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _qt_log.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
        apiclient = api.getRongyun()
        
        fromUserId = Users.auth_manager.getId(_auth_string)
        toUserIds = Users.auth_manager.getUsersExceptSelf(_auth_string)
        _data = _map['data']
        _context = _data['context']
        _title = "you have a message"
        
        _resp_result = apiclient.message_system_publish(from_user_id=fromUserId,
                                        to_user_id=toUserIds, #at most 1000
                                        object_name='RC:TxtMsg',
                                        content=json.dumps({"content":_context}),
                                        push_content=_title,
                                        push_data=_title) 
        
         
        if _resp_result[u'code']!="200":
            _qt_log.error("published question fail,please check your network")
            raise AppError(cons.qt_error.QT_ADD_FAIL)
        
        _q = Question(qt_title=_title,
                      qt_desc=_context,
                      qt_begin_time=util.getCurrentTime(),
                      qt_end_time=util.afterOneDay(), #close the chat view
                      qt_ask_user=fromUserId)
        
        _q.save()
        _qt_id = Question.qt_manager.getLastestQtId(fromUserId)
        
        # set close the window when it run at _q.qt_end_time,may be should client to change
        ## define the timer to close the windows
        
        rs_data = dict(user_auth=_auth_string,
                       user_token=_token,
                       user_token_expires=util.formatTime(_token_expires),
                        qt_id=_qt_id
                       )
        resp_json = json_object(rs_data,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
        
    except AppError,e:
        _qt_log.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _qt_log.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG["code"],cons.respon_msg.ERROR_MSG["desc"])
    finally:        
        return JsonResponse(resp_json.__dict__,safe=False)


@csrf_exempt
def closeQt(request):
    resp_json = None
    try:
        if request.method!="POST":
            _qt_log.error("the request is not post method")
            raise AppError(cons.respon_msg.POST_ERROR_METHOD)
         
        if not request.POST.get("strJson"):
            _qt_log.error("have not pass any args ...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
        
        jsonstring = request.POST.get("strJson")
        _qt_log.info("updateStatus,jsonstirng is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        _auth_string = _map['user_auth']
        _token = _map['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
         
        if _token_expires == 0:
            _qt_log.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _qt_log.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
        _id = _map['data']['qt_id']
        
        _ask_id = Users.auth_manager.getId(_auth_string)
        
        _qt = Question.objects.get(qt_id=_id,qt_ask_user=_ask_id)
        _qt.qt_status = "2"  ##not any one to answer the question
        _qt.save()
        
        rs_data = dict(user_auth=_auth_string,
                       user_token=_token,
                       user_token_expires=util.formatTime(_token_expires)
                       )
        resp_json = json_object(rs_data,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
        
    except AppError,e:
        _qt_log.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _qt_log.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG["code"],cons.respon_msg.ERROR_MSG["desc"])
    finally:        
        return JsonResponse(resp_json.__dict__,safe=False)


@csrf_exempt
def answer(request):
    resp_json = None
    try:
        if request.method!="POST":
            _qt_log.error("the request is not post method")
            raise AppError(cons.respon_msg.POST_ERROR_METHOD)
         
        if not request.POST.get("strJson"):
            _qt_log.error("have not pass any args ...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
        
        jsonstring = request.POST.get("strJson")
        _qt_log.info("answer,jsonstirng is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        _auth_string = _map['user_auth']
        _token = _map['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
         
        if _token_expires == 0:
            _qt_log.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _qt_log.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
        _answer_id = Users.auth_manager.getId(_auth_string)
        ask_Id = Users.auth_manager.getId(_auth_string)
        _qt_id =  _map['data']['qt_id']
        _qt = Question.objects.get(qt_id=_qt_id,qt_ask_user=ask_Id)
        
        apiclient = api.getRongyun()
        _resp_result = apiclient.message_system_publish(from_user_id=_answer_id,
                                        to_user_id=_qt.qt_ask_user, #at most 1000
                                        object_name='RC:TxtMsg',
                                        content=json.dumps({"content":_qt.qt_desc}),
                                        push_content="您发布的问题已经有人回复,快去看看吧",
                                        push_data="有人回复问题") 
        
        if _resp_result[u'code']!="200":
            _qt_log.error("answer question fail,please check your network")
            raise AppError(cons.qt_error.QT_ADD_FAIL)
        
        _qt.qt_answer_user = _answer_id
        _qt.qt_status = "1"   ##executing 
        _qt.save()
        rs_data = dict(user_auth=_auth_string,
                       user_token=_token,
                       user_token_expires=util.formatTime(_token_expires)
                       )
        resp_json = json_object(rs_data,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
        
    except AppError,e:
        _qt_log.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _qt_log.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG["code"],cons.respon_msg.ERROR_MSG["desc"])
    finally:        
        return JsonResponse(resp_json.__dict__,safe=False)


@csrf_exempt
def remark(request):
    resp_json = None
    try:
        if request.method!="POST":
            _qt_log.error("the request is not post method")
            raise AppError(cons.respon_msg.POST_ERROR_METHOD)
         
        if not request.POST.get("strJson"):
            _qt_log.error("have not pass any args ...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
        
        jsonstring = request.POST.get("strJson")
        _qt_log.info("remark,jsonstirng is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        _auth_string = _map['user_auth']
        _token = _map['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
         
        if _token_expires == 0:
            _qt_log.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _qt_log.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
        ask_Id = Users.auth_manager.getId(_auth_string) 
        
        _data = _map['data']
        _qt_id = _data['qt_id']
        
        _qt = Question.objects.get(qt_ask_user=ask_Id,qt_id=_qt_id)
        
        _qt.groom_degree = _data['groom_degree']
        _qt.server_degree = _data['server_degree']
        _qt.ability_degree = _data['ability_degree']
        _qt.qt_answer_remarked = _data['qt_answer_remarked']
        
        _qt.save()
        rs_data = dict(user_auth=_auth_string,
                       user_token=_token,
                       user_token_expires=util.formatTime(_token_expires)
                       )
        resp_json = json_object(rs_data,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _qt_log.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _qt_log.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG["code"],cons.respon_msg.ERROR_MSG["desc"])
    finally:        
        return JsonResponse(resp_json.__dict__,safe=False)


def listAll(request):
    resp_json = None
    try:
        if request.method!="GET":
            _qt_log.error("the request is not post method")
            raise AppError(cons.respon_msg.GET_ERROR_METHOD)
         
        if not request.GET.get("strJson"):
            _qt_log.error("have not pass any args ...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
        
        jsonstring = request.POST.get("strJson")
        _qt_log.info("listAll,jsonstirng is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        _auth_string = _map['user_auth']
        _token = _map['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
         
        if _token_expires == 0:
            _qt_log.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _qt_log.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)

        _data = _map['data']
        _index = _data["pageIndex"]
        _size = _data["pageSize"]
        
        user_id = Users.auth_manager.getId(_auth_string)
        _qt_list = Question.qt_manager.getQtByAsker(user_id,_data['condition'],_data['order_by'],_data['optional_field'])
        resp_json = json_object(_qt_list,cons.respon_msg.SUCCESS_MSG['code'],cons.respon_msg.SUCCESS_MSG['desc'])
    except AppError,e:
        _qt_log.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _qt_log.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG["code"],cons.respon_msg.ERROR_MSG["desc"])
    finally:        
        return JsonResponse(resp_json.__dict__,safe=False)


def listRemark(request):
    resp_json = None
    try:
        if request.method!="GET":
            _qt_log.error("the request is not post method")
            raise AppError(cons.respon_msg.GET_ERROR_METHOD)
         
        if not request.GET.get("strJson"):
            _qt_log.error("have not pass any args ...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
        
        jsonstring = request.POST.get("strJson")
        _qt_log.info("listRemark,jsonstirng is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        _auth_string = _map['user_auth']
        _token = _map['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
         
        if _token_expires == 0:
            _qt_log.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _qt_log.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)

        _data = _map['data']
        _index = _data["pageIndex"]
        _size = _data["pageSize"]
        
        user_id = Users.auth_manager.getId(_auth_string)
        _remark_list = Question.qt_manager.getQuestionRemark(user_id, _data['condition'], _data['order_by'], _index, _size)
        resp_json = json_object(_remark_list,cons.respon_msg.SUCCESS_MSG['code'],cons.respon_msg.SUCCESS_MSG['desc'])
    except AppError,e:
        _qt_log.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _qt_log.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG["code"],cons.respon_msg.ERROR_MSG["desc"])
    finally:        
        return JsonResponse(resp_json.__dict__,safe=False)
    






