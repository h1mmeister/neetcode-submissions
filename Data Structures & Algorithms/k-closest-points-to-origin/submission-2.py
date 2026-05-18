from heapq import heappush, heappushpop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distance = x*x + y*y
            if len(heap) < k:
                heappush(heap, (-distance, (x, y)))
            else:
                heappushpop(heap, (-distance, (x, y)))

        return [y for x, y in heap]



        