nums = [2, 7, 11, 15]
target = 9
# for循环
n = 0
m = 0
for i in nums:
    for j in nums:
        a = i + j
        if a == target:
            print("找到了")
        else:
            pass
        m += 1
    n += 1
    print(n,m)
    