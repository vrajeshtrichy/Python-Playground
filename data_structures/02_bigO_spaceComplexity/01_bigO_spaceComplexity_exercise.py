def boooooo(n):
    for e in range(len(n)):
        print('boooo!')


boooooo([1, 2, 3, 4, 5])  # Space Complexity O(1)


# The Time complexity of this function is O(n)
# THe Space Complexity
# We Don't care about the input
# In this function we are not creating any space except 'e'

def arrayHiNTimes(n):
    hiArray = []  # New Data Structure
    for e in range(n):
        hiArray.append('Hi')
        # hiArray[e] = 'hi' # WRONG
    return hiArray


print(arrayHiNTimes(6))
# In this function we create a new DS and fill it in n loop. So, Space complexity is O(n). We Ignore the constant
# time O(1) for the variable 'e'
