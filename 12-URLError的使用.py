from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from urllib.error import URLError

#  URLError的使用：在代码中，我们需要用try-except语句来包围并捕获相应的异常
'''
 URLError
首先解释下URLError可能产生的原因：
- 网络无连接，即本机无法上网
- 连接不到特定的服务器：login123
- 服务器不存在：www.sxt123.cn
'''

url = "http://www.sxt123.cn/index/login/login123"

headers = {
    "User-Agent": UserAgent().chrome
}
try:
    req = Request(url, headers=headers)
    resp = urlopen(req)
    print(resp.read().decode())
except URLError as e:
    if e.args == ():
        print(e.code)
    else:
        print(e.args[0].errno)
print("访问完成")