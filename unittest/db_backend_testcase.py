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
  collect_name = 'db_backend_collect'
  obj_id = None
  @classmethod
  def setUpClass(cls):  
    
    print '-------------- %s ----------------------' % (cls)

  def testcase_insert(self):
    self.obj_id = db_backend.insert(self.collect_name, self.data)

    return self.assertIsNotNone(self.obj_id)

  def testcase_update(self):

    print db_backend.update(self.collect_name,{'_id':self.obj_id},{'$set':{'':'11'}})


def suite():

  tests  = [
      'testcase_insert',
      'testcase_update'
      ]
  return unittest.TestSuite(map(TestDbBackend, tests))

if __name__ == '__main__':

  TestDbBackend.setUpClass()
  unittest.TextTestRunner(verbosity=2).run(suite())