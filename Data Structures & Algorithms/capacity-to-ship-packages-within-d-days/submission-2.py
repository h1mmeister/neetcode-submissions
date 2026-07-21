class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        result = right

        def check(capacity):
            count = 1
            cap = capacity

            for weight in weights:
                if cap - weight < 0:
                    count += 1
                    cap = capacity
                cap -= weight

            return count <= days


        while left <= right:
            capacity = left + (right - left) // 2
            if check(capacity):
                result = min(capacity, result)
                right = capacity - 1
            else:
                left = capacity + 1

        return result
                


        