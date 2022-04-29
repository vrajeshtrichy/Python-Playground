def reverseString(str):
    if len(str) == 0:
        return str
    rev = str[-1] + reverseString(str[:-1])
    print(rev)
    return rev


reverseString('yoyo mastery')
# should return: 'yretsam oyoy'
