#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import random
import smtplib
from time import strftime
import time

from django.core.exceptions import ValidationError
from django.core.validators import validate_email


WEEK_TIME = 60 * 60 * 24 * 7
DAY_TIME = 60 * 60 * 24

def getTokenExpires():
    return time.time() + WEEK_TIME

def formatTime(input_time):
    return strftime('%Y-%m-%d %H:%M:%S',time.localtime(input_time))

def getCurrentTime():
    return time.time()

def formatStrToTime(str_time):
    return time.mktime(time.strptime(str_time,'%Y-%m-%d %H:%M:%S'))

def afterOneDay():
    return time.time() + DAY_TIME

def getDayFromZeroTime():
    _str_time = strftime('%Y-%m-%d',time.localtime(time.time()))
    _str_time = _str_time + " 00:00:00"
    _time = formatStrToTime(_str_time)
    return _time

def validateEmail(email):
    try:  
        validate_email( email )  
        return True  
    except ValidationError,e:  
        return False   

def listToStr(split_sign,_list_obj):
    return split_sign.join([str(i) for i in _list_obj])


def strToList(split_sign,_str_obj):
    return _str_obj.split(split_sign)
    

def getVerifyCode():
    nums = []
    for i in range(6):
        nums.append(random.randint(0,9))
    random.shuffle(nums)
    return ''.join([str(i) for i in nums])


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

## it not safe,have not been encrypt to send it
def sendEmail(to_addr,email_text,headText):
    from_addr = "kxl602@163.com"
    msg = MIMEText(email_text,"plain","utf-8")
    msg['From'] =  _format_addr(u'App产品经理  <%s>' % from_addr)
    msg['To'] =  _format_addr(u'xxxx用户  <%s>' % to_addr)
    msg['Subject'] = Header(u'请根据以下的验证码修改个人密码', 'utf-8').encode()
    
    server = smtplib.SMTP("smtp.163.com", 25) ##SSL 456  994 不安全为25
    server.starttls()
    server.set_debuglevel(1)
    server.login(from_addr, "lxklxk602")
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


def handle_uploaded_file(f,path):
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


if __name__ == '__main__':
#     _t = getTokenExpires()
#     print type(_t)
#     _cu = getCurrentTime()
#     print _cu
#     print formatTime(1451808142.131)
#     print formatStrToTime('2016-01-03 16:02:22')
#     print validateEmail("123934@22.com")
#     print getVerifyCode()
    
#     sendEmail("2897220919@qq.com", "hello python", "请确认你的验证码") 
#     print "done"    
#     print getDayFromZeroTime()
    
#     print listToStr(",", [0,92,394,2])
    print strToList(",", "0,10,33,89,33")
    