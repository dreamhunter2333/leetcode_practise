#
# @lc app=leetcode.cn id=2544 lang=python3
#
# [2544] 交替数字和
#

# @lc code=start
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        flag = -1
        while n:
            flag = 0 - flag
            delta = n % 10
            res += flag * delta
            n = n // 10
        return res * flag


# @lc code=end
print(Solution().alternateDigitSum(521))
print(Solution().alternateDigitSum(111))
print(Solution().alternateDigitSum(886996))
