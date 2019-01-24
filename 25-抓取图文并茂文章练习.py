import requests
from fake_useragent import UserAgent
from lxml import etree

url = 'http://www.farmer.com.cn/xwpd/rdjj1/201807/t20180726_1393916.htm'
headers = {
    "User-Agent": UserAgent().chrome
}
response = requests.get(url, headers=headers)
# print(response.text)

# xpath解析
e = etree.HTML(response.text)
title = e.xpath('//h1/text()')
# 内容由多个p组成,每个取出来，拼接成一个context
all_p_tag = e.xpath('//div[@class="content"]//p')
content = [] #列表
for p in all_p_tag:
    info = p.xpath('string(.)')
    content.append(info)
# print(content)
# 可以遍历url访问获取图片保存
img_urls = e.xpath('//div[@class="content"]//img/@src')
# print(img_urls)
# 多个图片名称:0 2 4是空串
img_names = e.xpath('//div[@align="center"]')
for num in range(1,len(img_names),2):
    img_name = img_names[num].xpath('string(.)')
    # print(img_name)




