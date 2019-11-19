# -*- coding: utf-8 -*-

"""
4. 寻找两个有序数组的中位数

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
"""


class Solution:
    def test(self, nums1: list, nums2: list) -> float:
        """
        算法的时间复杂度不符合
        """
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            return (nums[int(len(nums)/2)] + nums[int(len(nums)/2 - 1)])/2
        else:
            return nums[int((len(nums) - 1)/2)]


if __name__ == "__main__":
    print(Solution().test(nums1 = [1, 2], nums2 = [3, 4]))