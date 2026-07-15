class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        min_heap = []

        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1

        for key, value in hash_map.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (value, key))
            else:
                heapq.heappushpop(min_heap, (value, key))

        return [key for value, key in min_heap]
        