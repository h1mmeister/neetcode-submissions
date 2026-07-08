class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        min_minutes = 0
        fresh_oranges = 0

        queue = collections.deque()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh_oranges += 1
                elif grid[row][col] == 2:
                    queue.append([row, col])


        while queue and fresh_oranges > 0:
            min_minutes += 1

            for _ in range(len(queue)):
                curr_row, curr_col = queue.popleft()

                for dr, dc in directions:
                    new_row = curr_row + dr
                    new_col = curr_col + dc

                    if (new_row in range(len(grid)) and new_col in range(len(grid[0])) and grid[new_row][new_col] == 1):
                        grid[new_row][new_col] = 2
                        fresh_oranges -= 1
                        queue.append([new_row, new_col])

        return min_minutes if fresh_oranges == 0 else -1
        