class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {

        auto is_feasible = [&](int capacity) {
            int count = 1;
            int curr_cap = capacity;

            for (int weight : weights) {
                if ((curr_cap - weight) < 0) {
                    count += 1;
                    curr_cap = capacity;
                }
                curr_cap -= weight;
            }

            return count <= days;
        };

        int left = *max_element(weights.begin(), weights.end());
        int right = accumulate(weights.begin(), weights.end(), 0);

        while (left < right) {
            int capacity = left + (right - left) / 2;
            if (is_feasible(capacity)) {
                right = capacity;
            } else {
                left = capacity + 1;
            }
        }
        return left;
    }
};