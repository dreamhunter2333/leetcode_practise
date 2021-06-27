#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows == 1:
            return s
        cache = [""] * numRows
        n = len(s)
        i = 0
        flag = 0
        flag_z = numRows - 1
        flag_new = 2 * numRows - 2
        for i in range(n):
            if flag == flag_new:
                flag = 0
            if flag < flag_z:
                cache[flag] += s[i]
            else:
                j = flag_z - flag % flag_z
                cache[j] += s[i]
            flag += 1
        return ''.join(cache)

# @lc code=end
