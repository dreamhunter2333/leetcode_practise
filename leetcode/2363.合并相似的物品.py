#
# @lc app=leetcode.cn id=2363 lang=python3
#
# [2363] 合并相似的物品
#
from typing import List
from collections import Counter


# @lc code=start
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        return [
            [k, v]
            for k, v in sorted((
                Counter({k: v for k, v in items1}) +
                Counter({k: v for k, v in items2})
            ).items())
        ]


# @lc code=end
print(Solution().mergeSimilarItems(
    items1=[[1, 1], [4, 5], [3, 8]],
    items2=[[3, 1], [1, 5]]
))
print(Solution().mergeSimilarItems(
    items1=[[1, 1], [3, 2], [2, 3]],
    items2=[[2, 1], [3, 2], [1, 3]]
))
print(Solution().mergeSimilarItems(
    items1=[[1, 3], [2, 2]],
    items2=[[7, 1], [2, 2], [1, 4]]
))
