import requests
import re
from fake_useragent import UserAgent

url = "https://www.qiushibaike.com/text/page/2/"
headers = {
    "User-Agent": UserAgent().chrome
}
# 构造请求
response = requests.get(url, headers=headers)
info = response.text
# print(info)

# 匹配其中的内容 <div class="content">\s*<span>\s*（.+）\s*</span>
# infos = re.findall(r'', info) # 这里加入断点进行调试，再菜单栏中找到类似计算机的图标进行测试：（输入：re.findall(r'<div class="content">\s*<span>\s*(.+)\s*</span>',info)）# \s 匹配任意空白字符，等价于 [\t\n\r\f]. \s* 换行
infos = re.findall(r'<div class="content">\s*<span>\s*(.+)\s*</span>',info)
print(infos)

# 保存到文件中
with open('16duanzi.txt','w',encoding='utf-8') as f:
    for info in infos:
        f.write(info + "\n\n\n")