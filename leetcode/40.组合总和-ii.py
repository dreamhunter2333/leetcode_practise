#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        def dfs(path, i=0):
            if sum(path) == target:
                res.append(path[:])
                return True
            elif sum(path) > target:
                return True
            for j in range(i, n):
                # 剪枝
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                path.append(candidates[j])
                kk = dfs(path, j+1)
                path.pop()
                if kk:
                    return

        dfs([])

        return res


print(Solution().combinationSum2(
    [2, 5, 2, 1, 2],
    5
))

# @lc code=end
