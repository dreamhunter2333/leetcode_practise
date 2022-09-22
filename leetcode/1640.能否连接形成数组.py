#
# @lc app=leetcode.cn id=1640 lang=python3
#
# [1640] 能否连接形成数组
#
from typing import List


# @lc code=start
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        arr_map = {num: i for i, num in enumerate(arr)}
        for piece in pieces:
            pre_index = None
            for num in piece:
                if num not in arr_map or (
                    pre_index is not None and
                    arr_map[num] - pre_index != 1
                ):
                    return False
                pre_index = arr_map[num]
        return True


# @lc code=end
print(Solution().canFormArray(arr=[15, 88], pieces=[[88], [15]]))
print(Solution().canFormArray(arr=[49, 18, 16], pieces=[[16, 18, 49]]))
print(Solution().canFormArray(
    arr=[91, 4, 64, 78], pieces=[[78], [4, 64], [91]]
))
