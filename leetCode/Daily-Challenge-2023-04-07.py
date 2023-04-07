# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
#
# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
#
# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

# Example 1
# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

# Example 2
# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.

# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] is either 0 or 1.

class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        if len(grid) == 0: return 0
        islands = 0
        rows = len(grid)
        columns = len(grid[0])
        total_enclaves = 0

        # if current position is island and not border,
        #     using DFS, check if it's a closed island and mark
        #         if yes: increment island count
        # for i in range(0, rows):
        #     for j in range(0, columns):
        #         if grid[i][j] == 1:
        #             print("R", i, "C", j)
        #             enclaves = self.check_and_mark_island_using_dfs(grid, rows, columns, i, j, 0)

        for i in range(0, rows):
            for j in range(0, columns):
                if grid[i][j] == 1:
                    print("R", i, "C", j)
                    closed_island, enclaves = self.check_and_mark_island_using_dfs(grid, rows, columns, i, j, True, 0)
                    if closed_island:
                        islands += 1
                        total_enclaves += enclaves
                        print("islands count: ", islands)
                        print("enclaves count: ", total_enclaves)
                    print("dfs completed")

        for r in grid:
            print(r)
        print(total_enclaves)
        return total_enclaves

    def check_and_mark_island_using_dfs(self, grid, rows, columns, y, x, is_closed_island, enclaves):
        print(y, x)

        if y < 0 or x < 0 or y >= rows or x >= columns or grid[y][x] != 1: return is_closed_island, enclaves

        if grid[y][x] == 1:
            grid[y][x] = 2
            enclaves += 1
            if y == 0 or x == 0 or y == rows - 1 or x == columns - 1:
                is_closed_island = False
                print("switch")

        print("is_closed_island", is_closed_island)
        # Up
        is_closed_island, enclaves = self.check_and_mark_island_using_dfs(grid, rows, columns, y - 1, x, is_closed_island, enclaves)
        # Right
        is_closed_island, enclaves = self.check_and_mark_island_using_dfs(grid, rows, columns, y, x + 1, is_closed_island, enclaves)
        # Down
        is_closed_island, enclaves = self.check_and_mark_island_using_dfs(grid, rows, columns, y + 1, x, is_closed_island, enclaves)
        # Left
        is_closed_island, enclaves = self.check_and_mark_island_using_dfs(grid, rows, columns, y, x - 1, is_closed_island, enclaves)

        return is_closed_island, enclaves
        # print(y, x)
        #
        # if y < 0 or x < 0 or y >= rows or x >= columns or grid[y][x] != 1: return enclaves
        #
        # if grid[y][x] == 1:
        #     grid[y][x] = 2
        #     enclaves += 1
        #     if y == 0 or x == 0 or y == rows - 1 or x == columns - 1:
        #         enclaves -= 1
        #
        #     print(enclaves)
        # # Up
        # enclaves = self.check_and_mark_island_using_dfs(grid, rows, columns, y - 1, x, enclaves)
        # # Right
        # enclaves = self.check_and_mark_island_using_dfs(grid, rows, columns, y, x + 1, enclaves)
        # # Down
        # enclaves = self.check_and_mark_island_using_dfs(grid, rows, columns, y + 1, x, enclaves)
        # # Left
        # enclaves = self.check_and_mark_island_using_dfs(grid, rows, columns, y, x - 1, enclaves)
        #
        # return enclaves


sol = Solution()
grid = [[1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0]]


# grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]


# grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]

# grid = [[0, 0, 1, 0, 0],
#         [0, 1, 0, 1, 0],
#         [0, 1, 1, 1, 0]]

closed_islands = sol.numEnclaves(grid)

print(closed_islands)
