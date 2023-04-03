#
# @lc app=leetcode.cn id=1053 lang=python3
#
# [1053] 交换一次的先前排列
#

# @lc code=start
from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-1, -1, -1):
            target_list = [
                j for j in range(i+1, n) if arr[j] < arr[i]
            ]
            if not target_list:
                continue
            j = max(target_list, key=lambda p: arr[p])
            arr[i], arr[j] = arr[j], arr[i]
            break
        return arr

# @lc code=end
