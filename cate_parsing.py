!usr/bin/python
coding=utf-8

# import pymongo
# import requests
# from bs4 import BeautifulSoup

# #spider1: 获取赶集网上北京二手所有类目的链接

# headers = {
# 	'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
# }

# client = pymongo.MongoClient('localhost', 27017)
# ganji = client['ganji']
# cate_link = ganji['cate_link']
# page_link = ganji['pape_link']
# item_info = ganji['item_info']

# def get_cateLink_from(url):
# 	homeUrl = 'http://bj.ganji.com'
# 	html = requests.get(url,headers=headers)
# 	bsObj = BeautifulSoup(html.content, 'html.parser')
# 	cateList = bsObj.select('dl.fenlei dt a')
# 	cateTitle = [i.get_text() for i in cateList]
# 	cateLink = [homeUrl + i.get('href') for i in cateList]
# 	for title, link in zip(cateTitle, cateLink):
# 		cate_link.insert_one({'cate_title':title, 'cate_link':link})

# url = 'http://bj.ganji.com/wu/'
# get_cateLink_from(url)
# print 'inserted'
# print cate_link.find().count()
# print 'done'

import requests
from bs4 import BeautifulSoup

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}

#爬取赶集网-北京下所有类目链接。从实际网站观察，类目数量不足20个，所以爬取的cateList不存入数据库，直接使用。
def getCateFrom(url):
	homeUrl = 'http://bj.ganji.com'
	homeHtml = requests.get(url, headers=headers)
	homeBsObj = homeHtml(html.content, 'lxml')
	cateFindRs = homeBsObj.select('dl.fenlei dt a')
	cateTitleList = [cate.get_text() for cate in cateFindRs]
	cateLinkList = [homeUrl + cate.get('href') for cate in cateFindRs]
	cateList = []
	for cateTitle, cateLink in zip(cateTitleList, cateLinkList):
		cateMsg = {'cateTitle':cateTitle, 'cateLink':cateLink}
		#print cateMsg
		cateList.append(cateMsg)
	return cateList



