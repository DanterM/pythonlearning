import math

s = math.pi
print(s)

# 调用函数
# Python内置了很多有用的函数，我们可以直接调用。
# 要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。可以直接从Python的官方网站查看文档：

# 调用abs函数：
a = abs(-100)
print(a)

# 调用函数的时候，如果传入的参数数量不对，会报TypeError的错误，并且Python会明确地告诉你：abs()有且仅有1个参数，但给出了两个
# 如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误，并且给出错误信息：str是错误的参数类型

# 而max函数max()可以接收任意多个参数，并返回最大的那个：
b = max(1,2,3,4,5,7,10)
print(b)





# 数据类型转换
# 
# Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：
a = int('123')
print(a)

a = int('12.34')
print(a)

a = float('12.34')
print(a)

a = str(1.23)
print(a)

a = str(100)
print(a)

a = bool(1)
print(a)

a = bool('')
print(a)

