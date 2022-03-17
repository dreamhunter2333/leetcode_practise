#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#

# @lc code=start
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:

        words.sort()
        pre_set = set()
        res = ""
        for w in words:
            if len(w) == 1:
                pre_set = {w}
                res = max(res, w, key=len)
                continue
            cur = w[:-1]
            if cur not in pre_set:
                continue
            pre_set.add(w)
            res = max(res, w, key=len)

        return res


# print(Solution().longestWord(
#     ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# ))
# @lc code=end
