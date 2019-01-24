from urllib.request import Request,urlopen
from fake_useragent import UserAgent
#cookie的使用：页面登陆完成后，拷贝cookie过来
#用户名：17703181473 密码：123456

'''
1. Cookie
为什么要使用Cookie呢？
Cookie，指某些网站为了辨别用户身份、进行session跟踪而储存在用户本地终端上的数据（通常经过加密）
比如说有些网站需要登录后才能访问某个页面，在登录之前，你想抓取某个页面内容是不允许的。那么我们可以利用Urllib库保存我们登录的Cookie，然后再抓取其他页面就达到目的了。
1.1 Opener
当你获取一个URL你使用一个opener(一个urllib.OpenerDirector的实例)。在前面，我们都是使用的默认的opener，也就是urlopen。它是一个特殊的opener，可以理解成opener的一个特殊实例，传入的参数仅仅是url，data，timeout。
如果我们需要用到Cookie，只用这个opener是不能达到目的的，所以我们需要创建更一般的opener来实现对Cookie的设置
1.2 Cookielib
cookielib模块的主要作用是提供可存储cookie的对象，以便于与urllib模块配合使用来访问Internet资源。Cookielib模块非常强大，我们可以利用本模块的CookieJar类的对象来捕获cookie并在后续连接请求时重新发送，比如可以实现模拟登录功能。该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar
'''

url = "http://www.sxt.cn/index/user.html"
headers = {
    "User-Agent": UserAgent().chrome,
    "Cookie": "UM_distinctid=168517e8edb15b-0cc8953246df7e-b781636-100200-168517e8edd26f; PHPSESSID=t4nqu8fi2p7sif5ndm25p198a3; CNZZDATA1261969808=1753540418-1547550079-http%253A%252F%252Fwww.sxt.cn%252F%7C1547612723"
}
request = Request(url, headers=headers)
response = urlopen(request)
info = response.read().decode()
print(info)