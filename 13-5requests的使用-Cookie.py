import requests
from fake_useragent import UserAgent

# request模块的session自动保存cookies
'''
  session自动保存cookies:requests.session()
seesion的意思是保持一个会话，比如 登陆后继续操作(记录身份信息) 而requests是单次请求的请求，身份信息不会被记录
'''
url = "http://www.sxt.cn/index/login/login"
headers = {
    "User-Agent": UserAgent().chrome
}
params = {
    "user": "17703181473",
    "password": "123456"
}
# 创建一个session对象
session = requests.Session()
# 用session对象发出post请求，设置cookies
response = session.post(url, headers=headers,data=params)
# 访问user
info_url = "http://www.sxt.cn/index/user.html"
resp = session.get(info_url, headers=headers)
print(resp.text)