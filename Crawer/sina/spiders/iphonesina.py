# -*- coding: utf-8 -*-
import json
import sys
from scrapy import Spider, Request
import re
from bs4 import BeautifulSoup
from sina.items import NewItem

class IphonesinaSpider(Spider):
    name = "iphonesina"
    allowed_domains = ["news.sina.cn"]
    start_urls = ['http://news.sina.cn/']

    def start_requests(self):
        urlapi = 'http://interface.sina.cn/wap_api/news_roll.d.html?col=38790&level=1%2C2&show_num=30&page={}&act=more&jsoncallback=callbackFunction&callback=jsonp{}'
        for i in range(1, 100):
            yield Request(url=urlapi.format(i, i-1), callback=self.parse)
        # url = 'https://news.sina.cn/gn/2017-09-29/detail-ifymmiwm1010607.d.html?vt=4'
        # yield Request(url, callback=self.parse_contents)

    def parse(self, response):
        re = response.text.strip('callbackFunction(')[0:-2]
        jd = json.loads(re)
        for result in jd['result']['data']['list']:
            item = NewItem()
            item['title'] = result['title']
            # print(item['title'])
            item['comment'] = result['comment']
            # print(item['comment'])
            item['source'] = result['source']
            # print(item['source'])
            # print(result['URL'])
            # item['contents'] = result['URL']
            yield Request(url=result['URL'], meta={'key': item}, callback=self.parse_contents, dont_filter=True)

    def parse_contents(self, response):
        item = response.meta['key']
        time = response.xpath('/html/body/main/section[1]/article/section[1]/figure/figcaption/time/span/text()').extract_first()
        if time == None:
            time = response.css('.art_time::text').extract_first()
            if time == None:
                time = response.xpath('/html/body/div[1]/section[3]/p/time[1]/text()').extract_first()
        # print(time)
        item['time'] = time
        # 正文
        texts = []
        text = ''
        for p in response.css('.art_box p::text').extract():
            texts.append(p.strip())
            text = ''.join(texts)
        item['contents'] = text
        if len(item['contents']) == 0:
            item['contents'] = response.url
        yield item
