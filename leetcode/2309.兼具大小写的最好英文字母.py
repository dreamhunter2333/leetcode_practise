#
# @lc app=leetcode.cn id=2309 lang=python3
#
# [2309] 兼具大小写的最好英文字母
#

# @lc code=start
from string import ascii_lowercase, ascii_uppercase


class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        for lower, upper in zip(reversed(ascii_lowercase), reversed(ascii_uppercase)):
            if lower in s and upper in s:
                return upper
        return ""


# @lc code=end
print(Solution().greatestLetter("lEeTcOdE"))
print(Solution().greatestLetter("arRAzFif"))
print(Solution().greatestLetter("AbCdEfGhIjK"))
