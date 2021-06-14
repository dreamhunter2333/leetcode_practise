#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        x = 0
        y = 0

        max_y = len(matrix[0])

        while x < len(matrix):
            if matrix[x][y] == target:
                return True
            if matrix[x][y] < target:
                y += 1
                if y >= max_y:
                    y = 0
                    x += 1
            else:
                break

        return False

# @lc code=end
