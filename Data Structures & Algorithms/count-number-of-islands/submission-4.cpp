class Solution {
    private:
        int rows;
        int cols;

        const vector<pair<int, int>> DIRECTIONS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        void dfs(int row, int col, vector<vector<char>>& grid) {
            if (row < 0 || col < 0 || row >= rows || col >= cols || grid[row][col] != '1') {
                return;
            }

            grid[row][col] = '#';

            for (const auto& dir : DIRECTIONS) {
                int new_row = row + dir.first;
                int new_col = col + dir.second;
                dfs(new_row, new_col, grid);
            }
        }

    public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) {
            return 0;
        }

        int num_of_islands {0};
        rows = grid.size();
        cols = grid[0].size();

        for (int row {0}; row < rows; ++row) {
            for(int col {0}; col < cols; ++col) {
                if (grid[row][col] == '1') {
                    dfs(row, col, grid);
                    num_of_islands++;
                }
            }
        }

        return num_of_islands;
    }
};
