from itemadapter import ItemAdapter
import json

class MyPipeline:
    def open_spider(self, spider):
        try:
            self.file = open('totCase.json', 'w', encoding='utf-8')
            #self.file = open('caseRate.json', 'w', encoding='utf-8')
            #self.file = open('vaccineRate.json', 'w', encoding='utf-8')
            #self.file = open('fatalityRate.json', 'w', encoding='utf-8')
            self.file.write('[')
        except Exception as err:
            print(err)

    def process_item(self, item, spider):
        dict_item = dict(item) #⽣成字典对象
        json_str = json.dumps(dict_item, ensure_ascii=False) + ",\n" #⽣成json串
        self.file.write(json_str) #将json串写⼊到⽂件中
        return item

    def close_spider(self, spider):
        self.file.write(']')
        self.file.close() #关闭⽂件