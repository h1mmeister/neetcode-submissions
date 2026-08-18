class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0 for _ in range(n)]for _ in range(m)]

        def unique_path_helper(row, col):
            if row == m-1 and col == n-1:
                return 1
            elif row >= m or col >= n:
                return 0
            if not cache[row][col]:
                right = unique_path_helper(row, col + 1)
                down = unique_path_helper(row + 1, col)
                cache[row][col] = right + down

            return cache[row][col]
        return unique_path_helper(0,0)
        