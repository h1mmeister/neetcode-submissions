class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def rob_helper(idx):
            if idx >= len(nums):
                return 0

            if idx in cache:
                return cache[idx]

            picked_house = nums[idx] + rob_helper(idx + 2)
            not_picked_house = rob_helper(idx + 1)
            cache[idx] = max(picked_house, not_picked_house)
            return cache[idx]

        return rob_helper(0)
        