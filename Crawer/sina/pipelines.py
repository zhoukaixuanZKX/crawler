# -*- coding: utf-8 -*-
from .spiders import SQL
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SinaPipeline(object):
    def process_item(self, item, spider):
        data = dict(item)
        SQL.Sql.inserdata(data)
        return item
