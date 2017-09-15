import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime
import pandas


def getCommentCount(newsurl):
    # 评论链接
    commenturl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
    # 用正则表达式从正文连接中得到信息，m.group取出id
    m = re.search('doc-i(.*).shtml', newsurl)
    newid = m.group(1)
    # commentual.format(newid)把newid添加到评论链接中，通过get函数得到回应
    comments = requests.get(commenturl.format(newid))
    # 得到内容为取出多余字符，带入到js中。
    jd = json.loads(comments.text.strip('var date='))
    return jd['result']['count']['total']

def getNewDetial(newsurl):

    result = {}     # 定义字典，用于传出数据
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    result['title'] = soup.select('#artibodyTitle')[0].text         # 标题
    timetemp = soup.select('.time-source')[0].contents[0].strip()
    result['time'] = datetime.strptime(timetemp, '%Y年%m月%d日%H:%M')  # 时间
    result['newssource'] = soup.select('.time-source span a')[0].text   # 新闻源
    # 正文
    texts = []
    text = ''
    for p in soup.select('#artibody p')[:-1]:
        texts.append(p.text.split()[0])
        ' '.join(texts)
        # print(len(texts))
    result['content'] = texts
    # 编辑人
    result['newsman'] = soup.select('.article-editor')[0].text.lstrip('责任编辑： ').strip()
    # 评论
    result['comment'] = getCommentCount(newsurl)
    return result


def parselistlinks(url):
    newsdetial = []     # 存放页面信息
    res = requests.get(url)
    jd = json.loads(res.text.lstrip('  newsloadercallback(').rstrip(');'))  # 得到回传信息，刨除无用信息载入json

    for x in (jd['result']['data']):
        print(x['url'])                 # 从字典中得到url
        newsdetial.append(getNewDetial(x['url']))   # 得到也页面信息
    return newsdetial

if __name__ == '__main__':
    url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&callback=newsloadercallback&_=1505353908881'
    news_total = []     # 存放所有页面信息
    for i in range(1, 2):   # 抓取2列表个页面
        print(url.format(i))
        newsu = (url.format(i))
        newsary = parselistlinks(newsu)
        news_total.extend(newsary)
    print(len(news_total))  # 显示抓取页面个数

    # 导入信息到Excel中
    df = pandas.DataFrame(news_total)
    df.to_excel('new_total.xlsx')


