testMatrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1]
]


def count_islands(grid):
    if len(grid) == 0: return 0

    rows = len(grid)
    columns = len(grid[0])
    islands = 0

    # if current position is island,
    #     increment island count
    #     mark current position and neighbouring island as visited using DFS
    for i in range(0, rows):
        for j in range(0, columns):
            if grid[i][j] == 1:
                islands += 1
                mark_visited_using_dfs(grid, rows, columns, i, j)
    return islands


def mark_visited_using_dfs(grid, rows, columns, y, x):
    if y < 0 or x < 0 or y >= rows or x >= columns or grid[y][x] != 1: return

    if grid[y][x] == 1:
        grid[y][x] = 2
    print(rows, columns, y, x)
    # Up
    mark_visited_using_dfs(grid, rows, columns, y - 1, x)
    # Right
    mark_visited_using_dfs(grid, rows, columns, y, x + 1)
    # Down
    mark_visited_using_dfs(grid, rows, columns, y + 1, x)
    # Left
    mark_visited_using_dfs(grid, rows, columns, y, x - 1)

    return


number_of_islands = count_islands(testMatrix)
print(number_of_islands)