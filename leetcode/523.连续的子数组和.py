#
# @lc app=leetcode.cn id=523 lang=python3
#
# [523] 连续的子数组和
#

# @lc code=start
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = 0
        remain_map = {0: -1}
        for i in range(len(nums)):
            remainder = (remainder + nums[i]) % k
            if remainder in remain_map:
                if i - remain_map[remainder] > 1:
                    return True
            else:
                remain_map[remainder] = i
        return False
# @lc code=end
