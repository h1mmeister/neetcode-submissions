import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = Counter(nums)
        
        # nlargest automatically builds the heap and extracts the top k elements
        return heapq.nlargest(k, hash_map.keys(), key=hash_map.get)

        