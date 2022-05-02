def add80(n):
    print('Long time')
    return n + 80

print('Without Caching')
print(add80(5))
print(add80(5))

###
# Memoization 1
cache = {}
def memoizedadd80(n):
    if n in cache:
        return cache[n]
    else:
        print('Long time')
        cache[n] = n + 80
        return cache[n]

print('With Memoization 1')
print('1', memoizedadd80(6))
print('2', memoizedadd80(6))

###
# Memoization 2
# We can try to avoid caching in Global Scope
def memoizedadd80_2():
    cache = {}
    def memo_closure(n):
        if n in cache:
            return cache[n]
        else:
            print('Long time')
            cache[n] = n + 80
            return cache[n]
    return memo_closure

print('With Memoization 2')
memoized = memoizedadd80_2()
print('1', memoized(5))
print('2', memoized(5))