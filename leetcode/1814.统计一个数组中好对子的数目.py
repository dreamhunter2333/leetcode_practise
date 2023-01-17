#
# @lc app=leetcode.cn id=1814 lang=python3
#
# [1814] 统计一个数组中好对子的数目
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        res = 0
        count_map = defaultdict(int)
        for num in nums:
            rev_num = int(str(num)[::-1])
            res += count_map[num - rev_num]
            count_map[num - rev_num] += 1
        return res % (10 ** 9 + 7)
# @lc code=end
