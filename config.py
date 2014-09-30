#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Filename: config.py
# -----------------------------------------------------------------
# 2014-10-01  created
import os.path
import base64

#-- application config --
PROJECT_NAME = 'falco'
SECRET_KEY = 'NjNkM2RhZDVkODE1Njk1N2NiMmZhNDBhMzMzZWRlZjZmZjYyMjc2ODFkM2JjMzllZWVmN2ZiMDIyMjZiNzcyMA=='
SITE_COOKIE = 'ZWRkNzNkZTQzYzQ4YzYwZDE1OGQ1YWZmNWRlNmJjYmRkODU3NmRkNGI3ZDQ3NWZhZTZiODkxZWRhNWIzMzg5NA=='
SITE_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.join(SITE_PATH, 'static')
UPLOAD_ROOT_PATH = os.path.join(SITE_PATH, 'static/upload')
TEMPLATE_PATH = os.path.join(SITE_PATH, 'template')
LOGIN_URL = '/login'

#-- session timeout --
SESSION_TIMEOUT = 3600*4
REST_SESSION_TIMEOUT = 3600*24*30

# default log filename
LOG_PATH = os.path.join(SITE_PATH, 'log')
LOG_FILE = os.path.join(LOG_PATH, '%s.log' % (PROJECT_NAME))


#-- mysql db config --
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = ''
MYSQL_PASSWD = ''
MYSQL_NAME = ''

#-- mongodb config --
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MDB_NAME = 'test'

# sub-urls
JS_URL = u"/js"
CSS_URL = u"/css"
IMG_URL = u"/img"