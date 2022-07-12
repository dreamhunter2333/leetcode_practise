#
# @lc app=leetcode.cn id=1252 lang=python3
#
# [1252] 奇数值单元格的数目
#
from typing import List


# @lc code=start
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        cache_r = [0] * m
        cache_c = [0] * n
        for r, c in indices:
            cache_r[r] += 1
            cache_c[c] += 1
        return sum(
            (cache_r[r] + cache_c[c]) % 2
            for r in range(m)
            for c in range(n)
        )


# @lc code=end
print(Solution().oddCells(m=2, n=3, indices=[[0, 1], [1, 1]]))
print(Solution().oddCells(m=2, n=2, indices=[[1, 1], [0, 0]]))
