class Solution {
    private:
        int rows;
        int cols;

        void dfs(int row, int col, vector<vector<char>>& grid) {
            if (row < 0 || col < 0 || row >= rows || col >= cols || grid[row][col] != '1') {
                return;
            }

            grid[row][col] = '#';
            dfs(row + 1, col, grid);
            dfs(row - 1, col, grid);
            dfs(row, col + 1, grid);
            dfs(row, col - 1, grid);
        }

    public:
        int numIslands(vector<vector<char>>& grid) {
            if (grid.empty()) {
                return 0;
            }

            int num_of_islands = 0;
            rows = grid.size();
            cols = grid[0].size();

            for (int row {0}; row < rows; ++row) {
                for (int col {0}; col < cols; ++col) {
                    if (grid[row][col] == '1') {
                        dfs(row, col, grid);
                        num_of_islands++;
                    }
                }
            }

            return num_of_islands;
        }
};
