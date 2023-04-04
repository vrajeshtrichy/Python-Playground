# Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

# Return the minimum number of substrings in such a partition.

# Note that each character should belong to exactly one substring in a partition.

 

# Example 1:

# Input: s = "abacaba"
# Output: 4
# Explanation:
# Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
# It can be shown that 4 is the minimum number of substrings needed.
# Example 2:

# Input: s = "ssssss"
# Output: 6
# Explanation:
# The only valid partition is ("s","s","s","s","s","s").

# Start with count as 1 and empty set.
# Iterate over the string and check is character is repeating.
# If yes we increment count, clear set and add the new character to set.
# If no we add the character to set and continue the loop.
# Return count.


class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        outSet = set()
        for c in s:
            if c in outSet:
                count += 1
                # print(outSet)
                outSet = set()
                outSet.add(c)
            else:
                outSet.add(c)
                print(outSet)
        return count
        # inputStrArr = s.
        # outputStrArr = []
        # return inputStrArr
    

sol = Solution()
inputStr = "abacaba"
count = sol.partitionString(inputStr)
print(count)