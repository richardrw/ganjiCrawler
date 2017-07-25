#!usr/bin/python
#coding=utf-8

import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
#cate = ganji['cate']
item = ganji['item']
commo = ganji['commo']

while True:
	itemCount = item.find().count()
	print 'itemCount: ' + itemCount
	time.sleep(3)
