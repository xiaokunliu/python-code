#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from libmc import (
    Client, MC_HASH_MD5, MC_POLL_TIMEOUT, MC_CONNECT_TIMEOUT, MC_RETRY_TIMEOUT
)
from mc_decorator import create_decorators
u"""
创建数据库的连接
"""

mc = Client(
    # 服务器列表
    [
        'localhost',
        'localhost:11212',
        'localhost:11213 mc_213'
    ],
    do_split=True,       # 默认是False，拒绝大于1MB的存储，True表示小于10M会被切分成多个块，但是不能存储大于10M
    comp_threshold=0,    #
    noreply=False,
    prefix=None,
    hash_fn=MC_HASH_MD5,
    failover=False
)

mc.config(MC_POLL_TIMEOUT, 100)  # 100 ms
mc.config(MC_CONNECT_TIMEOUT, 300)  # 300 ms
mc.config(MC_RETRY_TIMEOUT, 5)  # 5 s

globals().update(create_decorators(mc))


class PyMemcached(object):
    u"""
    使用Libmc库
    1.安装memcached:
    sudo apt-get install memcahced

    2. 启用分布式缓存,启动另外的两个监听端口
    /usr/bin/memcached -m 64 -p 11212 -u memcache -l 127.0.0.1 -d
    /usr/bin/memcached -m 64 -p 11213 -u memcache -l 127.0.0.1 -d

    3. 安装libmc
    pip install libmc
    """

    @staticmethod
    def get_cache():
        pass
