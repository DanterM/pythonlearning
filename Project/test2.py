a= 'Hi, %s, you have $%d.' % ('Michael', 1000000)
print(a)

b = 'Hello,%s，%d'%('asdf',20)
print(b)


s1 = 72
s2 = 85
r = (s2-s1)/s2*100
# print(r)
print('分数提升%d%%'%r)

c=['a','b','c']
print(len(c))
print(c[0])
print(c[1])
print(c[2])
print(c[-1])
print(len(c)-1)


age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')


wangzhen = 23
if wangzhen >= 23:
    print('王震',wangzhen,'岁')


d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
print(d.get('Tracy'))

s = set([1,2,3,1,2])
s.add(4)
s.remove(3)
print(s)


s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

abc = ['1','2','3','7','0']
abc.sort()
print(abc)

cd = 'abc'
print(cd.replace('a','A'))
print(cd)

def muilt(x):
    return x*x

print(muilt(2))


# a的b次方
def leicheng(a,b):
    c=1
    while b > 0:
        b -= 1
        c = c*a
    return c
print(leicheng(2,2))
print(leicheng(2,4))


# 0+？
def leijia(a):
    c = 0
    for x in list(range(a)):
        c = x + c
    return c
print(leijia(5))


# 阶乘
def jiecheng(n):
    if n==1:
        return 1
    return n*jiecheng(n-1)
print(jiecheng(4))

# 1+3+5+...+99
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n+2
print(L)



L = []
L = list(range(100))
print(L)
print(L[10:100])
print(L[-1:])
print(L[::2])
print((1,2,3,4)[::2])


d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k,v)



# import requests
# import urllib
# from urllib import urlopen
# # html = requests.get("http://st.zzint.com/pur!queryBidList.action")
# # print(html.text)
#
#
#
# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html
#
# url = "http://www.zjgdpf.org.cn"
# html = getHtml(url)
# print(html)


# import urlopen
# doc = urlopen("http://www.baidu.com").read()
# print(doc)


import urllib.request
request=urllib.request.Request('http://danterm.me')
response=urllib.request.urlopen(request)
html=response.read()
print(html)