class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def dfs(idx):
            if idx >= len(s):
                return 1
            if s[idx] == '0':
                return 0
            if idx in cache:
                return cache[idx]

            one_digit = dfs(idx + 1)

            two_digits = 0
            if idx + 1 < len(s):
                digits = int(s[idx : idx + 2])
                if 10 <= digits <= 26:
                    two_digits = dfs(idx + 2)

            cache[idx] = one_digit + two_digits
            return cache[idx]

        return dfs(0)
        