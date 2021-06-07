#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        delta = sum(nums) - target
        if delta < 0 or delta % 2:
            return 0
        max_t = delta // 2
        dp = [[0] * (max_t+1) for _ in range(len(nums)+1)]
        dp[0][0] = 1
        for i in range(1, len(nums)+1):
            for j in range(max_t+1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] += dp[i-1][j-nums[i-1]]
        return dp[-1][-1]
        # 优化复杂度
        # delta = sum(nums) - target
        # if delta < 0 or delta % 2:
        #     return 0
        # max_t = delta // 2
        # dp = [0] * (max_t+1)
        # dp[0] = 1

        # for num in nums:
        #     for j in range(max_t, num-1, -1):
        #         dp[j] += dp[j-num]
        # return dp[max_t]
# @lc code=end
