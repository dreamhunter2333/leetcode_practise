#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        sell = [0] * n
        buy = [-prices[0]] + [0] * (n - 1)
        for i in range(1, n):
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            sell[i] = max(sell[i-1], buy[i] + prices[i])
        return sell[-1]


print(Solution().maxProfit([1, 2, 3, 0, 2]))
# @lc code=end
