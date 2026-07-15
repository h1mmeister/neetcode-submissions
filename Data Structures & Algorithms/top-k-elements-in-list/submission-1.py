class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1

        sorted_hash_map = sorted(hash_map.items(), key = lambda x: x[1], reverse = True)

        return [key for key, value in sorted_hash_map[:k]]
        