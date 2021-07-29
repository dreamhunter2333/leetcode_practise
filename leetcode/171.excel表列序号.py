#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        return sum(
            (ord(columnTitle[n - i]) - ord('A') + 1) * (26 ** (i - 1))
            for i in range(1, n + 1)
        )

# @lc code=end
