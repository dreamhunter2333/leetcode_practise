#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H 指数 II
#

# @lc code=start
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        res = 0
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                res = n - mid
                right = mid - 1
            else:
                left = mid + 1
        return res

# @lc code=end
