#
# @lc app=leetcode.cn id=553 lang=python3
#
# [553] 最优除法
#

# @lc code=start
from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:

        return "/".join(
            map(str, nums)
            ) if len(nums) < 3 else "{}/({})".format(
                nums[0], "/".join(map(str, nums[1:]))
            )


# print(Solution().optimalDivision([1000, 100]))
# @lc code=end
