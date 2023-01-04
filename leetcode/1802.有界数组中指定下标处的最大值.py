#
# @lc app=leetcode.cn id=1802 lang=python3
#
# [1802] 有界数组中指定下标处的最大值
#

# @lc code=start
import math


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        res = 1
        res1 = int(math.sqrt(maxSum - n)) + 1
        if res1 <= min(index + 1, n - index):
            res = max(res, res1)

        c = (
            - 2 * (maxSum - n) + 2 -
            (n - index) * (n - index + 1)
        )
        b = 2 * n - 2 * index - 3
        if b * b >= 4 * c:
            res2 = int((math.sqrt(b * b - 4 * c) - b) // 2)
            if res2 > n - index and res2 <= index + 1:
                res = max(res, res2)

        c = (
            - 2 * (maxSum - n) + 2 -
            (index + 1) * (index + 2)
        )
        b = 2 * index - 1
        if b * b >= 4 * c:
            res3 = int((math.sqrt(b * b - 4 * c) - b) // 2)
            if res3 <= n - index and res3 > index + 1:
                res = max(res, res3)

        res4 = int((
            (index + 1) * (index + 2)
            +
            (n - index) * (n - index + 1)
            + 2 * (maxSum - n) - 2
        ) // (2 * n))
        if res4 > n - index and res4 > index + 1:
            res = max(res, res4)

        return res


# @lc code=end
print(Solution().maxValue(4, 2, 6))
print("====")
print(Solution().maxValue(6, 1, 10))
