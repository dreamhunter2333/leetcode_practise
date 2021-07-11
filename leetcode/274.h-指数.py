#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        for i in range(n, 0, -1):
            if citations[i-1] >= i:
                return i
        return 0

# @lc code=end
