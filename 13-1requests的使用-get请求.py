import requests
from fake_useragent import UserAgent

# request模块的get请求
'''
get请求:params
参数是字典，我们也可以传递json类型的参数
'''
url = "http://www.baidu.com/s"
headers = {
    "User-Agent": UserAgent().chrome
}
# 参数
params = {
    "wd": "爬虫"
}

response = requests.get(url, headers=headers, params=params)
print(response.text)