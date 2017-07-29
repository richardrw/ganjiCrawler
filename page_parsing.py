#!usr/bin/python
#coding=utf-8

# import pymongo
# import requests
# import random
# from bs4 import BeautifulSoup

# #Spider2：获取赶集网上北京二手市场所有类目下的商品链接

# headers = {
# 	'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
# 	'Connection':'keep-alive'
# }
# #http://cn-proxy.com/
# proxy_list = [
#     '211.143.155.173:80',
#     '117.143.109.35:8080',
#     '111.62.251.24:80',
#     '117.143.109.35:8081'
#     ]
# proxy_ip = random.choice(proxy_list)
# proxies = {'http':proxy_ip}

# client = pymongo.MongoClient('localhost', 27017)
# ganji = client['ganji']
# cate_link = ganji['cate_link']
# page_link = ganji['page_link']

# #从cate_link中读取每个类目的链接
# def get_link_from():
# 	for i in cate_link.find():
# 		yield i['cate_link']

# def get_page_from(url):
# 	html = requests.get(url, headers=headers, proxies=proxies)
# 	print html.status_code
# 	bsObj = BeautifulSoup(html.content, 'html.parser')
# 	html_info = bsObj.select('div.noinfotishi')
# 	if len(html_info) == 0:
# 		pageList = bsObj.select('table.tbimg tr.zzinfo > td.t > a')
# 		print '%s  ---------已找到商品信息' %str(url)
# 		try:
# 			for i in pageList:
# 				title = i.get_text()
# 				link = i.get('href')
# 				page_link.insert_one({'page_title':title, 'page_link':link})
# 				print title,link
# 		        print '%s ----------------插入成功' %str(url)
# 		except:
# 			pass
# 	else:
# 		print 'sorry'
# 		print "%s  ---------------------没有找到相关商品" %str(url)

# def get_all_page_from(url,endNum):
# 	for i in range(1, endNum+1):
# 		if i == 1:
# 			page_url = url
# 		else:
# 			page_url = url + 'o{}/'.format(i)
# 		print page_url
# 		get_page_from(page_url)

# urlList = get_link_from()
# for url in urlList:
# 	get_all_page_from(url, 100)

import requests
import random
import get_ipproxy
from bs4 import BeautifulSoup
from db_execute import DbExecute

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
	}

proxyList = get_ipproxy(127.0.0.1:8000)
proxies = {'http':random.choice(proxyList)}

#爬取某类下某一页的商品链接
def getItemLinkFrom(url, num):
	url = '%s/O%s/' %(url, num)
	pageHtml = requests.get('url', headers=headers, proxie=proxies)
	pageBsObj = BeautifulSoup(pageHtml.content, 'lxml')
	hasItem = pageBsObj.select('div noinfotishi')
	if len(hasItem) == 0:
		print '%s ----------------------------没有找到相关商品。' %str(url)
	else:
		itemLinkList = pageBsObj.select('table.tbimg tr zzinfo > td.t > a')
		itemTitleList = [item.get_text() for item in itemTitleList]
		itemLinkList = [item.get('href') fro item in itemLinkList]
		itemList = []
		for itemTitle, itemLink in zip(itemTitleList, itemLinkList):
			itemMsg = {'itemTitle':itemTitle, 'itemLink':itemLink}
			#print itemMsg
			itemList.append(itemMsg)
		yield itemList
	insertItem = DbExecute()
	insertItem.insertItem(itemList)
	

#爬取某类下所有商品链接
def getAllItemLinkFrom(url, num):
	for pageNum in xrange(2, num+1):
		getItemLinkFrom(url, pageNum)




