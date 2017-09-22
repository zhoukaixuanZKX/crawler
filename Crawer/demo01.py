
#将一条新闻内容存到数据库
import requests
import json
import re
from bs4 import BeautifulSoup
from Crawer.ConnectsMySQL import MySQLToolDemo


#获取评论的函数
def getCommentCounts(newsurl):
    #新浪新闻里面的评论连接
    commentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'

    m = re.search('doc-i(.*).shtml', newsurl)
    newsid = m.group(1)
    comments = requests.get(commentURL.format(newsid)) #将newsid补到commentURL里面
    jd = json.loads(comments.text.strip('var data='))
    return jd['result']['count']['total']


#内文信息抽取函式
def getNewsDetail(newsurl):
    tag = MySQLToolDemo.select()
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    result['title'] = soup.select(tag['title'])[0].text
    try:
        result['newssource'] = soup.select(tag['newssource'])[0].text
    except:
        result['newssource'] = soup.select('.time-source span')[0].text
    #timesource = soup.select(".time-source")[0].contents[0].strip()
    result['time'] = soup.select(tag['time'])[0].contents[0].strip()
    result['article'] = ' '.join([p.text.strip() for p in soup.select(tag['article'])[:-1]])
    result['editor'] = soup.select(tag['editor'])[0].text.lstrip('责任编辑：')
    result['comments'] = getCommentCounts(newsurl)
    return result


#建立剖析清单链接函数   得到一个分页下面22条新闻的内文
def parseListLinks(url):
    res = requests.get(url)
    jd = json.loads(res.text.lstrip('  newsloadercallback(').rstrip(');'))

    count = [0,0,0] #计算总数 0：总数 1:成功数量 2：失败数量
    for x in jd['result']['data']:     #x['url']是一个新闻的链接
        count[0] += 1
        print(x['url'])               #从字典中得到一个新闻的url
        count[1] += MySQLToolDemo.insert(getNewsDetail(x['url']))  #也得到一条新闻的内容
        count[2] = count[0]-count[1]
    return count

#批次抓取新  得到几个分页下面新闻内文
def batch(url):
    count = [0,0,0]
    for i in range(1, 50):
        pageurl = url.format(i)
        outputresult = parseListLinks(pageurl)
        for x in range(0,3):
            count[x] += outputresult[x]
    print('总共抓取：{}  成功:{}  失败：{}'.format(count[0],count[1],count[2]))

if __name__ == '__main__':

    news = 'http://news.sina.com.cn/c/nd/2017-09-20/doc-ifymenmt5619682.shtml'  #一条新闻的链接
    content = getNewsDetail(news)  #一条新闻链接的内文信息

    #MySQLTool.CreatTable()        #建表
    MySQLToolDemo.insert(content)      #将一条新闻链接的内文信息插入到数据库

    #一个分页链接，里面包括22条新闻
    #url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page=2&callback=newsloadercallback&_=1505372975114'
    #print(parseListLinks(url))    #返回结果是一个 [{第一条新闻内文},{第二条新闻内文},{第三条新闻内文},{}...]
    #将一批分页信息里面的的新闻内容存到数据库里面

    #批次存储多个页面
    #url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&callback=newsloadercallback'
    #batch(url)