#
# @lc app=leetcode.cn id=1104 lang=python3
#
# [1104] 二叉树寻路
#

# @lc code=start
from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        label_bin = bin(label)
        m = len(label_bin) - 2
        if m % 2 == 0:
            n = 2 ** m - label
        else:
            n = label + 1 - 2 ** (m - 1)

        res = []

        while m:
            if m % 2 == 0:
                res.append(2 ** m - n)
            else:
                res.append(2 ** (m - 1) + n - 1)
            m -= 1
            n = n // 2 + n % 2

        res.reverse()
        return res

# @lc code=end
