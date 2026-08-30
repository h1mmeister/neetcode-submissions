class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        unordered_map<int, vector<pair<int, int>>> adj_list;
        for (auto& time : times) {
            int source = time[0];
            int target = time[1];
            int weight = time[2];
            adj_list[source].push_back({target, weight});
        }

        unordered_map<int, int> time_map;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> min_heap;
        min_heap.push({0, k});

        while (!min_heap.empty()) {
            auto [time, node] = min_heap.top();
            min_heap.pop();

            if (time_map.count(node)) continue;
            time_map[node] = time;

            if (static_cast<int>(time_map.size()) == n) {
                break;
            }

            for (auto& [neighbor_node, neighbor_time] : adj_list[node]) {
                if (!time_map.count(neighbor_node)) {
                    min_heap.push({time + neighbor_time, neighbor_node});
                }
            }
        }

        if (static_cast<int>(time_map.size()) != n) {
            return -1;
        }

        int total_time = 0;
        for (const auto& [node, time] : time_map) {
            total_time = max(total_time, time);
        }

        return total_time;
        
    }
};
