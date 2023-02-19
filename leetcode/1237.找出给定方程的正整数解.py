#
# @lc app=leetcode.cn id=1237 lang=python3
#
# [1237] 找出给定方程的正整数解
#

# @lc code=start
from typing import List


class Solution:
    def findSolution(self, customfunction, z: int) -> List[List[int]]:
        ans = []
        y = 1000
        for x in range(1, 1001):
            while y and customfunction.f(x, y) > z:
                y -= 1
            if y == 0:
                break
            if customfunction.f(x, y) == z:
                ans.append([x, y])
        return ans

# @lc code=end
