class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        if (grid.empty() || grid[0].empty()) {
            return;
        }

        int ROWS = grid.size();
        int COLS = grid[0].size();
        queue<pair<int, int>> q;

        int DIRECTIONS[4][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

        for (int row = 0; row < ROWS; ++row) {
            for (int col = 0; col < COLS; ++col) {
                if (grid[row][col] == 0) {
                    q.push({row, col});
                }
            }
        }

        while (!q.empty()) {
            auto [curr_row, curr_col] = q.front();
            q.pop();

            for (const auto& dir : DIRECTIONS) {
                int new_row = curr_row + dir[0];
                int new_col = curr_col + dir[1];

                if ((new_col < 0) || (new_row < 0) || (new_row >= ROWS) || (new_col >= COLS) || (grid[new_row][new_col] != INT_MAX)) {
                    continue;
                }

                grid[new_row][new_col] = grid[curr_row][curr_col] + 1;
                q.push({new_row, new_col});
            }
        }


    }
};
