#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Filename: database.py
# -----------------------------------------------------------------
# 2014-10-30  created

import sys

import redis

from tornado.log import logging
sys.path.append("../..")
import config

### Connct to Redis ###
redis_conn = None
try:
  redis_conn = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DB)
  logging.info("Redis Connected successfully")
except Exception, e:
  logging.error("Could not connect to Redis:%s\n" % e)