#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于K的子数组
#

# @lc code=start
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        multi_sum = 1
        left = 0
        right = 0

        while right < n:
            multi_sum *= nums[right]
            while left <= right and multi_sum >= k:
                multi_sum //= nums[left]
                left += 1
            res += right - left + 1
            right += 1
        return res


# print(Solution().numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
# print(Solution().numSubarrayProductLessThanK(nums=[1, 2, 3], k=0))
# @lc code=end
