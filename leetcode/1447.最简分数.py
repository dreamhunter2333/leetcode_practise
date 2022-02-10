#
# @lc app=leetcode.cn id=1447 lang=python3
#
# [1447] 最简分数
#

# @lc code=start
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:

        def gcd(a: int, b: int) -> int:
            return a if b % a == 0 else gcd(b % a, a)

        return [
            "{}/{}".format(j, i)
            for i in range(2, n + 1)
            for j in range(1, i)
            if gcd(j, i) == 1
        ]


# print(Solution().simplifiedFractions(1))
# @lc code=end
