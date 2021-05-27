#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while True:
            x, x0 = (x // 2, x % 2) if x >= 2 else (0, x)
            y, y0 = (y // 2, y % 2) if y >= 2 else (0, y)

            if x0 != y0:
                res += 1

            if x == y == 0:
                break

        return res
# @lc code=end
