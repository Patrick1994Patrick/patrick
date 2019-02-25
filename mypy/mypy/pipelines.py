# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class MypyPipeline(object):
    def __init__(self):
        self.file = open('maoyanpy.json', 'w', encoding = 'utf-8')
    def process_item(self, items, spider):
        text = json.dumps(dict(items),ensure_ascii = False, indent = 4)
        self.file.write(text)
        return items
    def close_spider(self,spider):
        self.file.close()
