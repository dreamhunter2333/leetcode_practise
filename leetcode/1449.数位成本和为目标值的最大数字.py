#
# @lc app=leetcode.cn id=1449 lang=python3
#
# [1449] 数位成本和为目标值的最大数字
#

# @lc code=start
from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        d = dict((v, str(i)) for i, v in enumerate(cost, 1))
        dp = [''] + ['0'] * target
        for i in range(1, target+1):
            for k, v in d.items():
                if i >= k and dp[i-k] != '0':
                    dp[i] = max(dp[i], v+dp[i-k], key=int)
        return dp[target]

# @lc code=end
