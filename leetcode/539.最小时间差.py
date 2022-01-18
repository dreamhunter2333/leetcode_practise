#
# @lc app=leetcode.cn id=539 lang=python3
#
# [539] 最小时间差
#

# @lc code=start
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = [int(t[:2]) * 60 + int(t[3:]) for t in timePoints]
        times.sort()
        times.append(times[0] + 24 * 60)
        n = len(times)
        return min(
            times[i + 1] - times[i]
            for i in range(n - 1)
        )


# print(Solution().findMinDifference(timePoints=["23:59", "00:00"]))
# print(Solution().findMinDifference(timePoints=["00:00", "23:59", "00:00"]))
# @lc code=end
