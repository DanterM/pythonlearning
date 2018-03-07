# from selenium import webdriver
# url = "http://st.zzint.com/login.action"
# # picName = url.replace(".html",".jpg")
# brower = webdriver.PhantomJS("/Users/Jarvis/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs")
# brower.get(url)
# brower.maximize_window()
# brower.save_screenshot("/Users/Jarvis/Desktop/a.png")
# brower.close()






from selenium import webdriver
import time
from PIL import Image
# 打开验证码界面
driver = webdriver.Chrome
url = "http://weixin.sogou.com/antispider/?from=%2fweixinwap%3Fpage%3d2%26_rtype%3djson%26ie%3dutf8%26type%3d2%26query%3d%E6%91%A9%E6%8B%9C%E5%8D%95%E8%BD%A6%26pg%3dwebSearchList%26_sug_%3dn%26_sug_type_%3d%26"
driver.set_window_size(width=1200, height=800, windowHandle='current')
cookies = driver.get_cookies()

# 处理cookies
driver.get(url)
for k, v in cookies.iteritems():
    cookie_dict = {'name': k, 'value': v}
    driver.add_cookie(cookie_dict)
driver.get(url)

# 获取截图
driver.get_screenshot_as_file('CrawlResult/screenshot.png')

# 获取指定元素位置
element = driver.find_element_by_id('seccodeImage')
left = int(element.location['x'])
top = int(element.location['y'])
right = int(element.location['x'] + element.size['width'])
bottom = int(element.location['y'] + element.size['height'])

# 通过Image处理图像
im = Image.open('CrawlResult/screenshot.png')
im = im.crop((left, top, right, bottom))
im.save('CrawlResult/code.png')