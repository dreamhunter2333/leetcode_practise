#
# @lc app=leetcode.cn id=2357 lang=python3
#
# [2357] 使数组中所有元素都等于零
#
from typing import List


# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(num for num in nums if num))
# @lc code=end
