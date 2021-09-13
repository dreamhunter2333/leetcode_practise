#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for x1, y1 in points:
            count = defaultdict(int)
            for x2, y2 in points:
                z = (x2 - x1) ** 2 + (y2 - y1) ** 2
                count[z] += 1
            res += sum(c * (c - 1) for c in count.values())
        return res


# @lc code=end
