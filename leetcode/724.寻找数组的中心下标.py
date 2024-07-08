#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#
from typing import List


# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = 0
        nums_sum = sum(nums)
        for i in range(len(nums)):
            if 2 * prefix_sum == (nums_sum - nums[i]):
                return i
            prefix_sum += nums[i]
        return -1


# @lc code=end
print(Solution().pivotIndex([-1, -1, -1, -1, -1, 0]))
