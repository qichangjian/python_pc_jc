import requests
from fake_useragent import UserAgent
from lxml import etree

# 爬取图虫网图片练习

url = "https://tuchong.com/1485770/19399344/#image351010920"
response = requests.get(url, headers={"User-Agent": UserAgent().chrome})
e = etree.HTML(response.text)
img_urls = e.xpath('//article/img/@src')

print(img_urls)

for url in img_urls:
    response = requests.get(url, headers={"User-Agent": UserAgent().chrome}) # 根据每个图片的url得到图片
    img_name = url[url.rfind('/')+1:]     # 修改下载下来的图片名称： 截取最后变得/后的图片名称
    with open('img/'+img_name, 'wb') as f: # img目录要存在
        f.write(response.content)