from urllib.request import Request,urlopen
from fake_useragent import UserAgent
from urllib.parse import quote

# Get请求的参数都是在Url中体现的,如果有中文，需要转码，这时我们可使用
'''
Get 请求
    大部分被传输到浏览器的html，images，js，css, … 都是通过GET方法发出请求的。它是获取数据的主要方法
    例如：www.baidu.com 搜索
    Get请求的参数都是在Url中体现的,如果有中文，需要转码，这时我们可使用
    urllib.parse.urlencode()
    urllib.parse. quote()
'''

# url = "http://www.baidu.com/s?wd=爬虫"

# 测试转码
# print(quote("爬虫"))

url = "http://www.baidu.com/s?wd={}".format(quote("爬虫")) #format格式化函数（http://www.cnblogs.com/lonelyhiker/p/8570113.html）
headers = {
    "User-Agent":UserAgent().chrome
}

request = Request(url,headers=headers)
reponse = urlopen(request)
print(reponse.read().decode())