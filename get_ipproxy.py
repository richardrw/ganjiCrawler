#!usr/bin/python
#coding=utf-8

import requests
import json

def getProxyFrom(url):
	ProxyHtml = requests.get(url)
	proxyJson = json.loads(ProxyHtml.text)
	proxyList = []
	for proxy in proxyJson:
		ip = proxy[0][0]
		port = proxy[0][1]
		proxyList.append('%s:%s') %(ip, port)
	return proxyList

if __name__ == '__main__':
	getProxyFrom(url)
