#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#

# @lc code=start
from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        texts = text.split(" ")
        n = len(texts)
        res = []
        for i in range(1, n - 1):
            if texts[i-1] == first and texts[i] == second:
                res.append(texts[i+1])
        return res


# print(Solution().findOcurrences(
#     text="we will we will rock you", first="we", second="will"
# ))
# @lc code=end
