#
# @lc app=leetcode.cn id=1418 lang=python3
#
# [1418] 点菜展示表
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        cache_map = defaultdict(lambda: defaultdict(int))

        for name, table, food in orders:
            foods.add(food)
            cache_map[table][food] += 1

        foods = sorted(foods)

        return [
            ["Table"] + foods,
            *[
                [t] + [str(cache_map[t][f]) for f in foods]
                for t in sorted(cache_map, key=lambda k: int(k))
            ]
        ]


# @lc code=end
