import json

str = '{"name":"盗梦空间"}'
print(type(str))

# 字典转换为json对象
'''json.loads():把Json格式字符串解码转换成Python对象 '''
obj = json.loads(str)
print(type(obj))

# json对象转换回来
''' json.dumps():从python原始类型向json类型 '''
str2 = json.dumps(obj, ensure_ascii=False) # ensure_ascii=False 乱码转换为中文
print(type(str2), ":", str2)

# json对象写为文件
'''json.dump():将Python内置类型序列化为json对象后写入文件 '''
json.dump(obj, open("20movie.txt", 'w',encoding='utf-8'),ensure_ascii=False)

# 读取文件为python类型
''' json.load():读取文件中json形式的字符串元素 转化成python类型'''
str3 = json.load(open('20movie.txt'))