#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for o in ops:
            if o == "C":
                res.pop()
            elif o == "D":
                res.append(res[-1] * 2)
            elif o == "+":
                res.append(res[-1] + res[-2])
            else:
                res.append(int(o))

        return sum(res)


# print(Solution().calPoints(["5", "2", "C", "D", "+"]))
# print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
# print(Solution().calPoints(["1"]))
# @lc code=end
