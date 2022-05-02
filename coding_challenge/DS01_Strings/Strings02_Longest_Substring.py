def lengthOfLongestSubstring_brute(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) <= 1:
        return len(s)
    longest = 0
    string = s
    i = 0
    for i in range(len(string)):
        charObj = {}
        len_substr = 0
        for j in range(i, len(string)):
            if string[j] in charObj:
                # i +=1
                break
            else:
                charObj[string[j]] = True
                len_substr += 1

                longest = max(len_substr, longest)

    return longest


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) <= 1:
        return len(s)
    longest = 0
    len_substr = 1
    string = s
    charObj = {}
    lPointer = 0
    rPointer = lPointer + 1
    charObj[string[lPointer]] = lPointer
    while lPointer < rPointer and rPointer < len(string):

        if string[rPointer] not in charObj:
            charObj[string[rPointer]] = rPointer
            len_substr += 1
            rPointer += 1
        else:
            lPointer = charObj[string[rPointer]] + 1
            rPointer = lPointer +1
            charObj = {}
            charObj[string[lPointer]] = lPointer
            len_substr = 1
        # print(charObj, lPointer, rPointer, len_substr)
        longest = max(longest, len_substr)

    #     check if string[rpointer] in charObj
    #     if false
    #       charObj[string[rpointer]]=rpointer
    #       len_substr += 1
    #       rpointer += 1
    #     else:
    #       lpointer = charObj[string[rpointer]] +1

    return longest

def lengthOfLongestSubstring_optimum(s):
    if len(s) <= 1:
        return len(s)
    longest = 0
    # len_substr = 0
    fullString = s
    charObj = {}
    lPointer = 0
    for rPointer in range(len(fullString)):
        currentChar = fullString[rPointer]
        if currentChar not in charObj:
            charObj[currentChar] = rPointer
            # THIS CAN BE MOVED FROM IF SINCE THIS STEP IS IN ALL ELSE CASES
        else:
            if lPointer <= charObj[currentChar]:
                lPointer = charObj[currentChar] + 1
                charObj[currentChar] = rPointer
            else:
                charObj[fullString[rPointer]] = rPointer
        len_substr = rPointer - lPointer + 1
        print(charObj, lPointer, rPointer, len_substr)
        longest = max(longest, len_substr)

    return longest


    # while lPointer < len(fullString):
    #     if fullString[rPointer] not in charObj:
    #             charObj[fullString[rPointer]] = rPointer
    #             len_substr = rPointer - lPointer + 1
    #     else:
    #         if lPointer > charObj[fullString[rPointer]]:
    #             charObj[fullString[rPointer]] = rPointer
    #             # rPointer += 1
    #             len_substr = rPointer - lPointer + 1
    #         else:
    #             len_substr = rPointer - lPointer + 1
    #             lPointer = charObj[fullString[rPointer]] + 1
    #             charObj[fullString[rPointer]] = rPointer
    #     rPointer += 1
    #     print(charObj, lPointer, rPointer, len_substr)
    #     longest = max(longest, len_substr)
        # asd
    # return longest

string2 = "abcbdaac#"
string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
print('backspaceCompare_brute', lengthOfLongestSubstring_brute(string2))
print('lengthOfLongestSubstring', lengthOfLongestSubstring_optimum(string2))
