from urllib.request import Request, HTTPCookieProcessor, build_opener
from fake_useragent import UserAgent
from urllib.parse import urlencode
from http.cookiejar import MozillaCookieJar

# cookie的使用：页面登陆完成后，保存cookie到文件中，并使用该文件中cookie
# 用户名：17703181473 密码：123456

# 第一步：登陆：保存cookie到文件中
def get_cookie():
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
    # 创建保存可以序列化cookie的文件对象
    cookie_jar = MozillaCookieJar()
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    response = opener.open(request)
    cookie_jar.save("11-3cookie.txt", ignore_expires=True, ignore_discard=True) # 后两个参数代表，不管cookie是否过期

# 第二步：获取cookie从文件中，并访问页面
def use_cookie():
    info_url = "http://www.sxt.cn/index/user.html"
    headers = {
        "User-Agent": UserAgent().chrome
    }
    # 构造访问个人页面请求
    request = Request(info_url, headers=headers)
    # 创建保存可以序列化cookie的文件对象
    cookie_jar = MozillaCookieJar()
    # 加载cookie文件
    cookie_jar.load("11-3cookie.txt",  ignore_expires=True, ignore_discard=True) # 加载cookie文件
    # 构造可保存cookie的控制器
    handler = HTTPCookieProcessor(cookie_jar)
    # 构造opener
    opener = build_opener(handler)
    # 发送请求
    response = opener.open(request)
    # 打印信息
    print(response.read().decode())

# 模拟程序入口
if __name__ == '__main__':
    # get_cookie()
    use_cookie()

