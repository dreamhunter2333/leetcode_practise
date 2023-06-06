#
# @lc app=leetcode.cn id=2352 lang=python3
#
# [2352] 相等行列对
#

from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = defaultdict(int)
        for g in grid:
            count[f"{g}"] += 1
        res = 0
        n = len(grid)
        for i in range(n):
            key = [grid[j][i] for j in range(n)]
            res += count[f"{key}"]

        return res


# @lc code=end
print(Solution().equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
print(Solution().equalPairs(
    [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
))
