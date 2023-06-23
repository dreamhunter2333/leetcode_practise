#
# @lc app=leetcode.cn id=2496 lang=python3
#
# [2496] 数组中字符串的最大值
#
from typing import List


# @lc code=start
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(
            int(s) if s.isdigit() else len(s)
            for s in strs
        )


# @lc code=end
print(Solution().maximumValue(["alic3", "bob", "3", "4", "00000"]))
print(Solution().maximumValue(["1", "01", "001", "0001"]))
