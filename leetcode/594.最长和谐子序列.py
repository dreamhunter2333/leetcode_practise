#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hash_dict = {}
        for num in nums:
            hash_dict[num] = hash_dict.get(num, 0) + 1
        return max(
            (
                hash_dict[num] + hash_dict[num + 1]
                for num in hash_dict
                if num + 1 in hash_dict
            ),
            default=0
        )


# print(Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
# print(Solution().findLHS([1, 2, 3, 4]))
# print(Solution().findLHS([1, 1, 1, 1]))
# @lc code=end
