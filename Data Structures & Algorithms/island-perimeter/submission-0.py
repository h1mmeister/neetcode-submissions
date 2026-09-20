class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
                return 1
            
            if grid[row][col] == "#":
                return 0

            grid[row][col] = '#'
            result = dfs(row + 1, col) + \
                      dfs(row, col + 1) + \
                      dfs(row - 1, col) + \
                      dfs(row, col - 1)

            return result


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    perimeter += dfs(row, col)

        return perimeter
        