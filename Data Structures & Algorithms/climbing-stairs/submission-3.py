class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        
        def helper(n):
            nonlocal cache 
            if n == 1:
                return 1
            if n == 2:
                return 2

            if n in cache:
                return cache[n]

            cache[n] = helper(n-1) + helper(n-2)
            return cache[n]

        return helper(n)
        