#
# @lc app=leetcode.cn id=2559 lang=python3
#
# [2559] 统计范围内的元音字符串数
#
from typing import List


# @lc code=start
TARGET = set("aeiou")


class Solution:

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum = [0]
        cur = 0
        for word in words:
            if word[0] in TARGET and word[-1] in TARGET:
                cur += 1
            prefix_sum.append(cur)

        return [
            prefix_sum[end+1] - prefix_sum[start]
            for start, end in queries
        ]


# @lc code=end
print(Solution().vowelStrings(
    words=["aba", "bcb", "ece", "aa", "e"],
    queries=[[0, 2], [1, 4], [1, 1]]
))
print(Solution().vowelStrings(
    words=["a", "e", "i"],
    queries=[[0, 2], [0, 1], [2, 2]]
))
