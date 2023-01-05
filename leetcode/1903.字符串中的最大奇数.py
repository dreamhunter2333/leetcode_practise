#
# @lc app=leetcode.cn id=1903 lang=python3
#
# [1903] 字符串中的最大奇数
#

# @lc code=start
ODD = {"1", "3", "5", "7", "9"}


class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if num[i] in ODD:
                return num[:i+1]
        return ""


# @lc code=end
print(Solution().largestOddNumber("52"))
print(Solution().largestOddNumber("4206"))
print(Solution().largestOddNumber("35427"))
