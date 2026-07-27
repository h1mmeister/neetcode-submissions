class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int num_of_intervals_removed = 0;
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
                return a[1] < b[1];
        });
        int prev_interval_end = intervals[0][1];

        for (int idx = 1; idx < intervals.size(); ++idx) {
            int curr_interval_start = intervals[idx][0];
            int curr_interval_end = intervals[idx][1];

            if (curr_interval_start >= prev_interval_end) {
                prev_interval_end = curr_interval_end;
            } else {
                num_of_intervals_removed += 1;
            }
        }
        return num_of_intervals_removed;    
    }
};
