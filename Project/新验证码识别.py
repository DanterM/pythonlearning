from selenium import webdriver
import pytesseract
import time
from PIL import Image
import urllib.request
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
# 定义自己的用户名密码
username = "山东信和诚建设项目管理有限公司"
password = "000333"
# 执行操作的页面地址
url = 'http://st.zzint.com/login.jsp'


def handleLogin():
    # driver.set_window_size(1366, 768)
    driver.maximize_window()
    driver.get(url)

    # 获取截图
    driver.get_screenshot_as_file('/Users/Jarvis/Desktop/Jarvis/screenshot.png')

    # 获取指定元素位置
    element = driver.find_element_by_xpath("//img[contains(@id, 'imgyzm')]")
    left = int(element.location['x'] + 630)
    top = int(element.location['y'] + 325)
    right = int(element.location['x'] + 760)
    bottom = int(element.location['y'] + 362)
    # 通过Image处理图像
    im = Image.open('/Users/Jarvis/Desktop/Jarvis/screenshot.png')
    im = im.crop((left, top, right, bottom))
    im.save('/Users/Jarvis/Desktop/Jarvis/vcode.png')
    image = Image.open('/Users/Jarvis/Desktop/Jarvis/vcode.png')
    vcode = pytesseract.image_to_string(image)
    print(vcode)


handleLogin()