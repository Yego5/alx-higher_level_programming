import random
number = random.randint(-10000, 10000)
if number >= 0:
	l_digit = number % 10
else:
	l_digit = ((number * -1) % 10) * -1
msg = "Last digit of %d is %d and is" % (number, l_digit)
if l_digit == 0:
	print(msg, "0")
elif l_digit > 5:
	print(msg, "greater than 5")
else:
	print(msg, "less than 6 and not 0")
