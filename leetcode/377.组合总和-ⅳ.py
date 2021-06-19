#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target

        for t in range(1, target + 1):
            for n in nums:
                if t < n:
                    continue
                dp[t] += dp[t - n]

        return dp[-1]


print(Solution().combinationSum4([4, 2, 1], 32))
# @lc code=end
