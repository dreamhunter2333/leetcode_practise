#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def findTopKth(low, high):
            pivot = random.randint(low, high)
            nums[low], nums[pivot] = nums[pivot], nums[low]
            base = nums[low]
            i = low
            j = low + 1
            while j <= high:
                if nums[j] > base:
                    nums[i + 1], nums[j] = nums[j], nums[i + 1]
                    i += 1
                j += 1
            nums[low], nums[i] = nums[i], nums[low]
            if i == k - 1:
                return nums[i]
            elif i > k - 1:
                return findTopKth(low, i - 1)
            else:
                return findTopKth(i + 1, high)
        return findTopKth(0, len(nums) - 1)

# @lc code=end
