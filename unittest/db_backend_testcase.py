#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright © 2014 Chengdu WeShare Technology
# All rights reserved.
#
# Filename: db_backend_testcase.py
# -----------------------------------------------------------------
# 2014-10-11 created
import sys
sys.path.append('..')

from tornado.test.util import unittest
from db.mongo.settings import db_backend


class TestDbBackend(unittest.TestCase): 

  data = {}
  @classmethod
  def setUpClass(cls):  
  
    print '-------------- %s ----------------------' % (cls)

  def testcase_insert(self):
    return self.assertEqual(self.data, db_backend.insert("db_backend_collect", self.data)) 

def suite():

  tests  = [
      'testcase_insert',
      ]
  return unittest.TestSuite(map(TestDbBackend, tests))

if __name__ == '__main__':

  TestDbBackend.setUpClass()
  unittest.TextTestRunner(verbosity=2).run(suite())