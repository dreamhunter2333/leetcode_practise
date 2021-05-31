#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
        # return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0

# @lc code=end
