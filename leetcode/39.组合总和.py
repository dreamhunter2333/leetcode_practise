#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def dfs(path, i=0):
            if sum(path) == target:
                res.append(path[:])
                return
            elif sum(path) > target:
                return
            for j in range(i, n):
                path.append(candidates[j])
                dfs(path, j)
                path.pop()

        dfs([])

        return res

# @lc code=end
