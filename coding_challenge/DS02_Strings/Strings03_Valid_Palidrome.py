import re

def textPreprocessing(text):
    text = re.sub(r"[^A-Za-z0-9]", "", text).lower()
    return text

def isPalindrome_1(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) <= 1:
        return True
    text = textPreprocessing(s)
    # print(text)
    lPointer = 0
    rPointer = len(text) - 1
    while lPointer <= rPointer:
        if text[lPointer] != text[rPointer]:
            return False
        lPointer += 1
        rPointer -= 1
    return True


def isPalindromeBetween(lPointer, rPointer, text):
    if len(text) <= 1:
        return True
    while lPointer <= rPointer:
        if text[lPointer] != text[rPointer]:
            return False
        lPointer += 1
        rPointer -= 1
    return True


def isAlmostPalindrome_1(s):
    """
    :type s: str
    :rtype: bool
    """
    text = textPreprocessing(s)
    # print(text)
    lPointer = 0
    rPointer = len(text) - 1

    if isPalindromeBetween(lPointer, rPointer, text):
        return 'Palindrome'

    while lPointer <= rPointer:
        if text[lPointer] != text[rPointer]:
            if isPalindromeBetween(lPointer+1, rPointer, text):
                return 'Almost Palindrome'
            elif isPalindromeBetween(lPointer, rPointer-1, text):
                return 'Almost Palindrome'

        lPointer += 1
        rPointer -= 1
    return 'Not an almost palindrome'

def isAlmostPalindrome_RK(s):
    """
    :type s: str
    :rtype: bool
    """
    if isPalindrome_1(s):
        return 'Palindrome'
    text = textPreprocessing(s)
    # print(text)
    extraCharCount = 0
    extraChar = []
    lPointer = 0
    rPointer = len(text) - 1
    while lPointer <= rPointer:
        if text[lPointer] != text[rPointer]:
            if text[lPointer + 1] == text[rPointer]:
                extraCharCount += 1
                extraChar.append(text[lPointer])
                lPointer += 1
            if text[lPointer] == text[rPointer-1]:
                extraCharCount += 1
                extraChar.append(text[rPointer])
                rPointer -= 1

        lPointer += 1
        rPointer -= 1
    return {'almostPalindrome': extraCharCount==1 ,'extraCharCount':extraCharCount, 'extraChar':extraChar}


str1 = "aabaa"
str2 = "Abccba"
str3 = "a"
str4 = "Abc"
str5 = "A man, a plan, a canal: panama"
print(str1, '\n--> ', isPalindrome_1(str1))
print(str2, '\n--> ', isPalindrome_1(str2))
print(str3, '\n--> ', isPalindrome_1(str3))
print(str4, '\n--> ', isPalindrome_1(str4))
print(str5, '\n--> ', isPalindrome_1(str5))

print('=================')
print('Almost Palindrome')
print('=================')
str6 = "A man, ab plan, a canal: panama"
str7 = "abccba"
str8 = "A man, acb plan, a canal: panama"
str9 = "abcdefdba"
print(str6, '\n--> ', isAlmostPalindrome_1(str6))
print(str7, '\n--> ', isAlmostPalindrome_1(str7))
print(str8, '\n--> ', isAlmostPalindrome_1(str8))
print(str9, '\n--> ', isAlmostPalindrome_1(str9))
