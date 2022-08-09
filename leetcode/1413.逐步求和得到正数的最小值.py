#
# @lc app=leetcode.cn id=1413 lang=python3
#
# [1413] 逐步求和得到正数的最小值
#
from typing import List


# @lc code=start
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_num = 0
        sum_num = 0
        for num in nums:
            sum_num += num
            min_num = min(min_num, sum_num)
        return 1 - min_num


# @lc code=end
print(Solution().minStartValue(nums=[-3, 2, -3, 4, 2]))
print(Solution().minStartValue(nums=[1, 2]))
print(Solution().minStartValue(nums=[1, -2, -3]))
