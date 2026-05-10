"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        heap = []

        for interval in intervals:
            if heap and interval.start >= heap[0]:
                heapq.heapreplace(heap, interval.end)
            else:
                heapq.heappush(heap, interval.end)

        return len(heap)


        