#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#

# @lc code=start
class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        delta = ord('a') - ord('A')
        for c in s:
            if ord('A') <= ord(c) <= ord('Z'):
                c = chr(ord(c) + delta)
            res += c
        return res

# @lc code=end
