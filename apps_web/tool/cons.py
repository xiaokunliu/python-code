#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"define the web project absoulte path"
# BASE_PATH = "D://python//git//apps_web//"  #"D://python//git//apps_web//"  F://mywork//work//apps_web//

"""the json code"""

class respon_msg(object):
    SUCCESS_MSG = {"code":200,"desc":"success"}
    ERROR_MSG = {"code":0,"desc":"error"}
    FAIL_DESC = "fail"
    
    """ for server error """
    POST_ERROR_METHOD = {"code":50001,"msg":"should be use post method to sumbit the data"}
    GET_ERROR_METHOD = {"code":50002,"msg":"should be use get method to sumbit the data"}
    NOT_PASS_ARGS = {"code":50003,"msg":"not pass any args from client,the strJson is none"}
    OUT_OF_DATE = {"code":50004,"msg":"the token expies have been out of the date"}


"""  just for logic error code as follow """
class user_error(object):
    USER_NOT_EXIST = {"code":500010,"msg":"the user is not exist"}
    """ for register """
    INVALIDATE_AUTH = {"code":500011,"msg":"the auth have been changed through the network,invalidate operate "}
    REGISTER_FAIL = {"code":500012,"msg":"the user have been registered before"}
    INVALIDATE_EMAIL  = {"code":500013,"msg":"invalidate user email"}
    
    """ for login """
    LOGIN_FAIL = {"code":500021,"msg":"login fail,input error email or password or have not been registered"}
    
    """ for update  """
    UPDATE_PWD_FAIL = {"code":500031,"msg":"update pwd fail,input the previous password error"}
    UPDATE_DETAIL_FAIL = {"code":500032,"msg":"update the user detail fail"}
    UPDATE_DETAIL_FAIL = {"code":500032,"msg":"update the user detail fail"}
    
    ## TODO add other function code
    
class qt_error(object):    
    QT_ADD_FAIL = {"code":500100,"msg":"publish question fail"}
    CLOSE_QT_FAIL = {"code":500101,"msg":"update question status fail"}
    QT_ANSWER_FAIL = {"code":500102,"msg":"answer question fail"}
    QT_REMARK_FAIL = {"code":500103,"msg":"remark question fail"}
    

class task_error(object):
    TASK_ADD_FAIL = {"code":500200,"msg":"publish task fail"}
    TASK_REPLOY_FAIL = {"code":500201,"msg":"reploy task fail"}
    TASK_ANSWER_FAIL = {"code":500202,"msg":"answer task fail"}
    TASK_REMARK_FAIL = {"code":500203,"msg":"remark task fail"}


class invitor_error(object):
    INVITOR_ADD_FAIL = {"code":500300,"msg":"publish invitor fail"}
    #INVITOR_REPLOY_FAIL = {"code":500301,"msg":"update question status fail"}
    INVITOR_ANSWER_FAIL = {"code":500301,"msg":"answer invitor fail"}
    INVITOR_REMARK_FAIL = {"code":500302,"msg":"remark invitor fail"}

 
 
 