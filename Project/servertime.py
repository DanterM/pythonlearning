import urllib.request
import time
import datetime

def get_webservertime(url):
    # 返回一个对象
    response = urllib.request.urlopen(url)
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
    print(dat, tm)

print('京东时间：')
get_webservertime('https://www.jd.com/')
print('采购网时间：')
get_webservertime('http://st.zzint.com/login.jsp')


now = datetime.datetime.now()
currentTime = str(now.hour)+":"+str(now.minute)+":"+str(now.second)
print(currentTime)
currentHour = str(now.hour)
currentMinute = str(now.minute)
currentSecond = str(now.second)

print(currentHour)
print(currentMinute)
print(currentSecond)


# 时间距 判断成功
# if int(currentHour)==9 and int(currentSecond)>=1:
#     # 立即运行程序
#     print("已运行程序")
# elif int(currentHour) <= 9 :
#     waitTime = 1+(60 - int(currentSecond)) + (59 - int(currentMinute)) * 60
#     print("距服务器开启还需等待"+str(waitTime)+"秒")
#     time.sleep(waitTime)
#     print("已运行程序")




# 先获取到服务器开放剩余时间   加time.sleep等待后运行即可


if int(currentHour)==9 :
    # 立即运行程序
    print("已运行程序")
elif int(currentHour) < 9 :
    waitTime = (8-currentHour)*3600 + (60 - int(currentSecond)) + (59 - int(currentMinute)) * 60
    print("距服务器开启还需等待"+str(waitTime)+"秒")
    time.sleep(waitTime)
    print("已运行程序")


def getTime():
    response = urllib.request.urlopen()
    header = response.info()
    ts = header._headers[1][1]
    ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    ttime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)
    dat = "%u-%02u-%02u" % (ttime.tm_year, ttime.tm_mon, ttime.tm_mday)
    tm = "%02u:%02u:%02u" % (ttime.tm_hour, ttime.tm_min, ttime.tm_sec)
    print(dat, tm)


def getWaitTime():
    print('京东时间：')
    get_webservertime('https://www.jd.com/')
    print('采购网时间：')
    get_webservertime('http://st.zzint.com/login.jsp')
    now = datetime.datetime.now()
    currentTime = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    print(currentTime)
    currentHour = str(now.hour)
    currentMinute = str(now.minute)
    currentSecond = str(now.second)


    print(currentHour)
    print(currentMinute)
    print(currentSecond)