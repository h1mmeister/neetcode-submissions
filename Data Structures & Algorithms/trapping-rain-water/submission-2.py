class Solution:
    def trap(self, height: List[int]) -> int:
        water_stored = 0
        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        while left < right:
            if left_max < right_max:
                water_stored += max(0, left_max - height[left])
                left += 1
                left_max = max(left_max, height[left])

            else:
                water_stored += max(0, right_max - height[right])
                right -= 1
                right_max = max(right_max, height[right])

        return water_stored


        