# -*- coding: utf-8 -*-
from scrapy import Item, Field

class SkroutzItem(Item):
    product_name = Field()
    image_urls = Field()
    images = Field()