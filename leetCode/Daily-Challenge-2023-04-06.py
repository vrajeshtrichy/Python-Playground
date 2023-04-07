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

# if land == Island, start with flag True. Use DFS to find islands and mark them, also if island is in border flag False
# Count closed island if flag = true


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if len(grid) == 0: return 0
        islands = 0
        rows = len(grid)
        columns = len(grid[0])
        islands = 0

        # if current position is island and not border,
        #     using DFS, check if it's a closed island and mark
        #         if yes: increment island count
        for i in range(0, rows):
            for j in range(0, columns):
                if grid[i][j] == 0:
                    print("R", i, "C", j)
                    closed_island = self.check_and_mark_island_using_dfs(grid, rows, columns, i, j, True)
                    if closed_island:
                        islands += 1
                        print("islands count: ", islands)

                        for r in grid:
                            print(r)
                    print("dfs completed")
        return islands

    def check_and_mark_island_using_dfs(self, grid, rows, columns, y, x, is_closed_island):
        print(y, x)

        if y < 0 or x < 0 or y >= rows or x >= columns or grid[y][x] != 0: return is_closed_island

        if grid[y][x] == 0:
            grid[y][x] = 2
            if y == 0 or x == 0 or y == rows - 1 or x == columns - 1:
                is_closed_island = False
                print("switch")

        print(is_closed_island)
        # Up
        is_closed_island = self.check_and_mark_island_using_dfs(grid, rows, columns, y - 1, x, is_closed_island)
        # Right
        is_closed_island = self.check_and_mark_island_using_dfs(grid, rows, columns, y, x + 1, is_closed_island)
        # Down
        is_closed_island = self.check_and_mark_island_using_dfs(grid, rows, columns, y + 1, x, is_closed_island)
        # Left
        is_closed_island = self.check_and_mark_island_using_dfs(grid, rows, columns, y, x - 1, is_closed_island)

        return is_closed_island


sol = Solution()
grid = [[1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0]]


# grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]

# grid = [[0, 0, 1, 0, 0],
#         [0, 1, 0, 1, 0],
#         [0, 1, 1, 1, 0]]

closed_islands = sol.closedIsland(grid)

print(closed_islands)
