import requests
from fake_useragent import UserAgent

# request模块的post请求
'''
 post请求 :data
参数是字典，我们也可以传递json类型的参数
'''
url = "http://www.sxt.cn/index/login/login"
headers = {
    "User-Agent": UserAgent().chrome
}
# 参数
params = {
    "user": "17703181473",
    "password": "123456"
}

response = requests.get(url, headers=headers, data=params)
print(response.text)