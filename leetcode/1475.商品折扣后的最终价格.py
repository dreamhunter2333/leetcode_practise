#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#
from typing import List


# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)

        def find(i: int) -> int:
            for j in range(i+1, n):
                if prices[i] >= prices[j]:
                    return prices[i] - prices[j]
            return prices[i]

        return [
            find(i)
            for i in range(n)
        ]

# @lc code=end
