from selenium import webdriver
from time import sleep
# 使用selenium爬取虎牙直播中lol直播模块的主播名和观看人数

driver = webdriver.Chrome()
url = 'https://www.huya.com/g/lol'
driver.get(url)
num = 1
while True:
    print('第' + str(num) + "页----------------------------------------------")
    num += 1
    sleep(5) # 防止页面没有加载出来，就获取页面
    html = driver.page_source
    names = driver.find_elements_by_xpath('//i[@class="nick"]')
    counts = driver.find_elements_by_xpath('//i[@class="js-num"]')
   #driver.find_element_by_xpath('//a[@class="laypage_nasda"]').click()
    for name, count in zip(names, counts):
        print(name.text, ":", count.text)
    if driver.page_source.find('laypage_next') != -1:
        driver.find_element_by_xpath('//a[@class="laypage_next"]').click()
    else:
        break
driver.quit()
