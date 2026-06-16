class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != 1:
                return 0

            grid[row][col] = 2

            return 1 + dfs(row + 1, col) \
                     + dfs(row - 1, col) \
                     + dfs(row, col + 1) \
                     + dfs(row, col - 1)


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    curr_area = dfs(row, col)
                    max_area = max(max_area, curr_area)

        return max_area
        