#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        # return (num - 1) % 9 + 1 if num else 0
        while num > 9:
            temp = 0
            while num > 0:
                temp += num % 10
                num = num // 10
            num = temp
        return num


# print(Solution().addDigits(999))
# @lc code=end
