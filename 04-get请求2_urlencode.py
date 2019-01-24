from urllib.request import Request,urlopen
from fake_useragent import UserAgent
from urllib.parse import urlencode

# urlencode:多个参数用它
args = {
    "wd":"爬虫",
    "ie":"utf-8"
}
print(urlencode(args))

url = "http://www.baidu.com/s?wd={}".format(urlencode(args)) #format格式化函数（http://www.cnblogs.com/lonelyhiker/p/8570113.html
headers = {
    "User-Agent":UserAgent().chrome
}

request = Request(url,headers=headers)
reponse = urlopen(request)
print(reponse.read().decode())