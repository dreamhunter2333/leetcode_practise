#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        dp = [0] * (days+1)

        for i in range(1, days+1):
            dp[i] = max([
                dp[j] + prices[i-1] - prices[j+1]
                for j in range(i-2)
            ] + [prices[i-1] - prices[0], dp[i-1], 0])
        print(dp)
        return dp[-1]


print(Solution().maxProfit([1, 2, 3, 0, 2]))
# @lc code=end
