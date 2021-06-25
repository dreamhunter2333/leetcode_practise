#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        x, y = 0, 1
        for _ in range(n-1):
            x, y = y, x + y

        return y

# @lc code=end
