class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        max_heap = []
        result = []

        for num in nums:
            if num not in hash_map:
                hash_map[num] = -1
            else:
                hash_map[num] -= 1

        for key, value in hash_map.items():
            heapq.heappush(max_heap, (value, key))

        for _ in range(k):
            result.append(heapq.heappop(max_heap)[1])

        return result

        