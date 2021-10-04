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
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '-':
                continue
            res.append(s[i].upper())
            count += 1
            if count == k:
                count = 0
                res.append('-')
        if len(res) % (k + 1) == 0 and res:
            res.pop()
        return ''.join(reversed(res))

# @lc code=end
