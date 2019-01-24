from urllib.request import Request,urlopen
from fake_useragent import UserAgent
import ssl

# https请求中ssl安全认证
'''
请求 SSL证书验证
    现在随处可见 https 开头的网站，urllib可以为 HTTPS 请求验证SSL证书，就像web浏览器一样，如果网站的SSL证书是经过CA认证的，则能够正常访问，如：https://www.baidu.com/
    如果SSL证书验证不通过，或者操作系统不信任服务器的安全证书，比如浏览器在访问12306网站如：https://www.12306.cn/mormhweb/的时候，会警告用户证书不受信任。（据说 12306 网站证书是自己做的，没有通过CA认证）
忽略SSL安全认证
    context = ssl.createunverified_context()
    添加到context参数里
    response = urllib.request.urlopen(request, context = context)
'''

url = "https://www.12306.cn/index/"

headers={
    "User-Agent":UserAgent().chrome
}
request = Request(url,headers=headers)
# 忽略ssl安全认证验证证书
context = ssl._create_unverified_context()
response = urlopen(request,context=context)
info = response.read().decode()
print(info)