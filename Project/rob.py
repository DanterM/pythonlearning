from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import selenium
from selenium import webdriver
# 目标1：模拟浏览器登录后获取源码（已解决）
Cookie = "JSESSIONID=F0122D5D4D457A4C1E8EA2D17F8ED84C"

url = "http://st.zzint.com/pur!queryBidList.action"

headers = {
    'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Cookie': Cookie,
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
    'Host': 'st.zzint.com',
    'Referer': 'http://www.sse.com.cn/assortment/stock/list/share/' #可省略
}

req = urllib.request.Request(url,None,headers)
response = urllib.request.urlopen(req)
the_page = response.read()

# print(the_page.decode("utf8")) #测试是否能正常获取.action网页的源代码
# 获取http://st.zzint.com/pur!queryBidList.action网页源码成功
# 目标1 结束






# 目标2：获取到所需投标链接（已解决）
# 列出所有pur!queryRemark.action?packageId=????的链接

soup = BeautifulSoup(the_page,"html5lib")

# 尝试搜索含有'报价'字段的链接（成功，可以加入检索条件↓↓↓↓↓↓↓↓↓↓）
# b = soup.find(text="投标")
# print(b)

# 获取所有a标签中href的链接
# 获取带有"报价"字段的链接
for link in soup.find_all(name='a',text="投标"):
    # abc = link.get('href')

    abc = 'http://st.zzint.com/'+link.get('href')
    # print(abc)
    req1 = urllib.request.Request(abc,None,headers)
    response1 = urllib.request.urlopen(req1)
    the_page1 = response1.read()
    print(the_page1)

    # selenium点击报价事件
    driver = webdriver.Chrome()
    driver.get(abc)
    # element = driver.find_element_by_xpath("//input[@value='报价']")
    element = driver.find_element_by_link_text("报价")

# 目标2.1：增加嵌套循环？找到与运行当天时间对应的链接（已解决，原因：找到相应字段对应的链接后就能直接得到想要的链接地址）

# 目标2.2：测试投标链接是否能正常打开
# 目标2.3：（如果未到系统开放时间，则忽略浏览器提示信息，继续刷新，直到进入正确的页面）


# driver.refresh()
#****刷新当前页面**

# 目标3：同时成功打开n个正确的报价链接
# url1 = link.get('href')
# req1 = urllib.request.Request(url,None,headers)
# response1 = urllib.request.urlopen(req)
# the_page1 = response.read()

# 目标4：模拟浏览器操作点开报价链接并进入最终报价页面


# 目标5：模拟浏览器输入报价和验证码，之后自动点击报价-------报价成功


# 补充目标6：自动登录？（cookie+动态验证码图像识别（屏幕截图））