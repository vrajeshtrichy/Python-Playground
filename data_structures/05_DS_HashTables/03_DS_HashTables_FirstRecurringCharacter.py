# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return undefined

def firstRecurringCharacter(input):
    charObj = {}
    for c in input:
        if c not in charObj:
            charObj[c] = True
        else:
            return c
    return None


def firstRecurringCharacter2(input):
    charObj = {}
    for c in input:
        if c in charObj:
            return c
        else:
            charObj[c] = True
    return None


# Time Complexity is O(n)
# Space complexity is O(n) - we are creating charObj object

array1 = [2, 5, 1, 2, 3, 5, 1, 2, 4]
array2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
array3 = [2, 3, 4, 5]
print(firstRecurringCharacter2(array3))
# Bonus... What if we had this:
#  [2,5,5,2,3,5,1,2,4]
#  return 5 because the pairs are before 2,2
