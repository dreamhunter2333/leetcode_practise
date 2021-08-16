#
# @lc app=leetcode.cn id=526 lang=python3
#
# [526] 优美的排列
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countArrangement(self, n: int) -> int:
        cache = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    cache[i].append(j)

        res = 0
        vis = set()

        def dfs(index=1):
            if index == n + 1:
                nonlocal res
                res += 1
                return

            for x in cache[index]:
                if x not in vis:
                    vis.add(x)
                    dfs(index + 1)
                    vis.discard(x)

        dfs()
        return res

# @lc code=end
