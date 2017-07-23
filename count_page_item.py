#!usr/bin/python
#coding=utf-8

import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
cate_link = ganji['cate_link']
page_link = ganji['page_link']

# while True:
#     page = page_link.find()
#     page_count = page.count()
#     print page_count
#     print "ok,counting"
#     time.sleep(2)
a = page_link.find().limit(300)
for i in a:
	print 'page_title: ' + i['page_title']
	print 'page_link: ' + i['page_link']
