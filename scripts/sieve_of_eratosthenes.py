
# N - We will find all primes less than N
N = 100

# Create three empty lists
# - One to collect primes
# - One to collect the numbers we haven't checked yet
# - One to collect the composites
primes = []
numbers = []
composites = []

# Initialize the numbers list
for i in range(2,N+1):
    numbers.append(i)

# Loop while there are unchecked numbers
while len(numbers) > 0:

    # The first number in the numbers list is prime
    primes.append(numbers[0])

    # Any multiple of that first number is a composite
    for i in range(numbers[0],N+1,numbers[0]):
        composites.append(i)

    # Use sets to remove the composites
    numbers = list(set(numbers)-set(composites))

    # Sets are unorderd, so numbers must be put back in order
    numbers.sort()

# Print the prime list
print(primes)
