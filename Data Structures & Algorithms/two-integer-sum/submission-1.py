class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                total = nums[i] + nums[j]
                if total == target:
                    return [i, j]
                


        