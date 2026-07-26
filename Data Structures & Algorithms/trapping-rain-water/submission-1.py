class Solution:
    def trap(self, height: List[int]) -> int:
        water_stored = 0

        left = [0] * len(height)
        right = [0] * len(height)

        left[0] = height[0]
        for idx in range(1, len(height)):
            left[idx] = max(left[idx - 1], height[idx])

        right[len(height) - 1] = height[len(height) - 1]
        for idx in range(len(height) - 2,-1, -1):
            right[idx] = max(right[idx + 1], height[idx])

        for idx in range(len(height)):
            water_stored += min(left[idx], right[idx]) - height[idx]

        return water_stored

        