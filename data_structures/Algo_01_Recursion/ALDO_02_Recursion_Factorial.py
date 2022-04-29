def findFactorialRecursive(number):
    if number == 1:
        return number
    factorial = number * findFactorialRecursive(number - 1)
    return factorial


def findFactorialRecursive_better(number):
    if number <= 2:
        return number
    return number * findFactorialRecursive(number - 1)


def findFactorialIterative(number):
    factorial = 1
    for i in range(number, 1, -1):
        factorial = factorial * i
    return factorial


print(findFactorialIterative(5))  # O(n)
print(findFactorialRecursive_better(5))  # O(n)
