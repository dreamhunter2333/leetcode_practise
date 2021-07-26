#
# @lc app=leetcode.cn id=1713 lang=python3
#
# [1713] 得到子序列的最少操作次数
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        len_target = len(target)
        cache_map = {
            target[i]: i
            for i in range(len_target)
        }
        res = []

        def get_index(target_i):
            if (not res or res[-1] < target_i):
                return len(res)
            low = 0
            high = len(res) - 1
            while (low < high):
                mid = (high + low) // 2
                if res[mid] < target_i:
                    low = mid + 1
                else:
                    high = mid
            return low

        for n in arr:
            if n not in cache_map:
                continue
            index1 = cache_map[n]
            index = get_index(index1)
            if index == len(res):
                res.append(index1)
            else:
                res[index] = index1

        return len_target - len(res)


# @lc code=end
