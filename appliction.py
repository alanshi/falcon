#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Filename: application.py
# -----------------------------------------------------------------
# 2014-10-01  created

import sys
import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.log
from tornado.options import define, options
from tornado.log import logging

import config
import routing
#############################################################
#  command line options

define("port", default = 8000, help = "run on the given port", type = int)  # port number
define("ip_address", default = "", help = "run on the given ip_address", type = str)  # port number
define("debug_template", default = 0, help="display template input data", type=int) # template debug option

class Application(tornado.web.Application):

  def __init__(self):

    settings = dict(
 
      template_path = os.path.join(os.path.dirname(__file__), config.TEMPLATE_PATH),
      static_path = os.path.join(os.path.dirname(__file__), config.STATIC_PATH),
      static_urls = {'js': config.JS_URL,
                     'css': config.CSS_URL,
                     'img': config.IMG_URL},

      site_path = config.SITE_PATH,
      xsrf_cookies = True,
      cookie_secret = config.SECRET_KEY,
      session_timeout = config.SESSION_TIMEOUT,
      rest_session_timeout = config.REST_SESSION_TIMEOUT,
      login_url = config.LOGIN_URL,
      autoescape = None,
      debug = True,

    )

    super(Application,self).__init__(routing.routings,**settings)

def main():

  tornado.options.log_file_prefix = config.LOG_FILE   # set log file
  tornado.options.options.logging = "debug"   # set log level
  tornado.options.parse_command_line()

  try:
    #start server
    application = Application()

    application.settings['DEBUG_TEMPLATE'] = tornado.options.options.debug_template
    logging.info("Start %s HTTP server on port:%d ...\n\n" % (config.PROJECT_NAME,options.port))
    http_server = tornado.httpserver.HTTPServer(application,xheaders=True)
    http_server.listen(port=options.port,address=options.ip_address)
    tornado.ioloop.IOLoop.instance().start()

  except Exception as e:
    #start server fail
    logging.critical('Failed to start HTTP server, due to : %s' % (e))
    logging.info("HTTP server is terminated.")

if __name__ == "__main__":
  main()

