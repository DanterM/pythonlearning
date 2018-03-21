import time
import urllib.request



while True:
    while True:
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
        print(dat, tm) #查看刷新时间

        # 到达设定时间，结束内循环
        # 在8：59：45秒的时候点开页面能得到最新的页面
        if ttime.tm_hour >= 9 and ttime.tm_min >= 0 and ttime.tm_sec >= 0:
            break
    print("Success!")
    break