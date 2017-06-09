#4.7 Override 3.3

def computegrade(score):

    print("分数在0.0-1.0之间！")
    # score = float(input("输入你的分数："))

    if score >= 0.9 and score <= 1:
        Grade = "A"
        print("你的成绩是：" + str(score))
        print("你的等级是" + Grade)
    elif score >= 0.8 and score < 0.9:
        Grade = "B"
        print("你的成绩是：" + str(score))
        print("你的等级是" + Grade)
    elif score >= 0.7 and score < 0.8:
        Grade = "C"
        print("你的成绩是：" + str(score))
        print("你的等级是" + Grade)
    elif score >= 0.6 and score < 0.7:
        Grade = "D"
        print("你的成绩是：" + str(score))
        print("你的等级是" + Grade)
    elif score >= 0 and score < 0.6:
        Grade = "F"
        print("你的成绩是：" + str(score))
        print("你的等级是",Grade)
    else:
        print("输入错误！")

print(min(1,2,3))
computegrade(0.5)