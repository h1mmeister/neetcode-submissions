class Solution:
    def __init__(self):
        self.cache = {}

    def climbStairs(self, n: int) -> int:
        return self.helper(n)

    def helper(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        if n in self.cache:
            return self.cache[n]

        self.cache[n] = self.helper(n-1) + self.helper(n-2)

        return self.cache[n]

        