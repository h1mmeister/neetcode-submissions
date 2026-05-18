class Solution {
public:
    using Node = pair<int, vector<int>>;

    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {

        auto compare = [](const Node& a, const Node& b) {
            return a.first < b.first;
        };

        priority_queue<Node, vector<Node>, decltype(compare)> heap(compare);

        for (const auto& point : points) {
            int distance = point[0] * point[0] + point[1] * point[1];
            heap.emplace(distance, point);

            if (heap.size() > k) {
                heap.pop();
            }
        }

        vector<vector<int>> result;
        while(!heap.empty()) {
            result.push_back(heap.top().second);
            heap.pop();
        }

        return result; 
    }
};
