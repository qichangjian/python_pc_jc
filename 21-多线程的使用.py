from threading import Thread
from queue import Queue
from fake_useragent import UserAgent
import requests
from lxml import etree

# 多线程的使用：多线程爬取糗事百科中的段子，保存下来 解析

# 爬虫类
class CrawlInfo(Thread):
    # 初始化
    def __init__(self, url_queue, html_queue):
        Thread.__init__(self)
        self.url_queue = url_queue
        self.html_queue = html_queue

    def run(self):
        headers = {
            "User-Agent": UserAgent().chrome
        }
        while self.url_queue.empty() == False:
            response = requests.get(self.url_queue.get(), headers=headers)
            # print(response.text)
            if response.status_code == 200:
                # print(response.text)
                self.html_queue.put(response.text) # 存储内容到保存queue中

# 解析类
class ParseInfo(Thread):
    def __init__(self, html_queue):
        Thread.__init__(self)
        self.html_queue = html_queue

    def run(self):
        while self.html_queue.empty() == False:
            # 解析lxml 爬取返回的内容
            e = etree.HTML(self.html_queue.get())
            # 有25个span
            span_content = e.xpath('//div[@class="content"]/span[1]')
            # print(span_content)
            # 写入文件中
            with open('21duanzi.txt','a',encoding='utf-8') as f:
                for span in span_content:
                    # span内容格式化
                    info = span.xpath('string(.)') # . 当前节点
                    print(info)
                    f.write(info + "\n")  # 每个段子换行

# 模拟入口
if __name__ == '__main__':
    # 存储url的容器
    url_queue = Queue()
    # 创建存储爬取回来内容的容器
    html_queue = Queue()
    base_url = 'https://www.qiushibaike.com/text/page/{}/'
    for i in range(1, 14):
        new_url = base_url.format(i)
        url_queue.put(new_url)
     # 创建爬虫
    crawl_list = []
    for i in range(0, 3):
        crawl1 = CrawlInfo(url_queue, html_queue)
        crawl_list.append(crawl1)
        crawl1.start()
    # 等待线程结束。 原因：因为主线程不会等待其他线程，没有这个没有数据的原因就是，副线程没有执行完，主线程就结束了
    # join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生
    for crawl in crawl_list:
        crawl.join()

    # 创建解析线程
    parse_list = []
    for i in range(0, 3):
        parse = ParseInfo(html_queue)
        parse_list.append(parse)
        parse.start()
    for parse in parse_list:
        parse.join()