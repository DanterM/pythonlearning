#4.6 : Override3.1

def computepay(hours,rate):
	if hours <= 40 and hours > 0:
		earn = hours * rate
		print("You have " + str(earn) + " dollars")
	elif hours > 40:
		earn = (hours - 40) * 1.5 * rate + 40 * rate
		print("You have " + str(earn) + " dollars")
	elif hours < 0:
		print("You should input right number!")

computepay(45,10)