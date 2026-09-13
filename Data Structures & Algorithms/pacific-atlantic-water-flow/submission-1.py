class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()

        def bfs(cells, visit):
            queue = collections.deque(cells)
            visit.update(cells)

            while queue:
                curr_row, curr_col = queue.popleft()

                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    new_row = curr_row + dr
                    new_col = curr_col + dc

                    if ((0 <= new_row < ROWS) and (0 <= new_col < COLS) and (new_row, new_col) not in visit and heights[new_row][new_col] >= heights[curr_row][curr_col]):
                        queue.append((new_row, new_col))
                        visit.add((new_row, new_col))


        pacific_cells = [(0, col) for col in range(COLS)] + [(row, 0) for row in range(ROWS)]
        atlantic_cells = [(ROWS - 1, col) for col in range(COLS)] + [(row, COLS - 1) for row in range(ROWS)]
        
        bfs(pacific_cells, pacific)
        bfs(atlantic_cells, atlantic)

        return [[row, col] for row in range(ROWS) for col in range(COLS) if (row, col) in pacific and (row, col) in atlantic ]