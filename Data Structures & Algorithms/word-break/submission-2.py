class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for idx in range(n - 1, -1, -1):
            for word in wordDict:
                if idx + len(word) <= len(s) and s[idx : idx + len(word)] == word:
                    dp[idx] = dp[idx + len(word)]
                    if dp[idx]:
                        break

        return dp[0]

        