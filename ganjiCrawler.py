#!usr/bin/python
#coding=utf-8

from cate_parsing import getCateFrom
from page_parsing import getAllItemLinkFrom

cateList = getCateFrom(url)
for cateUrl in cateList:
	getAllItemLinkFrom(cateUrl, 100)