#
# @lc app=leetcode.cn id=1775 lang=python3
#
# [1775] 通过最少操作次数使数组的和相等
#
from typing import List


# @lc code=start
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        delta = sum(nums1) - sum(nums2)
        if delta == 0:
            return 0
        if delta < 0:
            nums1, nums2 = nums2, nums1
            delta = -delta
        if len(nums2) * 6 < len(nums1) * 1:
            return -1
        res = 0
        d_nums = sorted([
            num - 1
            for num in nums1
        ] + [
            6 - num
            for num in nums2
        ], reverse=True)
        while delta > 0:
            delta -= d_nums[res]
            res += 1
        return res


# @lc code=end
print(Solution().minOperations(
    nums1=[1, 2, 3, 4, 5, 6], nums2=[1, 1, 2, 2, 2, 2]
))
print(Solution().minOperations(
    nums1=[1, 1, 1, 1, 1, 1, 1], nums2=[6]
))
print(Solution().minOperations(
    nums1=[6, 6], nums2=[1]
))
