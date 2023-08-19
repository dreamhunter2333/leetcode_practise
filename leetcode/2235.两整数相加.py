#
# @lc app=leetcode.cn id=2235 lang=python3
#
# [2235] 两整数相加
#

# @lc code=start
class Solution:
    def sum(self, num1: int, num2: int) -> int:

        MAX_POSTIVE_INT = 0x8000_0000
        MASK = 0xffff_ffff

        while num2:
            num_low = (num1 ^ num2) & MASK
            num2 = ((num1 & num2) << 1) & MASK
            num1 = num_low

        return (
            num1
            if num1 < MAX_POSTIVE_INT
            else
            ~(num1 ^ MASK)
        )


# @lc code=end
print(Solution().sum(-100, -100))
