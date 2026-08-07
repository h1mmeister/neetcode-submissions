class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for remaining in range(1, amount + 1):
            for coin in coins:
                if coin <= remaining:
                    dp[remaining] = min(dp[remaining], 1 + dp[remaining - coin])

        return -1 if dp[amount] == float("inf") else dp[amount]
        