#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        x = 0
        y = len(matrix[0]) - 1

        while 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
            if matrix[x][y] == target:
                return True
            if matrix[x][y] < target:
                x += 1
            else:
                y -= 1

        return False

# @lc code=end
