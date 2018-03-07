# 如何判断有几个投标？
# 将0版本更改成测试版本
# 判断服务器时间

from selenium import webdriver
import pytesseract
import os
import time
from PIL import Image
from time import sleep
from selenium.webdriver.common.keys import Keys
import selenium
from selenium.webdriver.support.wait import WebDriverWait
import urllib.request
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import datetime


def handleLogin():
    # 定义自己的用户名密码
    driver = webdriver.Chrome()
    username = "山东信和诚建设项目管理有限公司"
    password = "000333"
    # 执行操作的页面地址
    url = 'http://st.zzint.com/login.jsp'
    # driver.set_window_size(1366, 768)
    driver.maximize_window()
    driver.get(url)
    # 目前还没学会cookie怎么用先获取到吧肯定用的到
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
    left = int(element.location['x'] +620)
    top = int(element.location['y'] +325 )
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

    # elem = ActionChains(driver).key_down(Keys.COMMAND).click(driver.find_element_by_link_text("查询"))

    # for handle in driver.window_handles:
    #     driver.switch_to_window(handle)



    # # 非循环查询：
    # try:
    #     WebDriverWait(driver,100).until(EC.presence_of_element_located((By.LINK_TEXT,"投标")))
    #     driver.find_element_by_link_text("投标").click()
    #
    # finally:
    #     pass
    #
    # try:
    #     WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//form[@id='pur!addBid']/table/tbody/tr[3]/td/input[1]")))
    #     driver.find_element_by_xpath("//form[@id='pur!addBid']/table/tbody/tr[3]/td/input[1]").click()
    # finally:
    #     pass
    #
    #
    # #之后进入最终报价页面
    # try:
    #     WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//form[@id='pur!saveBid']/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[7]/input")))
    #     # 自定义输入的值 '0'
    #     driver.find_element_by_xpath("//form[@id='pur!saveBid']/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[7]/input").send_keys('1')
    #
    #     #获取相对静态验证码
    #     yanzhengma = driver.find_element_by_xpath("//form[@id='pur!saveBid']/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/font").text
    #     driver.find_element_by_xpath("//form[@id='pur!saveBid']/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[8]/input").send_keys(yanzhengma)
    #     #点击提交
    #     driver.find_element_by_xpath("//form[@id='pur!saveBid']/table/tbody/tr[3]/td/input").click()
    # finally:
    #     pass



    now = datetime.datetime.now()
    currentTime = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    print(currentTime)
    currentHour = str(now.hour)
    currentMinute = str(now.minute)
    currentSecond = str(now.second)

    if int(currentHour) == 00 and int(currentSecond) >= 11:
        # 立即运行程序
        print("已运行程序")
    elif int(currentHour) == 00 and int(currentSecond) < 11:
        waitTime = 11 - int(currentSecond)
        print(waitTime)
        time.sleep(waitTime)
    elif int(currentHour) == 23:
        # 23：59：20  51s
        waitTime = 11 + (60 - int(currentSecond)) + (59 - int(currentMinute)) * 60
        print("距服务器开启还需等待" + str(waitTime) + "秒")
        time.sleep(waitTime)
        print("已运行程序")




    # 如何判断有几个投标？
    list = [3,4,5,6,7,8] # 假定有5个工程
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//form[@id='pur!queryBidList']/table[2]/tbody/tr[" + str(3) + "]/td[9]/a[2]")))
        for n in list:

            try:
                # 现在无法确定投标路径是否正确 等待验证
                WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, "//form[@id='pur!queryBidList']/table[2]/tbody/tr[" + str(n) + "]/td[9]/a[2]")))
                driver.find_element_by_xpath("//form[@id='pur!queryBidList']/table[2]/tbody/tr[" + str(n) + "]/td[9]/a[2]").click()
                # print(driver.find_element_by_xpath("//form[@id='pur!queryBidList']/table[2]/tbody/tr[" + str(n) + "]/td[9]/a[2]"))

                try:
                    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//form[@id='pur!addBid']/table/tbody/tr[3]/td/input[1]")))

                    s = driver.find_elements_by_tag_name("input")
                    # elements = driver.find_element_by_link_text("详情")
                    b = len(s)
                    print(b)

                    driver.find_element_by_xpath("//form[@id='pur!addBid']/table/tbody/tr[3]/td/input[1]").click()
                finally:
                    pass

                # 之后进入最终报价页面
                try:
                    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//form[@id='pur!saveBid']/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[7]/input")))
                    # 自定义输入的值 '0'
                    driver.find_element_by_xpath("//form[@id='pur!saveBid']/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[7]/input").send_keys('0')
                    # 获取相对静态验证码
                    yanzhengma = driver.find_element_by_xpath("//form[@id='pur!saveBid']/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/font").text
                    driver.find_element_by_xpath("//form[@id='pur!saveBid']/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[8]/input").send_keys(yanzhengma)
                    # 点击提交
                    driver.find_element_by_xpath("//form[@id='pur!saveBid']/table/tbody/tr[3]/td/input").click()

                finally:
                    pass

                # 提交过后返回主界面？

                try:
                    # WebDriverWait(driver,10).until(EC.alert_is_present(("保存成功！")))
                    time.sleep(1)
                    if EC.alert_is_present:

                        print("Alert exists")

                        alert = driver.switch_to_alert()

                        print(alert.text)

                        alert.accept()

                        print("Alert accepted")

                    else:

                        print("NO alert exists")
                finally:
                    pass

            finally:
                pass

    finally:
        pass

    sleep(3)









if __name__== '__main__':
    handleLogin()





    # 问题1：系统载入时间的不同 只能让程序不停的尝试 已解决 用try

    # 问题2：进入详情界面识别关键字 之后实现优先级别 已解决 不需要

    # 问题3：目标是最快的选上 而不是自动化