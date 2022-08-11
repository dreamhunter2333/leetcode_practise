#
# @lc app=leetcode.cn id=1417 lang=python3
#
# [1417] 重新格式化字符串
#

# @lc code=start
from string import digits


class Solution:
    def reformat(self, s: str) -> str:
        n = len(s)
        cache_letters = []
        cache_nums = []
        for c in s:
            if c in digits:
                cache_nums.append(c)
            else:
                cache_letters.append(c)
        if len(cache_letters) in (len(cache_nums), len(cache_nums) - 1):
            return "".join(
                cache_letters.pop()
                if i % 2 else
                cache_nums.pop()
                for i in range(n)
            )
        if len(cache_letters) - 1 == len(cache_nums):
            return "".join(
                cache_nums.pop()
                if i % 2 else
                cache_letters.pop()
                for i in range(n)
            )
        return ""


# @lc code=end
# print(Solution().reformat("a0b1c2"))
# print(Solution().reformat("leetcode"))
# print(Solution().reformat("1229857369"))
# print(Solution().reformat("covid2019"))
# print(Solution().reformat("ab123"))
print(Solution().reformat("619mama"))
