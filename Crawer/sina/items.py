# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class NewItem(Item):
    title = Field()
    contents = Field()
    editor = Field()
    source = Field()
    time = Field()
    comment = Field()

