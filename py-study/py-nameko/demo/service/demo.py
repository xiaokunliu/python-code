# -*- coding: utf-8 -*-
# vim: et ts=4 sw=4
"""
服务入口文件。
"""
import logging
import time

from nameko.dependency_providers import Config
from nameko_consul import http
from nameko_dyconf import DyConf
from nameko_redis import Redis
from nameko_swagger import Swagger
from nameko_zipkin import Zipkin

logger = logging.getLogger(__name__)


class Service(object):

    name = 'demo'
    dyconf = DyConf()
    cache = Redis('cache')
    swagger = Swagger()
    zipkin = Zipkin(name)
    config = Config(name)

    @swagger.unmarshal_request
    @http('GET', '/v1/demo/health')
    def http_get_health(self, request):
        return dict(code='OK', msg='', data={}, time=int(time.time()))

    @swagger.unmarshal_request
    @http('GET', '/v1/demo/path/index/<int:uid>')
    def path_index(self, request, uid):
        logger.info(request)
        logger.info(uid)
        return dict(code='OK', msg='', data={r"msg": "path index success..."},
                    time=int(time.time()))

    @swagger.unmarshal_request
    @http('GET', '/v1/demo/query/index')
    def query_index(self, request, cid):
        logger.info(request)
        logger.info(cid)
        return dict(code='OK',
                    msg='',
                    data={"cid": cid},
                    time=int(time.time()))

    @swagger.unmarshal_request
    @http('GET', '/v1/demo/query/many')
    def query_many(self, request,
                   cid,
                   uid=0,
                   channelid=0):
        logger.info(request)
        logger.info(cid)
        logger.info(uid)
        logger.info(channelid)
        return dict(code='OK',
                    msg='',
                    data={"cid": cid,
                          "uid": uid,
                          "channelid": channelid},
                    time=int(time.time()))

    @swagger.unmarshal_request
    @http('POST', '/v1/demo/post')
    def do_post(self, request,
                   cid,
                   uid=0,
                   channelid=""):
        logger.info(request)
        logger.info(cid)
        logger.info(uid)
        logger.info(channelid)
        return dict(code='OK',
                    msg='do post message',
                    data={"cid": cid,
                          "uid": uid,
                          "channelid": channelid},
                    time=int(time.time()*1000))

    @swagger.unmarshal_request
    @http('POST', '/v1/demo/post/query')
    def query_post(self, request,
                   cid,
                   uid=0,
                   channelid=""):
        logger.info(request)
        logger.info(cid)
        logger.info(uid)
        logger.info(channelid)
        return dict(code='OK',
                    msg='query post message',
                    data={"cid": cid,
                          "uid": uid,
                          "channelid": channelid},
                    time=int(time.time() * 1000))

    @swagger.unmarshal_request
    @http('POST', '/v1/demo/post/body')
    def query_body(self, request, jsonParameters):
        return dict(code='OK',
                    msg='query post message',
                    data=jsonParameters,
                    time=int(time.time() * 1000))