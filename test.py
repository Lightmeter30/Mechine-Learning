import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

# 发送搜索请求
url = "http://yzb.buaa.edu.cn/"

# 获取网页内容并且进行解码
html = requests.get(url + "xlss.htm")
html.encoding = "utf-8"
# 使用默认解析器解析html文件，得到一个对象
soup = BeautifulSoup(html.text, "lxml")


content = soup.select("ul.newslist > li > a")
date = soup.select("ul.newslist > li > span")

table = PrettyTable(["序号", "链接", "标题", "时间"])
table.padding_width = 1

for i in range(len(content)):
  link = url + content[i]['href']
  title = content[i]['title']
  table.add_row([i + 1, link, title, date[i].string])
  
print(table)