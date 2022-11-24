#
# @lc app=leetcode.cn id=795 lang=python3
#
# [795] 区间子数组个数
#
from typing import List


# @lc code=start
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res = 0
        pre_count = 0
        min_count = 0
        for num in nums:
            if num < left:
                min_count += 1
                res += pre_count
            elif left <= num <= right:
                res += 1
                res += (pre_count + min_count)
                pre_count += (1 + min_count)
                min_count = 0
            else:
                pre_count = 0
                min_count = 0
        return res


# @lc code=end
print(Solution().numSubarrayBoundedMax(nums=[2, 1, 4, 3], left=2, right=3))
print(Solution().numSubarrayBoundedMax(nums=[2, 9, 2, 5, 6], left=2, right=8))
print(Solution().numSubarrayBoundedMax(
    nums=[73, 55, 36, 5, 55, 14, 9, 7, 72, 52], left=32, right=69
))
