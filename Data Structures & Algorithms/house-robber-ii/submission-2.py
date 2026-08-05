class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        first = self.rob_helper(nums[0: -1], 0, {})
        second = self.rob_helper(nums[1:], 0, {})

        return max(first, second)

    def rob_helper(self, nums, idx, cache):
        if idx >= len(nums):
            return 0

        if idx in cache:
            return cache[idx]

        cache[idx] = max(nums[idx] + self.rob_helper(nums, idx + 2, cache), self.rob_helper(nums, idx + 1, cache))
        return cache[idx]
        