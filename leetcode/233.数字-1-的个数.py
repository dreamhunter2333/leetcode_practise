#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        res = 0

        digit = 1
        cur = n % 10
        left = n // 10
        right = 0

        while left != 0 or cur != 0:
            if cur == 0:
                res += left * digit
            elif cur == 1:
                res += left * digit + right + 1
            else:
                res += (left + 1) * digit

            right += digit * cur
            cur = left % 10
            left = left // 10
            digit *= 10

        return res


# @lc code=end
