#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [n] * n
        cache = [z * z for z in range(n)]

        for i in range(1, n+1):
            for j in range(1, i):
                j2 = cache[j]
                if j2 > i:
                    break
                if i == j2:
                    dp[i] = 1
                    break
                if j2 < i:
                    dp[i] = min(dp[i - j2]+1, dp[i])

        return dp[-1]

# @lc code=end
