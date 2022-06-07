#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#
from typing import List


# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if n > h:
            return -1
        if n == h:
            return max(piles)
        start = (sum(piles) + h - 1) // h
        end = max(piles)
        while start < end:
            k = (start + end) // 2
            res = sum(
                (pile + k - 1) // k
                for pile in piles
            )
            if res > h:
                start = k + 1
            else:
                end = k
        return end


# @lc code=end
print(Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8))
print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
print(Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
