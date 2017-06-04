#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
this encrypt.py is used for encrypt the text or build the token or auth
"""

import base64
import hashlib
import md5
import uuid


ENCRYPT_KEY = "" ## TODO create auth and token key

class NullError(Exception):
    pass

# use for this to encrypt the text
def md5_1(strText):
    if strText is not None:
        m5 = hashlib.md5();
        m5.update(strText)
        return m5.hexdigest().upper()
    raise NullError("the strText %s is null.." % strText)

def md5_2(strText):
    if strText is not None:
        m5_2 = md5.new()
        m5_2.update(strText)
        return m5_2.hexdigest().upper()
    raise NullError("the strText %s is null.." % strText)

def sha1(strText):
    if strText is not None:
        encry_sha1 = hashlib.sha1()
        encry_sha1.update(strText)
        return encry_sha1.hexdigest().upper()
    raise NullError("the strText %s is null.." % strText)

def encode_base64(strText):
    if strText is not None:
        return base64.b64encode(strText)
    raise NullError("the strText %s is null.." % strText)


def decode_base64(strText):
    if strText is not None:
        return base64.b64decode(strText)
    raise NullError("the strText %s is null.." % strText)

def uuid_3(namespace,name):
    return uuid.uuid3(namespace,name)   # use MD5 encrypt text,just for unqiue namespace and name

def uuid_5(namespace,name):
    return uuid.uuid5(namespace,name) # use SHA! encrypt text,just for unqiue namespace and name

def uuid_1():
    _str =  uuid.uuid1().__str__()
    return _str.replace("-","").upper()

def build_auth(user_name,user_pwd):
    _encryptName = sha1(user_name)
    _encryptPwd = sha1(user_pwd)
    _text = _encryptName + _encryptPwd + ENCRYPT_KEY
    return sha1(_text)

def build_token():
    _ud1 = uuid_1()
    _ud2 = uuid_1()
    strText = _ud1 + _ud2
    return sha1(strText)



# if __name__ == '__main__':
    #B05231A6E448C977849BE158F32C38E120EAFA35
#     print build_token()
#     print build_auth("xiaoxiao", "123456")
#     _strText = "sha1djlkl"
#     encry_text = sha1(_strText)
#     print encry_text
#      
#     s = encode_base64("xiaoxiao")
#     print s
#      
#     print decode_base64(s)
#     print uuid_1()

