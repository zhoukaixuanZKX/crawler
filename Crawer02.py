import requests
import json
import re
from bs4 import BeautifulSoup
from datetime import datetime

#使用request获取文章内容
res = requests.get('http://news.sina.com.cn/o/2017-09-13/doc-ifykuftz6614143.shtml')
res.encoding = 'utf-8 '
#将获取的网页内容丢进 BeautifulSoup方便之后的剖析
soup = BeautifulSoup(res.text,'html.parser')

#获得新闻内文标题
title = soup.select("#artibodyTitle")[0].text

#获得新闻发布时间和来源
time = soup.select(".time-source")[0]
#打印结果是： 外围是一层最大的span  里面还有一层span  来源包含在中间那层span里面
'''<span class="time-source" id="navtimeSource">2017年09月13日08:51		<span>
<span data-sudaclick="media_name"><a href="http://www.thepaper.cn/newsDetail_forward_1792685" rel="nofollow" target="_blank">澎湃新闻</a></span></span>
</span>'''
#上面的语句会把span里面的时间和来源一块取出来

#将时间和来源分别取来
time = soup.select(".time-source")[0].contents   #contents会根据标签将里面的内容列成一个list。

#会打印以下内容， 这是一个list，里面含有两个元素，以逗号分割
'''['2017年09月13日08:51\t\t', <span>
<span data-sudaclick="media_name"><a href="http://www.thepaper.cn/newsDetail_forward_1792685" rel="nofollow" target="_blank">澎湃新闻</a></span></span>, '\n']'''

#要取时间，取得list的第一个元素
timesource = soup.select(".time-source")[0].contents[0].strip()
print(timesource)   #2017年09月13日08:51
#上面取出的时间是字符串格式，要存到数据库里面要转换成时间格式
#字符串转时间 -strptime
#dt = datetime.strptime(timesource,'%Y年%m月%d日%H:%M')dt

#时间转字串 -strftime
#dt.strftime('%Y-%m-%d')

#要导入
#from datetime import datetime

#将timesource转换为时间
dt = datetime.strptime(timesource,'%Y年%m月%d日%H:%M')
print(dt)   #2017-09-13 08:51:00

#时间转换成字符串
dt.strftime("%Y-%m-%d")
#print(dt)     #2017-09-13


#处理新闻来源信息
source = soup.select('.time-source span a')[0].text

#取得文章内文
text = soup.select('#artibody p')[:-1]

#因为正文放在多个p标签里面，要把p标签里面的东西取出来，连在一起
article = []
for p in soup.select('#artibody p')[:-1]:
    article.append(p.text.strip())
print(article)
print(' '.join(article))

#简写
[p.text.strip() for p in soup.select('#artibody p')[:-1]]  #包含所有的p元素，只是将p标签移除掉，是一个list
' '.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])  #将list元素合并在一起，中间用空格隔开


#取得编辑名称
editor = soup.select('.article-editor')[0].text.lstrip('责任编辑：')
print(editor)

#取得评论数
comments = requests.get('http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fykuftz6614143&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20&')

#从json变成python的字典 使用json.load的方法 使用之前把js做个清除
#comments.text.strip('var data=')
#变成python的字典
jd = json.loads(comments.text.strip('var data='))

#找到我们需要的东西：在result的count下面  的total
print(jd['result']['count']['total'])

#剖析新闻标识

#方法一：使用strip 和spilt
newsurl = 'http://news.sina.com.cn/o/2017-09-13/doc-ifykuftz6614143.shtml'
#根据斜线做切割，取最后一部分http://news.sina.com.cn/o/2017-09-13/doc-ifykuftz6614143.shtml
newsid = newsurl.split('/')[-1].rstrip('.shtml').lstrip('doc-i')

#方法二：使用正则表达式  使用re模块
#使用re,sesrch方法 把id取出来
m = re.search('doc-i(.*).shtml',newsurl)
newsid= m.group(1)
print(newsid)