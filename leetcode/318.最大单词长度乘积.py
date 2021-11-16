#
# @lc app=leetcode.cn id=318 lang=python3
#
# [318] 最大单词长度乘积
#

# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        n = len(words)
        word_sets = [set(w) for w in words]
        for i in range(n-1):
            for j in range(i+1, n):
                if word_sets[i] & word_sets[j]:
                    continue
                res = max(res, len(words[i]) * len(words[j]))
        return res


# @lc code=end
