#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright © 2014
# All rights reserved.
#
# Filename: db_api.py
# -----------------------------------------------------------------
# 2014-10-26 created

import db_backend


def add_user(user_doc):
  """
  add a user info collect

  inputs:

    user_doc = {
      'username':'',
      'email':'',
      'phone':'',
      'password':'',
      'avatar':'',
      'intro':''
      'user_type':''

    }

  returns:

    False             -     failure
    Others            -     user info data
  
  """
  logging.info('add_user  Entering...')

  return db_api.insert(collect_name = 'user',
                       data = user_doc
    )

  logging.info('add_user  Leaving...')

  pass
