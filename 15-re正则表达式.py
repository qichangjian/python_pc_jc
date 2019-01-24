import re


str = "I Study Python3.6 Everyday"
'''
常用方法
re.match
    re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
    函数语法： re.match(pattern, string, flags=0)
re.search
    re.search 扫描整个字符串并返回第一个成功的匹配。
    函数语法： re.search(pattern, string, flags=0)
re.sub
    re.sub 替换字符串 re.sub(pattern,replace,string)
re.findall
    re.findall 查找全部 re.findall(pattern,string,flags=0)
'''
print("-----------------------match()--------------------------------")
m1 = re.match(r'I', str) # 匹配I开头
print(m1.group())
m2 = re.match(r'\w', str) # 匹配字母数字及下划线
print(m2.group())
m3 = re.match(r'.', str) # 	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
print(m3.group())
m4 = re.match(r'\D',str) # 匹配任意非数字
print(m4.group())
m5 = re.match(r'i', str, re.I) # 使匹配对大小写不敏感
print(m5.group())
m6 = re.match(r'\S',str) # 匹配任意非空字符
print(m6.group())

print("-----------------------search--------------------------------")
print("-----匹配Student-------")
s1 = re.search(r'Study', str)
print(s1.group())
s2 = re.search(r'S\w+', str) #re+	匹配1个或多个的表达式 \w	匹配字母数字及下划线
print(s2.group())
print("-----匹配Python3.6-------")
s3 = re.search(r'P\w+.\d',str) # \d	匹配任意数字，等价于 [0-9]
print(s3.group())

print("-----------------------re.findall--------------------------------")
print("-----匹配所有y-------")
f1 = re.findall(r'y', str)
print(f1)

print("-----------------------re.sub--------------------------------")
sub = "OneDay"
sub1 = re.sub(r"Study", str, sub)
print(sub1)

print("-----------------------test()--------------------------------")
str2 = '<div><a href="http://www.baidu.com">123百度123</a></div>'
# 提取a标签的内容
t1 = re.findall(r'<a href="http://www.baidu.com">(.+)</a>', str2) # (re)	G匹配括号内的表达式，也表示一个组
print(t1)
# 提取herf
t2 = re.findall(r'<a href="(.+)">',str2)
print(t2)

# 将str2的div换成span
su1 = re.sub(r'<div><a href="http://www.baidu.com">123百度123</a></div>', r'<span><a href="http://www.baidu.com">123百度123</a></span>', str2)
print(su1)
su2 = re.sub(r'<div>(.+)</div>', r'<span>\1</span>', str2) # \1 第一组
print(su2)