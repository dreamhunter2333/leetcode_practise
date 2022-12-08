#
# @lc app=leetcode.cn id=1812 lang=python3
#
# [1812] 判断国际象棋棋盘中一个格子的颜色
#

# @lc code=start
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (
            ord(coordinates[0]) - ord('a') + 1
            +
            int(coordinates[1])
        ) % 2 == 1


# @lc code=end
print(Solution().squareIsWhite("a1"))
print(Solution().squareIsWhite("h3"))
print(Solution().squareIsWhite("c7"))
