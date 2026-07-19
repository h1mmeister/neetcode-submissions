class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) {
            return {};
        }

        sort(intervals.begin(), intervals.end());
        vector<vector<int>> merged_intervals;

        merged_intervals.push_back(intervals[0]);

        for (int idx = 1; idx < intervals.size(); ++idx) {
            int curr_intervals_start = intervals[idx][0];
            int curr_intervals_end = intervals[idx][1];

            int& prev_intervals_end = merged_intervals.back()[1];

            if (curr_intervals_start <= prev_intervals_end) {
                prev_intervals_end = max(prev_intervals_end, curr_intervals_end);
            } else {
                merged_intervals.push_back({curr_intervals_start, curr_intervals_end});
            }
        }
        return merged_intervals;
    }
};
