from urllib.request import urlopen,Request
from fake_useragent import UserAgent
# Ajax请求

'''
Ajax的请求获取数据
    有些网页内容使用AJAX加载，而AJAX一般返回的是JSON,直接对AJAX地址进行post或get，就返回JSON数据了
'''
#解析json: https://www.json.cn/
#判断是ajax请求：1.再header中有X-Requested-With: XMLHttpRequest  2.查看代码有没有
#提高效率的方式修改limit
base_url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20"
#假设有一万条数据，没有到停止
i = 0
while True:
    headers={
        "User-Agent":UserAgent().chrome
    }
    url = base_url.format(i*20)#20 40 60
    request = Request(url,headers=headers)
    response = urlopen(request)
    info = response.read().decode()
    if info == "" or info is None:
        break
    print(info)
    i += 1