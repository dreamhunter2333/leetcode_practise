#
# @lc app=leetcode.cn id=462 lang=python3
#
# [462] 最少移动次数使数组元素相等 II
#
from typing import List


# @lc code=start
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        target = nums[len(nums) // 2]
        return sum(
            abs(target - num)
            for num in nums
        )


# @lc code=end
print(Solution().minMoves2([1, 2, 3]))
print(Solution().minMoves2([1, 10, 2, 9]))
