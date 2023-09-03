#
# @lc app=leetcode.cn id=1921 lang=python3
#
# [1921] 消灭怪物的最大数量
#

from typing import List


# @lc code=start
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        res = 0
        cur_time = 0
        for t in sorted(
            d / s
            for d, s in zip(dist, speed)
        ):
            if cur_time and t <= cur_time:
                break
            cur_time += 1
            res += 1
        return res


# @lc code=end
print(Solution().eliminateMaximum(
    dist=[1, 3, 4], speed=[1, 1, 1]
))
print(Solution().eliminateMaximum(
    dist=[1, 1, 2, 3], speed=[1, 1, 1, 1]
))
print(Solution().eliminateMaximum(
    dist=[3, 2, 4], speed=[5, 3, 2]
))
print(Solution().eliminateMaximum(
    dist=[4, 2, 3], speed=[2, 1, 1]
))
