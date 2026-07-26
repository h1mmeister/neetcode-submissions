class Solution:
    def trap(self, height: List[int]) -> int:
        water_stored = 0

        for idx in range(1, len(height) - 1):
            left_max = max(height[:idx])
            right_max = max(height[idx + 1:])
            min_height = min(left_max, right_max)
            water_stored += max(0, min_height - height[idx])

        return water_stored
        