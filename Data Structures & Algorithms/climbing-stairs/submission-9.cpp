class Solution {
public:
    int climbStairs(int n) {
        if (n == 1) return 1;
        if (n == 2) return 2;

        vector<int> dp(n + 1, 0);
        dp[1] = 1;
        dp[2] = 2;

        for (int idx = 3; idx < n + 1; ++idx) {
            dp[idx] = dp[idx - 1] + dp[idx - 2];
        }

        return dp[n];
    }
};
