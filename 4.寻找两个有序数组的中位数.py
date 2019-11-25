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
            https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2511
        """
        def find_center_num(nums1: List[int], nums2: List[int], center: int) -> float:
            if not nums1:
                return nums2[center]
            if not nums2:
                return nums1[center]
            center1, center2 = len(nums1) // 2, len(nums2) // 2
            num1, num2 = nums1[center1], nums2[center2]
            if center1 + center2 < center:
                if num1 > num2:
                    return find_center_num(nums1, nums2[center2+1:], center - center2 -1)
                else:
                    return find_center_num(nums1[center1+1:], nums2, center - center1 -1)
            else:
                if num1 > num2:
                    return find_center_num(nums1[:center1], nums2, center)
                else:
                    return find_center_num(nums1, nums2[:center2], center)
        nums_len = len(nums1) + len(nums2)
        if nums_len % 2 == 0:
            return (find_center_num(nums1, nums2, nums_len // 2) + 
                find_center_num(nums1, nums2, nums_len // 2 - 1)) / 2
        else:
            return find_center_num(nums1, nums2, nums_len // 2)


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays(nums1 = [1, 2], nums2 = [3, 4]))
# @lc code=end

