#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = []
        count = 0
        for c in s[::-1]:
            if c == '-':
                continue
            if count == k:
                count = 0
                res.append('-')
            res.append(c.upper())
            count += 1
        return ''.join(reversed(res))

# @lc code=end
