import requests
from fake_useragent import UserAgent
from day1.YDMPython3_Util import get_code

# 自动获取验证码图片，通过云打码识别，然后自动登陆

# 登录
def do_login(code):
    login_url = 'http://www.yundama.com/index/login?'
    f_data = {
        "username": "398707160_pt",
        "password": "123456abc",
        "utype": "1",
        "vcode": code
    }
    response = session.get(login_url, headers=headers, params=f_data)
    print(response.text)

# 获取验证码
def get_image():
    img_url = 'http://www.yundama.com/index/captcha'
    response = session.get(img_url,headers=headers)
    # 保存验证码图片
    with open('ydm.jpg', 'wb') as f:
        f.write(response.content)
    filename = b'ydm.jpg'
    code = get_code(filename)
    return code.decode()

# 模拟程序入口
if __name__ == '__main__':
    # 保证是一个回话，让服务器知道返回数据到哪里
    session = requests.Session()
    # 登录首页
    index_url = 'http://www.yundama.com/'
    headers = {
        "User-Agent": UserAgent().chrome
    }
    response = session.get(index_url, headers=headers)
    # 获取验证码
    code = get_image()
    # 登录
    do_login(code)

