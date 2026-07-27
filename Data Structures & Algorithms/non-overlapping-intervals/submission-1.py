class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_interval_end = intervals[0][1]
        removed = 0

        for curr_interval_start, curr_interval_end in intervals[1:]:
            if curr_interval_start < prev_interval_end:
                removed += 1
                prev_interval_end = min(prev_interval_end, curr_interval_end)

            else:
                prev_interval_end = curr_interval_end

        return removed

        