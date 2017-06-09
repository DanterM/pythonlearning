enterHours = int(input('Please Input Your Work Hours:'))
# enterHours = 20
enterRate = 10
try:
    if enterHours <= 40 and enterHours > 0:
        earn = enterHours * enterRate
        print("You have " + str(earn) + " dollars")
    elif enterHours > 40:
        earn = (enterHours - 40) * 1.5 * enterRate + 40 * enterRate
        print("You have " + str(earn) + " dollars")
    elif enterHours < 0:
        print("You should input right number!")
except:
    print("Error, please enternumeric input!")
