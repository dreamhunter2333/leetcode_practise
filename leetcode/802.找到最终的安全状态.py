#
# @lc app=leetcode.cn id=802 lang=python3
#
# [802] 找到最终的安全状态
#

# @lc code=start
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        res = [None] * n

        def dfs(i):
            if res[i] is not None:
                return res[i]
            res[i] = False
            for j in graph[i]:
                if not dfs(j):
                    return False
            res[i] = True
            return True

        return [i for i in range(n) if dfs(i)]


print(Solution().eventualSafeNodes([[0], [2, 3, 4], [3, 4], [0, 4], []]))
# @lc code=end
