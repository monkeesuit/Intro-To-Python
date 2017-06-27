

num = int(input('Enter a numer to be check for primality: '))
ceiling = round(pow(num, .5)) + 1

for i in range(2, ceiling):
	if (num % i == 0):
		print('{} is composite'.format(num))
		break
else:
		print('{} is prime'.format(num))
