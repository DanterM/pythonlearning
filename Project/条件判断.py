# 计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。
#
# 比如，输入用户年龄，根据年龄打印不同的内容，在Python程序中，用if语句实现：

age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

#根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。

# 也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了：

age = 3
if age >= 18:
    print('Your age is', age)
    print('Adult')
else:
    print('Your age is', age)
    print('Teenager')

# 注意不要少写了冒号:

# 当然上面的判断是很粗略的，完全可以用elif做更细致的判断：

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# elif是else
# if的缩写，完全可以有多个elif，所以if语句的完整形式就是：

# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>


# if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else，
# 所以，请测试并解释为什么下面的程序打印的是teenager：
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')


# if判断条件还可以简写，比如写：
x=123
if x:
    print('True')
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。


# 最后看一个有问题的条件判断。很多同学会用input()读取用户的输入，这样可以自己输入，程序运行得更有意思：
age = input('age:')
age=int(age)
if age>=18:
    print('你成年了')
else:print('呵呵')

# 这是因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')




# 练习
#
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：

height = 1.75
weight = 80.5

bmi = weight/(height*height)
if bmi<18.5:
    print('过轻')
elif bmi<25:
    print('正常')
elif bmi<28:
    print('过重')
elif bmi<32:
    print('肥胖')
elif bmi>32:
    print('严重肥胖')
print(bmi)




# 综合运用
while True:
    try:
        weights = input('请输入你的体重（千克）):' )
        weight = float(weights)
        if 0<weight<300:
            break
        print('你在逗我么，难道你不在地球上\n')
    except ValueError:
        print('我又不知道你是谁，干嘛用外星文写你体重\n')

while True:
    try:
        heights = input('\n请输入你的身高（米）:' )
        height = float(heights)
        if 0.5<height<3:
            break
        print('请不要调戏我，虚报身高是没用的\n')
    except ValueError:
        print('如果您不认真输入，电脑将启动自爆程序.....\n')

BMI = weight/height/height

if BMI > 32:
    print ('\n你的BMI指数为 %.1f ' %(BMI))
    print ('你没救了')
    input("\n测试结束，按任意键退出")
elif BMI >28:
    print ('\n你的BMI指数为 %.1f ' %(BMI))
    print ('你个猪 -。-！')
    input("\n测试结束，按任意键退出")
elif BMI >25:
    print ('\n你的BMI指数为 %.1f ' %(BMI))
    print ('你他喵的吃的太多了 =。=')
    input("\n测试结束，按任意键退出")
elif BMI >18.5:
    print ('\n你的BMI指数为 %.1f ' %(BMI))
    print ('好孩子，继续保持')
    input("\n测试结束，按任意键退出")
else :
    print ('\n你的BMI指数为 %.1f ' %(BMI))
    print ('你把粮食都浪费到哪了，来来来都给我吧')
    input("\n测试结束，按任意键退出")