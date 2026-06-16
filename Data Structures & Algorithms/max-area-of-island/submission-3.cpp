class Solution {
private:
    int rows;
    int cols;

    int dfs(int row, int col, vector<vector<int>>& grid) {
        if (row < 0 || col < 0 || row >= rows || col >= cols || grid[row][col] != 1) return 0;

        grid[row][col] = 2;

        return (1 + dfs(row + 1, col, grid) + dfs(row - 1, col, grid) + dfs(row, col + 1, grid) + dfs(row, col - 1, grid));
    }

public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;

        int max_area = 0;
        rows = grid.size();
        cols = grid[0].size();

        for (int row {0}; row < rows; ++row) {
            for (int col {0}; col < cols; ++col) {
                if (grid[row][col] == 1) {
                    int curr_area = dfs(row, col, grid);
                    max_area = max(max_area, curr_area);
                }
            }
        }
        return max_area;
    }
};
