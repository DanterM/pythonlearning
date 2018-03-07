# from selenium import webdriver
# import time
#
# browser=webdriver.Chrome()
# browser.maximize_window() # 窗口最大化
#
# browser.get('https://www.baidu.com') # 在当前浏览器中访问百度
#
# # 新开一个窗口，通过执行js来新开一个窗口
# js='window.open("https://www.sogou.com");'
# browser.execute_script(js)
# # time.sleep()
# print(browser.current_window_handle) # 输出当前窗口句柄（百度）
# handles = browser.window_handles # 获取当前窗口句柄集合（列表类型）
# print(handles) # 输出句柄集合
#
# for handle in handles:   # 切换窗口（切换到搜狗）
#     if handle != browser.current_window_handle:
#         print('switch to ',handle)
#         browser.switch_to_window(handle)
#         print(browser.current_window_handle) # 输出当前窗口句柄（搜狗）
#         break
#
#
# browser.close() #关闭当前窗口（搜狗）
# browser.switch_to_window(handles[0]) #切换回百度窗口
#
# time.sleep(10)
# browser.quit()




# 下列代码运行成功且不关闭标签页

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("setf").click()
handles = driver.window_handles
for handle in handles:
    if driver.current_window_handle != handle:
        driver.switch_to.window(handle)
driver.find_element_by_link_text("百度首页").click()