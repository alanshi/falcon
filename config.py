#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Filename: config.py
# -----------------------------------------------------------------
# 2014-10-01  created
import os.path
import base64

#-- application config --
PROJECT_NAME = 'falcon'
SECRET_KEY = 'NjNkM2RhZDVkODE1Njk1N2NiMmZhNDBhMzMzZWRlZjZmZjYyMjc2ODFkM2JjMzllZWVmN2ZiMDIyMjZiNzcyMA=='
SITE_COOKIE = 'ZWRkNzNkZTQzYzQ4YzYwZDE1OGQ1YWZmNWRlNmJjYmRkODU3NmRkNGI3ZDQ3NWZhZTZiODkxZWRhNWIzMzg5NA=='
SITE_PORT = 8000
SITE_IPADDRESS = "127.0.0.1"
SITE_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.join(SITE_PATH, 'static')
TEMPLATE_PATH = os.path.join(SITE_PATH, 'template')
UPLOAD_ROOT_PATH = os.path.join(STATIC_PATH, 'upload')
LOGIN_URL = '/login'
DEBUG_MODE = True


#-- session timeout --
SESSION_TIMEOUT = 3600*4
REST_SESSION_TIMEOUT = 3600*24*30

#-- logging config --

LOG_PATH = os.path.join(SITE_PATH, 'log')
LOG_FILE = os.path.join(LOG_PATH, '%s.log' % (PROJECT_NAME))
LOG_LEVEL = "debug"

#-- mysql db config --
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = ''
MYSQL_PASSWD = ''
MYSQL_NAME = ''

#-- mongodb config --
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGODB_NAME = PROJECT_NAME
MONGODB_MAX_POOL_SIZE = 10


#-- redis config --
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0

# sub-urls
JS_URL = u"/js"
CSS_URL = u"/css"
IMG_URL = u"/img"

#secret config
HTTP_ONLY = True
XSRF_COOKIES = False
AUTOESCAPE = None


DEFAULT_PAGE_SIZE = 50
