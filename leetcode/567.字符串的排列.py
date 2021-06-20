#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        n = len(s1)
        for i in range(0, len(s2) - n + 1):
            if Counter(s2[i:i+n]) == count1:
                return True
        return False

# @lc code=end
