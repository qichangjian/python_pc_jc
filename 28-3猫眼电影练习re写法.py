import requests
from fake_useragent import UserAgent
from random import randint
from time import sleep
import re

# 相比xpath方法只是修改了parse_index和parse_info，format_actors方法，解析方式不同 ()中间为想要的

# 发送请求方法
def get_html(url):
    headers = {
        "User-Agent": UserAgent().chrome
    }
    # 防止访问频率过高 ：随机睡眠
    # sleep(randint(3, 10))
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else:
        return None

# 解析html(解析url),并返回每个电影的url
def parse_index(html):
    # 拿到每个电影的url
    all_url = re.findall(r' <a href="(/films/\d+)" target="_blank" data-act="movies-click" data-val="{movieId:\d+}">', html)
    return ['http://maoyan.com{}'.format(url) for url in all_url]

# 解析单个电影的url内容:电影名，电影类型，演员
def parse_info(html):
    # 因为返回的是列表，所以取第一个
    name = re.findall(r'<h3 class="name">(.+)</h3>', html)[0]
    types = re.findall(r'<li class="ellipsis">(.+)</li>', html)[0]
    actors = re.findall(r'<li class="celebrity actor".+>\s+<a href="/films/cel.+>\s+<img.+>\s+</a>\s+<div.+>\s+<a.+>\s+(.+)\s+</a>', html)

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