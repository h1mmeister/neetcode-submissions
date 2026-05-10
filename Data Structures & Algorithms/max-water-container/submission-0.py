class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 

        for i in range(0, len(heights) - 1):
            first_pillar = heights[i]
            for j in range(i + 1, len(heights)):
                second_pillar = heights[j]

                min_pillar = min(first_pillar, second_pillar)
                curr_area = min_pillar * (j - i)
                max_area = max(max_area, curr_area)

        return max_area
        