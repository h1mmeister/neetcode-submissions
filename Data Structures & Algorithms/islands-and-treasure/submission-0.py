class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [[0,1], [0,-1], [1,0], [-1,0]]

        queue = collections.deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append([row, col])

        while queue:
            curr_row, curr_col = queue.popleft()

            for dr, dc in DIRECTIONS:
                new_row = curr_row + dr
                new_col = curr_col + dc

                if new_row < 0 or new_col < 0 or new_row >= ROWS or new_col >= COLS or grid[new_row][new_col] != 2147483647:
                    continue
                grid[new_row][new_col] = grid[curr_row][curr_col] + 1
                queue.append([new_row, new_col])


        