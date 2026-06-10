class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        running_sum = 0

        left = 0
        for right in range(len(nums)):
            right_elem = nums[right]
            running_sum += right_elem

            while running_sum >= target:
                min_length = min(min_length, right - left + 1)
                left_elem = nums[left]
                running_sum -= left_elem
                left += 1

        return min_length if min_length != float('inf') else 0


        