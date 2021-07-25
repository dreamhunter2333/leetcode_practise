#
# @lc app=leetcode.cn id=1743 lang=python3
#
# [1743] 从相邻元素对还原数组
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        node_map = defaultdict(set)
        res = []

        for val1, val2 in adjacentPairs:
            node_map[val1].add(val2)
            node_map[val2].add(val1)

        val = None
        for k in node_map:
            if len(node_map[k]) == 2:
                continue
            val = k
            break

        pre_val = None

        while val is not None:
            res.append(val)
            next_val = None
            for item_val in node_map[val]:
                if item_val != pre_val:
                    next_val = item_val
                    break
            pre_val = val
            val = next_val

        return res

# @lc code=end
