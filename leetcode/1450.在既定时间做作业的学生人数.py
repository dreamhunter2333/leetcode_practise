#
# @lc app=leetcode.cn id=1450 lang=python3
#
# [1450] 在既定时间做作业的学生人数
#
from typing import List


# @lc code=start
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(
            1 for i in range(len(startTime))
            if startTime[i] <= queryTime <= endTime[i]
        )

# @lc code=end
