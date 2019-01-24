import requests
from fake_useragent import UserAgent
from lxml import etree
import pymysql
# 彩票数据所在的url
url = 'http://datachart.500.com/ssq/'
# 提取数据
response = requests.get(url, headers={"User-Agent": UserAgent().chrome})
# 通过xpath去解析
e = etree.HTML(response.text)
# 第几期
date_times = e.xpath('//tbody[@id="tdata"]/tr/td[1]/text()')
trs = e.xpath('//tbody[@id="tdata"]/tr[not(@class)]') # 一期中所有的双色球号码，其中包含红球和篮球
for date_time, tr in zip(date_times,trs):
    # red_ball = tr.xpath('./td[@class="chartBall01"]/text()')  # 解析红球
    # blue_ball = tr.xpath('./td[@class="chartBall02"]/text()')  # 解析红球
    # 用空白符分隔开红球列表
    # 提取红球
    red_ball = '-'.join(tr.xpath('./td[@class="chartBall01"]/text()'))
    # 提取蓝球 蓝球只有一个
    blue_ball = tr.xpath('./td[@class="chartBall02"]/text()')[0]
    print("第" + date_time + "红球是：" + red_ball + " 蓝球：" + blue_ball)