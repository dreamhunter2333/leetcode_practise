#
# @lc app=leetcode.cn id=2011 lang=python3
#
# [2011] 执行操作后的变量值
#
from typing import List


# @lc code=start
class Solution:

    MAP = {"X++": 1, "++X": 1, "--X": -1, "X--": -1}

    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(self.MAP[op] for op in operations)
# @lc code=end
