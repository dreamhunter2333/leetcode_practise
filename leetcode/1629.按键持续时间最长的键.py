#
# @lc app=leetcode.cn id=1629 lang=python3
#
# [1629] 按键持续时间最长的键
#

# @lc code=start
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        res_map = {}
        for i, key in enumerate(keysPressed):
            res_map[key] = max(
                res_map.get(key, 0), releaseTimes[i] - (releaseTimes[i - 1] if i else 0)
            )

        return max(res_map, key=lambda key: res_map[key] + ord(key) / 1000)

# @lc code=end
