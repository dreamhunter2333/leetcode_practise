#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_index = float("inf")
        res = []
        map1 = {
            name: i
            for i, name in enumerate(list1)
        }
        for i, name in enumerate(list2):
            if name not in map1:
                continue
            if i + map1[name] < min_index:
                min_index = i + map1[name]
                res = [name]
            elif i + map1[name] == min_index:
                res.append(name)

        return res


# print(Solution().findRestaurant(
#     list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
#     list2=["KFC", "Shogun", "Burger King"]
# ))
# @lc code=end
