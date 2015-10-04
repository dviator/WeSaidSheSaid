# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags


class CSPANItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field(input_processor=MapCompose(remove_tags))
    speaker = scrapy.Field(input_processor=MapCompose(remove_tags))
    url = scrapy.Field(input_processor=MapCompose(remove_tags))
    speechTime = scrapy.Field(input_processor=MapCompose(remove_tags))
    collectionTime = scrapy.Field(input_processor=MapCompose(remove_tags))
    city = scrapy.Field(input_processor=MapCompose(remove_tags))
    state = scrapy.Field(input_processor=MapCompose(remove_tags))

    
