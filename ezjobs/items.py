# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class JobsItem(Item):
    company = Field() 
    title = Field() 
    link = Field() 
    region = Field()
    tags = Field()
    date = Field()
    crawled = Field()

class RemotiveItem(Item):
    company = Field() 
    title = Field() 
    link = Field() 
    region = Field()
    tags = Field()
    date = Field()
    crawled = Field()

