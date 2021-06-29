#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        pre_ord = ord('A') - 1
        while columnNumber > 0:
            temp = columnNumber % 26 or 26
            res.append(pre_ord + temp)
            columnNumber = columnNumber // 26 - temp // 26
        return ''.join(map(chr, reversed(res)))


print(Solution().convertToTitle(52))
# @lc code=end
