#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright © 2014
# All rights reserved.
#
# Filename: db_api_testcase.py
# -----------------------------------------------------------------
# 2014-10-11 created
import sys
sys.path.append('..')

from tornado.test.util import unittest
from db.mongo import db_api

class TestDbApi(unittest.TestCase): 

  data = {}
  obj_id = None
  collect_name = 'user'
  @classmethod
  def setUpClass(cls):  
    
    print '-------------- %s ----------------------' % (cls)

  def testcase_add_user(self):
    self.obj_id = db_api.add_user(self.data)
    return self.assertIsNotNone(self.obj_id)


def suite():

  tests  = [
      'testcase_add_user',
      
      ]
  return unittest.TestSuite(map(TestDbApi, tests))

if __name__ == '__main__':

  TestDbApi.setUpClass()
  unittest.TextTestRunner(verbosity=2).run(suite())