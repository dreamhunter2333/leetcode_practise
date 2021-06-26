#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 1
        n = len(digits)
        for i in range(n-1, -1, -1):
            temp = digits[i] + num
            num = temp // 10
            digits[i] = temp % 10
        if num:
            digits.insert(0, num)

        return digits

# @lc code=end
