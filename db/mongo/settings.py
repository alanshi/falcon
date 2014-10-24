#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright © 2014 Chengdu WeShare Technology
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
  "host": "localhost",             # Set host address
  "port": 27017,                   # Set port
  "db_file":config.PROJECT_NAME,    # Set database file
  "max_pool_size":10,
}

db_backend = DbBackend(DATABASE_SETTINGS)
