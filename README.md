# ganjiCrawler

这是一个爬去赶集网-北京下所有类目下所有商品信息的爬虫。

以下是爬虫构成说明：
1、cate_parsing.py用于爬取赶集网-北京下所有类目的链接。
2、page_parsing.py用于爬取某类目下某一页的商品链接。
3、item_parsing.py用于根据商品链接，爬取某商品下的详细信息。
4、count_page.py用于运行项目代码时，统计爬取的商品数。
5、db_execute.py用于存储、读取数据。
6、ganjiCrawler.py用于执行整个项目代码，爬取商品数据。