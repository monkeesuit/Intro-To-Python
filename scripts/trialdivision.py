

num = int(input('Enter a numer to be check for primality: '))
ceiling = int(pow(num, .5)) + 1										# Get ceiling of sqaure root of number (b/c of how range works 

for i in range(2, ceiling):
	if (num % i == 0):												# if any number between 2 and ceiling-1 divides num
		print('{} is composite'.format(num))						# then num is a composite unmber
		break
else:																# if we make it through the loop then the number is prime
	print('{} is prime'.format(num))
