class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        int n = tasks.size();
        vector<array<long long, 3>> sorted_tasks(n);

        for (int i = 0; i < n; i++) {
            sorted_tasks[i] = {tasks[i][0], tasks[i][1], i};
        }
        sort(sorted_tasks.begin(), sorted_tasks.end());

        vector<int> results;
        results.reserve(n);
        long long time = 0;
        int i = 0;

        using process_idx = pair<long long, long long>;
        priority_queue<process_idx, vector<process_idx>, greater<process_idx>> heap;

        while (i < n || !heap.empty()) {
            while (i < n && sorted_tasks[i][0] <= time) {
                heap.push({sorted_tasks[i][1], sorted_tasks[i][2]});
                i++;
            }
            if (heap.empty()) {
                time = sorted_tasks[i][0];
                continue;
            }
            auto [process, idx] = heap.top();
            heap.pop();
            time += process;
            results.push_back(int(idx));
        }
        return results;
    }
};