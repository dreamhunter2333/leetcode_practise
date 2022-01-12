#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#

# @lc code=start
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        first, second = nums.pop(0), float('inf')
        for num in nums:
            if num > second:
                return True
            if num > first:
                second = num
            else:
                first = num
        return False


# @lc code=end
