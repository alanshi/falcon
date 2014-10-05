#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Filename: index.py
# -----------------------------------------------------------------
# 2014-10-05  created

import datetime

from tornado.log import logging

from base import *


class IndexHandler(BaseHandler):

  def get(self):

    logging.info('IndexHandler Entering')
    self.write('IndexHandler at %s'  % (datetime.datetime.now()))
    logging.info('IndexHandler Leaving')