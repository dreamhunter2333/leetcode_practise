#
# @lc app=leetcode.cn id=1641 lang=python3
#
# [1641] 统计字典序元音字符串的数目
#

# @lc code=start
from functools import cache


DATA = ["a", "e", "i", "o", "u"]


class Solution:
    def countVowelStrings(self, n: int) -> int:
        @cache
        def dfs(pre_index: int, n: int) -> int:
            if n == 0:
                return 1
            return sum(
                dfs(i, n-1) for i in range(pre_index, 5)
            )

        return dfs(0, n)


# @lc code=end
print(Solution().countVowelStrings(1))
print(Solution().countVowelStrings(2))
print(Solution().countVowelStrings(33))
