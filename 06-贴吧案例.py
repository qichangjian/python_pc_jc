from urllib.request import Request,urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

# DEMO:爬取尚学堂贴吧，按照输入的关键字和第几页进行爬取，并放在存放在文件中

#得到html
def get_html(url):
    headers={
        "User-Agent":UserAgent().chrome
    }
    request = Request(url,headers=headers)
    reponse = urlopen(request)
    # print(reponse.read().decode())
    return reponse.read()#.decode()

#保存html  # path1路径 w:只写打开文件（打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。） utf-8：以怎样的编码打开文件 as f：打开后接口存为f（http://www.cnblogs.com/tianyiliang/p/8192703.html）
def save_html(filename,html_bytes):
    with open(filename,"w") as f:
        # code = html_bytes.encode(encoding='utf-8')
        # f.write(str(code))
        f.write(str(html_bytes))

def main():
    content = input("请输入要下载的内容：")
    num = input("请输入要下载多少页：")
    base_url = "http://tieba.baidu.com/f?ie=utf-8&{}"
    for pn in range(int(num)):
        args={
            "pn":pn + 50,# 每页50
            "kw":content
        }
        filename = "第" + str(pn+1) + "页.html"
        # get_html("http://tieba.baidu.com/f?ie=utf-8&")
        args = urlencode(args)
        print(base_url.format(args))
        print("正在下载"+filename)
        html_bytes = get_html(base_url.format(args))
        print(html_bytes)
        save_html(filename,html_bytes)

# 相当于Python模拟的程序入口 理解： https://blog.csdn.net/yjk13703623757/article/details/77918633/
if __name__ == '__main__':
    main()
    # save_html("1.html", "22")  # 测试保存文件