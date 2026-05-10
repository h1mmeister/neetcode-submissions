class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) + 1 

        while left <= right:
            speed = left + (right - left) // 2 

            hours = 0

            for idx in range(0, len(piles)):
                num = piles[idx]
                hours += math.ceil(num / speed)

            if hours <= h:
                right = speed - 1
            else:
                left = speed + 1

        return left

