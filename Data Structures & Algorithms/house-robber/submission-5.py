class Solution:
    def rob(self, nums: List[int]) -> int:
        num_of_houses = len(nums)

        if num_of_houses == 1:
            return nums[0]
        elif num_of_houses == 2:
            return max(nums[0], nums[1])
        
        dp = [0] * num_of_houses
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for idx in range(2, num_of_houses):
            dp[idx] = max(nums[idx] + dp[idx - 2], dp[idx - 1])
            
        return dp[-1]