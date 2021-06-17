#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        after_sum = 0
        while num1 and num2:
            num1, cur_a = num1[:-1], num1[-1]
            num2, cur_b = num2[:-1], num2[-1]
            cur_sum = int(cur_a) + int(cur_b) + after_sum
            after_sum = cur_sum // 10
            cur_sum = cur_sum % 10
            res.append(str(cur_sum))

        if num1:
            res.append(str(int(num1)+after_sum))
        elif num2:
            res.append(str(int(num2)+after_sum))
        elif after_sum:
            res.append(str(after_sum))

        return ''.join(reversed(res))

# @lc code=end
