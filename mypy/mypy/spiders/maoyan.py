# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MaoyanSpider(CrawlSpider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films']

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths = ('//div[@class="movie-item"]/a[@href]')), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//li[@class="active"]')), follow=True),
    )

    def parse_item(self, response):
        items = {}
        items['name'] = response.xpath('//h3[@class="name"]/text()').extract_first()
        items['tem'] = response.xpath('//li[@class="ellipsis"]/text()').extract_first()
        items['description'] = response.xpath('//span[@class="dra"]/text()').extract_first()
        print(items)
        yield items
