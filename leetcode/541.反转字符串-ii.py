#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        index = 0
        n = len(s)
        while index < n:
            for i in range(min(index + k - 1, n - 1), index - 1, -1):
                res += s[i]
            for i in range(index + k, min(index + 2 * k, n)):
                res += s[i]
            index = index + 2 * k
        return res

# @lc code=end
