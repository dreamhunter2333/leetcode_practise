#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#
from functools import cache
from typing import List


# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        avg = sum(nums) // k
        nums.sort()
        if nums[-1] > avg:
            return False
        n = len(nums)

        @cache
        def dfs(state, pre_sum):
            if state == 0:
                return True
            for i in range(n):
                if nums[i] + pre_sum > avg:
                    break
                if state >> i & 1 and dfs(
                    state ^ (1 << i), (pre_sum + nums[i]) % avg
                ):
                    return True
            return False
        return dfs((1 << n) - 1, 0)


# @lc code=end
print(Solution().canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4))
print(Solution().canPartitionKSubsets(nums=[1, 2, 3, 4], k=3))
print(Solution().canPartitionKSubsets(
    nums=[
      815, 625, 3889, 4471, 60, 494, 944, 1118,
      4623, 497, 771, 679, 1240, 202, 601, 883
      ],
    k=3
))
print(Solution().canPartitionKSubsets(nums=[2, 2, 2, 2, 3, 4, 5], k=4))
