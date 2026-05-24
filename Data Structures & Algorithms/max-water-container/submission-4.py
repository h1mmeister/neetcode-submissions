class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            first_bar = heights[left]
            second_bar = heights[right]

            curr_max_area = min(first_bar, second_bar) * (right - left)
            max_area = max(max_area, curr_max_area)

            if first_bar < second_bar:
                left += 1
            else:
                right -= 1

        return max_area