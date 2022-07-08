#
# @lc app=leetcode.cn id=1217 lang=python3
#
# [1217] 玩筹码
#

from typing import List


# @lc code=start
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        odd = 0
        for pos in position:
            if pos % 2:
                odd += 1
            else:
                even += 1
        return min(odd, even)


# @lc code=end
print(Solution().minCostToMoveChips([1, 2, 3]))
