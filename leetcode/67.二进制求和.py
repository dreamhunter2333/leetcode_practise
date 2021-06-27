#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []

        carry = 0
        n = len(a)
        m = len(b)

        for i in range(max(n, m)):
            if i < n:
                carry += int(a[n-1-i])
            if i < m:
                carry += int(b[m-1-i])

            res.append(str(carry % 2))
            carry = carry // 2

        if carry:
            res.append('1')

        return ''.join(reversed(res))


# @lc code=end
