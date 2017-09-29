# -*- coding: utf-8 -*-
import json

import requests
from scrapy import Spider, Request
import re
from bs4 import BeautifulSoup
from sina.items import NewItem


class SinaNewsSpider(Spider):
    name = "sina_news"
    allowed_domains = ["sina.com"]
    start_urls = ['http://news.sina.com.cn/']

    # def start_requests(self):
    #     url = 'http://mil.news.sina.com.cn/jssd/2017-09-28/doc-ifymfcih7268249.shtml'
    #     # url = 'http://mil.news.sina.com.cn/china/2017-09-28/doc-ifymkwwk6705200.shtml'
    #     yield Request(url=url, callback=self.parse_othernews)

    def parse(self, response):

        res = response.xpath('//div[@class="ct_t_01"]/h1/a/@href').extract()
        for re in res:
            yield Request(url=re, callback=self.parse_new, dont_filter=True)
        res = response.xpath('//div[@id="syncad_1"]/p/a/@href').extract()
        for re in res:
            yield Request(url=re, callback=self.parse_new, dont_filter=True)

        res = response.xpath('//*[@id="ad_entry_b2"]/ul/li/a/@href').extract()
        for re in res:
            yield Request(url=re, callback=self.parse_new, dont_filter=True)

        res = response.xpath('//*[@id="blk_08_cont01"]/ul/li/a/@href').extract()
        for re in res:
            yield Request(url=re, callback=self.parse_new, dont_filter=True)

    def parse_new(self, response):
        item = NewItem()        # 定义储存item
        title = response.css('#artibodyTitle::text').extract_first()    # 标题
        if title == None:
            yield Request(response.url, callback=self.parse_othernews, dont_filter=True)
        else:
            # 正文
            texts = []
            text = ''
            for p in response.css('#artibody p::text').extract()[:-1]:
                texts.append(p.strip())
                text = ''.join(texts)

            # 新闻源
            try:
                source = response.css('.time-source span a::text').extract_first()
            except:
                print('Source ERROR,Source parser changed')
                source = response.css('.time-source span:text').extract_first()

            # 编辑人
            editor = response.css('.article-editor::text').extract_first().lstrip('责任编辑： ').strip()
            # 时间
            time = response.css('.time-source::text').extract_first().strip()

            # 评论url
            # 用正则表达式从正文连接中得到信息，m.group取出id
            m = re.search('doc-i(.*).shtml', response.url)
            id = m.group(1)
            commenturl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
            item['title'] = title
            item['contents'] = text
            item['source'] = source
            item['editor'] = editor
            item['time'] = time[0:11]
            # 评论
            yield Request(url=commenturl.format(id), meta={'key': item}, callback=self.parse_comment, dont_filter=True)

    def parse_comment(self, response):
        item = response.meta['key']
        # 得到内容为取出多余字符，带入到js中。
        jd = json.loads(response.text.strip('var data='))
        try:
            res = jd['result']['count']['total']
        except:
            res = None
        yield item

    def parse_othernews(self, response):
        item = NewItem()
        # 标题
        item['title'] = response.xpath('//*[@id="main_title"]/text()').extract_first()
        # 正文
        texts = []
        text = ''

        for p in response.xpath('//div[@id="artibody"]/p/text()').extract():
            texts.append(p.strip())
            text = ''.join(texts)
        item['contents'] = text

        # 新闻源
        source = response.xpath('//*[@id="page-tools"]/span/span[2]/text()').extract_first()
        if source == None:
            item['source'] = response.xpath('//div[@id="page-tools"]/span/span[2]/a/text()').extract_first()
        else:
            item['source'] = source

        # 时间
        time = response.xpath('//*[@id="page-tools"]/span/span[1]/text()').extract_first()
        item['time'] = time[0:11]
        # 评论
        m = re.search('doc-i(.*).shtml', response.url)
        id = m.group(1)
        commenturl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=jc&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
        yield Request(url=commenturl.format(id), meta={'key': item}, callback=self.parse_comment, dont_filter=True)
