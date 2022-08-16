# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookingsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    address=scrapy.Field()
    rating=scrapy.Field()
    property_description=scrapy.Field()
    rating_count=scrapy.Field()
    breakfast_type=scrapy.Field()
    parking=scrapy.Field()
    rating_type=scrapy.Field()
    pets=scrapy.Field()
    
