#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (36.27%)
# Likes:    1788
# Dislikes: 0
# Total Accepted:    114.6K
# Total Submissions: 315.9K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 
# 你可以假设 nums1 和 nums2 不会同时为空。
# 
# 示例 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
# 
# 
# 示例 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
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
    print(Solution().findMedianSortedArrays(nums1 = [1, 2], nums2 = [3, 4]))
# @lc code=end

