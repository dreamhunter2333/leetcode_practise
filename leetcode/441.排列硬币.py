#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((pow(8 * n + 1, 0.5) - 1) / 2)

# @lc code=end
