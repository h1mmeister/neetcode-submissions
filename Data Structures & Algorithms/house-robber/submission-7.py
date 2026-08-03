class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        next1, next2 = 0, 0

        for idx in range(len(nums) - 1, -1, -1):
            curr = max(nums[idx] + next2, next1)
            next2, next1 = next1, curr

        return next1
        