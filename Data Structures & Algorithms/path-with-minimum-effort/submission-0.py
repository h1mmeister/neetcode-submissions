class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])

        min_heap = [[0, 0, 0]]
        visited = set()

        DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while min_heap:
            diff, curr_row, curr_col = heapq.heappop(min_heap)

            if (curr_row, curr_col) in visited:
                continue
            
            visited.add((curr_row, curr_col))

            if (curr_row, curr_col) == (ROWS - 1, COLS - 1):
                return diff

            for dr, dc in DIRECTIONS:
                new_row = curr_row + dr
                new_col = curr_col + dc

                if (new_row < 0 or new_col < 0 or new_row >= ROWS or new_col >= COLS or (new_row, new_col) in visited):
                    continue
                new_diff = max(diff, abs(heights[curr_row][curr_col] - heights[new_row][new_col]))
                heapq.heappush(min_heap, [new_diff, new_row, new_col])
        