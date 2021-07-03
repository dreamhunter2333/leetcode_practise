#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#

# @lc code=start
from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        cache = defaultdict(int)

        for c in s:
            cache[c] += 1

        return "".join(
            i * cache[i]
            for i in sorted(
                cache,
                key=lambda item: cache[item],
                reverse=True
            )
        )
# @lc code=end
