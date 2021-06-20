#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = max(max(i - j, dp[i-j]) * j for j in range(1, i))
        return dp[n]


# print(Solution().integerBreak(10))
# @lc code=end
