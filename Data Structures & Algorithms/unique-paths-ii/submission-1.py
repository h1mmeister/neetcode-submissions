class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        cache = [[0] * COLS for _ in range(ROWS)]

        def unique_paths_obst_helper(row, col):
            if row >= ROWS or col >= COLS:
                return 0
            elif obstacleGrid[row][col] == 1:
                return 0
            elif row == ROWS - 1 and col == COLS - 1:
                return 1
            
            if not cache[row][col]:
                right = unique_paths_obst_helper(row, col + 1)
                down = unique_paths_obst_helper(row + 1, col)
                cache[row][col] = right + down
            return cache[row][col]

        return unique_paths_obst_helper(0, 0)
        