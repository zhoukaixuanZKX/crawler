import requests
from bs4 import BeautifulSoup
res = requests.get("http://news.sina.com.cn/china/")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')

for news in soup.select('.news-item'):
    if len(news.select('h2')) > 0:
        title = news.select('h2')[0].text    #取出包含在标签h2中的标题头部   <h2><a></a></h2>
        time = news.select('.time')[0].text  #取出 class = time 的内容
        link = news.select('a')[0]['href']   #取出包含在标签a 中的链接
        print(time,title,link)
