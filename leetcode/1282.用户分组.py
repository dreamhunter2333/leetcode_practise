#
# @lc app=leetcode.cn id=1282 lang=python3
#
# [1282] 用户分组
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        cahce_dict = defaultdict(list)
        for i in range(len(groupSizes)):
            cahce_dict[groupSizes[i]].append(i)
        return [
            peoples[i:i+groupSize]
            for groupSize, peoples in cahce_dict.items()
            for i in range(0, len(peoples), groupSize)
        ]


# @lc code=end
print(Solution().groupThePeople([3, 3, 3, 3, 3, 1, 3]))
print(Solution().groupThePeople([2, 1, 3, 3, 3, 2]))
