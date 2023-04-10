# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()[]{}"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1: return False
        bracketsCombo = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        bracketsOpen = []
        for c in s:
            print(c)
            if c in bracketsCombo:
                bracketsOpen.append(c)
            # elif len(bracketsOpen) > 0 and c == bracketsCombo[bracketsOpen[-1]]:
            #         bracketsOpen.pop()
            # else: return False
            elif len(bracketsOpen) == 0 or bracketsCombo[bracketsOpen.pop()]  != c:
                return False

        return len(bracketsOpen) == 0


sol = Solution()

# s = "()[]{}"

s = "]"

print(sol.isValid(s))
