#
# @lc app=leetcode.cn id=1846 lang=python3
#
# [1846] 减小和重新排列数组后的最大元素
#

# @lc code=start
from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        if not arr:
            return -1
        arr.sort()
        res = 1
        for a in arr[1:]:
            if a - res > 1:
                res = res + 1
            else:
                res = a
        return res

# @lc code=end
