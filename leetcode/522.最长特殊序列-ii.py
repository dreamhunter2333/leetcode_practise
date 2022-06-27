#
# @lc app=leetcode.cn id=522 lang=python3
#
# [522] 最长特殊序列 II
#
from typing import List


# @lc code=start
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_sub(word1: str, word2: str) -> bool:
            """ return id word2 is sub str of word1"""
            start1 = start2 = 0
            end1 = len(word1)
            end2 = len(word2)
            while start1 < end1 and start2 < end2:
                if word1[start1] == word2[start2]:
                    start2 += 1
                start1 += 1
            return start2 == end2

        res = -1

        for i in range(len(strs)):
            check = True
            for j in range(len(strs)):
                if i != j and is_sub(strs[j], strs[i]):
                    check = False
                    break
            if check:
                res = max(res, len(strs[i]))

        return res


# @lc code=end
print(Solution().findLUSlength(["aba", "cdc", "eae"]))
print(Solution().findLUSlength(["aaa", "aaa", "aa"]))
