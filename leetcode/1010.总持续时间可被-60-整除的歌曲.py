#
# @lc app=leetcode.cn id=1010 lang=python3
#
# [1010] 总持续时间可被 60 整除的歌曲
#

# @lc code=start
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cache_map = {}
        res = 0
        for t in time:
            current = t % 60
            res += cache_map.get(60 - (current or 60), 0)
            cache_map[current] = cache_map.get(current, 0) + 1
        return res

# @lc code=end
