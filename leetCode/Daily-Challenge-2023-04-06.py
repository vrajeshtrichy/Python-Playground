# Given a 2D grid consists of 0s (land) and 1s (water).  
# An island is a maximal 4-directionally connected group of 0s and 
# a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

# Return the number of closed islands.


# Example 1:

# Input: grid = [[1,1,1,1,1,1,1,0],
#                [1,0,0,0,0,1,1,0],
#                [1,0,1,0,1,1,1,0],
#                [1,0,0,0,0,1,0,1],
#                [1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water (group of 1s).


# Example 2:

# Input: grid = [[0,0,1,0,0],
#                [0,1,0,1,0],
#                [0,1,1,1,0]]
# Output: 1
# Example 3:

# Input: grid = [[1,1,1,1,1,1,1],
#                [1,0,0,0,0,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,1,0,1,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,0,0,0,0,1],
#                [1,1,1,1,1,1,1]]
# Output: 2
 

# Constraints:

# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1

# Use a normal algorithm (bfs/dfs) to find the number of islands and mark them, 
# but only increment 1 to the count if no nodes in that island are on the border


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

    def minimizeArrayValue(self, nums: list[int]) -> int:
        minimum = 0
        return 0
    

sol = Solution()
# inputStr = "abacaba"
# count = sol.partitionString(inputStr)

nums = [3,7,1,6]

mini = sol.minimizeArrayValue(nums)
print(mini)