class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.rob_helper(nums[:-1]), self.rob_helper(nums[1:]))

    def rob_helper(Self, nums):
        dp = [0] * (len(nums) + 2)

        for idx in range(len(nums) - 1, -1, -1):
            dp[idx] = max(nums[idx] + dp[idx + 2], dp[idx + 1])

        return dp[0]

        