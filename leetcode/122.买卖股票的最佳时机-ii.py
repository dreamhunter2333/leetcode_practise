#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心
        # res = 0
        # for i in range(1, len(prices)):
        #     delta = prices[i] - prices[i-1]
        #     if delta > 0:
        #         res += delta
        # return res

        # 动态规划
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], dp[i-1] + prices[i] - prices[i-1])
        return dp[-1]


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
# @lc code=end
