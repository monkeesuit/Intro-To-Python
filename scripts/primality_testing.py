



# Take some input, convert it to an int
num = int(input('[prime?]>>>  '))

# Loop from 2 to the squareroot of the input
for i in range(2, int(num**.5)+1):

    # If any of these numbers divide the input
    # then it is composite and we are done
    if num % i == 0:
        print('Composite')
        quit()

# If we make it through those numbers
# and haven't found a factor
# then the input is prime
print('Prime')
