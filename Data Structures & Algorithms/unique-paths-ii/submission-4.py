class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0 

        dp = [[0] * COLS for _ in range(ROWS)]
        dp[0][0] = 1

        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 and col == 0:
                    continue
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                    continue

                top = dp[row - 1][col] if row > 0 else 0
                left = dp[row][col - 1] if col > 0 else 0

                dp[row][col] = top + left;

        return dp[ROWS - 1][COLS - 1]
        