import bisect
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
            
        min_length = float('inf')
        
        # Step 1: Build a Prefix Sum array
        # sums[i] will store the sum of nums[0] up to nums[i-1]
        sums = [0] * (n + 1)
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + nums[i - 1]
            
        # Step 2: Binary search for the target threshold for each starting point
        for i in range(n):
            # We want to find a spot where sums[to_index] - sums[i] >= target
            # Which is equivalent to searching for: sums[to_index] >= target + sums[i]
            to_find = target + sums[i]
            bound = bisect.bisect_left(sums, to_find)
            
            if bound <= n:
                min_length = min(min_length, bound - i)
                
        return min_length if min_length != float('inf') else 0
        