import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(6)
driver.get("https://www.baidu.com")
driver.execute_script("window.alert('这是一个测试Alert弹窗');")
try:
    WebDriverWait(driver,10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
finally:
    pass
  # 点击弹出里面的确定按钮