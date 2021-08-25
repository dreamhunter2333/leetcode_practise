#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

# @lc code=start
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        stack = [[0]]
        while stack:
            path = stack.pop(0)
            cur = path[-1]
            if cur == n - 1:
                res.append(path)
                continue
            stack.extend(
                path + [i]
                for i in graph[cur]
            )
        return res

# @lc code=end
