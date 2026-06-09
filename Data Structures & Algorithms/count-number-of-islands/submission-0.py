class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_islands = 0

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == '1':
                    self.dfs(row, col, grid)
                    num_of_islands += 1

        return num_of_islands

    def dfs(self, row, col, grid):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != '1':
            return 

        grid[row][col] = '#'
        self.dfs(row + 1, col, grid)
        self.dfs(row - 1, col, grid)
        self.dfs(row, col + 1, grid)
        self.dfs(row, col - 1, grid)
        return