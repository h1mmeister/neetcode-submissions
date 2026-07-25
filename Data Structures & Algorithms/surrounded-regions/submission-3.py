class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        ROWS = len(board)
        COLS = len(board[0])

        def capture(row, col):
            stack = []
            stack.append((row, col))

            while stack:
                curr_row, curr_col = stack.pop()
                if (curr_row < 0 or curr_col < 0 or curr_row >= ROWS or curr_col >= COLS or board[curr_row][curr_col] != 'O'):
                    continue

                board[curr_row][curr_col] = '#'
                stack.extend(((curr_row + 1, curr_col), 
                              (curr_row - 1, curr_col), 
                              (curr_row, curr_col + 1), 
                              (curr_row, curr_col - 1)))

        for row in range(ROWS):
            for col in (0, COLS - 1):
                if board[row][col] == 'O':
                    capture(row, col)

        for col in range(COLS):
            for row in (0, ROWS - 1):
                if board[row][col] == 'O':
                    capture(row, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '#':
                    board[row][col] = 'O'

        