class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        merged_intervals = [sorted_intervals[0]]

        for curr_interval_start, curr_interval_end in sorted_intervals[1:]:
            prev_interval_start, prev_interval_end = merged_intervals[-1]

            if curr_interval_start <= prev_interval_end:
                merged_intervals[-1] = [min(prev_interval_start, curr_interval_start), max(prev_interval_end, curr_interval_end)]
            else:
                merged_intervals.append([curr_interval_start, curr_interval_end])

        return merged_intervals
        