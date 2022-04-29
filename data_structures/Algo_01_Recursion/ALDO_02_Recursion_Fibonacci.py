# Given a number N return the index value of the Fibonacci sequence, where the sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

# For example: fibonacciRecursive(6) should return 8

def fibonacciIterative(n):
    a = 0
    b = 1
    sum = a + b
    while n >= 2:
        n -= 1
        sum = a + b
        a = b
        b = sum

    return sum


def fibonacciIterative_better(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


def fibonacciRecursive(n):
    if n < 2:
        return n
    # print(n)
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)
    # Fibonacci is the sum of the previous 2 numbers


# print(fibonacciIterative(6))
print(fibonacciIterative_better(20))  # O(n)
print(fibonacciRecursive(35))  # O(2^n) --> Exponential Time
