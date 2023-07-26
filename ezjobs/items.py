# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class Jobs(Item):
    company = Field() 
    title = Field() 
    location = Field() 
    link = Field() 
    date = Field()

class Remotive(Item):
    company = Field() 
    title = Field() 
    link = Field() 
    date = Field()

