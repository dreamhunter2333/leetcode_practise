#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res = []
        flag = ""
        if num < 0:
            num = - num
            flag = "-"
        while num > 0:
            res.append(num % 7)
            num = num // 7
        return flag + "".join(map(str, res[::-1]))


# print(Solution().convertToBase7(100))
# @lc code=end
