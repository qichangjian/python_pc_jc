from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor, build_opener
# cookie的使用：页面自动登陆
# 用户名：17703181473 密码：123456

# 先在登陆页面登陆(注意需要用保存cookie用HTTPCookieProcessor)
login_url = "http://www.sxt.cn/index/login/login"
headers = {
    "User-Agent": UserAgent().chrome
}
form_data = {
    "user": "17703181473",
    "password": "123456"
}
f_data = urlencode(form_data).encode()
request = Request(login_url, headers=headers, data=f_data)
# response = urlopen(request) # 错误的：这样没法携带cookie信息
handler = HTTPCookieProcessor
opener = build_opener(handler)
response = opener.open(request)
login_info = response.read().decode()
print(login_info)
# 再访问user页面
info_url = "http://www.sxt.cn/index/user.html"
request = Request(info_url, headers=headers)
# response = urlopen(request) # 错误的：这样没法携带cookie信息
response = opener.open(request)
info = response.read().decode()
print(info)