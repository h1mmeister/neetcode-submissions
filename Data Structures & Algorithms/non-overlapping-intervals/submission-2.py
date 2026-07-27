class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prev_interval_end = intervals[0][1]
        num_of_intervals_removed = 0

        for curr_interval_start, curr_interval_end in intervals[1:]:
            if curr_interval_start >= prev_interval_end:
                prev_interval_end = curr_interval_end

            else:
                num_of_intervals_removed += 1

        return num_of_intervals_removed

        