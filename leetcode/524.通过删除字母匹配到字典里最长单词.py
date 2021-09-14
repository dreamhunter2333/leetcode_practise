#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#

# @lc code=start
from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        n = len(s)
        res = ""
        for word in dictionary:
            m = len(word)
            i = 0
            j = 0
            while j < m and i < n:
                if s[i] == word[j]:
                    j += 1
                i += 1
            if j == m:
                res = min(res, word, key=lambda c: (-len(c), c))
        return res

# @lc code=end
