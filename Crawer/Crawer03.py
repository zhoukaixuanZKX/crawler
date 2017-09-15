#剖析分页信息
import requests
import json
import re
import pandas
from bs4 import BeautifulSoup
from datetime import datetime
res = requests.get('http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page=2&callback=newsloadercallback&_=1505372975114')
jd = json.loads(res.text.lstrip('  newsloadercallback(').rstrip(');'))

#新闻资料是放在 result下面的 data 的list之中
for ent in jd['result']['data']:
    ent['url']

commentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
def getCommentCounts(newsurl):
    m = re.search('doc-i(.*).shtml', newsurl)
    newsid = m.group(1)
    comments = requests.get(commentURL.format(newsid))
    jd = json.loads(comments.text.strip('var data='))
    return jd['result']['count']['total']

#内文信息抽取函式
def getNewsDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    result['title'] = soup.select("#artibodyTitle")[0].text
    result['newssource'] = soup.select('.time-source span a')[0].text
    timesource = soup.select(".time-source")[0].contents[0].strip()
    result['dt'] = datetime.strptime(timesource,'%Y年%m月%d日%H:%M')
    result['article'] = ' '.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
    result['editor'] = soup.select('.article-editor')[0].text.lstrip('责任编辑：')
    result['comments'] = getCommentCounts(newsurl)
    return result

#建立剖析清单链接函数
def parseListLinks(url):
    newsdetails = []
    res = requests.get(url)
    jd = json.loads(res.text.lstrip('  newsloadercallback(').rstrip(');'))
    for ent in jd['result']['data']:
        newsdetails.append(getNewsDetail(ent['url']))
    return newsdetails

#测试
url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page=2&callback=newsloadercallback&_=1505372975114'
#print(parseListLinks(url))

#使用for循环产生多页链接
url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&callback=newsloadercallback&_=1505372975114'
for i in range(1,10):
    url.format(i)

#批次抓取每链页里面新闻接的内文
url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&callback=newsloadercallback&_=1505372975114'
news_total = []
for i in range(1, 3):
    newsurl = url.format(i)
    newsary = parseListLinks(newsurl)
    news_total.extend(newsary)
#print(len(news_total))
#print(news_total)

#将对象保存至excel
df = pandas.DataFrame(news_total)
print(df.head())
df.to_excel('news.xlsx')