from urllib.request import Request
from urllib.request import build_opener
from fake_useragent import UserAgent
from urllib.request import HTTPHandler

#opener的例子 也就是实现response = urlopen(request)的效果

url = "http://www.baidu.com"
headers={
    "User-Agent":UserAgent().chrome
}
request = Request(url,headers=headers)
opener = build_opener()
# 传参HTTPHandler
'''
handler = HTTPHandler
opener = build_opener(handler)
'''
reponse = opener.open(request)
print(reponse.read().decode())