#
# @lc app=leetcode.cn id=890 lang=python3
#
# [890] 查找和替换模式
#
from typing import List


# @lc code=start
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        n = len(pattern)

        def check(word: str) -> bool:
            cache = {}
            cache2 = {}
            for i in range(n):
                if pattern[i] in cache and cache[pattern[i]] != word[i]:
                    return False
                if word[i] in cache2 and cache2[word[i]] != pattern[i]:
                    return False
                cache[pattern[i]] = word[i]
                cache2[word[i]] = pattern[i]
            return True

        return [word for word in words if check(word)]


# @lc code=end
print(Solution().findAndReplacePattern(
    words=["abc", "deq", "mee", "aqq", "dkd", "ccc"],
    pattern="abb"
))
