# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LolgameItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    date = scrapy.Field()
    teamA = scrapy.Field()
    teamB = scrapy.Field()
    scoreA = scrapy.Field()
    scoreB = scrapy.Field()
    fullTeamA = scrapy.Field()
    fullTeamB = scrapy.Field()
    dayNum = scrapy.Field()
    dayOrder = scrapy.Field()
    processor = scrapy.Field()
