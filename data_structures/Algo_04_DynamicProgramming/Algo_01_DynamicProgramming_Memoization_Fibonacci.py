from functools import lru_cache

def fibonacciIterative_better(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

# @lru_cache(maxsize=1000)
def fibonacciRecursive(n):
    if n < 2:
        return n
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)


print('Without Memoization')
# TIME Complexity --> O(2^n)
print(fibonacciRecursive(30))
print(fibonacciRecursive(30))
# print(fibonacciRecursive.cache_info())


def memoizedFibonacciClosure():
    cache = {}

    def memoizedFibonacci(n):
        if n in cache:
            return cache[n]
        else:
            print('Long time')
            cache[n] = fibonacciRecursive(n)
            return cache[n]

    return memoizedFibonacci


print('With Memoization')
fib = memoizedFibonacciClosure()
print('1 ', fib(30))
print('2 ', fib(30))


def fibMaster():
    cache = {}

    def memoizedFib(n):
        if n in cache:
            return cache[n]
        elif n < 2:
            cache[n] = n
            return cache[n]
        else:
            cache[n] = memoizedFib(n - 1) + memoizedFib(n - 2)
            return cache[n]

    return memoizedFib


print('With Dynamic Programming')
# TIME Complexity --> O(n)
fibonacci = fibMaster()
print('1 ', fibonacci(100))
print('2 ', fibonacci(100))
