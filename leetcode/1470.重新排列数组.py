#
# @lc app=leetcode.cn id=1470 lang=python3
#
# [1470] 重新排列数组
#
from typing import List


# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [
            num
            for i in range(n)
            for num in (nums[i], nums[i+n])
        ]
# @lc code=end
