class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]
        def dfs(idx, prev_idx):
            if idx >= len(nums):
                return 0
            if memo[idx][prev_idx + 1] != -1:
                return memo[idx][prev_idx + 1]

            LIS = 0 + dfs(idx + 1, prev_idx)

            if prev_idx == -1 or nums[idx] > nums[prev_idx]:
                LIS = max(LIS, 1 + dfs(idx + 1, idx))

            memo[idx][prev_idx + 1] = LIS
            return LIS
        return dfs(0, -1)
        