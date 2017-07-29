#！usr/bin/python
#coding=utf-8

import pymongo

class DbExecute(object):
	def __init__(self):
		client = pymongo.MongoClient('localhost', 27017)
		ganji = client['ganji']
		#cate = ganji['cate']
		item = ganji['item']
		commo = ganji['commo']

	# def insertCate(self, cateList=None):
	# 	if cateList:
	# 		for cate in cateList:
	# 			self.cate.insert(cate)

	def insertItem(self, itemList=None):
		if itemList:
			for item in valueList:
				self.item.insert(item)

	def insertCommo(self, commoList=None):
		if commoList:
			for commo in commoList:
				self.commo.insert(commo)

	def select(self, table=None, count=None):
		if table:
			# for msg in self.table.find().limmit(count):
			# 	print msg
			yield self.table.find().limmit(count)


