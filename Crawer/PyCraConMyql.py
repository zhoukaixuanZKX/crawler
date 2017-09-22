import requests
from bs4 import BeautifulSoup
import json
import re
from Pycrawler import ConntMysql


def getCommentCount(newsurl):
    # 评论链接
    commenturl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
    # 用正则表达式从正文连接中得到信息，m.group取出id
    m = re.search('doc-i(.*).shtml', newsurl)
    newid = m.group(1)
    # commentual.format(newid)把newid添加到评论链接中，通过get函数得到回应
    comments = requests.get(commenturl.format(newid))
    # 得到内容为取出多余字符，带入到js中。
    jd = json.loads(comments.text.strip('var data='))
    print(comments.text.strip('var data='))
    return jd['result']['count']['total']


def getNewDetial(newsurl):

    result = {}     # 定义字典，用于传出数据
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    # 标题
    result['title'] = soup.select('#artibodyTitle')[0].text
    # 正文
    texts = []
    for p in soup.select('#artibody p')[:-1]:
        texts.append(p.text.strip())
        ' '.join(texts)
    result['Contents'] = ' '.join(texts)
    # 新闻源
    try:
        result['Source'] = soup.select('.time-source span a')[0].text

    except:
        print('Source ERROR,Source parser changed')
        result['Source'] = soup.select('.time-source span')[0].text
    # 编辑人
    result['Editor'] = soup.select('.article-editor')[0].text.lstrip('责任编辑： ')
    # 时间
    result['time'] = soup.select('.time-source')[0].contents[0].strip()
    # result['time'] = datetime.strptime(timetemp, '%Y年%m月%d日%H:%M')  # 时间
    # 评论
    result['Comments'] = getCommentCount(newsurl)
    return result

def parselistlinks(url):
    res = requests.get(url)
    jd = json.loads(res.text.lstrip('  newsloadercallback(').rstrip(');'))  # 得到回传信息，刨除无用信息载入json
    count = [0, 0, 0]   # 计算数组,[0]为总数,[1]成功数量,[2]失败数量

    for x in (jd['result']['data']):
        count[0] += 1
        print(x['url'])                 # 从字典中得到url
        data = getNewDetial(x['url'])   # 得到也页面信息
        count[1] += ConntMysql.inserdata(data, db, 'Sinanew')
        count[2] = count[0] - count[1]
    return count

if __name__ == '__main__':
    # 多个页面
    url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&callback=newsloadercallback&_=1505353908881'
    db = ConntMysql.connmysql()
    count = [0, 0, 0]   # 总计数数组
    for i in range(1, 50):   # 抓取多个列表的页面
        print(url.format(i))
        newsurl = (url.format(i))
        outputresult = parselistlinks(newsurl)
        for x in range(0, 3):
            count[x] += outputresult[x]
    print('总共抓取: {}     成功: {}     失败: {}'.format(count[0], count[1], count[2]))
    db.close()

    # 单个页面扒取
    # url = 'http://news.sina.com.cn/c/nd/2017-09-18/doc-ifykywuc5918893.shtml'
    # getCommentCount(url)
    # db = ConntMysql.connmysql()
    # data = getNewDetial(url)
    # print(data)
    # ConntMysql.inserdata(data, db, 'Sinanew')
    # db.close()

