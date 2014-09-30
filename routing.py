#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Filename: routing.py
# -----------------------------------------------------------------
# 2014-10-01  created

import tornado.web
import config

routings = [

  (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": config.STATIC_PATH}),
  (r"/upload/(.*)", tornado.web.StaticFileHandler, {"path": config.UPLOAD_ROOT_PATH}),


]