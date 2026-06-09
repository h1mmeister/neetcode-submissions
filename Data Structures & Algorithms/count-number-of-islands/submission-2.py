from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_of_islands = 0
        rows, cols = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            grid[row][col] = '#'

            while queue:
                curr_row, curr_col = queue.popleft()

                for dr, dc in DIRECTIONS:
                    new_row = curr_row + dr
                    new_col = curr_col + dc

                    if new_row < 0 or new_col < 0 or new_row >= rows or new_col >= cols or grid[new_row][new_col] != '1':
                        continue
                    queue.append((new_row, new_col))
                    grid[new_row][new_col] = '#'


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    bfs(row, col)
                    num_of_islands += 1

        return num_of_islands

