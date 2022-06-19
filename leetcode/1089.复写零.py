#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#
from typing import List


# @lc code=start


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        top = 0
        i = -1
        while top < n:
            top += 1
            i += 1
            if arr[i] == 0:
                top += 1
        j = n - 1
        if top == n + 1:
            arr[j] = 0
            i -= 1
            j -= 1
        while j >= 0:
            arr[j] = arr[i]
            if arr[i] == 0:
                arr[j - 1] = 0
                j -= 1
            j -= 1
            i -= 1


# @lc code=end
arr = [1, 0, 2, 3, 0, 4, 5, 0]
arr2 = [1, 2, 3]
Solution().duplicateZeros(arr)
Solution().duplicateZeros(arr2)
print(arr, arr2)
