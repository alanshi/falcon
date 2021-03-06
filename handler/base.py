#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Filename: base.py
# -----------------------------------------------------------------
# 2014-10-05  created

import functools

import tornado.web
from tornado.log import logging

from db.mongo import db_interface

class BaseHandler(tornado.web.RequestHandler):

  """
  BaseHandler 类,继承自tornado.web.RequestHandler类,用于向Handler视图层提供最基础的服务
  """

  def __init__(self, *argc, **argkw):
    """
    初始化 BaseHandler类,实例化session
    """
    super(BaseHandler, self).__init__(*argc, **argkw)

    #打印handler入口日志
    #handler_name = self.__class__.__name__
    #logging.info("%s Entering..." % (handler_name))

    """
    TODO
    检查request请求合法性(数据过滤,安全检查)
    """

    #self.session = Session(self, self.application.settings['cookie_secret'],self.application.settings['session_timeout'])

    #logging.debug("BaseHandler session=%s" % self.session)

  @property
  def db(self):
    return db_interface

  @property
  def cache(self):
    return self.application.cache

def access_log(method):
  """
  access_log
  """
  @functools.wraps(method)
  def wrapper(self, *args, **kwargs):
    handler_name = self.__class__.__name__

    logging.info("%s Entering..." % (handler_name))
    
    logging.info("%s Leaving..." % (handler_name))
    
    return method(self, *args, **kwargs)

  return wrapper

class RestHandler(BaseHandler):

  """
  继承自 BaseHandler的类, 用于面向rest接口的handler
  """

  def __init__(self, *argc, **argkw):
    """
    初始化 RestHandler类,实例化session
    """
    
    super(RestHandler, self).__init__(*argc, **argkw)
    """
    TODO
    检查request请求合法性(数据过滤,安全检查)
    """
    #self.session = Session(self, self.application.settings['cookie_secret'],self.application.settings['rest_session_timeout'])
    #logging.debug("RestHandler session=%s" % self.session)