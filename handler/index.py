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
    self.write('IndexHandler at %s'  % (datetime.datetime.now()))
    logging.info('%s Leaving...' % (self.__class__.__name__))
    return