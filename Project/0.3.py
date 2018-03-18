# 0.3版本
# 简化代码
# .exe or .app
#等待测试
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
list = [3, 4, 5, 6, 7]
baojia = '0'


def handleLogin():
    # driver.set_window_size(1366, 768)
    driver.maximize_window()
    driver.get(url)
    # 获得cookie信息
    cookie1 = driver.get_cookies()
    # 将获得cookie的信息打印
    d = cookie1[0]['value']
    # print(d) 查看cookie

    elem = driver.find_element_by_xpath("//*[@id='userName']")
    elem.send_keys(username)
    elem = driver.find_element_by_xpath("//*[@id='wz']")
    elem.send_keys(password)
    # driver.find_element_by_xpath("//*[@id='wz']").send_keys(Keys.TAB)

    # 获取截图
    driver.get_screenshot_as_file('/Users/Jarvis/Desktop/screenshot.png')

    # 获取指定元素位置
    element = driver.find_element_by_xpath("//img[contains(@id, 'imgyzm')]")
    # element = driver.find_element_by_id('imgyzm')
    left = int(element.location['x'] + 620)
    top = int(element.location['y'] + 325)
    right = int(element.location['x'] + 720)
    bottom = int(element.location['y'] + 363)
    # print(left)
    # print(top)
    # print(right)
    # print(bottom)
    # 通过Image处理图像
    im = Image.open('/Users/Jarvis/Desktop/screenshot.png')

    im = im.crop((left, top, right, bottom))
    im.save('/Users/Jarvis/Desktop/vcode.png')
    image = Image.open('/Users/Jarvis/Desktop/vcode.png')
    vcode = pytesseract.image_to_string(image)
    # print(vcode)
    elem = driver.find_element_by_xpath("//*[@id='vcode']")
    elem.send_keys(vcode)

    elem = driver.find_element_by_xpath("//*[@type='image']")
    elem.click()







def pageChange():
    driver.switch_to_frame('menu')

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "menuTree_2_span")))
        elem = driver.find_element_by_id("menuTree_2_span")
        elem.click()
    finally:
        pass
    # 已进入投标总体页面
    driver.switch_to.default_content() #切出frame操作(不需要)

    driver.switch_to_frame('main')



def get_webservertime():
    while True:
        while True:
            # 返回一个对象
            response = urllib.request.urlopen('http://st.zzint.com/login.jsp')
            # 打印出远程服务器返回的header信息
            # print (response.info())
            header = response.info()
            ts = header._headers[1][1]
            # 将GMT时间转换成北京时间
            # ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
            ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
            ttime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)
            dat = "%u-%02u-%02u" % (ttime.tm_year, ttime.tm_mon, ttime.tm_mday)
            tm = "%02u:%02u:%02u" % (ttime.tm_hour, ttime.tm_min, ttime.tm_sec)
            # print(dat, tm) #查看刷新时间

            # 到达设定时间，结束内循环
            if ttime.tm_hour == 9 and ttime.tm_min == 0 and ttime.tm_sec == 0:
                break
        # 做正事，一天做一次
        execute()
        break

def execute():

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//form[@id='pur!queryBidList']/table[2]/tbody/tr[" + str(3) + "]/td[9]/a[2]")))

        for n in list:

            try:
                # 现在无法确定投标路径是否正确 等待验证
                WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, "//form[@id='pur!queryBidList']/table[2]/tbody/tr[" + str(n) + "]/td[9]/a[2]")))
                driver.find_element_by_xpath(
                    "//form[@id='pur!queryBidList']/table[2]/tbody/tr[" + str(n) + "]/td[9]/a[2]").click()

                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                        (By.XPATH, "//form[@id='pur!addBid']/table/tbody/tr[3]/td/input[1]")))

                    s = driver.find_elements_by_tag_name("input")
                    b = len(s)
                    print(b)

                    driver.find_element_by_xpath("//form[@id='pur!addBid']/table/tbody/tr[3]/td/input[1]").click()
                finally:
                    pass

                # 之后进入最终报价页面
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                    "//form[@id='pur!saveBid']/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[7]/input")))
                    # 自定义输入的值 '0'
                    driver.find_element_by_xpath(
                        "//form[@id='pur!saveBid']/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[7]/input").send_keys(
                        baojia)
                    # 获取相对静态验证码
                    yanzhengma = driver.find_element_by_xpath(
                        "//form[@id='pur!saveBid']/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/font").text
                    driver.find_element_by_xpath(
                        "//form[@id='pur!saveBid']/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[8]/input").send_keys(
                        yanzhengma)
                    # 点击提交
                    driver.find_element_by_xpath("//form[@id='pur!saveBid']/table/tbody/tr[3]/td/input").click()

                finally:
                    pass

                try:
                    WebDriverWait(driver, 10).until(EC.alert_is_present())
                    driver.switch_to.alert.accept()
                finally:
                    pass

            finally:
                pass

    finally:
        pass



if __name__== '__main__':
    handleLogin()
    pageChange()
    get_webservertime()



    # 问题1：系统载入时间的不同 只能让程序不停的尝试 已解决 用try

    # 问题2：进入详情界面识别关键字 之后实现优先级别 已解决 不需要

    # 问题3：目标是最快的选上 而不是自动化