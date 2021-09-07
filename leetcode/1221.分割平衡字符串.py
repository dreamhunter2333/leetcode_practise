#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        l = 0
        for ch in s:
            if ch == 'L':
                l += 1
            else:
                l -= 1
            if l == 0:
                res += 1
        return res

# @lc code=end
