import requests
from fake_useragent import UserAgent

# request模块的代理访问
'''
 代理访问:proxies
采集时为避免被封IP，经常会使用代理。requests也有相应的proxies属性
'''
url = "http://httpbin.org/get"
headers = {
    "User-Agent": UserAgent().chrome
}
# 代理字典
proxies = {
    "http": "219.139.141.61:9999"
}

response = requests.get(url, headers=headers, proxies=proxies)
print(response.text)