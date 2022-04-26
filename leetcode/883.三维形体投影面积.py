#
# @lc app=leetcode.cn id=883 lang=python3
#
# [883] 三维形体投影面积
#

# @lc code=start
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        max_y_z = [0] * n
        for x in range(n):
            max_z = 0
            for y in range(n):
                if grid[x][y] == 0:
                    continue
                res += 1
                max_z = max(max_z, grid[x][y])
                max_y_z[y] = max(max_y_z[y], grid[x][y])
            res += max_z
        res += sum(max_y_z)
        return res


# print(Solution().projectionArea([[1, 2], [3, 4]]))
# @lc code=end
