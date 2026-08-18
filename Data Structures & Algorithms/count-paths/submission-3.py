class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0 for _ in range(n)]for _ in range(m)]

        def unique_path_helper(row, col):
            if row == 0 and col == 0:
                return 1
            elif row < 0 or col < 0:
                return 0
            if not cache[row][col]:
                left = unique_path_helper(row, col - 1)
                up = unique_path_helper(row - 1, col)
                cache[row][col] = left + up

            return cache[row][col]
        return unique_path_helper(m-1,n-1)
        