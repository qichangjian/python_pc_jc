from bs4 import BeautifulSoup
from bs4.element import Comment
import re
# BeautifulSoup的使用
'''
 Beautiful Soup的简介
Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。
Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。
Beautiful Soup已成为和lxml、html6lib一样出色的python解释器，为用户灵活地提供不同的解析策略或强劲的速度
'''


str = '''
<title>爬虫</title>
<title id='title'>爬虫</title>
<div class='info' float='left'>Welcome to SXT</div>
<div class='info' float='right'>
    <span>Good Good Study</span>
    <span id="sid">Span id</span>
    <a href='www.bjsxt.cn'></a>
    <strong><!--没用--></strong>
</div>
'''

soup = BeautifulSoup(str,'lxml') # 需要安装lxml
# 获取标签
print(soup.title)
print(soup.div)

# 获取属性
print(soup.div.attrs)

# 获取单个属性
print(soup.div.get('class'))
print(soup.div['float'])
print(soup.a['href'])

# 获取内容
print(soup.div.string)
print(soup.div.text)

# 获取注释
'''
Comment
Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号，但是如果不好好处理它，可能会对我们的文本处理造成意想不到的麻烦
'''
print(soup.strong.string)
if type(soup.strong.string) == Comment:
    print(soup.strong.string)
    print(soup.strong.prettify())
else:
    print(soup.strong.text)

# 查看类型
'''
四大对象种类
Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:
    Tag
    NavigableString
    BeautifulSoup
    Comment
'''
print(type(soup.div.string))
print(type(soup.strong.text))

# 筛选方法
print("----------------------搜索文档树------------------------------")
'''
搜索文档树
Beautiful Soup定义了很多搜索方法,这里着重介绍2个: find() 和 find_all() .
其它方法的参数和用法类似,请举一反三
'''
print("-------------------find_all----------------------")
#  方式一：字符串：标签
# 最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的标签
print(soup.find_all('div')) # 返回所有的div标签

# 方式二：正则表达式
# 如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容
print(soup.find_all(re.compile("^div")))

# 方式三：列表：也就是多个标签
# 如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回
print(soup.find_all(['span','a'])) #返回所有匹配到的span a标签

# 方式四：keyword：也就是id
# 如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性
print(soup.find_all(id="sid")) # 返回id为sid的标签

# 方式四：按CSS搜索，也就是class
# 按照CSS类名搜索tag的功能非常实用,但标识CSS类名的关键字 class 在Python中是保留字,使用 class 做参数会导致语法错误.从Beautiful Soup的4.1.1版本开始,可以通过 class_ 参数搜索有指定CSS类名的tag
print(soup.find_all(class_="info")) # 返回class为info的标签

# 方式五：按属性的搜索
print(soup.find_all(float="left"))
print(soup.find_all(attrs={'float':'left'})) # 另一种写法

# 方式六：True
# True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
print("---------Ture Start-----------")
print(soup.find_all(True))
print("---------Ture End-----------")

print("----------------------CSS选择器（扩展）------------------------------")
'''
soup.select(参数)

表达式	说明
tag	选择指定标签
*	选择所有节点
#id	选择id为container的节点
.class	选取所有class包含container的节点
li a	选取所有li下的所有a节点
ul + p	(兄弟)选择ul后面的第一个p元素
div#id > ul	(父子)选取id为id的div的第一个ul子元素
table ~ div	选取与table相邻的所有div元素
a[title]	选取所有有title属性的a元素
a[class=”title”]	选取所有class属性为title值的a
a[href*=”sxt”]	选取所有href属性包含sxt的a元素
a[href^=”http”]	选取所有href属性值以http开头的a元素
a[href$=”.png”]	选取所有href属性值以.png结尾的a元素
input[type="redio"]:checked	选取选中的hobby的元素
'''
print(soup.select('title')) # 标签选择器
print(soup.select('#title'))# id选择器
print(soup.select(".info")) # 类选择器class
print(soup.select("div span")) # div中的span
print(soup.select("div > span")) # div中的span: 注意要有空格
print(soup.select('div')[1].select('a')) # 第二个div中a标签
print(soup.select('title')[0]) # 第一个title
print(soup.select('title')[0].text) # title中内容


