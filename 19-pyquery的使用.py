from pyquery import PyQuery as pq
import requests
from fake_useragent import UserAgent

# pyquery 使用爬取西刺代理的ip
'''
 pyquery
  介绍
如果你对CSS选择器与Jquery有有所了解，那么还有个解析库可以适合你--Jquery
官网https://pythonhosted.org/pyquery/
'''

url = "https://www.xicidaili.com/"
headers = {
    "User-Agent": UserAgent().chrome
}
response = requests.get(url,headers=headers)
doc = pq(response.text)
trs = doc('#ip_list tr') # 得到tr列表元素
for num in range(1,len(trs)): # 遍历每个tr,取出存取ip的td中的ip内容 eq是选择并列标签中的第几个
    ip = trs.eq(num).find('td').eq(1).text()
    port = trs.eq(num).find('td').eq(2).text()
    type_h = trs.eq(num).find('td').eq(5).text()
    print(ip, ":", port, ":", type_h)



