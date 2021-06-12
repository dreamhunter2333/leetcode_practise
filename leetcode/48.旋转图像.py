#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_m = len(matrix)
        len_n = len_m - 1
        start = -1

        while len_m > 1:
            start += 1
            for i in range(start, start+len_m-1):
                (
                    matrix[start][i],
                    matrix[i][len_n-start],
                    matrix[len_n-start][len_n-i],
                    matrix[len_n-i][start]
                ) = (
                    matrix[len_n-i][start],
                    matrix[start][i],
                    matrix[i][len_n-start],
                    matrix[len_n-start][len_n-i],
                )
            len_m -= 2


a = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
Solution().rotate(a)
print(a)
# @lc code=end
