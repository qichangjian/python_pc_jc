from urllib.request import Request,build_opener
from fake_useragent import UserAgent
from urllib.request import ProxyHandler
# 设置代理Proxy

# 这个url可以返回请求信息：设置代理后ip就不一样了
url = "http://httpbin.org/get"
headers={
    "User-Agent":UserAgent().chrome
}
request = Request(url,headers=headers)
'''
使用代理的两种方式
    1.需要用户名密码（可以自己买，比如：快代理）
        handler = ProxyHandler({"http":"username:密码@ip:port"})
    2.不需要用户名密码(需要靠运气，不一定能用)
        免费代理（西刺）：https://www.xicidaili.com/
        handler = ProxyHandler({"http":"ip:port"})
'''
# 传参ProxyHandler(参数是一个字典：类型 : 用户名：密码：IP:端口号)
# handler = ProxyHandler({"http":"398707160:j8inhg2g@120.27.224.41:16818"})
# 免费代理handler = ProxyHandler({"http":"ip:port"})
handler = ProxyHandler({"http":"121.61.3.4:9999"})
opener = build_opener(handler)
reponse = opener.open(request)
print(reponse.read().decode())