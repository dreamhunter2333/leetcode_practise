#
# @lc app=leetcode.cn id=1636 lang=python3
#
# [1636] 按照频率将数组升序排序
#
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_counter = Counter(nums)
        return sorted(nums, key=lambda num: (nums_counter[num], -num))


# @lc code=end
print(Solution().frequencySort(
    [2, 3, 1, 3, 2]
))
