class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return board

        ROWS = len(board)
        COLS = len(board[0])

        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 or col == 0 or row == ROWS - 1 or col == COLS -1:
                    if board[row][col] == 'O':
                        self.dfs(board, row, col)
                        

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '#':
                    board[row][col] = 'O'


    def dfs(self, board, row, col):
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != 'O':
            return
        
        board[row][col] = '#'
        self.dfs(board, row + 1, col)
        self.dfs(board, row - 1, col)
        self.dfs(board, row, col + 1)
        self.dfs(board, row, col - 1)
        