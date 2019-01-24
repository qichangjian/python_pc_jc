from selenium import webdriver

chrome = webdriver.Chrome()
chrome.get('http://www.baidu.com')

# 得到渲染后的页面
html = chrome.page_source
print(html)

# 保存图片:很慢才传回来
chrome.save_screenshot('zbios_efde696.png')

# 退出浏览器
# chrome.quit()