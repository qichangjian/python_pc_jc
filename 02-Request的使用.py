from urllib.request import urlopen
from urllib.request import Request
from random import choice # 随机选择
# DEMO:伪装user-agent,实现动态UA

url = "http://www.baidu.com"
# 封装请求头：这个是浏览器访问请求头中的信息
# 三种不同浏览器种类的user-agent （user-agent大全：https://blog.csdn.net/u012195214/article/details/78889602）
user_agents=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
]
# 测试随机输出一种浏览器user-agent
# print(choice(user_agents))
headers = {
     "User-Agent": choice(user_agents)
}
# Request封装
request = Request(url, headers=headers)
# request = Request(url)
# 查看一下请求头:注意agent A是小写
# print(request.get_header("User-agent"))

# 发送请求
response = urlopen(request)
# 读取内容
info = response.read()
# 打印内容
# print(info.decode())
