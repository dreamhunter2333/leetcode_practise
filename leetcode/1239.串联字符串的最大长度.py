#
# @lc app=leetcode.cn id=1239 lang=python3
#
# [1239] 串联字符串的最大长度
#

# @lc code=start
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = ['']
        for a in arr:
            if len(a) != len(set(a)):
                continue
            dp.extend([
                d + a
                for d in dp
                if len(d + a) == len(set(d + a))
            ])
        return len(max(dp, key=len))

# @lc code=end
