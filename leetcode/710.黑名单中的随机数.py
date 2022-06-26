#
# @lc app=leetcode.cn id=710 lang=python3
#
# [710] 黑名单中的随机数
#
import random
from typing import List


# @lc code=start
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        m = len(blacklist)
        self.bound = n - m
        self.data = {}
        start = n - m
        for b in blacklist:
            if b < self.bound:
                while start in blacklist:
                    start += 1
                self.data[b] = start
                start += 1

    def pick(self) -> int:
        res = random.randint(0, self.bound - 1)
        return self.data.get(res, res)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
# @lc code=end
