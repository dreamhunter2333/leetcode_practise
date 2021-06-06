#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = 10000
        max_profit = 0
        for p in prices:
            if p > min_p:
                max_profit = max(max_profit, p-min_p)
            else:
                min_p = p
        return max_profit

# @lc code=end
