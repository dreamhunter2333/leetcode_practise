#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        pre_max = float("-inf")
        max_num = float("-inf")
        res = None
        for index, num in enumerate(nums):
            if num > max_num:
                pre_max = max_num
                max_num = num
                res = index
            elif pre_max <= num <= max_num:
                pre_max = num
        return res if pre_max == float("-inf") or (
            pre_max == 0 or max_num / pre_max >= 2
        ) else -1

# @lc code=end
