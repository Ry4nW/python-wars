class Solution:
    def solve(self, weights, values, capacity):
        dp = [[0 for i in range(capacity + 1)] for _ in range(len(values) + 1)]

        for j in range(1, len(values) + 1):
            for i in range(1, capacity + 1):
                if weights[j - 1] > i:
                    dp[j][i] = dp[j - 1][i]
                else:
                    dp[j][i] = max(dp[j - 1][i], values[j - 1] + dp[j - 1][i - weights[j - 1]])
        
        return dp[len(values)][capacity]
