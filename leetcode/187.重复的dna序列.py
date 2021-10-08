#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#

# @lc code=start
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        count_map = {}
        for i in range(10, len(s) + 1):
            dna = s[i - 10:i]
            count = count_map.get(dna, 0)
            if count == 1:
                res.append(dna)
            count_map[dna] = count + 1
        return res

# @lc code=end
