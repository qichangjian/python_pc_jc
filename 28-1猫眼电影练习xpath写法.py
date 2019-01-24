import requests
from fake_useragent import UserAgent
from lxml import etree
from random import randint
from time import sleep

# 发送请求方法
def get_html(url):
    headers = {
        "User-Agent": UserAgent().chrome
    }
    # 防止访问频率过高 ：随机睡眠
    sleep(randint(3, 10))
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else:
        return None

# 解析html(解析url),并返回每个电影的url
def parse_index(html):
    e = etree.HTML(html)
    # 拿到每个电影的url
    all_url = e.xpath('//div[@class="channel-detail movie-item-title"]/a/@href')
    return ['http://maoyan.com{}'.format(url) for url in all_url]

# 解析单个电影的url内容:电影名，电影类型，演员
def parse_info(html):
    e = etree.HTML(html)
    name = e.xpath('//h3[@class="name"]/text()')[0] # 因为返回的是列表，所以取第一个
    types = e.xpath('//li[@class="ellipsis"][1]/text()')[0]
    actors = e.xpath('//li[@class="celebrity actor"]/div[@class="info"]/a/text()')
    actors = format_actors(actors)
    # 返回一个字典
    return {
        "name": name,
        "types": types,
        "actors": actors
    }

# 处理演员：去重 也就是格式化
def format_actors(actors):
    actor_set = set()
    for actor in actors:
        actor_set.add(actor.strip()) # 去空格
    return actor_set

def main():
    index_url = 'http://maoyan.com/films'
    html = get_html(index_url)
    movie_urls = parse_index(html)
    # print(movie_urls)
    for movie_url in movie_urls:
        movie_html = get_html(movie_url)
        movie = parse_info(movie_html)
        print(movie)

if __name__ == '__main__':
    main()