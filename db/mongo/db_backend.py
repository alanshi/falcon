#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright © 2014 Chengdu WeShare Technology
# All rights reserved.
#
# Filename: db_backend.py
# -----------------------------------------------------------------
# 2014-10-11 created


import sys

from tornado.log import logging

try:
  from pymongo import Connection
  from bson.objectid import ObjectId
  from bson.errors import *
  from pymongo import ASCENDING, DESCENDING
  from pymongo.errors import *
except ImportError:
    raise ImportError

sys.path.append("../..")
import config

class Singleton(object):
  """
  Singleton 单例模式,用于保证DbBackend类只被实例化一次
  """
  def __new__(cls, *args, **kw):   
    if not hasattr(cls, '_instance'):   
      orig = super(Singleton, cls)   
      cls._instance = orig.__new__(cls, *args, **kw)   
    return cls._instance   


def check_objectId(data):
  """
  This method verifies the key dict['_id'] is a standard ObjectId or not
  """
  logging.info("Entering check_objectId...")
  try:
    if type(data['_id']) is not ObjectId:
      data['_id'] = ObjectId(data['_id'])
    return data
  except KeyError:
    logging.error("data['_id'] doesn't exist!")
    logging.info("Leaving check_objectId...")
    return None
  except TypeError:
    logging.error("data is not a dict!")
    logging.info("Leaving check_objectId...")
    return None
  except InvalidId:
    logging.error("data['_id'] is not a valid ObjectId!")
    logging.info("Leaving check_objectId...")
    return None

'''
  数据库后端操作接口,对业务逻辑接口提供对数据库的操作支持
'''
class DbBackend(Singleton):

  _db_conn = None
  _database = None


  def __init__(self, db_parm):

    '''
      数据库连接初始化
    '''
    
    try:
      self.__class__._db_conn = Connection(db_parm['host'], db_parm['port'])      
      self.__class__._database = self.__class__._db_conn[db_parm.get("db_file", "rainbow")]
    except Exception, e:
      logging.critical('Failed to connect mongodb: %s' % (e) )
      logging.info('Leaving DbBackend....')
      return None

  @property
  def _database(self):
    return self.__class__._database

  def findone(self, collect_name, condition={}):
    """
    search in collect by a condition dict for the 1st document ONLY
      collect_name      -     collection name to be searched
      condition         -     a dict for the search condition
    returns:
      None              -     failed to enquiry
      Others            -     the documents
    """
    logging.info('Enter database findone ...')
    check_objectId(condition)
    logging.info("collect_name=%s, condition=%s" %
                  (collect_name, condition)
    )

    try:
      ret = self._database[collect_name].find_one(condition)
      logging.info("Leaving findonet...")
      return ret
    except Exception,e:
      logging.error("findone in collection '%s' error: %s" % (collect_name, e))
      logging.info("Leaving findone_collect...")
      return None

  def find_collect(self, collect_name, condition={}, skip=0, limit=config
                   .DEFAULT_PAGE_SIZE, fields=None):
    """
    search in collect by a condition dict
      collect_name      -     collection name to be searched
      condition         -     a dict for the search condition
      skip             -      skips the top [skip] elements for pagination
      limit            -      number of documents to be returned
                              zero for unlimited
    returns:
      None              -     failed to enquiry
      Others            -     the documents list
    """
    logging.info('Enter database find ...')
    check_objectId(condition)
    logging.info("collect_name=%s, condition=%s, skip=%s, limit=%s" %
                  (collect_name, condition, skip, limit)
    )

    try:
      if  limit < 0:
        logging.error("limit=%d is not acceptable!" % limit)
        return None
      else:

        ret = self._database[collect_name].find(condition, fields=fields)

        # sort dataset
        if type(sort) is list:
          ret.sort(sort)

        if skip:
          ret.skip(int(skip))

        if limit != 0:
          logging.info("Leaving find_collect")
          return list(ret.limit(int(limit)))
        else:
          logging.info("Leaving find_collect")
          return list(ret)
    except Exception,e:
      logging.error("findone in collection '%s' error: %s" % (collect_name, e))
      logging.info("Leaving findone_collect...")
      return None


  def update(self, collect_name, condition, data):
    '''
      update collect data:
        collect_name      -     collection name to be updated
        condition         -     a dict for the search condition
        data              -     a dict for data to be updated
      returns:
        None              -     Nothing being updated
        Other             -     The updated object_id
    '''
    logging.info('Enter database update ...')
    check_objectId(condition)
    check_objectId(data)
    
    try:
      logging.debug("condition=%s, data=%s" % (condition,data))
      ret = self._database[collect_name].find_and_modify(query=condition, update=data, new=True)
      logging.info("Leaving update...")
      return result
    except Exception, e:
      logging.error("update collection '%s' error: %s" % (collect_name, e))
      logging.info("Leaving update_collect...")
      return None

  def delete_collect(self, collect_name, condition={}):
    """
      delete collect by the specified condition
        collect_name    -   collection name
        condition       -   a dict for the search condition

      returns:
        None            -   failed to delete
        True            -   success
    """
    logging.info('enter database delete....')
    check_objectId(condition)
    logging.debug("collect_name=%s, condition=%s" %
                  (collect_name, condition))

    try:
      collect = self.findone_collect(collect_name,condition)
      if collect is not None:
        result = self._database[collect_name].remove(condition)   
        logging.info('leaving delete_collect....')
        return True
      return None
    except Exception,e:
      logging.error("delete collection '%s', error:%s" % (collect_name, e))
      logging.info('Leaving delete_collect....')
      return None

  def insert(self, collect_name, data):
    """
    insert
      collect_name      -   collection name
      data              -   document to be inserted
    returns:
      None              -   failed to insert docment
      Other             -   the object_id in string
    """
    logging.info("Enter database insert....")
    logging.debug("collect_name=%s, data=%s" % (collect_name, data))

    try:
      _id = self._database[collect_name].insert(data)
      logging.info('Leaving insert...')
      return str(_id)
    except Exception, e:
      logging.error('insert into collect %s, error:%s' % (collect_name, e))
      logging.info('Leaving insert_collect....')
      return None
      