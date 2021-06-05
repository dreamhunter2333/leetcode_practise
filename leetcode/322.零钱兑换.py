#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [2**31] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] = min(1 + dp[j-coin], dp[j])
        return -1 if dp[amount] == 2**31 else dp[amount]


print(Solution().coinChange(coins=[1, 2, 5], amount=11))
# @lc code=end
