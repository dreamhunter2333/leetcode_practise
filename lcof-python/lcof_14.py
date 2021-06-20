"""
剑指 Offer 14- I. 剪绳子
剑指 Offer 14- II. 剪绳子 II
"""


class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = max(
                max(i-j, dp[i-j]) * j for j in range(1, i)
            )
        return dp[n]

    def cuttingRope2(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = max(
                max(i-j, dp[i-j]) * j for j in range(1, i)
            )
        return dp[n] % (10 ** 9 + 7)
