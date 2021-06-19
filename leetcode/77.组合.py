#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def dfs(cur, path):
            if len(path) == k:
                res.append(path[:])
                return
            # 剪枝
            if len(path) + (n - cur + 1) < k:
                return
            path.append(cur)
            dfs(cur + 1, path)
            path.pop()
            dfs(cur + 1, path)

        dfs(1, [])

        return res

# @lc code=end
