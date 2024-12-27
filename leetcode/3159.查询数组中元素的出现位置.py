#
# @lc app=leetcode.cn id=3159 lang=python3
#
# [3159] 查询数组中元素的出现位置
#
from typing import List


# @lc code=start
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        dst = [
            i
            for i in range(len(nums))
            if nums[i] == x
        ]
        return [
            dst[query - 1] if query - 1 < len(dst) else -1
            for query in queries
        ]


# @lc code=end
