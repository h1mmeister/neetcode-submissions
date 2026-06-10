class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        running_sum = 0

        left = 0
        for right, value in enumerate(nums):
            running_sum += value

            while running_sum >= target:
                min_length = min(min_length, right -left + 1)
                running_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0
        