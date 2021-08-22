#
# @lc app=leetcode.cn id=789 lang=python3
#
# [789] 逃脱阻碍者
#

# @lc code=start
from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        source = [0, 0]
        get_d = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
        distance = get_d(source, target)
        return all(get_d(ghost, target) > distance for ghost in ghosts)

# @lc code=end
