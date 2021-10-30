#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        cache_map = {}
        for num in nums:
            cache_map[num] = cache_map.get(num, 0) + 1
        return [num for num in cache_map if cache_map[num] == 1]

# @lc code=end
