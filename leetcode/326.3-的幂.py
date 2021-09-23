#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3 ** 32 % n == 0

# @lc code=end
