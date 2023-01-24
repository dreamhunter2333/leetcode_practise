#
# @lc app=leetcode.cn id=1828 lang=python3
#
# [1828] 统计一个圆中点的数目
#
from typing import List


# @lc code=start
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for xj, yj, rj in queries:
            cur_count = 0
            for xi, yi in points:
                if (xj - xi) ** 2 + (yj - yi) ** 2 > rj ** 2:
                    continue
                cur_count += 1
            res.append(cur_count)
        return res


# @lc code=end
print(Solution().countPoints(
    points=[[1, 3], [3, 3], [5, 3], [2, 2]],
    queries=[[2, 3, 1], [4, 3, 1], [1, 1, 2]]
))
