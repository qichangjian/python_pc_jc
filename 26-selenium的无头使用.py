from selenium import webdriver

# 实现自己输入搜索内容，然后自动点击

'''
什么是无头浏览器
现在许多网站有反爬虫功能。我们要做的就是尽量把我们的请求伪装成是真正的浏览器发出的一样。
最好就直接用浏览器来发送请求，比如使用WebDriver驱动浏览器模拟真人操作。
但是这样速度太慢，再说服务器的linux一般都是server版的，根本没有桌面，因此也没有浏览器可用。
所以我们就使用无头(headless)浏览器。功能跟真的浏览器一样，速度更快，只不过没有界面罢了。
'''
# chrome59版本以后可以变成无头的浏览器，加以下参数
options = webdriver.ChromeOptions()
options.add_argument('--headless')
chrome = webdriver.Chrome(chrome_options=options)

chrome = webdriver.Chrome()
chrome.get('https://cn.bing.com/')
# 搜索栏中输入了python
chrome.find_element_by_id('sb_form_q').send_keys('python')
# 点击搜索
chrome.find_element_by_id('sb_form_go').click()

html = chrome.page_source
print(html)
#chrome.quit()