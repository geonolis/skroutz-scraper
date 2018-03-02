# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from skroutz.items import SkroutzItem


class Pic(CrawlSpider):

    name = "pic"
    allowed_domains = ["www.skroutz.gr", "skroutz.gr"]
    start_urls = [
        # More start_urls can be added (more product categories)
        'https://www.skroutz.gr/c/25/laptop.html'
    ]
    
    rules = [
        Rule(LinkExtractor(
            allow=[r'.*c/\d{1,4}/.*\.html\?page=\d+']),
            callback='parse_item',
            follow=True)
    ]

    product_count = 0
    total_to_add = 0
    total_products = 0

    # Calculates the total products in this start_url
    def calculate_temp_total(self, response):
        line = response.xpath('//div/section/h1/span/text()').extract()[0]
        self.total_to_add = int(line[1:line.find(' ')])

    def parse_item(self, response):
        # Add the total number of products in this start_url to total_products
        if 'page=1>' in str(response):
            self.calculate_temp_total(response)
            self.total_products += self.total_to_add

        selector_list = response.css("div ol[id='sku-list'] li")
        prefix = ''
        if len(selector_list) < 20:  # if there is outer <div>
            prefix = 'div/'

        for selector in selector_list:
            if len(selector.xpath('{}h2/a/text()'.format(prefix)).extract()) == 0:
                continue
            link = selector.xpath('{}h2/a/@href'.format(prefix)).extract()[0]
            full_link = 'https://www.skroutz.gr' + str(link)
            request = Request(full_link, callback=self.parse_product)
            item = SkroutzItem()
            request.meta['item'] = item
            yield request

    def parse_product(self, response):
        self.product_count += 1
        # Print which product the spider is currently processing
        print('\r## Product : {} of ~{}'.format(str(self.product_count), self.total_products)),
        item = response.meta['item']
        item['product_name'] = response.xpath('//div/div/h1/text()').extract()[0].strip()
        # Locate the image links and store them in the image_urls Field
        main_image = 'https:' + response.xpath('//*[@id="sku-info"]/div[2]/div/a[4]/@href').extract()[0]
        other_images = response.xpath('//*[@id="sku-info"]/div[2]/div/ul/li/a/@href').extract()[:-6]
        other_images = ['https:' + x for x in other_images]
        other_images.insert(0, main_image)
        item['image_urls'] = other_images
        return item
        