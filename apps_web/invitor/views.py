import json

from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from invitor.models import InvitorTask
from rongyun import api
from tool import cons, util
from tool.logs import getAppLog
from tool.webapp import AppError, json_object
from users.models import Users


# Create your views here.
_invitor_log = getAppLog()

def test(request):
    return HttpResponse("<h3>hello invitor</h3>")

@csrf_exempt
def addInvitor(request):
    resp_json = None
    try:
        if request.method!="POST":
            _invitor_log.error("client must use post method to submit json data")
            raise AppError(cons.respon_msg.POST_ERROR_METHOD)
        
        if not request.POST.get("strJson"):
            _invitor_log.error("it have not pass any args ...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
        
        jsonstring = request.POST.get("strJson")
        _invitor_log.info("addTask,jsonstirng is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        _auth_string = _map['user_auth']
        _token = _map['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
        
        _invitor_log.info("the _token_expires is %s" % _token_expires)
        
        if _token_expires == 0:
            _invitor_log.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _invitor_log.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
        _data = _map['data']
        labelType = _data['invitor_label_type']
        user_latitude = _data['user_latitude']
        user_longitude = _data['user_longitude']
        _context = _data['invitor_dec']
        _title = "you have a message"
                
        apiclient = api.getRongyun()
        fromUserId = Users.auth_manager.getId(_auth_string)
        _count = InvitorTask.invitor_manager.countInvitor(fromUserId)
        if _count>3:
            _invitor_log.error("you just could publish the project three times at a day")
            raise AppError(cons.task_error.TASK_ADD_FAIL)
        
        toUserIds = Users.auth_manager.getUserIdByLabelType(labelType, user_latitude, user_longitude)
        _resp_result = apiclient.message_system_publish(from_user_id=fromUserId,
                                        to_user_id=toUserIds, #at most 1000
                                        object_name='RC:TxtMsg',
                                        content=json.dumps({"content":_context}),
                                        push_content=_title,
                                        push_data=_title) 
         
        if _resp_result[u'code']!="200":
            _invitor_log.error("addInvitor fail,please check your network")
            raise AppError(cons.invitor_error.INVITOR_ADD_FAIL)
        
        _invitor_task = InvitorTask(project_publisher=fromUserId,
                                    project_invitors=util.listToStr(",", toUserIds),
                                    project_context= _context,
                                    project_time=util.getCurrentTime()
                                    )
        _invitor_task.save()
        _obj = dict(user_auth=_auth_string,
                    user_token=_token,
                    _token_expires = util.formatTime(_token_expires)
                    )
        resp_json = json_object(_obj,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _invitor_log.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _invitor_log.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG["code"],cons.respon_msg.ERROR_MSG["desc"])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False)


def listAllByToday(request):
    resp_json = None
    try:
        if request.method!="GET":
            _invitor_log.error("client must use get method to submit json data")
            raise AppError(cons.respon_msg.GET_ERROR_METHOD)
        
        if not request.GET.get("strJson"):
            _invitor_log.error("it have not pass any args ...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
        
        jsonstring = request.POST.get("strJson")
        _invitor_log.info("listAllByToday,jsonstring is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        _auth_string = _map['user_auth']
        _token = _map['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
        
        _invitor_log.info("the _token_expires is %s" % _token_expires)
        
        if _token_expires == 0:
            _invitor_log.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _invitor_log.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
#         _data = _map['data']
        _user_id = Users.auth_manager.getId(_auth_string)
        _task_list = InvitorTask.invitor_manager.getCurrentInvitor(_user_id)
        _obj = dict(dataList=_task_list,
                    total=len(_task_list)
                    )
        resp_json = json_object(_obj,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _invitor_log.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _invitor_log.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG["code"],cons.respon_msg.ERROR_MSG["desc"])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False)


def queryInvitorById(request):
    resp_json = None
    try:
        if request.method!="GET":
            _invitor_log.error("client must use get method to submit json data")
            raise AppError(cons.respon_msg.GET_ERROR_METHOD)
        
        if not request.GET.get("strJson"):
            _invitor_log.error("it have not pass any args ...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
        
        jsonstring = request.POST.get("strJson")
        _invitor_log.info("queryInvitorById,jsonstring is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        _auth_string = _map['user_auth']
        _token = _map['user_token']
        
        _token_expires = Users.auth_manager.token_expires(_auth_string)
        
        _invitor_log.info("the _token_expires is %s" % _token_expires)
        
        if _token_expires == 0:
            _invitor_log.error("the user is not exist...")
            raise AppError(cons.user_error.USER_NOT_EXIST)
        elif 0 < _token_expires < util.getCurrentTime():
            _invitor_log.error("the user token have been out of the date")
            raise AppError(cons.respon_msg.OUT_OF_DATE)
        
        _data = _map['data']
        _invitor_id = _data['invitor_id']
        _user_id = Users.auth_manager.getId(_auth_string)
        _obj = InvitorTask.invitor_manager.getInvitorTask(_user_id, _invitor_id)
        resp_json = json_object(_obj,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _invitor_log.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _invitor_log.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG["code"],cons.respon_msg.ERROR_MSG["desc"])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False) 