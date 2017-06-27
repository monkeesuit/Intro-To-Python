def fib(n):
    
    # Base case:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case:
    else:
        return fib(n-1) + fib(n-2)

def fib_seq(n):
    for i in range(n):
        if i == n-1:
            print(fib(i))
        else:
            print(fib(i), end =', ')

def main():
    n = int(input('Enter A Number: '))
    fib_seq(n)

main()
