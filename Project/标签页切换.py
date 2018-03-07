#标签页切换

from selenium import webdriver


browser=webdriver.Chrome()

browser.get('http://www.baidu.com')

# 获取当前窗口句柄（窗口A）

handle = browser.current_window_handle

# 打开一个新的窗口

browser.find_element_by_link_text('新闻').click()

# 获取当前所有窗口句柄（窗口A、B）

handles = browser.window_handles

# 对窗口进行遍历

for newhandle in handles:

    # 筛选新打开的窗口B

    if newhandle!=handle: # 切换到新打开的窗口B
        browser.switch_to_window(newhandle)

    # 在新打开的窗口B中操作
        browser.find_element_by_id('xx').click()
    # 关闭当前窗口B
        browser.close()
    #切换回窗口A
        browser.switch_to_window(handles[0])