class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if (board.size() == 0 or board[0].size() == 0) {
            return;
        }

        int ROWS = board.size();
        int COLS = board[0].size();

        for (int row = 0; row < ROWS; ++row) {
            for (int col = 0; col < COLS; ++col) {
                if (row == 0 || col == 0 || row == ROWS - 1 || col == COLS - 1) {
                    if (board[row][col] == 'O') {
                    dfs(board, row, col);
                    }
                }
            }
        }

        for (int row = 0; row < ROWS; ++row) {
            for (int col = 0; col < COLS; ++col) {
                if (board[row][col] == 'O') {
                    board[row][col] = 'X';
                } else if (board[row][col] == '#') {
                    board[row][col] = 'O';
                }
            }
        }
    }

private:
    void dfs(vector<vector<char>>& board, int row, int col) {
        if (row < 0 || col < 0 || row >= board.size() || col >= board[0].size() || board[row][col] != 'O'){
            return;
        }

        board[row][col] = '#';
        dfs(board, row + 1, col);
        dfs(board, row - 1, col);
        dfs(board, row, col + 1);
        dfs(board, row, col - 1);

    }
};
