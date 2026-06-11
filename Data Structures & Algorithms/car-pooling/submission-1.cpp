class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        sort(trips.begin(), trips.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });

        int curr_num_of_passengers {0};
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> min_heap;

        for (const auto& trip : trips) {
            int num_of_passengers = trip[0];
            int start = trip[1];
            int end = trip[2];

            while (!min_heap.empty() && min_heap.top().first <= start) {
                curr_num_of_passengers -= min_heap.top().second;
                min_heap.pop();
            }

            curr_num_of_passengers += num_of_passengers;
            if (curr_num_of_passengers > capacity) {
                return false;
            }

            min_heap.push({end, num_of_passengers});

        }
        return true;
    }
};