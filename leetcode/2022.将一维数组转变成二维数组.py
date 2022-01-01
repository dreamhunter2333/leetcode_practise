#
# @lc app=leetcode.cn id=2022 lang=python3
#
# [2022] 将一维数组转变成二维数组
#

# @lc code=start
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        res = [[0] * n for _ in range(m)]
        count_m = 0
        count_n = 0
        for num in original:
            res[count_m][count_n] = num
            count_n += 1
            if count_n == n:
                count_m += 1
                count_n = 0
        return res

# @lc code=end
