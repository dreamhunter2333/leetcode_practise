#
# @lc app=leetcode.cn id=1337 lang=python3
#
# [1337] 矩阵中战斗力最弱的 K 行
#

# @lc code=start
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        data = {
            i: sum(mat[i])
            for i in range(len(mat))
        }
        return sorted(range(len(mat)), key=lambda k: data[k])[:k]

# @lc code=end
