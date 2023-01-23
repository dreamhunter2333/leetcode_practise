#
# @lc app=leetcode.cn id=2303 lang=python3
#
# [2303] 计算应缴税款总额
#
from typing import List


# @lc code=start
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res = 0
        pre_upper = 0
        for upper, percent in brackets:
            if income < upper:
                res += (income - pre_upper) * percent
                break
            res += (upper - pre_upper) * percent
            pre_upper = upper
        return res / 100


# @lc code=end
print(Solution().calculateTax(
    brackets=[[3, 50], [7, 10], [12, 25]], income=10
))
print(Solution().calculateTax(
    brackets=[[1, 0], [4, 25], [5, 50]], income=2
))
print(Solution().calculateTax(
    brackets=[[2, 50]], income=0
))
