#
# @lc app=leetcode.cn id=1744 lang=python3
#
# [1744] 你能在你最喜欢的那天吃到你最喜欢的糖果吗？
#

# @lc code=start
from typing import List
from itertools import accumulate


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        res = []

        candy_sum = list(accumulate(candiesCount))
        candy_sum.append(0)

        for query in queries:
            candy_type, day_index, max_candy_count = query
            res.append(
                candy_sum[candy_type-1] < (day_index+1) * max_candy_count
                and
                candy_sum[candy_type] >= day_index+1
            )
        return res


print(Solution().canEat(
    [7, 11, 5, 3, 8],
    [[2, 2, 6]]
))
# @lc code=end
