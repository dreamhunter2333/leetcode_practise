#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        s = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[s] = nums1[i]
                i -= 1
            else:
                nums1[s] = nums2[j]
                j -= 1
            s -= 1

        while j >= 0:
            nums1[s] = nums2[j]
            j -= 1
            s -= 1

        while i >= 0:
            nums1[s] = nums1[i]
            i -= 1
            s -= 1

        return nums1

# @lc code=end
