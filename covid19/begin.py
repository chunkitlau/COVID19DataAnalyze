from scrapy import cmdline
cmdline.execute("scrapy crawl covid19".split())
# covid19 为爬虫的名字，在 spider.py 中定义