# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field() #国家或地区名
    date = scrapy.Field() #⽇期
    # totCase
    totCase = scrapy.Field() #累计确诊病例
    # caseRate
    #caseRate = scrapy.Field() #确诊病例占总⼈⼝⽐
    # vaccineRate
    #vaccineRate = scrapy.Field() #接种⾄少⼀针疫苗⼈数占总⼈⼝⽐
    # fatalityRate
    #fatalityRate = scrapy.Field() #死亡率
    pass