#
# @lc app=leetcode.cn id=3011 lang=python3
#
# [3011] 判断一个数组是否可以变为有序
#
from typing import List


# @lc code=start
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        preBitCount = 0
        preMax = 0
        curMax = 0
        for num in nums:
            curBitCount = num.bit_count()
            if curBitCount == preBitCount:
                curMax = max(num, curMax)
            else:
                preBitCount = curBitCount
                preMax = curMax
                curMax = num
            if num < preMax:
                return False
        return True


# @lc code=end
