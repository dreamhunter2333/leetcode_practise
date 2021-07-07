#
# @lc app=leetcode.cn id=1711 lang=python3
#
# [1711] 大餐计数
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        res = 0
        cache_list = [2 ** i for i in range(22)]
        cache_map = defaultdict(int)

        for d in deliciousness:
            res += cache_map[d]
            for j in cache_list:
                if j < d:
                    continue
                cache_map[j - d] += 1

        return res % (10 ** 9 + 7)


# print(Solution().countPairs([
#     149, 107, 1, 63, 0, 1, 6867,
#     1325, 5611, 2581, 39, 89, 46, 18, 12, 20, 22, 234
# ]))
# print(Solution().countPairs([1, 3, 5, 7, 9]))
# print(Solution().countPairs([1, 1, 1, 3, 3, 3, 7]))
print(Solution().countPairs([1048576, 1048576]))
# @lc code=end
