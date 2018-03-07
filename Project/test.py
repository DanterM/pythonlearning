import pytesseract
import os
import sys,time
from PIL import Image
from selenium import webdriver
import urllib.request
import webbrowser

PostUrl = "http://st.zzint.com"

# driver=webdriver.Chrome
# driver.get(PostUrl)
#
#
#
# driver.get_screenshot_as_file('/Users/Jarvis/Desktop/image1.jpg')  # 比较好理解
# im = Image.open('/Users/Jarvis/Desktop/image1.jpg')
# box = (516, 417, 564, 437)  # 设置要裁剪的区域
# region = im.crop(box)  # 此时，region是一个新的图像对象。
# # region.show()#显示的话就会被占用，所以要注释掉
# region.save("/Users/Jarvis/Desktop/image_code.jpg")


# webbrowser.open_new("http://st.zzint.com")
# im_url = 'http://st.zzint.com/vcode.action'
# im_data = urllib.request.urlopen(im_url).read()
# f=open('/Users/Jarvis/Desktop/vcode.png','wb')
# f.write(im_data)
# f.close()


image = Image.open('/Users/Jarvis/Desktop/vcode.png')

vcode = pytesseract.image_to_string(image)

print(vcode)