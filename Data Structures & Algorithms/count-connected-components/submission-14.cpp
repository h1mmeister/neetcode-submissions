class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        int num_of_components = 0;
        vector<vector<int>> adj_list(n);

        for (const auto& edge : edges) {
            adj_list[edge[0]].push_back(edge[1]);
            adj_list[edge[1]].push_back(edge[0]);
        }

        vector<bool> visited(n, false);

        for (int node = 0; node < n; ++node) {
            if (!visited[node]) {
                visited[node] = true;
                ++num_of_components;

                queue<int> q;
                q.push(node);

                while (!q.empty()) {
                    int curr_node = q.front();
                    q.pop();

                    for (int neighbor : adj_list[curr_node]) {
                        if (!visited[neighbor]) {
                            visited[neighbor] = true;
                            q.push(neighbor);
                        }
                    }
                }
            }
        }
        return num_of_components;
    }
};
