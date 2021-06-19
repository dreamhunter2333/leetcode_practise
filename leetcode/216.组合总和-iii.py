#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(path: List[int], start: int = 1):
            if sum(path) == n and len(path) == k:
                res.append(path[:])
                return
            if sum(path) > n or len(path) >= k:
                return
            for i in range(start, 10):
                path.append(i)
                dfs(path, i+1)
                path.pop()

        dfs([])

        return res


# print(Solution().combinationSum3(3, 9))
# @lc code=end
