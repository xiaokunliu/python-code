from django.http.response import JsonResponse

from dictionary.models import LabelType
from tool import cons
from tool.logs import getAppLog
from tool.webapp import AppError, json_object


# Create your views here.
_dic_log = getAppLog()

def getLabelTypes(request):
    resp_json = None
    try:
        if request.method!="GET":
            _dic_log.error("this must be use get method")
            raise AppError(cons.respon_msg.GET_ERROR_METHOD)       
         
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
        
        _dic_log.info(_obj_list)
        resp_json = json_object(_obj_list,cons.respon_msg.SUCCESS_MSG["code"],cons.respon_msg.SUCCESS_MSG["desc"])
        
    except AppError,e:
        _dic_log.error(e)
        _obj = {"msg":e[0]['msg']}
        resp_json = json_object(_obj,e[0]['code'],cons.respon_msg.FAIL_DESC)
    except BaseException as e:
        _dic_log.error(e)
        _obj = {"msg":e}
        resp_json = json_object(_obj,cons.respon_msg.ERROR_MSG['code'],cons.respon_msg.ERROR_MSG['desc'])
    finally:
        return JsonResponse(resp_json.__dict__,safe=False)
    
    
    
    
    
    