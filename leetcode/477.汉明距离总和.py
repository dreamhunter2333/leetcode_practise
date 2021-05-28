#
# @lc app=leetcode.cn id=477 lang=python3
#
# [477] 汉明距离总和
#

# @lc code=start
from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        str_nums = map("{:032b}".format, nums)
        str_nums_bits = zip(*str_nums)
        sum = 0
        nums_len = len(nums)
        for b in str_nums_bits:
            c = b.count('1')
            sum += c * (nums_len - c)
        return sum
# @lc code=end
