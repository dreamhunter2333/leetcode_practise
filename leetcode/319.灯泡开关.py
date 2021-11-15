#
# @lc app=leetcode.cn id=319 lang=python3
#
# [319] 灯泡开关
#

# @lc code=start
import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n + 0.5))

# @lc code=end
