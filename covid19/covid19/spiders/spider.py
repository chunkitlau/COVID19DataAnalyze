import scrapy
import re
from covid19.items import MyItem # 从 items.py 中引入 MyItem 对象

class mySpider(scrapy.spiders.Spider):
    name = "covid19" # 爬虫的名字是 covid19
    allow_domains = ['https://ourworldindata.org/explorers/'] # 允许爬取的网站域名
    # totCase
    start_urls = ['https://ourworldindata.org/explorers/'\
       'coronavirus-data-explorer?tab=table&zoomToSelection=true&time=2021-12-' + str(date).zfill(2) +
       '&facet=none&pickerSort=desc&pickerMetric=total_vaccinations_per_hundred&'\
       'Metric=Confirmed+cases&Interval=Cumulative&Relative+to+Population=false&'\
       'Color+by+test+positivity=false' for date in range(5, 20)] #爬取5~19⽇数据
    
    # caseRate
    #start_urls = ['https://ourworldindata.org/explorers/'\
    #    'coronavirus-data-explorer?tab=table&time=2021-12-19&facet=none&'\
    #    'Metric=Confirmed+cases&Interval=Cumulative&Relative+to+Population=true&Color+by+test+positivity=false']
    
    # vaccineRate
    #start_urls = ['https://ourworldindata.org/explorers/'\
    #    'coronavirus-data-explorer?tab=table&time=2021-12-19&facet=none&'\
    #    'Metric=People+vaccinated&Interval=Cumulative&Relative+to+Population=true&Color+by+test+positivity=false']

    # fatalityRate
    #start_urls = ['https://ourworldindata.org/explorers/'\
    #    'coronavirus-data-explorer?tab=table&time=2021-12-19&facet=none&'\
    #    'uniformYAxis=0&pickerSort=asc&pickerMetric=location&Metric=Case+fatality+rate&Interval=Cumulative&Relative+to+Population=true&Color+by+test+positivity=false&country=~OWID_WRL']
    
    def parse(self, response):
        item = MyItem()
        for each in response.xpath('/html/body/main/div/div[3]/div/div[1]/div/table/tbody/tr'):
            item['country'] = each.xpath('td[1]/text()').get()
            # totCase
            
            item['totCase'] = each.xpath('td[2]/text()').get().replace(',', '') #去除逗号
            if re.search('million', item['totCase']): #将million转换为数字概念的1e6
                item['totCase'] = item['totCase'].replace(' million', '')
                item['totCase'] = int(float(item['totCase']) * 1000000)
            else:
                item['totCase'] = int(item['totCase'])
            
            # caseRate
            # item['caseRate'] = float(each.xpath('td[2]/text()').get().replace(',', '')) #去除逗号
            # vaccineRate
            #item['vaccineRate'] = each.xpath('td[2]/text()').get()
            #if item['vaccineRate'] == None: # 没有接种疫苗的国家或地区不考虑
            #    continue
            #item['vaccineRate'] = item['vaccineRate'].replace('"', '')
            # fatalityRate
            #item['fatalityRate'] = each.xpath('td[2]/text()').get()
            #if item['fatalityRate'] == None: #没有死亡率的国家认为是0%
            #    item['fatalityRate'] = '0.00%'
            
            item['date'] = re.findall(".*time=(.*?)&.*", response.url)[0] #获取爬取的⽇期
            yield item