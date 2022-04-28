def reverse(str):
    reversedStr = ''
    # Check for Data type
    for i in range(len(str) - 1, -1, -1):
        reversedStr += str[i]
    return reversedStr


def reverse2(str):
    list(str).reverse()
    return ''.join(str)


print(reverse2('Rajesh'))
