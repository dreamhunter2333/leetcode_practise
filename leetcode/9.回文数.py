#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0 or (x % 10 == 0 and x != 0)):
            return False

        res = 0
        temp = x

        while res < temp:
            res = 10 * res + temp % 10
            temp = temp // 10

        return res == temp or res // 10 == temp
# @lc code=end
