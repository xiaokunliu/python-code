#!/usr/bin/env python
# -*- coding: UTF-8 -*-

u"""
使用SqlAlchemy ORM框架进行DB操作开发
http://docs.sqlalchemy.org/en/latest/
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import logging

_Base = declarative_base()
_logger = logging.getLogger(__name__)


class BaseModel(_Base):
    u"""
    数据库基础模型
    """
    _engine = None

    @classmethod
    def build_sql_engine(cls,
                         user_name,
                         password,
                         db_name,
                         host="127.0.0.1",
                         port=3306):
        _sql = "mysql://%{user_name}s:%{password}@" \
               "%{host}s:%{port}s/%{db_name}?charset=utf8" % \
               {"user_name": user_name,
                "password": password,
                "host": host,
                "port": port,
                "db_name": db_name}
        _logger.info("the sql is [%s]", _sql)
        if not cls._engine:
            cls._engine = create_engine(_sql,)
        return cls._engine

    @classmethod
    def drop_tables(cls):
        cls.metadata.drop_all(bind=cls._engine)

    @classmethod
    def create_tables(cls):
        cls.metadata.create_all(bind=cls._engine)

    @classmethod
    def build_session(cls):
        Session = sessionmaker(bind=cls._engine)
        return Session()

## 使用实例


class UserInfo(BaseModel):
    u"""
    定义一个持久化的用户模型
    """
    pass

