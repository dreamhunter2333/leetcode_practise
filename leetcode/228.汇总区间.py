#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
from typing import List


# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        start = None
        pre = float("inf")
        for num in nums:
            if num == pre + 1:
                res[-1] = f"{start}->{num}"
                pre = num
            else:
                res.append(f"{num}")
                pre = num
                start = num

        return res


# @lc code=end
print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]))
print(Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]))
