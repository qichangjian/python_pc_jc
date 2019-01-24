import requests
from fake_useragent import UserAgent
from lxml import etree

# 爬取糗事百科文字中的所有笑话
'''
每个方法都干自己的事情
'''

# url管理
class URLManager(object):
    def __init__(self):
        # 初始化容器：空list
        self.new_url = []
        self.old_url = []

    # 获取一个url
    def get_new_url(self):
        # 从新的列表中取出来放入老的列表
        url = self.new_url.pop()
        self.old_url.append(url)
        return url

    # 增加一个url
    def add_new_url(self,url):
        # 已经存在于列表中和爬取过的url不用添加，url 不是空的
        if url not in self.new_url and url and url not in self.old_url:
            self.new_url.append(url)

    # 增加多个url
    def add_new_urls(self,urls):
        for url in urls:
            self.add_new_url(url)

    # 判断是否还有可以爬取的url
    def has_new_url(self):
        return self.get_new_url_size() > 0
        # 获取可以爬取的数量

    def get_new_url_size(self):
        return len(self.new_url)

    # 获取已经爬取的数量
    def get_old_url_size(self):
        return len(self.old_url)

# 爬取
class Downloader:
    def download(self, url):
        response = requests.get(url, headers={"User-Agent": UserAgent().random})
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        else:
            return None

# 解析
class Parser:
    def parse(self, html):
        e = etree.HTML(html)
        datas = self.parse_info(e) # url解析 出来的 数据
        #datas = [span.xpath('string(.)') for span in e.xpath('//div[@class="content"]/span[1]')]
        urls = self.parse_urls(e) # url 解析出来数据其中的url
        #urls = [ 'https://www.qiushibaike.com{}'.format(url) for url in e.xpath('//ul[@class="pagination"]/li/a/@href')]
        return datas, urls

    # 解析数据的方法
    def parse_info(self, e):
        spans = e.xpath('//div[@class="content"]/span[1]')
        datas = []
        for span in spans:
            datas.append(span.xpath('string(.)'))
        return datas

    # 解析数据中url的方法
    def parse_urls(self, e):
        base_url = 'https://www.qiushibaike.com{}'
        urls = []
        # url是下一页的href
        for url in e.xpath('//ul[@class="pagination"]/li/a/@href'):
            print(url)
            urls.append(base_url.format(url))
        return urls

# 数据处理
class DataOutPut:
    def save(self, datas):
        with open('duanzi.txt', 'a', encoding='utf-8') as f:
            for data in datas:
                f.write(data)

# 调度:上边方法怎样合作的
class DiaoDu:
    # 初始化调度类
    def __init__(self):
        self.downloader = Downloader()
        self.url_manager = URLManager()
        self.parser = Parser()
        self.data_saver = DataOutPut()

    # 调度运行的方法
    def run(self, url):
        # 添加要解析的url
        self.url_manager.add_new_url(url)
        # 循环执行: 知道没有要解析的url后跳出
        while self.url_manager.has_new_url():
            # 得到url
            url = self.url_manager.get_new_url()
            # 爬取url中的数据
            html = self.downloader.download(url)
            # 解析爬取url中的数据
            data, urls = self.parser.parse(html)
            # 保存数据到文本
            self.data_saver.save(data)
            # 添加解析url中新出现的urls
            self.url_manager.add_new_urls(urls)

if __name__ == '__main__':
    # 构建调度对象
    diao_du = DiaoDu()
    diao_du.run('https://www.qiushibaike.com/text/page/1/')