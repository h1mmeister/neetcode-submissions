class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_of_islands = 0
        rows, cols = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != '1':
                return 

            grid[row][col] = '#'

            for dr, dc in DIRECTIONS:
                dfs(row + dr, col + dc)


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    num_of_islands += 1

        return num_of_islands
        