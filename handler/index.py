#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Filename: index.py
# -----------------------------------------------------------------
# 2014-10-05  created

import datetime

from tornado.log import logging

import base


class IndexHandler(base.BaseHandler):

  def get(self):
    logging.info('%s Entering...' % (self.__class__.__name__))
    logging.info('write IndexHandler')
    render_str = 'IndexHandler at %s'  % (datetime.datetime.now())
    self.render('index.html',render_str=render_str)
    logging.info('%s Leaving...' % (self.__class__.__name__))
    return