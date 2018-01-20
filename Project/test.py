import math


def quadratic(a, b, c):
    for i in (a, b, c):
        if not isinstance(i, (float, int)):
            raise TypeError('pls enter your number')
            continue
        d = b*b-4*a*c
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        x3 = ('faild')
        if d>=0 :
            return x1,x2
        else:
            return x3



        # 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')