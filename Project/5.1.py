#编写一个程序，重复读取数据，直到用户输入“done”。一旦输入“done”，打印总和、个数与平均值。
# 如果用户输入的不是数字，使用try和except捕获异常，打印错误信息，然后跳过继续执行循环。

sum = 0
time = 0
while True:
    try:
        x = input("输入数字：")
        if x == "done":
            break

        sum = sum + int(x)

        time = time +1
    except:
        print("输入有误！")

print("总和为：",sum)
print("个数为",time)
print("平均值为：",sum/time)

