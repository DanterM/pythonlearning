from selenium import webdriver
  # 引入ActionChains 类*
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("http://yunpan.360.cn")


# 获取当前窗口句柄（主窗口）
handle = driver.current_window_handle

#****定位到要右击的元素**
right_click =driver.find_element_by_link_text("服务套餐")
right1_click =driver.find_element_by_link_text("帮助")

#****对定位到的元素执行鼠标右键操作
# ActionChains(driver).click(right_click).perform()
ActionChains(driver).key_down(Keys.COMMAND).click(right_click).perform()
sleep(1)
ActionChains(driver).key_down(Keys.COMMAND).click(right1_click).perform()

#成功打开新标签页 进展顺利


# 获取当前所有窗口句柄（主、服务套餐、帮助窗口）
handles = driver.window_handles

for newHandle in handles:
    if newHandle!=handle:
        # 切换到新打开的窗口B
        driver.switch_to_window(newHandle)
        sleep(2)
        driver

        # 在新打开的窗口B中操作   待使用
        # driver.find_element_by_id('xx').click()

        # 关闭当前窗口B  待使用
        # driver.close()

        # 切换回窗口A
        # driver.switch_to_window(handles[0])