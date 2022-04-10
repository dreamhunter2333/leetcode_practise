#
# @lc app=leetcode.cn id=804 lang=python3
#
# [804] 唯一摩尔斯密码词
#

# @lc code=start
from typing import List

MORSE_LIST = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
    ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
    "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
]
MORSE_DICT = {
    chr(ord("a") + i): value
    for i, value in enumerate(MORSE_LIST)
}


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set(
            "".join(MORSE_DICT[char] for char in word)
            for word in words
        ))


# print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
# @lc code=end
