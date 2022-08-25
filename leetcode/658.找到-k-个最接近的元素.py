#
# @lc app=leetcode.cn id=658 lang=python3
#
# [658] 找到 K 个最接近的元素
#
from typing import List


# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        return sorted(sorted(arr, key=lambda a: (abs(a - x), a))[:k])
# @lc code=end
