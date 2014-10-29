#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright © 2014 
# All rights reserved.
#
# Filename: settings.py
# -----------------------------------------------------------------
# 2014-10-12  created

'''
  Database backends
'''
from db_backend import DbBackend
import config

#数据库配置
DATABASE_SETTINGS = {
  #"engine": "backends.mongodb", # name of monogdb moduel
  "host": config.MONGODB_HOST,             # Set host address
  "port": config.MONGODB_PORT,                   # Set port
  "db_file":config.MONGODB_NAME,    # Set database file
  "max_pool_size":config.MONGODB_MAX_POOL_SIZE,
}

db_backend = DbBackend(DATABASE_SETTINGS)
