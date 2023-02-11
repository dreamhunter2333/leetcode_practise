#
# @lc app=leetcode.cn id=2335 lang=python3
#
# [2335] 装满杯子需要的最短总时长
#
from typing import List


# @lc code=start
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        if amount[2] > amount[1] + amount[0]:
            return amount[2]
        return (sum(amount) + 1) // 2


# @lc code=end
print(Solution().fillCups([1, 4, 2]))
print(Solution().fillCups([5, 4, 4]))
