#
# @lc app=leetcode.cn id=790 lang=python3
#
# [790] 多米诺和托米诺平铺
#

# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0, 0, 0, 0] for _ in range(n)]
        dp[0][0] = 1
        dp[0][1] = 1

        for i in range(1, n):
            dp[i][0] = dp[i-1][1]
            dp[i][1] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3]
            dp[i][2] = dp[i-1][0] + dp[i-1][3]
            dp[i][3] = dp[i-1][0] + dp[i-1][2]

        return dp[n-1][1] % mod


# @lc code=end
print(Solution().numTilings(4))
