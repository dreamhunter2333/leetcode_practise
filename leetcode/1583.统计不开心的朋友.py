#
# @lc app=leetcode.cn id=1583 lang=python3
#
# [1583] 统计不开心的朋友
#

# @lc code=start
from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        order = [
            {preferences[i][j]: j for j in range(n - 1)}
            for i in range(n)
        ]

        match = [0] * n
        for x, y in pairs:
            match[x] = y
            match[y] = x

        res = 0
        for x in range(n):
            y = match[x]
            index = order[x].get(y, 0)
            for i in range(index):
                u = preferences[x][i]
                v = match[u]
                if order[u].get(x, 0) < order[u].get(v, 0):
                    res += 1
                    break

        return res

# @lc code=end
