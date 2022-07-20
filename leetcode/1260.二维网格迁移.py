#
# @lc app=leetcode.cn id=1260 lang=python3
#
# [1260] 二维网格迁移
#
from typing import List


# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not grid or not grid[0]:
            return grid
        m = len(grid)
        n = len(grid[0])
        res = [
            grid[i][j]
            for i in range(m - 1, -1, -1)
            for j in range(n - 1, -1, -1)
        ]

        for _ in range(k):
            res.append(res.pop(0))

        return [
            [
                res.pop()
                for j in range(n)
            ]
            for i in range(m)
        ]


# @lc code=end
print(Solution().shiftGrid(
    grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    k=1
))
print(Solution().shiftGrid(
    grid=[[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]],
    k=4
))
