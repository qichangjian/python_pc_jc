import requests
from fake_useragent import UserAgent
from lxml import etree
import pymysql

'''
创建数据库ball
创建表t_ball
'''
# 第一步：提取数据
# 彩票数据所在的url
url = 'http://datachart.500.com/ssq/'
# 提取数据
response = requests.get(url, headers={"User-Agent": UserAgent().chrome})
# 通过xpath去解析
e = etree.HTML(response.text)
# 第几期
date_times = e.xpath('//tbody[@id="tdata"]/tr/td[1]/text()')
trs = e.xpath('//tbody[@id="tdata"]/tr[not(@class)]') # 一期中所有的双色球号码，其中包含红球和篮球

# 第二步：连接数据库
# 链接数据库
client = pymysql.connect(host='localhost', port=3306, user='root', password='root', charset='utf8', db='ball')
cursor = client.cursor()
# 插入数据的sql
sql = 'insert into t_ball values(0,%s,%s,%s)'
# reverse() 函数用于反向列表中元素。
# 查看数据是否存在： 用于叠加数据，比如说新增了一期
select_new_sql = "select * from t_ball where date_time = %s"
date_times.reverse() # 反序

# # 记录有多少条新数据
# index = 0
# for data_time in date_times:
#     reslut = cursor.execute(select_new_sql, [data_time])
#     # 判断数据是否存在
#     if reslut == 1:
#         break
#     index += 1
# print(index)
# trs.reverse()

for date_time, tr in zip(date_times,trs):
    # 用空白符分隔开红球列表
    # 提取红球
    red_ball = '-'.join(tr.xpath('./td[@class="chartBall01"]/text()'))
    # 提取蓝球 蓝球只有一个
    blue_ball = tr.xpath('./td[@class="chartBall02"]/text()')[0]
    print("第" + date_time + "红球是：" + red_ball + " 蓝球：" + blue_ball)
    # 添加数据到数据库
    cursor.execute(sql, [date_time, red_ball, blue_ball])
    client.commit()

# 关闭数据库
cursor.close()
client.close()
