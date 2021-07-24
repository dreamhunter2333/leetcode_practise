#
# @lc app=leetcode.cn id=1736 lang=python3
#
# [1736] 替换隐藏数字得到的最晚时间
#

# @lc code=start
class Solution:
    def maximumTime(self, time: str) -> str:
        h1, h2, sp, m1, m2 = time

        if h1 == h2 == '?' or (h1 == '2' and h2 == '?'):
            h1 = '2'
            h2 = '3'
        elif h2 == '?':
            h2 = '9'
        elif h1 == '?':
            h1 = '2' if h2 in ('0', '1', '2', '3') else '1'

        return ''.join([
            h1, h2, sp,
            '5' if m1 == '?' else m1,
            '9' if m2 == '?' else m2
        ])

# @lc code=end
