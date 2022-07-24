#
# @lc app=leetcode.cn id=1184 lang=python3
#
# [1184] 公交站间的距离
#

from typing import List


# @lc code=start
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        all_distance = sum(distance)
        if start > destination:
            start, destination = destination, start
        res = sum(distance[start:destination])
        return min(res, all_distance - res)


# @lc code=end
print(Solution().distanceBetweenBusStops(
    distance=[1, 2, 3, 4], start=0, destination=1
))
print(Solution().distanceBetweenBusStops(
    distance=[1, 2, 3, 4], start=0, destination=2
))
