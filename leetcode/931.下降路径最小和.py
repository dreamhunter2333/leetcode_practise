#
# @lc app=leetcode.cn id=931 lang=python3
#
# [931] 下降路径最小和
#
from typing import List


# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix[0]
        for i in range(1, n):
            new_dp = [float("inf")] * n
            for j in range(n):
                new_dp[j] = matrix[i][j] + min(
                    dp[j - 1 + p]
                    for p in range(3)
                    if 0 <= j - 1 + p < n
                )
            dp = new_dp
        return min(dp)


# @lc code=end
print(Solution().minFallingPathSum([
    [2, 1, 3], [6, 5, 4], [7, 8, 9]
]))
print(Solution().minFallingPathSum(
    [[-19, 57], [-40, -5]]
))
print(Solution().minFallingPathSum([
    [100, -42, -46, -41],
    [31, 97, 10, -10],
    [-58, -51, 82, 89],
    [51, 81, 69, -51]
]))
