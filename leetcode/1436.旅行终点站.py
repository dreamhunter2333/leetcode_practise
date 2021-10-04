#
# @lc app=leetcode.cn id=1436 lang=python3
#
# [1436] 旅行终点站
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        route = defaultdict(set)
        for c1, c2 in paths:
            route[c1].add(c2)
            route[c2] = route[c2]
        for r, v in route.items():
            if not v:
                return r
        return ""

# @lc code=end
