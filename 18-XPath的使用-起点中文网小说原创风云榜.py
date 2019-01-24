from lxml import etree
import requests
from fake_useragent import UserAgent
# Xpath 爬取起点中文网中小说类原创风云榜玄幻小说名称和作者
# 再chrome中安装Xpath Helper插件

'''
1. 介绍
    之前 BeautifulSoup 的用法，这个已经是非常强大的库了，不过还有一些比较流行的解析库，例如 lxml，使用的是 Xpath 语法，同样是效率比较高的解析方法。如果大家对 BeautifulSoup 使用不太习惯的话，可以尝试下 Xpath
    官网 http://lxml.de/index.html
    w3c http://www.w3school.com.cn/xpath/index.asp
2. XPath语法
    XPath 是一门在 XML 文档中查找信息的语言。XPath 可用来在 XML 文档中对元素和属性进行遍历。XPath 是 W3C XSLT 标准的主要元素，并且 XQuery 和 XPointer 都构建于 XPath 表达之上
'''
url = "https://www.qidian.com/rank/yuepiao?chn=21"
headers = {
    "User-Agent": UserAgent().chrome
}
response = requests.get(url, headers=headers)

e = etree.HTML(response.text)
# 获取小说名称，作者
names = e.xpath('//h4/a/text()')
authors = e.xpath('//p[@class="author"]/a[1]/text()')
print(names)
print(authors)

# 循环遍历1
# for num in range(len(names)):
#     print(names[num],":",authors[num])

# 循环遍历2
for name,author in zip(names,authors):
    print(name,":",author)