#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
this is for task service logic 
"""


import json

from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rongyun import api
from task.models import AppTask
from tool import cons, util
from tool.logs import getAppLog
from tool.webapp import AppError, json_object
from users.models import Users


# Create your views here.
_task_log = getAppLog()

def test(request):
    return HttpResponse("<h3>hello task...</h3>")


@csrf_exempt
def addTask(request):
    resp_json =None
    try:
        if request.method!="POST":
            _task_log.error("client must use post method to submit json data")
            raise AppError(cons.respon_msg.POST_ERROR_METHOD)
        
        if not request.POST.get("strJson"):
            _task_log.error("it have not pass any args ...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
         
        jsonstring = request.POST.get("strJson")
        _task_log.info("addTask,jsonstirng is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        _data = _map['data']
        _auth_string = _data['user_auth']
        _token = _data['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
        
        _task_log.info("the _token_expires is %s" % _token_expires)
        
        if _token_expires == 0:
            _task_log.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _task_log.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
        apiclient = api.getRongyun()
        fromUserId = Users.auth_manager.getId(_auth_string)
        toUserIds = Users.auth_manager.getUsersExceptSelf(_auth_string)
        _data = _map['data']
        _context = _data['task_desc']
        _title = _data['task_title']
        
        _resp_result = apiclient.message_system_publish(from_user_id=fromUserId,
                                        to_user_id=toUserIds, #at most 1000
                                        object_name='RC:TxtMsg',
                                        content=json.dumps({"content":_context}),
                                        push_content=_title,
                                        push_data="有人发布任务客，快去看看吧") 
        
         
        if _resp_result[u'code']!="200":
            _task_log.error("addTask fail,please check your network")
            raise AppError(cons.task_error.TASK_ADD_FAIL)
        
        _task = AppTask(task_title=_data['task_title'],
                        task_price=float(_data['task_price']),
                        task_type_codes=_data['task_type_codes'],
                        task_desc=_data['task_desc'],
                        task_deploy_time = util.getCurrentTime(),
                        task_deploy_user=fromUserId,
                        task_status="0"  ##publish the task
                        )
        
        _task.save()
        _obj=dict(user_auth=_auth_string,
                  user_token=_token,
                  user_token_expires=util.formatTime(_token_expires)
                  )
        resp_json = json_object(_obj,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _task_log.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _task_log.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG["code"],cons.respon_msg.ERROR_MSG["desc"])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False)
     
        
@csrf_exempt
def redeploy(request):
    resp_json = None
    try:
        if request.method!="POST":
            _task_log.error("client must use post method to submit json data")
            raise AppError(cons.respon_msg.POST_ERROR_METHOD)
        
        if not request.POST.get("strJson"):
            _task_log.error("it have not pass any args ...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
         
        jsonstring = request.POST.get("strJson")
        _task_log.info("redeploy task,jsonstirng is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        _data = _map['data']
        _auth_string = _data['user_auth']
        _token = _data['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
        
        _task_log.info("the _token_expires is %s" % _token_expires)
        
        if _token_expires == 0:
            _task_log.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _task_log.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
        apiclient = api.getRongyun()
        fromUserId = Users.auth_manager.getId(_auth_string)
        toUserIds = Users.auth_manager.getUsersExceptSelf(_auth_string)
        _data = _map['data']
        _tid = _data['task_id']
        _t = AppTask.objects.get(task_id=_tid,task_deploy_user=fromUserId)
        
        _resp_result = apiclient.message_system_publish(from_user_id=fromUserId,
                                        to_user_id=toUserIds, #at most 1000
                                        object_name='RC:TxtMsg',
                                        content=json.dumps({"content":_t.task_desc}),
                                        push_content=_t.task_title,
                                        push_data="有人发布任务客，快去看看吧") 
        
         
        if _resp_result[u'code']!="200":
            _task_log.error("published question fail,please check your network")
            raise AppError(cons.task_error.TASK_REPLOY_FAIL)
        
        _t.task_status = "2"
        _t.save()
       
        _obj = dict(user_auth=_auth_string,
                    user_token=_token,
                    user_token_expires=util.formatTime(_token_expires)
                    )
        resp_json = json_object(_obj,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _task_log.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _task_log.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG["code"],cons.respon_msg.ERROR_MSG["desc"])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False)

@csrf_exempt
def receiveTask(request):
    resp_json = None
    try:
        if request.method!="POST":
            _task_log.error("client must use post method to submit json data")
            raise AppError(cons.respon_msg.POST_ERROR_METHOD)
        
        if not request.POST.get("strJson"):
            _task_log.error("it have not pass any args ...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
         
        jsonstring = request.POST.get("strJson")
        _task_log.info("receiveTask,jsonstirng is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        _data = _map['data']
        _auth_string = _data['user_auth']
        _token = _data['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
        
        _task_log.info("the _token_expires is %s" % _token_expires)
        
        if _token_expires == 0:
            _task_log.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _task_log.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
        apiclient = api.getRongyun()
        fromUserId = Users.auth_manager.getId(_auth_string)
        _data = _map['data']
        _tid = _data['task_id']
        _t = AppTask.objects.get(task_id=_tid,task_deploy_user=fromUserId)
        
        _resp_result = apiclient.message_system_publish(from_user_id=fromUserId,
                                        to_user_id=_t.task_deploy_user, #at most 1000
                                        object_name='RC:TxtMsg',
                                        content=json.dumps({"content":_t.task_desc}),
                                        push_content=_t.task_title,
                                        push_data="有人发布任务客，快去看看吧") 
        
         
        if _resp_result[u'code']!="200":
            _task_log.error("receiveTask fail,please check your network")
            raise AppError(cons.task_error.TASK_ANSWER_FAIL)
        
        _t.task_status = "1"
        _t.save()
       
        _obj = dict(user_auth=_auth_string,
                    user_token=_token,
                    user_token_expires=util.formatTime(_token_expires)
                    )
        resp_json = json_object(_obj,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _task_log.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _task_log.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG["code"],cons.respon_msg.ERROR_MSG["desc"])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False)


@csrf_exempt
def cooperate(request):
    resp_json = None
    try:
        if request.method!="POST":
            _task_log.error("client must use post method to submit json data")
            raise AppError(cons.respon_msg.POST_ERROR_METHOD)
        
        if not request.POST.get("strJson"):
            _task_log.error("it have not pass any args ...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
         
        jsonstring = request.POST.get("strJson")
        _task_log.info("receiveTask,jsonstirng is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        _data = _map['data']
        _auth_string = _data['user_auth']
        _token = _data['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
        
        _task_log.info("the _token_expires is %s" % _token_expires)
        
        if _token_expires == 0:
            _task_log.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _task_log.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
        fromUserId = Users.auth_manager.getId(_auth_string)
        _data = _map['data']
        _tid = _data['task_id']
        _t = AppTask.objects.get(task_id=_tid,task_deploy_user=fromUserId)
        
        _t.task_status = "3"
        _t.save()
       
        _obj = dict(user_auth=_auth_string,
                    user_token=_token,
                    user_token_expires=util.formatTime(_token_expires)
                    )
        resp_json = json_object(_obj,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _task_log.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _task_log.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG["code"],cons.respon_msg.ERROR_MSG["desc"])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False)



def queryTaskByPublisher(request):
    resp_json = None
    try:
        if request.method!="POST":
            _task_log.error("client must use post method to submit json data")
            raise AppError(cons.respon_msg.POST_ERROR_METHOD)
        
        if not request.POST.get("strJson"):
            _task_log.error("it have not pass any args ...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
         
        jsonstring = request.POST.get("strJson")
        _task_log.info("receiveTask,jsonstirng is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        _auth_string = _map['user_auth']
        _token = _map['user_token']
        _token_expires = Users.auth_manager.token_expires(_auth_string)
        _task_log.info("the _token_expires is %s" % _token_expires)
        
        if _token_expires == 0:
            _task_log.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _task_log.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
        _data = _map['data']
        _index = _data['pageIndex']
        _size = _data['pageSize']
        ask_id = Users.auth_manager.getId(_auth_string)
        _task_list = AppTask.task_manager.getTaskByAsker(ask_id, _index, _size)
        resp_json = json_object(_task_list,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _task_log.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _task_log.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG["code"],cons.respon_msg.ERROR_MSG["desc"])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False)
