#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        maxn = float("-inf")
        right = None
        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]

        minn = float("inf")
        left = None
        for i in range(n-1, -1, -1):

            if minn < nums[i]:
                left = i
            else:
                minn = nums[i]

        return 0 if right is None else right - left + 1

# @lc code=end
