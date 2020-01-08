# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    start_date = scrapy.Field()
    end_date = scrapy.Field()
    contact_email = scrapy.Field()
  
	
class DocumentItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    description = scrapy.Field()
    datePublished = scrapy.Field()
    title = scrapy.Field()  