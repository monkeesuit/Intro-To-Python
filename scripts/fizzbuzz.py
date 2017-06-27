
# Loop through integers: 1, 2, 3,...,100
for i in range(1, 101):

	# Test Divisibility of i by 3
	if (i % 3 == 0):
		print('Fizz', end = '')			# Suppress the newline w/ end = ''

	# Test Divisibility of i by 5
	if (i % 5 == 0):
		print('Buzz', end = '')

	# Test if i is NOT Divisible by both 3 and 5
	if (i % 3 != 0) and (i % 5 != 0):
		print(i, end = '')

	print()								# Newline
