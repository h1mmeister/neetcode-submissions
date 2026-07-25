class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return board

        ROWS = len(board)
        COLS = len(board[0])

        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 or col == 0 or row == ROWS - 1 or col == COLS - 1:
                    if board[row][col] == 'O':
                        self.bfs(board, row, col)


        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '#':
                    board[row][col] = 'O'

    def bfs(self, board, row, col):
        board[row][col] = '#'

        queue = collections.deque()
        queue.append((row, col))

        while queue:
            curr_row, curr_col = queue.popleft()

            DIRECTIONS = [[0,1], [0,-1], [1, 0], [-1,0]]

            for dr, dc in DIRECTIONS:
                new_row = curr_row + dr
                new_col = curr_col + dc

                if (0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] == 'O'):
                    board[new_row][new_col] = '#'
                    queue.append((new_row, new_col))





