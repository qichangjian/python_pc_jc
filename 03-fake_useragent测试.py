from fake_useragent import UserAgent

# 测试网上写的动态UA模块(需要先pip)

ua = UserAgent()
print(ua.chrome)
print(ua.firefox)
print(ua.ie)