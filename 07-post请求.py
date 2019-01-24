from urllib.request import Request,urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent
# post请求：添加data参数

'''
Post 请求
    我们说了Request请求对象的里有data参数，它就是用在POST里的，我们要传送的数据就是这个参数data，data是一个字典，里面要匹配键值对
发送请求/响应header头的含义：
    名称 | 含义 ---|--- Accept | 告诉服务器，客户端支持的数据类型 Accept-Charset | 告诉服务器，客户端采用的编码 Accept-Encoding | 告诉服务器，
    客户机支持的数据压缩格式 Accept-Language | 告诉服务器，客户机的语言环境 Host | 客户机通过这个头告诉服务器，想访问的主机名 If-Modified-Since | 客户机通过这个头告诉服务器，资源的缓存时间 Referer | 客户机通过这个头告诉服务器，它是从哪个资源来访问服务器的。
    （一般用于防盗链） User-Agent | 客户机通过这个头告诉服务器，客户机的软件环境 Cookie | 客户机通过这个头告诉服务器，可以向服务器带数据 Refresh | 服务器通过这个头，告诉浏览器隔多长时间刷新一次 Content-Type | 服务器通过这个头，回送数据的类型 Content-Language | 服务器通过这个头，告诉服务器的语言环境 Server | 服务器通过这个头，告诉浏览器服务器的类型 Content-Encoding | 服务器通过这个头，告诉浏览器数据采用的压缩格式 Content-Length | 服务器通过这个头，告诉浏览器回送数据的长度
'''
url = "http://www.sxt.cn/index/login/login.html"
headers= {
    "User-Agent":UserAgent().chrome
}
#写一个字典：因为有可能有中文
form_data={
    "user": "17703181473",
    "password": "123456"
}
#转换为字符串
f_data = urlencode(form_data)
# 字符串抓换为字节数组
request = Request(url,data=f_data.encode(),headers=headers)
reponse = urlopen(request)
print(reponse.read().decode())
