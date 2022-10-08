#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#

from typing import List


# @lc code=start
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        n = len(nums1)
        indexs = sorted(range(n), key=lambda i: nums2[i])
        left = 0
        right = n - 1
        ans = [0]*n
        for num in nums1:
            if num > nums2[indexs[left]]:
                ans[indexs[left]] = num
                left += 1
            else:
                ans[indexs[right]] = num
                right -= 1
        return ans


# @lc code=end
print(Solution().advantageCount(nums1=[2, 7, 11, 15], nums2=[1, 10, 4, 11]))
