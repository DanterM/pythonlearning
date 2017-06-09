# 3.1

enterHours = input('Please Input Your Work Hours:')
enterHours = int(enterHours)
enterRate = 10
enterHours = 45

if enterHours <= 40 and enterHours>0:
	earn = enterHours*enterRate
	print ("You have "+str(earn)+" dollars")
elif enterHours > 40:
	earn = (enterHours-40)*1.5*enterRate + 40*enterRate
	print ("You have "+str(earn)+" dollars")
elif enterHours <0:
	print("You should input right number!")