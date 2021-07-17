#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        pre = float("-inf")
        res = float("-inf")
        for i in range(n):
            pre = max(pre + nums[i], nums[i])
            res = max(pre, res)
        return res

# @lc code=end
