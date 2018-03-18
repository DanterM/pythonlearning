import time
import datetime
import httplib2

t = time.time()

print (t)                       #原始时间数据
print (int(t))                  #秒级时间戳
print (int(round(t * 1000)))    #毫秒级时间戳

nowTime = lambda:int(round(t * 1000))
print (nowTime());              #毫秒级时间戳，基于lambda

print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   #日期格式化





def GetCnblogsServerTime():
    """获取cnblogs服务器时间
    GetCnblogsServerTime() -> list

    NOTE: 原理是通过服务器头文件响应获取服务器时间
    """
    conn = httplib2.HTTPConnectionWithTimeout( 'http://st.zzint.com/login.jsp' )
    conn.request( 'GET', '/' )
    response = conn.getresponse()
    ts =  response.getheader('date')
    ltime = time.strptime( ts[5:25], '%d %b %Y %H:%M:%S' )         #按照特定时间格式将字符串转换为时间类型
    serverTime =  time.strftime( '%H:%M:%S',time.localtime(time.mktime(ltime)+ 8*3600 )).split(':')    #将GMT时间转换为北京时间并以列表形式返回, -> [ hour, minute, second ]
    print(serverTime)
    return serverTime


GetCnblogsServerTime()