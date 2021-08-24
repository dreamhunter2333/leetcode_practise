#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        route_map = defaultdict(list)
        for f1, f2, f3 in flights:
            route_map[f1].append((f2, f3))
        stack = [(src, 0, -1)]
        cache_map = {}
        res = float("inf")
        while stack:
            cur_pos, price, count = stack.pop(0)
            if cur_pos == dst and count <= k:
                res = min(res, price)
            if price >= cache_map.get(cur_pos, float('inf')) or count >= k:
                continue
            cache_map[cur_pos] = price
            stack.extend([
                (next_pos, price + add_price, count + 1)
                for next_pos, add_price in route_map[cur_pos]
            ])
        return -1 if res == float("inf") else res

# @lc code=end
