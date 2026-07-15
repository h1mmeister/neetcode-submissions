class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = collections.Counter(nums)

        sorted_keys = sorted(hash_map.keys(), key = hash_map.get, reverse = True)
        
        return sorted_keys[: k]
        