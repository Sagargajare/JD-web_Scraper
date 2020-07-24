# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JustdialItem(scrapy.Item):
    name = scrapy.Field()
    contact = scrapy.Field()
    rating = scrapy.Field()
    address = scrapy.Field()
