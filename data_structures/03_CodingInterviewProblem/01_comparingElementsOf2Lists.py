array1 = ['a', [], None, 'd', 'e']
array2 = ['x', [], None, 'd']

# Output True: if a common element is found
# Output False: if no common element found


# With Bruteforce, we can do a nested for loop and compare the two Arrays

# Option 2 Bruteforce, we can do a loop and check in the other Array

for e in array1:  # O(n)
    if e in array2:  # O(n)
        print('True')


# This is O(n^2) - Timecomplexity
# Space Complexity is O(1) as no new object is created

# can we assume always 2 parameters
# can we assume the two inputs are arrays
def containCommonItem(arr1, arr2):
    map = {}
    for e in arr1:  # O(n)
        print(type(e))
        if (type(e) == str or type(e) == int) and e not in map:
            map[e] = True
    print(map)
    for e in arr2:  # O(n)
        if (type(e) == str or type(e) == int) and e in map:
            return 'Found'
    return 'Not Found'


print(containCommonItem(array1, array2))
# Time Complexity - O(a+b)
# Space Complexity - O(a) - Size of the first array as the map object is created
