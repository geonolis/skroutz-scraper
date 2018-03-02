# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from skroutz.items import SkroutzItem


class Categories(CrawlSpider):
    name = "categories"
    allowed_domains = ["www.skroutz.gr", "skroutz.gr"]
    start_urls = [
        'https://www.skroutz.gr'
    ]
    
    rules = [
        Rule(LinkExtractor(
            allow=[r'.*c/\d{1,4}/((?!/).)*\.html$']),
            callback='parse_item',
            follow=True)
    ]

    def parse_item(self, response):
        # Continue only if it's not a general category
        try:
            response.xpath('//div/section/h1/span/text()').extract()[0]
        except IndexError:
            return
        print(response.url)

        with open('skroutz/categories.txt', 'a+') as file:
            file.write(response.url + '\n')
            