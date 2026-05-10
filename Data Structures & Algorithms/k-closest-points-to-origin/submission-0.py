class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        min_heap = []
        
        for x, y in points:
            distance = x**2 + y**2
            heapq.heappush(min_heap, (distance, [x,y]))

        for i in range(0, k):
            distance, point = heapq.heappop(min_heap)
            result.append(point)

        return result
        