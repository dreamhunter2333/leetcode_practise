#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy = [-prices[0]] + [0] * (n - 1)
        sell = [0] * n
        for i in range(1, n):
            buy[i] = max(buy[i-1], sell[i-1] - prices[i])
            sell[i] = max(sell[i-1], buy[i] + prices[i] - fee)
        return sell[-1]


# @lc code=end
