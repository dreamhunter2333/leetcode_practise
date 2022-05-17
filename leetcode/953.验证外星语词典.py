#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#
from typing import List


# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {
            order[i]: i
            for i in range(len(order))
        }
        return words == sorted(
            words,
            key=lambda word: tuple(
                order_dict[c] for c in word
            )
        )


# @lc code=end
print(Solution().isAlienSorted(
    words=["hello", "leetcode"],
    order="hlabcdefgijkmnopqrstuvwxyz"
))
print(Solution().isAlienSorted(
    words=["word", "world", "row"],
    order="worldabcefghijkmnpqstuvxyz"
))
