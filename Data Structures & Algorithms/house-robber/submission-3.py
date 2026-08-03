class Solution:
    def rob(self, nums: List[int]) -> int:
        self.cache = {}
        return self.rob_helper(nums, 0)

    def rob_helper(self, nums, idx):
        if idx >= len(nums):
            return 0

        if idx in self.cache:
            return self.cache[idx]

        picked_house = nums[idx] + self.rob_helper(nums, idx + 2)
        not_picked_house = self.rob_helper(nums, idx + 1)
        self.cache[idx] = max(picked_house, not_picked_house)

        return self.cache[idx]
        