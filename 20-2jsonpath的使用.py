from jsonpath import jsonpath
import requests
from fake_useragent import UserAgent
import json

# jsonpath 解析拉钩网json文件 只取出name和code
'''
JsonPath
JsonPath 是一种信息抽取类库，是从JSON文档中抽取指定信息的工具，提供多种语言实现版本，包括：Javascript, Python， PHP 和 Java。
JsonPath 对于 JSON 来说，相当于 XPATH 对于 XML。
'''

url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    "User-Agent": UserAgent().chrome
}
response = requests.get(url, headers=headers)

names = jsonpath(json.loads(response.text), '$..name') # 参数二是jsonpath的表达式 参数一：是json对象。response.text是str
codes = jsonpath(json.loads(response.text), '$..code') # $:根节点| ..:就是不管位置，选择所有符合条件的条件
print(names)
print(codes)
