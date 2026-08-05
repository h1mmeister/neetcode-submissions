class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.rob_helper(nums[:-1]), self.rob_helper(nums[1:]))

    def rob_helper(self, nums):
        next1 = 0
        next2 = 0

        for idx in range(len(nums) - 1, -1, -1):
            curr = max(nums[idx] + next2, next1)
            next2, next1 = next1, curr

        return next1
        