from selenium import webdriver
import time

base_url = "http://www.hao123.com"
driver = webdriver.Chrome()
driver.get(base_url)
s = driver.find_elements_by_tag_name("a")
for i in s:
    print(i.get_attribute("href"))