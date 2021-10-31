#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1_set = set("qwertyuiop")
        line2_set = set("asdfghjkl")
        line3_set = set("zxcvbnm")

        def filter_word(word):
            word_set = set(word.lower())
            return (
                word_set.issubset(line1_set) or
                word_set.issubset(line2_set) or
                word_set.issubset(line3_set)
            )

        return [word for word in words if filter_word(word)]

# @lc code=end
