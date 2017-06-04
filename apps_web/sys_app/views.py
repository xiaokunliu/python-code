
## TODO add feedback
import json

from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from sys_app.models import AppFeedback
from tool import cons
from tool.logs import getAppLog
from tool.webapp import AppError, json_object


# Create your views here.
_sys_log = getAppLog()

def test(request):
    return HttpResponse("<h3>test sys_app</h3>")

@csrf_exempt
def feedback(request):
    resp_json = None
    try:
        if request.method!="POST":
            _sys_log.error("it must be use post method to submit request params")
            raise AppError(cons.respon_msg.POST_ERROR_METHOD)
        
        if not request.POST.get("strJson"):
            _sys_log.error("it have not pass any args ...")
            raise AppError(cons.respon_msg.NOT_PASS_ARGS)
        
        jsonstring = request.POST.get("strJson")
        _sys_log.info("feedback,jsonstirng is %s" % jsonstring)
        
        _map = json.loads(jsonstring)
        _data = _map['data']
        
        _feedback = AppFeedback(feed_email=_data['feed_email'],feed_context=_data['feed_context'])
        _feedback.save()
        
        resp_json = json_object(dict(),cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
    except AppError,e:
        _sys_log.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException,e:
        _sys_log.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG["code"],cons.respon_msg.ERROR_MSG["desc"])
    finally:
        return JsonResponse(resp_json.__dict__,save=False)
    
    