import urllib.request
import time
import datetime


def get_webservertime():
    # # 返回一个对象
    # response = urllib.request.urlopen('http://st.zzint.com/login.jsp')
    # # 打印出远程服务器返回的header信息
    # # print (response.info())
    # header = response.info()
    # ts = header._headers[1][1]
    #
    # # 将GMT时间转换成北京时间
    # # ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    # ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    # ttime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)
    # dat = "%u-%02u-%02u" % (ttime.tm_year, ttime.tm_mon, ttime.tm_mday)
    # tm = "%02u:%02u:%02u" % (ttime.tm_hour, ttime.tm_min, ttime.tm_sec)
    # print(dat, tm)
    # print(ttime.tm_hour)
    # print(ttime.tm_min)
    # print(ttime.tm_sec)

    while True:
        # 判断是否达到设定时间，例如0:00
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
            print(dat, tm)
            # 到达设定时间，结束内循环
            if ttime.tm_hour == 11 and ttime.tm_min == 8 and ttime.tm_sec ==30:
                print("待break")
                break
        # 做正事，一天做一次
        print("成功")
        break





get_webservertime()
# print('京东时间：')
# get_webservertime('https://www.jd.com/')
# print('采购网时间：')
# get_webservertime('http://st.zzint.com/login.jsp')


# now = datetime.datetime.now()
# currentTime = str(now.hour)+":"+str(now.minute)+":"+str(now.second)
# print(currentTime)
# currentHour = str(now.hour)
# currentMinute = str(now.minute)
# currentSecond = str(now.second)
#
# print(currentHour)
# print(currentMinute)
# print(currentSecond)


# 时间距 判断成功
# if int(currentHour)==9 and int(currentSecond)>=1:
#     # 立即运行程序
#     print("已运行程序")
# elif int(currentHour) <= 9 :
#     waitTime = 1+(60 - int(currentSecond)) + (59 - int(currentMinute)) * 60
#     print("距服务器开启还需等待"+str(waitTime)+"秒")
#     time.sleep(waitTime)
#     print("已运行程序")




# 先获取到服务器开放剩余时间   加time.sleep等待后运行即可  XXXXXXXX


# def getTime():
#     response = urllib.request.urlopen()
#     header = response.info()
#     ts = header._headers[1][1]
#     ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
#     ttime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)
#     dat = "%u-%02u-%02u" % (ttime.tm_year, ttime.tm_mon, ttime.tm_mday)
#     tm = "%02u:%02u:%02u" % (ttime.tm_hour, ttime.tm_min, ttime.tm_sec)
#     print(dat, tm)
#
#
# def getWaitTime():
#     print('京东时间：')
#     get_webservertime('https://www.jd.com/')
#     print('采购网时间：')
#     get_webservertime('http://st.zzint.com/login.jsp')
#     now = datetime.datetime.now()
#     currentTime = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
#     print(currentTime)
#     currentHour = str(now.hour)
#     currentMinute = str(now.minute)
#     currentSecond = str(now.second)
#
#
#     print(currentHour)
#     print(currentMinute)
#     print(currentSecond)