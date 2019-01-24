import requests
from fake_useragent import UserAgent

# request模块的证书
'''
 ssl验证:verify=False
'''
url = "https://www.12306.cn/index/"
headers = {
    "User-Agent": UserAgent().chrome
}
# 禁用开头安全请求警告
requests.packages.urllib3.disable_warnings()
response = requests.get(url, verify=False, headers=headers)
# 设置返回字符编码方式
response.encoding = "utf-8"
print(response.text)