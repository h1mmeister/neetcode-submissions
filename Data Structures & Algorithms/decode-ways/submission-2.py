class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1

        for idx in range(n - 1, -1, -1):
            if s[idx] == '0':
                dp[idx] = 0
            else:
                dp[idx] = dp[idx + 1]

            if idx + 1 < n:
                two_digits = int(s[idx : idx + 2])
                if 10 <= two_digits <= 26:
                    dp[idx] += dp[idx + 2]

        return dp[0]
        