#
# @lc app=leetcode.cn id=2594 lang=python3
#
# [2594] 修车的最少时间
#
import math
from typing import List


# @lc code=start
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 0
        right = min(ranks) * cars * cars

        def check(res):
            return sum(
                int(math.sqrt(res // rank))
                for rank in ranks
            ) >= cars

        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return right


# @lc code=end
print(Solution().repairCars(
    ranks=[4, 2, 3, 1], cars=10
))
print(Solution().repairCars(
    ranks=[5, 1, 8], cars=6
))
