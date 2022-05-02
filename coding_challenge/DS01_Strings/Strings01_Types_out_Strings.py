def backspaceCompare_brute(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    cleanS = []
    cleanT = []

    for i in range(len(s)):
        cleanS.append(s[i])
        if cleanS[-1] == '#':
            cleanS.pop()
            if len(cleanS) > 0:
                cleanS.pop()

    for i in range(len(t)):
        cleanT.append(t[i])
        if cleanT[-1] == '#':
            cleanT.pop()
            if len(cleanT) > 0:
                cleanT.pop()

    def buildString(s):
        cleanS = []
        for i in range(len(s)):
            if s[i] != '#':
                cleanS.append(s[i])
            else:
                if len(cleanS) > 0:
                    cleanS.pop()
        return cleanS

    # print(cleanS, cleanT)
    # return cleanS == cleanT
    return buildString(s) == buildString(t)


def backspaceCompare(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    cleanS = []
    cleanT = []

    indexS = 0
    indexT = 0

    while indexS < len(s) or indexT < len(t):
        if indexS < len(s):
            cleanS.append(s[indexS])
            if cleanS[-1] == '#':
                cleanS.pop()
                if len(cleanS) > 0:
                    cleanS.pop()
        if indexT < len(t):
            cleanT.append(t[indexT])
            if cleanT[-1] == '#':
                cleanT.pop()
                if len(cleanT) > 0:
                    cleanT.pop()

        # if indexS < len(s):
        #     if s[indexS] != '#':
        #         cleanS.append(s[indexS])
        #     else:
        #         if len(cleanS) > 0:
        #             cleanS.pop()
        indexS += 1
        indexT += 1
    # print(cleanS, cleanT)
    return cleanS == cleanT


def backspaceCompare_pointer(s, t):
    sPointer = len(s) - 1
    tPointer = len(t) - 1
    while sPointer >= 0 or tPointer >= 0:
        print((sPointer >= 0 and s[sPointer] == '#') or (tPointer >= 0 and t[tPointer] == '#'))
        if (sPointer >= 0 and s[sPointer] == '#') or (tPointer >= 0 and t[tPointer] == '#'):
            if sPointer >= 0 and s[sPointer] == '#':
                backcount = 2
                while backcount > 0:
                    sPointer -= 1
                    backcount -= 1
                    if sPointer >= 0 and s[sPointer] == '#':
                        backcount += 2
            if tPointer >= 0 and t[tPointer] == '#':
                backcount = 2
                while backcount > 0:
                    tPointer -= 1
                    backcount -= 1
                    if tPointer >= 0 and t[tPointer] == '#':
                        backcount += 2
            print('if', sPointer, tPointer)
        else:
            if s[sPointer] != t[tPointer]:
                return False
            else:
                sPointer -= 1
                tPointer -= 1
            print('else', s[sPointer], t[tPointer], sPointer, tPointer)

    return True


s = "asd#"
t = "c#asdaa###d#"
print('backspaceCompare_brute', backspaceCompare_brute(s, t))
print('backspaceCompare', backspaceCompare(s, t))
print(backspaceCompare_pointer(s, t))
