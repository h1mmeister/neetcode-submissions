class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            first_pillar = heights[left]
            second_pillar = heights[right]

            min_height = min(first_pillar, second_pillar)
            curr_area  = min_height * (right - left)

            max_area = max(max_area, curr_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area