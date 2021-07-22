#
# @lc app=leetcode.cn id=1893 lang=python3
#
# [1893] 检查是否区域内所有整数都被覆盖
#

# @lc code=start
from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        def get_new(p1, p2, q1, q2):
            # p 包含 q
            if p1 <= q1 and q2 <= p2:
                return []
            # q 包含 p
            if q1 < p1 and p2 < q2:
                return [(q1, p1-1), (p2+1, q2)]
            # p q 有交集
            if p1 <= q1 and q1 <= p2 < q2:
                return [(p2+1, q2)]
            if q1 < p1 <= q2 and p2 >= q2:
                return [(q1, p1-1)]
            # p q 无交集
            if p2 < q1 or p1 > q2:
                return [(q1, q2)]
            if p2 == q1 and q2 > q1:
                return [(q1+1, q2)]
            if p1 == q2 and q2 > q1:
                return [(q1, q2-1)]
            return []

        stack = [(left, right)]
        for i1, i2 in ranges:
            n = len(stack)
            for _ in range(n):
                j1, j2 = stack.pop(0)
                stack.extend(get_new(i1, i2, j1, j2))

        return not stack


print(Solution().isCovered(
    [[37, 49], [5, 17], [8, 32]],
    29,
    49,
))
# @lc code=end
