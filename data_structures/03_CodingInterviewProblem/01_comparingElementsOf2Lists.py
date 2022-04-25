array1 = ['a', 'b', 'c', 'd', 'e']
array2 = ['x', 'y', 'z', 'd']

# Output True: if a common element is found
# Output False: if no common element found


# With Bruteforce, we can do a nested for loop and compare the two Arrays

# Option 2 Bruteforce, we can do a loop and check in the other Array

for e in array1: # O(n)
    if e in array2: # O(n)
        print('True')

# This is O(n^2)
