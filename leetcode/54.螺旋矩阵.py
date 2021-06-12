#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return

        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        max_len = (right+1) * (bottom+1)

        res = []
        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            for j in range(right, left-1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1

            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1

        return res[:max_len]


print(Solution().spiralOrder([[6, 9, 7]]))
# @lc code=end
