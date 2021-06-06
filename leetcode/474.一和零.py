#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        # 三维 dp
        # strs_len = len(strs)
        # dp = [
        #     [[0] * (n+1) for _ in range(m+1)]
        #     for _ in range(strs_len+1)
        # ]

        # for i in range(1, strs_len+1):
        #     count0 = strs[i-1].count('0')
        #     count1 = strs[i-1].count('1')
        #     for j in range(m+1):
        #         for k in range(n+1):
        #             dp[i][j][k] = dp[i-1][j][k]
        #             if j < count0 or k < count1:
        #                 continue
        #             dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-count0][k-count1] + 1)

        # return dp[strs_len][m][n]

        # 二维 dp
        dp = [[0] * (n+1) for _ in range(m+1)]

        for s in strs:
            count0 = s.count('0')
            count1 = s.count('1')
            for j in range(m, count0 - 1, -1):
                for k in range(n, count1 - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j-count0][k-count1] + 1)

        return dp[m][n]


print(Solution().findMaxForm(
    ["10", "0001", "111001", "1", "0"],
    5,
    3
))
# @lc code=end
