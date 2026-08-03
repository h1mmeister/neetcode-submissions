class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp  = [0] * (n + 2)

        for idx in range(n - 1, -1, -1):
            dp[idx] = max(nums[idx] + dp[idx + 2], dp[idx + 1])

        return dp[0]
        