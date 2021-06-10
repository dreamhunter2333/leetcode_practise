#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0
        while n > 4:
            n //= 5
            zero_count += n
        return zero_count

# @lc code=end
