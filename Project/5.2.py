#编写一个程序，提示用户输入一组数字，输出最大值和最小值，不要求平均值。


print("输入一组数字，数字间用逗号隔开")
max = 0
min = 0
while True:
    try:
        x = input("输入数字:")
        if x=="done":
           break
        if max <= int(x):
            max = int(x)
        if min >= int(x):
          min = int(x)
    except:
        print("输入错误，请重新输入")
print("最大值为：",max)
print("最小值为：",min)

