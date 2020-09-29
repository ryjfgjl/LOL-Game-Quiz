# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Rank2019Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    teamName = scrapy.Field()
    rank = scrapy.Field()
    region = scrapy.Field()