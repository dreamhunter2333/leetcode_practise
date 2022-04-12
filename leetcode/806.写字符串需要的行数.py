#
# @lc app=leetcode.cn id=806 lang=python3
#
# [806] 写字符串需要的行数
#

# @lc code=start
from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        cache = 0
        count = 0
        for c in s:
            i = ord(c) - ord("a")
            if cache + widths[i] > 100:
                count += 1
                cache = 0
            cache += widths[i]
        return (
            count + 1, cache
        ) if cache > 0 else (
            count, 100
        )


# print(Solution().numberOfLines(
#     widths=[
#         10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
#         10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
#         10, 10, 10, 10, 10, 10
#     ],
#     s="abcdefghijklmnopqrstuvwxyz"
# ))
# print(Solution().numberOfLines(
#     widths=[
#         4, 10, 10, 10, 10, 10, 10, 10, 10, 10,
#         10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
#         10, 10, 10, 10, 10, 10
#     ],
#     s="bbbcccdddaaa"
# ))
# @lc code=end
