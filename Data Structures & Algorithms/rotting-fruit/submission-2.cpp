class Solution {
private:
    using coords = pair<int, int>;
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int min_minutes = 0;
        int fresh_oranges = 0;

        queue<coords> q;
        vector<vector<int>> directions = {{0,1}, {0,-1}, {1, 0}, {-1,0}};

        for (int row = 0; row < grid.size(); row++) {
            for (int col = 0; col < grid[0].size(); col++) {
                if (grid[row][col] == 1) {
                    fresh_oranges += 1;
                } else if (grid[row][col] == 2) {
                    q.push({row, col});
                }
            }
        }

        while (!q.empty() && fresh_oranges > 0) {
            min_minutes += 1;

            int queue_size = q.size();
            for (int j = 0; j < queue_size; j++) {
                coords data = q.front();
                int curr_row = data.first;
                int curr_col = data.second;

                q.pop();

                for (int k = 0; k < directions.size(); k++) {
                    int new_row = curr_row + directions[k][0];
                    int new_col = curr_col + directions[k][1];

                    if ((0 <= new_row && new_row < grid.size()) &&
                        (0 <= new_col && new_col < grid[0].size()) &&
                        (grid[new_row][new_col] == 1)) {
                            grid[new_row][new_col] = 2;
                            fresh_oranges -= 1;
                            q.push({new_row, new_col});
                        }
                }
            }
        }

        return (fresh_oranges == 0) ? min_minutes : -1;
        
    }
};
